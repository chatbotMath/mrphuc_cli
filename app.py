import streamlit as st
import subprocess
import os

# --- Cấu hình trang ---
st.set_page_config(
    page_title="Giao diện Gemini CLI",
    page_icon="✨",
    layout="wide"
)

# --- Tiêu đề và Giới thiệu ---
st.title("✨ Giao diện Web cho Gemini CLI")
st.caption("Nhập một lệnh cho Gemini và xem kết quả trực tiếp.")
st.markdown("""
---
**Lưu ý quan trọng về xác thực:**
Ứng dụng này được triển khai trên Streamlit Cloud và sử dụng `GEMINI_API_KEY` được cấu hình trong mục 'Secrets' của Streamlit.
`gemini-cli` sẽ tự động sử dụng biến môi trường này để xác thực.
""")

# --- Giao diện người dùng ---
st.header("Nhập lệnh của bạn")

# Sử dụng form để nhóm ô nhập liệu và nút bấm
with st.form(key='gemini_form'):
    user_command = st.text_input(
        "Lệnh cho Gemini:",
        placeholder="Ví dụ: 'Tóm tắt các thay đổi trong repo này ngày hôm qua'",
        label_visibility="collapsed"
    )
    submit_button = st.form_submit_button(label='🚀 Thực thi')

# --- Logic xử lý ---
if submit_button and user_command:
    with st.spinner(f"Đang thực thi lệnh: `gemini {user_command}`..."):
        try:
            # Lệnh để chạy gemini-cli
            # Chúng ta truyền lệnh của người dùng như một đối số duy nhất
            # check=False để ngăn script dừng lại nếu có lỗi, chúng ta sẽ tự xử lý lỗi
            command = ['gemini', user_command]

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                # Đảm bảo API key từ Streamlit Secrets được sử dụng
                env=os.environ
            )
            
            st.markdown("---")
            st.header("Kết quả")

            # Hiển thị kết quả thành công
            if result.stdout:
                st.subheader("✅ Output:")
                st.code(result.stdout, language='bash')

            # Hiển thị lỗi (nếu có)
            if result.stderr:
                st.subheader("❌ Lỗi:")
                st.error(result.stderr)

        except FileNotFoundError:
            st.error(
                "Lỗi: Lệnh 'gemini' không được tìm thấy.\n"
                "Điều này có thể xảy ra nếu `setup.sh` không chạy đúng cách trên Streamlit Cloud."
            )
        except Exception as e:
            st.error(f"Đã xảy ra một lỗi không mong muốn: {e}")
elif submit_button:
    st.warning("Vui lòng nhập một lệnh để thực thi.")
