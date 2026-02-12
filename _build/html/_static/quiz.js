document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".quiz-item[data-correct], .quiz-item[data-correct-label]");
  const section = document.querySelector(".chapter-quiz");
  const chapterId = section?.getAttribute("data-chapter") || "x";

  items.forEach((item, i) => {
    // Controls container
    const bar = document.createElement("div");
    bar.className = "quiz-controls";

    // Bootstrap buttons
    const btnTrue  = document.createElement("button");
    const btnFalse = document.createElement("button");
    btnTrue.type = btnFalse.type = "button";
    // start as outlines; we'll flip to solid + active when selected
    btnTrue.className  = "btn btn-sm btn-outline-success";
    btnFalse.className = "btn btn-sm btn-outline-danger";
    btnTrue.textContent  = "DA";
    btnFalse.textContent = "NE";

    bar.appendChild(btnTrue);
    bar.appendChild(btnFalse);
    item.appendChild(bar);

    const correctBool  = item.getAttribute("data-correct");         // "true" | "false" | null
    const correctLabel = item.getAttribute("data-correct-label");   // optional future use

    function setButtons(choice /* "true" | "false" */) {
      // reset classes to outlines
      btnTrue.className  = "btn btn-sm btn-outline-success";
      btnFalse.className = "btn btn-sm btn-outline-danger";
      btnTrue.ariaPressed  = "false";
      btnFalse.ariaPressed = "false";

      // activate selected
      if (choice === "true") {
        btnTrue.className = "btn btn-sm btn-success active";
        btnTrue.ariaPressed = "true";
      } else if (choice === "false") {
        btnFalse.className = "btn btn-sm btn-danger active";
        btnFalse.ariaPressed = "true";
      }
    }

    function markResult(choice /* "true" | "false" */) {
      item.classList.remove("is-correct", "is-wrong");
      // Only compute correctness for true/false questions
      if (correctBool === "true" || correctBool === "false") {
        const isTrueCorrect = (correctBool === "true");
        const userPickedTrue = (choice === "true");
        const ok = (userPickedTrue === isTrueCorrect);
        item.classList.add(ok ? "is-correct" : "is-wrong");
      }
    }

    function lockButtons() {
      // lock both buttons so the answer can’t be changed
      btnTrue.disabled = true;
      btnFalse.disabled = true;
      btnTrue.setAttribute("aria-disabled", "true");
      btnFalse.setAttribute("aria-disabled", "true");
      // flag on the item (useful if you later need to check)
      item.dataset.locked = "1";
    }

    function applyChoice(choice) {
      // if already locked, ignore clicks
      if (item.dataset.locked === "1") return;
      setButtons(choice);
      markResult(choice);
      lockButtons();
    }

    // Click handlers
    btnTrue.addEventListener("click",  () => applyChoice("true"));
    btnFalse.addEventListener("click", () => applyChoice("false"));

    // Restore previous selection (if any)
    
  });
});
