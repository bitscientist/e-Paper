# use pillow to create a bitmap file

from PIL import Image, ImageDraw, ImageFont

output_path = 'imagedraw.bmp'
# Create a new image with a white background
#img = Image.new('L', (400, 300), color=255)
img = Image.new('1', (400, 300), color=1)
    
# Create a drawing object
draw = ImageDraw.Draw(img)

# Draw text
fnt = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 48)
draw.text((50, 10), "Hello, World!", font=fnt, fill=0)
fnt = ImageFont.truetype('C:/Windows/Fonts/Verdana.ttf', 48)
draw.text((50, 100), "Hello, World!", font=fnt, fill=0)
fnt = ImageFont.truetype('C:/Windows/Fonts/Tahoma.ttf', 48)
draw.text((50, 200), "Hello, World!", font=fnt, fill=0)

# Draw a rectangle
rectangle_bbox=(10, 10, 390, 290)
draw.rectangle(rectangle_bbox, fill=None, outline=0, width=5)
 
# Save the image
img.save(output_path)
print(f"Image {output_path} saved successfully")
img.show()
