# imgtextify-py3

"Textify" images using Python 3 and PIL

## USAGE
### imgtexify
textify one image


`python3 imgtextify.py [imgpath] [x-res] [thresh] [darkchar] [lightchar] [num_newlines] [nospaces]`

- imgpath - path to image (jpg, png, anything PIL can handle)
- x-res - number of columns in output (y-res is scaled accordingly) (default 20)
- thresh - threshold brightness (0-255) inclusive to print lightchar instead of darkchar (default 150)
- darkchar - character to print for dark squares (default `*`)
- lightchar - character to print for light squares (default `.`)
- num_newlines = number of newlines (- 1) in between lines (default 1)
- nospaces - if an argument is passed here, do NOT print spaces in between output characters (default with spaces)

note that the darkchar and lightchar can be multiple characters, given that you properly escape needed characters (like parentheses)

### imgtextify2
textify two images and interlace


`python3 imgtextify2.py [imgpath] [imgpath2] [x-res] [thresh] [thresh2] [darkchar] [lightchar] [darkchar2] [lightchar2] [num_newlines] [nospaces]`

- thresh2 - threshold brightness (0-255) inclusive for second image to print lightchar instead of darkchar (default 150)
- imgpath2 - path to second image (jpg, png, anything PIL can handle), resized to dimensions of first image
- darkchar2 - character to print for dark squares in second image (default `@`)
- lightchar2 - character to print for light squares in second image (default `-`)

`python3 imgtextify3.py [imgpath] [imgpath2] [imgpath3] [x-res] [thresh] [thresh2] [thresh3] [darkchar] [lightchar] [darkchar2] [lightchar2] [darkchar3] [lightchar3] [num_newlines] [nospaces]`

- thresh3 - threshold brightness (0-255) inclusive for third image to print lightchar instead of darkchar (default 150)
- imgpath3 - path to third image (jpg, png, anything PIL can handle), resized to dimensions of first image
- darkchar3 - character to print for dark squares in third image (default `o`)
- lightchar3 - character to print for light squares in third image (default `_`)

## LICENSE

GPL v3
