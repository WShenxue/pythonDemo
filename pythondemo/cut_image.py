# _*_ coding:utf8 _*_
from PIL import Image


def fill_image(img):
    width, height = img.size
    new_image_length = width if width > height else height
    new_image = Image.new(img.mode, (new_image_length, new_image_length), color='white')
    if width > height:
        new_image.paste(img(0, int(new_image_length - height) / 2))
    elif width < height:
        new_image.paste(img, int(new_image_length - width) / 2, 0)
    else:
        # 增加同样大小图片处理
        new_image = img
    return new_image


def cut_image(img):
    width, height = img.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    cut_image_list = [img.crop(box) for box in box_list]
    return cut_image_list


def save_image(image_list):
    index = 1
    for image in image_list:
        image.save('./../resources/cut_image' + str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "./../resources/cut_image.jpg"
    image = Image.open(file_path)
    image = fill_image(image)
    image_list = cut_image(image)
    save_image(image_list)
