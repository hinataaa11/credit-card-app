from pathlib import Path
from io import BytesIO
import sys, urllib.request
from PIL import Image, ImageOps, ImageDraw

FILE_ID='1dY17XUanKaZeuvKA5sj9UqNayqbuqhoe'
URL=f'https://drive.google.com/uc?export=download&id={FILE_ID}'
OUT=Path(__file__).resolve().parents[1]/'assets'

def square(im, size, pad=0):
    im=im.convert('RGBA')
    side=max(im.size)
    canvas=Image.new('RGBA',(side,side),(255,255,255,0))
    canvas.alpha_composite(im,((side-im.width)//2,(side-im.height)//2))
    if pad:
        inner=int(size*(1-pad*2))
        resized=ImageOps.contain(canvas,(inner,inner),Image.Resampling.LANCZOS)
        result=Image.new('RGBA',(size,size),(17,24,39,255))
        result.alpha_composite(resized,((size-resized.width)//2,(size-resized.height)//2))
        return result
    return ImageOps.fit(canvas,(size,size),method=Image.Resampling.LANCZOS,centering=(0.5,0.5))

try:
    req=urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req,timeout=30) as r:
        data=r.read()
    im=Image.open(BytesIO(data)); im.load()
    square(im,192).save(OUT/'icon-192.png')
    square(im,512).save(OUT/'icon-512.png')
    square(im,512,pad=0.10).save(OUT/'icon-maskable-512.png')
    print('Drive icon downloaded and generated successfully.')
except Exception as e:
    print(f'WARNING: could not download Drive icon: {e}', file=sys.stderr)
    print('Keeping the bundled fallback icons.', file=sys.stderr)
