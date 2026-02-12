-- helper stays unchanged -----------------------------------------------
local pandoc = require 'pandoc'
local function wrap(html)
  html = html:gsub('<table(.-)>',
          '<div class="pst-scrollable-table-container">' ..
          '<table class="table table-striped table-hover table-sm"%1>')
  return html:gsub('</table>', '</table></div>')
end

------------------------------------------------------------------------
-- 1 ✓ regular Pandoc tables – unchanged
function Table(tbl)
  local html = pandoc.write(pandoc.Pandoc{tbl}, 'html')
  return pandoc.RawBlock('html', wrap(html))
end

-- the quick test we use for “this is that ugly pipe-table”
local function looks_like_pipe_table(txt)
  return txt:match('^%s*|')            -- starts with a pipe
     and txt:find('\\begin{pmatrix}')  -- contains the matrix header
end

-- 2 ✓ paragraphs that Pandoc tagged as **Para**
function Para(el)
  local txt = pandoc.utils.stringify(el)
  if looks_like_pipe_table(txt) then
    local html = pandoc.pipe('pandoc',
        { '-f', 'latex', '-t', 'html', '--mathjax' }, txt)
    return pandoc.RawBlock('html', wrap(html))
  end
end

-- 3 ✓ paragraphs that Pandoc tagged as **Plain** (your case)
function Plain(el)
  local txt = pandoc.utils.stringify(el)
  if looks_like_pipe_table(txt) then
    local html = pandoc.pipe('pandoc',
        { '-f', 'latex', '-t', 'html', '--mathjax' }, txt)
    return pandoc.RawBlock('html', wrap(html))
  end
end
