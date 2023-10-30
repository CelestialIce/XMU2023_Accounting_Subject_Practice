from PIL import Image


def convert_dark_png_images(input_folder, output_folder, threshold=100):
    # 遍历文件夹中的所有PNG图片
    import os
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(
                output_folder, filename.replace(".png", "_tra.png"))

            # 打开PNG图片
            image = Image.open(input_path)

            # 转换图片中的比较黑色的部分为纯黑色
            width, height = image.size
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x, y))
                    # 计算颜色的亮度（灰度）
                    brightness = (pixel[0] + pixel[1] + pixel[2]) / 3
                    if brightness < threshold and pixel[3] > 0:  # 如果比较黑色且不是透明
                        image.putpixel(
                            (x, y), (55, 255, 25, pixel[3]))  # 转换为纯黑色

            # 保存转换后的图片
            image.save(output_path)


if __name__ == "__main__":
    input_folder = "./"  # 输入文件夹路径
    output_folder = "./"  # 输出文件夹路径
    threshold = 100  # 亮度阈值，用于判断哪些部分是比较黑色的

    convert_dark_png_images(input_folder, output_folder, threshold)
