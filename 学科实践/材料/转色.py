from PIL import Image
import os


def convert_dark_png_images(input_folder):
    # 遍历文件夹中的所有PNG图片
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)

            # 打开PNG图片
            image = Image.open(input_path)

            # 转换图片中的比较黑色部分为绿色
            width, height = image.size
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x, y))
                    # 计算颜色的亮度（灰度）
                    brightness = (pixel[0] + pixel[1] + pixel[2]) / 3
                    # 如果颜色较暗（根据需要调整阈值），将其转换为绿色
                    if brightness < 50 and pixel[3] > 0:  # 50是一个示例阈值，您可以根据需要调整
                        image.putpixel((x, y), (55, 255, 25, 255))  # 转换为绿色

            # 保存转换后的图片，覆盖原始文件
            image.save(input_path)


if __name__ == "__main__":
    input_folder = "./"  # 输入文件夹路径

    convert_dark_png_images(input_folder)
