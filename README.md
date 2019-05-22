# imgtextify-py3

"Textify" images using Python 3 and PIL

## USAGE
`python3 imgtextify.py [imgpath] [x-res] [thresh] [darkchar] [lightchar] [num_newlines] [nospaces]`

- imgpath - path to image (jpg, png, anything PIL can handle)
- x-res - number of columns in output (y-res is scaled accordingly) (default 20)
- thresh - threshold brightness (0-255) inclusive to print lightchar instead of darkchar (default 150)
- darkchar - character to print for dark squares (default *)
- lightchar - character to print for light squares (default .)
- num_newlines = number of newlines (- 1) in between lines (default 1)
- nospaces - if an argument is passed here, do NOT print spaces in between output characters (default with spaces)


note that the darkchar and lightchar can be multiple characters, given that you properly escape needed characters (like parentheses)

## LICENSE

GPL v3
