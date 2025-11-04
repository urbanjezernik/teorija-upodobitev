#!/usr/bin/env python3
"""
tex2png.py — Compile all .tex files in a folder to PDFs and PNGs.

Typical use:
    python tex2png.py --dir img --recursive --dpi 600

Requirements:
    - latexmk (or pdflatex as a fallback)
    - ImageMagick's `magick` (or `convert`) and Ghostscript
    - (optional) pdfcrop (from TeX Live) if you need cropping for non-standalone docs

On macOS (Homebrew):
    brew install --cask mactex
    brew install imagemagick ghostscript
"""

import argparse
import os
import sys
import subprocess
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

def which_any(*candidates):
    for c in candidates:
        p = shutil.which(c)
        if p:
            return p
    return None

LATEXMK = which_any("latexmk")
PDLATEX = which_any("pdflatex")
PDFCROP = which_any("pdfcrop")
MAGICK = which_any("magick", "convert")  # prefer 'magick' if available

def compile_tex_to_pdf(tex_path: Path, quiet: bool = True) -> Path | None:
    """Compile a .tex file to .pdf using latexmk (preferred) or pdflatex fallback.
    Returns the PDF path on success, else None.
    """
    cwd = tex_path.parent
    pdf_path = tex_path.with_suffix(".pdf")

    if LATEXMK:
        cmd = [LATEXMK, "-pdf", "-halt-on-error", "-interaction=nonstopmode"]
        if quiet:
            cmd.append("-quiet")
        # run in the file's directory to respect relative includes
        cmd.extend([str(tex_path.name)])
        result = subprocess.run(cmd, cwd=str(cwd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.returncode != 0:
            print(f"[latexmk] ERROR compiling {tex_path}:\n{result.stdout}", file=sys.stderr)
            return None
    elif PDLATEX:
        # Run pdflatex up to twice to resolve references
        ok = True
        for i in range(2):
            cmd = [PDLATEX, "-halt-on-error", "-interaction=nonstopmode", str(tex_path.name)]
            result = subprocess.run(cmd, cwd=str(cwd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode != 0:
                ok = False
                print(f"[pdflatex] ERROR compiling {tex_path} (pass {i+1}):\n{result.stdout}", file=sys.stderr)
                break
        if not ok:
            return None
    else:
        print("ERROR: Neither latexmk nor pdflatex found in PATH.", file=sys.stderr)
        return None

    if not pdf_path.exists():
        # latexmk sometimes writes to the same folder; check existence after compile
        if not pdf_path.exists():
            print(f"ERROR: Expected PDF not found: {pdf_path}", file=sys.stderr)
            return None
    return pdf_path

def crop_pdf_if_requested(pdf_path: Path, do_crop: bool) -> Path:
    """Optionally crop the PDF using pdfcrop. Returns the (possibly new) PDF path to use."""
    if not do_crop:
        return pdf_path
    if not PDFCROP:
        print(f"WARNING: pdfcrop not found; skipping crop for {pdf_path.name}", file=sys.stderr)
        return pdf_path
    cropped = pdf_path.with_name(pdf_path.stem + ".cropped.pdf")
    cmd = [PDFCROP, str(pdf_path), str(cropped)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if result.returncode != 0:
        print(f"[pdfcrop] ERROR cropping {pdf_path}:\n{result.stdout}", file=sys.stderr)
        return pdf_path
    return cropped

def pdf_to_png(pdf_path: Path, png_path: Path, dpi: int, alpha_white: bool = True) -> bool:
    """Convert a (single-page) PDF to PNG using ImageMagick. Returns True on success."""
    if not MAGICK:
        print("ERROR: Neither 'magick' nor 'convert' found in PATH.", file=sys.stderr)
        return False

    # Use first page explicitly: input.pdf[0]
    pdf_input = f"{pdf_path}[0]"

    # Build command
    cmd = [MAGICK, "-density", str(dpi), pdf_input]
    if alpha_white:
        cmd += ["-background", "white", "-alpha", "remove", "-alpha", "off"]
    # Ensure maximum quality for line art
    cmd += ["-quality", "100", str(png_path)]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if result.returncode != 0:
        print(f"[ImageMagick] ERROR converting {pdf_path}:\n{result.stdout}", file=sys.stderr)
        return False
    return True

def process_tex_file(tex_path: Path, args) -> tuple[Path, bool, str]:
    """Compile a single .tex file to PNG; returns (png_path, success, message)."""
    try:
        pdf = tex_path.with_suffix(".pdf")
        png = tex_path.with_suffix(".png")

        if png.exists() and not args.overwrite:
            return (png, True, f"SKIP (exists): {png}")

        compiled_pdf = compile_tex_to_pdf(tex_path, quiet=not args.verbose)
        if compiled_pdf is None:
            return (png, False, f"FAIL compile: {tex_path}")

        use_pdf = crop_pdf_if_requested(compiled_pdf, args.crop)

        success = pdf_to_png(use_pdf, png, dpi=args.dpi, alpha_white=not args.transparent)
        if not success:
            return (png, False, f"FAIL convert: {tex_path}")

        if args.clean and compiled_pdf.exists():
            # Clean auxiliary files via latexmk if available, else remove common aux files
            if LATEXMK:
                subprocess.run([LATEXMK, "-c"], cwd=str(tex_path.parent))
            else:
                for ext in (".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"):
                    p = tex_path.with_suffix(ext)
                    if p.exists():
                        p.unlink(missing_ok=True)

        return (png, True, f"OK: {png}")
    except Exception as e:
        return (tex_path.with_suffix(".png"), False, f"EXCEPTION {tex_path}: {e}")

def find_tex_files(root: Path, recursive: bool) -> list[Path]:
    if recursive:
        return [p for p in root.rglob("*.tex")]
    else:
        return [p for p in root.glob("*.tex")]


def copy_pngs_to_build(png_paths: list[Path], src_root: Path) -> None:
    """Copy given PNG files (which are under src_root) into two build locations:
    _build/html/content/img/ and _build/html/content/content/img/ preserving
    the relative paths from src_root. Creates directories as needed.
    """
    repo_root = Path(__file__).resolve().parent
    targets = [repo_root / "_build" / "html" / "content" / "img",
               repo_root / "_build" / "html" / "content" / "content" / "img"]

    for t in targets:
        t.mkdir(parents=True, exist_ok=True)

    for p in png_paths:
        try:
            if not p.exists():
                continue
            try:
                rel = p.relative_to(src_root)
            except Exception:
                # If the png is not under src_root, fall back to its name only
                rel = Path(p.name)

            for base in targets:
                dest = base / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(p), str(dest))
                print(f"COPIED: {p} -> {dest}")
        except Exception as e:
            print(f"WARNING: failed to copy {p}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Compile .tex files to PDF and PNG.")
    parser.add_argument("--dir", "-d", type=str, default="img", help="Directory to scan (default: ./img)")
    parser.add_argument("--recursive", "-r", action="store_true", help="Recurse into subdirectories")
    parser.add_argument("--dpi", type=int, default=600, help="PNG density (dpi), default 600")
    parser.add_argument("--overwrite", "-f", action="store_true", help="Overwrite existing PNGs")
    parser.add_argument("--crop", action="store_true", help="Run pdfcrop before PNG conversion")
    parser.add_argument("--transparent", action="store_true", help="Keep transparency (do NOT force white background)")
    parser.add_argument("--clean", action="store_true", help="Remove auxiliary LaTeX files after successful build")
    parser.add_argument("--threads", type=int, default=1, help="Number of worker threads (default 1)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose compiler output")
    args = parser.parse_args()

    root = Path(args.dir).expanduser().resolve()
    if not root.exists():
        print(f"ERROR: directory not found: {root}", file=sys.stderr)
        sys.exit(2)

    tex_files = find_tex_files(root, args.recursive)
    if not tex_files:
        print(f"No .tex files found under {root}")
        sys.exit(0)

    print(f"Found {len(tex_files)} .tex file(s) under {root}")

    results = []
    if args.threads > 1:
        with ThreadPoolExecutor(max_workers=args.threads) as ex:
            futures = {ex.submit(process_tex_file, t, args): t for t in tex_files}
            for fut in as_completed(futures):
                png_path, ok, msg = fut.result()
                results.append((png_path, ok, msg))
                print(msg)
    else:
        for t in tex_files:
            png_path, ok, msg = process_tex_file(t, args)
            results.append((png_path, ok, msg))
            print(msg)

    # Copy successfully created PNGs into the build content folders
    successful_pngs = [r[0] for r in results if r[1]]
    if successful_pngs:
        copy_pngs_to_build(successful_pngs, root)

    failed = [r for r in results if not r[1]]
    if failed:
        print(f"\nCompleted with {len(failed)} failure(s).", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nAll done.")
        sys.exit(0)

if __name__ == "__main__":
    main()
