import os


def carve_jpg(fromfile, todir):
    jpgstart = b'\xff\xd8'
    jpgend = b'\xff\xd9'

    data = open(fromfile, 'rb').read()
    start = 0
    while True:
        idx1 = data.find(jpgstart, start)
        if idx1 < 0:
            break
        idx2 = data.find(jpgend, idx1)
        if idx2 < 0:
            break

        jpgdata = data[idx1:idx2+2]

        outfilepath = os.path.join(todir, f'{idx1}.jpg')

        with open(outfilepath, 'wb') as outfile:
            outfile.write(jpgdata)

        print(f'Image saved to {outfilepath}')
        start = idx2 + 2


def carve_png(fromfile, todir):
    pngstart = b'\x89\x50\x4e\x47'
    pngend = b'\xae\x42\x60\x82'

    data = open(fromfile, 'rb').read()
    start = 0
    while True:
        idx1 = data.find(pngstart, start)
        if idx1 < 0:
            break
        idx2 = data.find(pngend, idx1)
        if idx2 < 0:
            break

        pngdata = data[idx1:idx2+4]

        outfilepath = os.path.join(todir, f'{idx1}.png')

        with open(outfilepath, 'wb') as outfile:
            outfile.write(pngdata)

        print(f'Image saved to {outfilepath}')
        start = idx2 + 4


def carve_all(dump_dir, image_dir):
    for filename in os.listdir(dump_dir):
        if filename.endswith(".data"):
            filepath = os.path.join(dump_dir, filename)
            carve_jpg(filepath, image_dir)
            carve_png(filepath, image_dir)


# usage example
carve_all('메모리 덤프 폴더 경로', '이미지 저장 폴더 경로')
