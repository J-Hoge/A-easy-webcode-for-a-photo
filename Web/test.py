import os
import webbrowser
from flask import Flask, request, render_template, send_file
import logging
from PIL import Image
import io

logging.getLogger('werkzeug').disabled = True
# 禁用Flask开发服务器输出的日志信息，包括一些警告信息。这可以使Flask应用程序启动时不会在控制台输出过多的日志信息。

webbrowser.open('http://localhost:5000')  # 在默认浏览器中打开应用程序的首页。这可以帮助你快速测试你的应用程序，并且可以方便地在浏览器中查看应用程序的UI界面。

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取上传的文件
        file = request.files['file']

        # 读取图像文件
        image = Image.open(file)

        # 以下是处理过程，在这我们仅仅将他旋转180度
        # 旋转图像180度
        rotated_image = image.rotate(180)

        # 将图像文件内容存储到内存缓冲区中
        output_buffer = io.BytesIO()
        rotated_image.save(output_buffer, format='JPEG')
        output_buffer.seek(0)

        # 返回图像文件内容
        return send_file(output_buffer, mimetype='image/jpeg')
    else:
        return render_template('index2.html')


if __name__ == '__main__':
    app.run()
