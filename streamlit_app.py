import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="ReviewSnaps", layout="centered")

st.title("⭐ ReviewSnaps – Tạo ảnh review đẹp chỉ trong 5 giây!")

# Nhập thông tin review
with st.form("review_form"):
    name = st.text_input("👤 Tên người đánh giá", "Nguyễn Thị A")
    rating = st.slider("⭐ Số sao", 1, 5, 5)
    content = st.text_area("💬 Nội dung đánh giá", "Sản phẩm dùng siêu thích, giao hàng nhanh cực kỳ, 5 sao luôn!")
    submitted = st.form_submit_button("🎨 Tạo ảnh review")

if submitted:
    # Tạo ảnh nền trắng
    width, height = 600, 300
    img = Image.new("RGB", (width, height), color="#ffffff")
    draw = ImageDraw.Draw(img)

    # Load font (dự phòng nếu server không có font chuẩn)
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 20)
    except:
        font_title = font_text = ImageFont.load_default()

    # Vẽ nội dung lên ảnh
    draw.text((30, 30), name, font=font_title, fill="black")
    draw.text((30, 70), "⭐" * rating, font=font_text, fill="#f59e0b")
    draw.text((30, 120), content, font=font_text, fill="black")

    # Hiển thị ảnh
    st.image(img, caption="✅ Ảnh review đã tạo", use_column_width=False)

    # Cho phép tải ảnh
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Tải ảnh về",
        data=byte_im,
        file_name="review.png",
        mime="image/png"
    )
