
import os
import streamlit as st

# 创建一个文件夹用于保存上传的文件
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# 页面标题和说明文字
st.title("AI绘画体验馆")
st.write("请上传需要设计的草图")
markdown_files = ["AI绘画"]
selected_file = st.sidebar.selectbox("选择要阅读的博文", markdown_files)

# 选择文件并重命名
uploaded_file = st.file_uploader("选择文件", type=["png", "jpg"])


# 保存文件
if uploaded_file is not None:
    if file_name.strip():
        file_path = os.path.join("uploads", file_name+".docx")
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"已保存文件: {file_path}")
    else:
        st.error("请上传需要设计的草图")
