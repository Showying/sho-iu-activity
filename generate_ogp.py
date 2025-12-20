from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
WIDTH = 1200
HEIGHT = 630
BG_COLOR = "#FFFFFF"  # White
TEXT_COLOR = "#002B49"  # Navy Blue
SUBTEXT_COLOR = "#555555"
ACCENT_COLOR = "#C4A77D" # Gold

# Paths
PROFILE_IMG_PATH = "public/images/profile/Sho T 14.png"
OUTPUT_PATH = "public/ogp.png"

def create_ogp():
    # Create base image
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Add corner accents
    draw.polygon([(0, 0), (150, 0), (0, 150)], fill=ACCENT_COLOR) # Top left
    draw.polygon([(WIDTH, HEIGHT), (WIDTH-150, HEIGHT), (WIDTH, HEIGHT-150)], fill=ACCENT_COLOR) # Bottom right

    # Load and process profile image
    try:
        profile_img = Image.open(PROFILE_IMG_PATH).convert("RGBA")
        
        # Resize/Crop profile image to circle
        size = 400
        profile_img = profile_img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Create circular mask
        mask = Image.new('L', (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, size, size), fill=255)
        
        # Apply mask
        output_profile = Image.new('RGBA', (size, size), (0,0,0,0))
        output_profile.paste(profile_img, (0, 0), mask)
        
        # Paste onto main image
        img.paste(output_profile, (100, (HEIGHT - size) // 2), output_profile)
        
    except Exception as e:
        print(f"Error processing profile image: {e}")
        # Fallback placeholder
        draw.ellipse((100, (HEIGHT - 400) // 2, 500, (HEIGHT - 400) // 2 + 400), fill="#cccccc")

    # Add Text
    # Note: Using default font if custom font not found, but trying to load a system font if possible
    try:
        # Mac standard font location
        title_font = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 90, index=1) # Bold
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 32, index=0) # Regular
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    # Draw Text
    text_x = 550
    draw.text((text_x, 220), "Sho T Lab.", font=title_font, fill=TEXT_COLOR)
    
    # Draw Divider
    draw.rectangle([text_x, 340, text_x + 100, 346], fill=ACCENT_COLOR)
    
    draw.text((text_x, 370), "高橋 翔", font=subtitle_font, fill=SUBTEXT_COLOR)
    draw.text((text_x, 420), "iU情報経営イノベーション専門職大学", font=subtitle_font, fill=SUBTEXT_COLOR)
    draw.text((text_x, 470), "客員教授 活動実績", font=subtitle_font, fill=SUBTEXT_COLOR)

    # Save
    img.save(OUTPUT_PATH)
    print(f"OGP Image saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    create_ogp()
