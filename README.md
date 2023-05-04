# A-easy-web-code-for-a-photo
It's a easy web writed by python Flask. It can be used to choose a photo in local and then do something with your python code.

如果要使用首先要注意：Web下的static和templates两个文件夹一定要保留，不要把里面的文件单独拿出来
现在简单介绍一下：首先运行test.py，他会打开index2.html，在里面可以选择本地图片，然后传回py文件，还有一些其他css和js代码就不介绍了
```python
 # 读取图像文件
 image = Image.open(file)
```
然后我们对image进行操作了，现在只是简单的旋转180度，将他换成字符识别的模型就可以了，现在感觉可行的方案是把那个代码做成个函数，或者能不能把他传到另一个py文件里，但是最后都要在index()函数中返回结果，这样才会跳转到呈现结果的页面
```py
# 将图像文件内容存储到内存缓冲区中
        output_buffer = io.BytesIO()
        rotated_image.save(output_buffer, format='JPEG')
        output_buffer.seek(0)

        # 返回图像文件内容
        return send_file(output_buffer, mimetype='image/jpeg')
```
