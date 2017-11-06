#!/usr/bin/python
import rawpy, imageio, os

#using getcwd just returns python's CWD and not this file's CWD
#so this fixes that
cwd=os.path.dirname(__file__)

#race condition is rare here
if not os.path.exists(os.path.join(cwd, "images_converted")):
    os.mkdir(os.path.join(cwd, "images_converted"))

#loop through only .NEF extensions regardless of case
for c, y in enumerate([x for x in os.listdir(cwd) if str(x[-4:]).upper()==".NEF"]):
    path = os.path.join(cwd, y)
    print(str(c+1)+": converting "+y)
    try:
        raw=rawpy.imread(path)
        rgb = raw.postprocess()
        imageio.imsave(os.path.join(cwd,"images_converted",str(y[:-4])+".jpg"), rgb)
    except:
        print("unable to read source file or save converted image:",path)

