-- Works with Pandoc 3.x
local pandoc = require 'pandoc'

-- helper: add a class once
local function add_class(attr, class)
  for _,c in ipairs(attr.classes) do
    if c == class then return attr end
  end
  local id, cls, kv = attr.identifier, attr.classes, attr.attributes
  cls[#cls+1] = class
  return pandoc.Attr(id, cls, kv)
end

function Table (tbl)
  for _,class in ipairs{
        "table", "table-striped", "table-hover", "table-sm"} do
    tbl.attr = add_class(tbl.attr, class)
  end
  return tbl
end
