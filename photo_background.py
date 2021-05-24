import removebg
from PIL import Image


if __name__ == '__main__':
    rmbg = removebg.RemoveBg("8g7Fy3Q4N9uwZHmQFUz718aa", "error.log")

    out_path = r"E:\abc.jpg"
    rmbg.remove_background_from_img_file(img_file_path=out_path, bg_color='red')

    img = Image.open(out_path + "_no_bg.png")
    i = img.resize((358, 441), Image.ANTIALIAS)
    i.save(r"E:\bbb.png", quality=0)


