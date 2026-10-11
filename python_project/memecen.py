from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

def file_explorer():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    return file_path

def meme():
    print("Select an image:")
    image_path = file_explorer()

    if not image_path:
        print("No image selected.")
        return

    # Open image
    image = Image.open(image_path)

    # Resize if too large
    if image.width > 500 or image.height > 500:
        image.thumbnail((500, 500))

    draw = ImageDraw.Draw(image)

    # Input text
    top_text = input("Enter text for top line: ")
    bottom_text = input("Enter text for bottom line: ")

    # Try custom font, fallback if not found
    try:
        font = ImageFont.truetype("arial.ttf", size=40)
    except:
        font = ImageFont.load_default()

    # 🔥 Calculate top text size (FIXED)
    top_bbox = draw.textbbox((0, 0), top_text, font=font)
    top_text_width = top_bbox[2] - top_bbox[0]
    top_text_height = top_bbox[3] - top_bbox[1]

    # 🔥 Calculate bottom text size (FIXED)
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=font)
    bottom_text_width = bottom_bbox[2] - bottom_bbox[0]
    bottom_text_height = bottom_bbox[3] - bottom_bbox[1]

    # Positions
    top_x = (image.width - top_text_width) // 2
    top_y = 10

    bottom_x = (image.width - bottom_text_width) // 2
    bottom_y = image.height - bottom_text_height - 10

    # Draw text with outline
    draw.text(
        (top_x, top_y),
        top_text,
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill="black"
    )

    draw.text(
        (bottom_x, bottom_y),
        bottom_text,
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill="black"
    )

    # Save output
    output_path = "meme.png"
    image.save(output_path)

    print("✅ Meme generated successfully!")
    print(f"Saved as: {output_path}")

# Run
meme()
