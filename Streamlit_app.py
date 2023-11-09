
import os
import streamlit as st

# 创建一个文件夹用于保存上传的文件
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# 页面标题和说明文字
st.title("智能BG201作业提交")
st.write("请上传Word类型的文件，并输入学号+姓名来命名该文件")

# 选择文件并重命名
file_name = st.text_input("输入学号+姓名")
uploaded_file = st.file_uploader("选择文件", type="docx")


# 保存文件
if uploaded_file is not None:
    if file_name.strip():
        file_path = os.path.join("uploads", file_name+".docx")
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"已保存文件: {file_path}")
    else:
        st.error("请输入学号+姓名来命名文件")
