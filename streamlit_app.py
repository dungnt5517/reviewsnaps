import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="ReviewSnaps V2", layout="centered")

st.title("⭐ ReviewSnaps V2 – Tạo ảnh review bắt mắt như bài đăng Facebook!")

with st.form("review_form"):
    name = st.text_input("👤 Tên người đánh giá", "Nguyễn Thị A")
    rating = st.slider("⭐ Số sao", 1, 5, 5)
    content = st.text_area("💬 Nội dung đánh giá", "Sản phẩm dùng siêu thích, giao hàng nhanh cực kỳ, 5 sao luôn!")
    submitted = st.form_submit_button("🎨 Tạo ảnh review")

if submitted:
    # Khởi tạo canvas
    width, height = 600, 320
    bg_color = "#fef9f4"
    card_color = "white"

    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Fonts
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
        font_text = ImageFont.truetype("DejaVuSans.ttf", 20)
    except:
        font_title = font_text = ImageFont.load_default()

    # Card bo góc trắng ở giữa
    draw.rounded_rectangle([(20, 20), (width - 20, height - 20)], radius=20, fill=card_color)

    # Avatar tròn với chữ cái đầu
    draw.ellipse((40, 40, 90, 90), fill="#d1d5db")
    draw.text((54, 55), name[0].upper(), font=font_title, fill="black")

    # Tên người dùng
    draw.text((110, 50), name, font=font_title, fill="black")

    # Rating
    draw.text((110, 85), "⭐️" * rating, font=font_text, fill="#f59e0b")

    # Nội dung review
    draw.text((40, 140), content, font=font_text, fill="black")

    # Xuất ảnh
    st.image(img, caption="✅ Ảnh review đã tạo", use_container_width=False)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Tải ảnh về",
        data=byte_im,
        file_name="review_v2.png",
        mime="image/png"
    )
