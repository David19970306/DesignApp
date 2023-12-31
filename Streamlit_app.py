
import os
import streamlit as st
from PIL import Image
from tempfile import NamedTemporaryFile
# 创建一个文件夹用于保存上传的文件
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# 页面标题和说明文字
st.title("AI绘画体验馆")
st.write("请上传需要设计的草图")
markdown_files = ["AI绘画"]
selected_file = st.sidebar.selectbox("选择要使用的功能", markdown_files)

# 选择文件并重命名
uploaded_file = st.file_uploader("选择文件", type=["png", "jpg"])
# 保存文件
if uploaded_file is not None:
    temp_file = NamedTemporaryFile(delete=True)
    buffer = uploaded_file.getbuffer()
    if buffer:
        temp_file.write(buffer)
        image_file = open(temp_file.name, 'rb')
        image_bytes = image_file.read()
        st.image(image_bytes)
    else:
        st.error("请上传需要设计的草图")


# 请选择一个设计风格
designStyle = st.selectbox(
   "请选择一个设计风格",
   ('北欧风格', '工业风格', '极简风格'),
   index=None,
   placeholder="请选择一个设计风格...",
)
if designStyle == '北欧风格':
    st.write('北欧风格')
else:
    st.write("你还没有选择设计风格")


# 请选择一个AI权重
weight = st.slider('ai weight:', 0.0, 0.1, 1.0)
st.write("AI权重为：", weight)

if st.button('开始生成'):
    st.write('生成如下')
else:
    st.write('Goodbye')

    


