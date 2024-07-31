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


# jpeg base64 폐기 (패턴없음) : 알아야할 점 jpg를 base64화 하면 처음이 /9j/ 로 시작함
# png는 가능할지도?
# def carve_base64(fromfile, todir):
#     base64_png_start = b'\x64\x61\x74\x61\x3a'
#     base64_png_end = b'\x3d'

#     data = open(fromfile, 'rb').read()
#     start = 0
#     while True:
#         idx1 = data.find(base64_png_start, start)
#         if idx1 < 0:
#             break
#         idx2 = data.find(base64_png_end, idx1)
#         if idx2 < 0:
#             break

#         base64_jpeg = data[idx1:idx2+2]
#         base64_jpeg_str = base64_jpeg.decode('utf-8')
#         ouput_data = f"<img src={base64_jpeg_str} />"
#         outfilepath = os.path.join(todir, f'{idx1}.html')

#         with open(outfilepath, 'wb') as outfile:
#             outfile.write(ouput_data.encode('utf-8'))

#         print(f'Image saved to {outfilepath}')
#         start = idx2 + 2


def carve_all(dump_dir, image_dir):
    for filename in os.listdir(dump_dir):
        # 폴더 내 파일 명에 따라 변경 (startswith(<start_string>) or endswitdh(<end_string>))
        if filename.startswith("dump"):
            filepath = os.path.join(dump_dir, filename)
            carve_jpg(filepath, image_dir)
            carve_png(filepath, image_dir)
            # carve_base64(filepath, image_dir)


# usage example
carve_all('C:\\Users\\bhlee\\Downloads\\Test\\dump-5',
          'C:\\Users\\bhlee\\Downloads\\Test\\image')
