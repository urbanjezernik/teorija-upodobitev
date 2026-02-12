-- works with Pandoc 3.x
local pandoc = require 'pandoc'

function Table(tbl)
  local html = pandoc.write(pandoc.Pandoc{tbl}, 'html')
  html = html:gsub(
    '<table(.-)>',
    '<div class="pst-scrollable-table-container">' ..
    '<table class="table table-striped table-hover table-sm"%1>')
  html = html:gsub('</table>', '</table></div>')
  return pandoc.RawBlock('html', html)
end
