import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

st.set_page_config(page_title="ReviewSnaps V3", layout="centered")

st.title("⭐ ReviewSnaps V3 – Ảnh review chuyên nghiệp, sẵn sàng chia sẻ!")

with st.form("review_form"):
    name = st.text_input("👤 Tên người đánh giá", "Nguyễn Thị A")
    rating = st.slider("⭐ Số sao", 1, 5, 5)
    content = st.text_area("💬 Nội dung đánh giá", "Sản phẩm dùng siêu thích, giao hàng nhanh cực kỳ, 5 sao luôn!")
    submitted = st.form_submit_button("🎨 Tạo ảnh review")

if submitted:
    # Cấu hình
    width, height = 600, 360
    bg_color = "#fef9f4"
    card_color = "white"

    # Tạo canvas
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Font
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 26)
        font_text = ImageFont.truetype("DejaVuSans.ttf", 20)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 16)
    except:
        font_title = font_text = font_small = ImageFont.load_default()

    # Card bo góc giữa nền
    card_x0, card_y0 = 30, 30
    card_x1, card_y1 = width - 30, height - 30
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=25, fill=card_color)

    # Avatar tròn
    avatar_size = 50
    avatar_x = (width - avatar_size) // 2
    draw.ellipse((avatar_x, 50, avatar_x + avatar_size, 50 + avatar_size), fill="#d1d5db")
    draw.text((avatar_x + 15, 58), name[0].upper(), font=font_title, fill="black")

    # Tên căn giữa
    name_width = draw.textlength(name, font=font_title)
    draw.text(((width - name_width) / 2, 110), name, font=font_title, fill="black")

    # Hiển thị sao bằng icon
    star_icon_path = "star.png"  # file PNG hình sao vàng (32x32)
    if os.path.exists(star_icon_path):
        star_img = Image.open(star_icon_path).resize((24, 24))
        star_total_width = rating * 26
        start_x = (width - star_total_width) // 2
        for i in range(rating):
            img.paste(star_img, (start_x + i * 26, 150), star_img)
    else:
        draw.text(((width - 100) / 2, 150), "⭐" * rating, font=font_text, fill="#f59e0b")

    # Nội dung review (tự động xuống dòng)
    text_box_width = width - 100
    words = content.split()
    lines = []
    line = ""
    for word in words:
        test_line = line + word + " "
        if draw.textlength(test_line, font=font_text) < text_box_width:
            line = test_line
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    y_text = 190
    for line in lines:
        line_width = draw.textlength(line, font=font_text)
        draw.text(((width - line_width) / 2, y_text), line, font=font_text, fill="black")
        y_text += 30

    # Logo nhỏ hoặc verified
    footer = "✅ Verified Buyer"
    footer_width = draw.textlength(footer, font=font_small)
    draw.text((width - footer_width - 40, height - 50), footer, font=font_small, fill="#6b7280")

    # Hiển thị ảnh
    st.image(img, caption="✅ Ảnh review đã tạo", use_container_width=False)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Tải ảnh về",
        data=byte_im,
        file_name="review_pro.png",
        mime="image/png"
    )
