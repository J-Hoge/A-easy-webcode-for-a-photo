import numpy as np
from flask import Flask, render_template
import base64

app = Flask(__name__)


@app.route("/")
def index():
    # 读取图像文件并编码为base64字符串
    with open("./static/OIP.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # 渲染HTML模板并传递base64编码的图像数据
    return render_template("temp.html", image_data=encoded_string)


if __name__ == "__main__":
    app.run(debug=True)


