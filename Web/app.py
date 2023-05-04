import io
from flask import Flask, render_template, send_file
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    # 读取图像文件
    image = Image.open("./static/OIP.jpg")

    # 旋转图像180度
    rotated_image = image.rotate(180)

    # 将图像文件内容存储到内存缓冲区中
    output_buffer = io.BytesIO()
    rotated_image.save(output_buffer, format='JPG')
    output_buffer.seek(0)

    # 将缓冲区中的图像数据传递给render_template函数，通过模板引擎将图像内容嵌入到HTML页面中
    return render_template('result.html', out=output_buffer)


@app.route('/image')
def get_image():
    # 获取缓冲区中的图像数据并返回
    output_buffer = io.BytesIO()
    image = Image.open('path/to/image.png')
    image.save(output_buffer, 'JPG')
    output_buffer.seek(0)
    return send_file(output_buffer, mimetype='image/png')


if __name__ == '__main__':
    app.run()
