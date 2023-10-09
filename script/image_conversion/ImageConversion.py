from flask import Flask, request, render_template, send_file, redirect, url_for
from PIL import Image
import io
import os
import base64
import tempfile
import random
import string
import urllib.parse  # 导入 urllib.parse 模块

app = Flask(__name__, template_folder='D:\\online_server\\my_python\\script\\image_conversion\\templates')

ALLOWED_EXTENSIONS = {'bmp', 'jpg', 'jpeg', 'png', 'webp'}

# 存储转换后图像的内存字典
converted_images = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_and_convert():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']
        target_format = request.form['format']  # 获取用户选择的格式

        if file.filename == '':
            return "No selected file"

        if file and allowed_file(file.filename):
            original_image = Image.open(file)

            # 生成随机文件名
            random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            # 转换为用户选择的格式
            output_buffer = io.BytesIO()
            original_image.save(output_buffer, format=target_format)
            converted_image = output_buffer.getvalue()
            output_buffer.close()

            # 编码文件名为 URL 安全字符串
            encoded_filename = urllib.parse.quote(random_filename)

            # 存储转换后的图像到内存中
            converted_images[encoded_filename] = (target_format, converted_image)

            # 提供下载链接，引用内存中的图像
            return redirect(url_for('download', filename=encoded_filename))

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    # 解码 URL 安全的文件名
    decoded_filename = urllib.parse.unquote(filename)

    if decoded_filename in converted_images:
        target_format, converted_image = converted_images[decoded_filename]
        return send_file(io.BytesIO(converted_image), as_attachment=True, download_name=f'converted_image.{target_format}')
    else:
        return "File not found"

# 注册自定义过滤器
@app.template_filter('b64encode')
def b64encode_filter(s):
    return base64.b64encode(s).decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)
