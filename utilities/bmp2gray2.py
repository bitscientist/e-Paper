# Convert .bmp to 2-level grayscale (monochrome) and pack into 1-bit values for e-Paper display
try:
    from PIL import Image
except ImportError:
    print("Please install the Python Imaging Library (PIL) with 'pip install pillow'")

import numpy as np

def convert_to_2_level_grayscale(file_path):
    try:
        with Image.open(file_path) as img:
            # Convert the image to grayscale
            img = img.convert('L')
            
            # Normalize the pixel values to 2 levels (0, 255)
            img_np = np.array(img)
            img_np = (img_np // 128) * 255

            # Flatten the array to get a list of pixel values
            pixel_values = img_np.flatten().tolist()

            # Create the 2-level monochrome image
            img_2level = Image.fromarray(img_np.astype('uint8'), 'L')

            return pixel_values, img_2level

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def map_to_1bit_and_pack(values):
    # Map the 2-level grayscale values to 1-bit values
    mapping = {0: 0b0, 255: 0b1}
    bit_values = [mapping[value] for value in values]

    # Pack the 1-bit values into bytes
    packed_bytes = bytearray()
    for i in range(0, len(bit_values), 8):
        byte = 0
        for j in range(8):
            if i + j < len(bit_values):
                byte |= (bit_values[i + j] << (7 - 1 * j))
        #packed_bytes.append(~byte & 0xFF)
        packed_bytes.append(byte)
    
    # Convert the bytearray to a list of integers
    packed_list = list(packed_bytes)
    return packed_list

def list_to_hex_file(values, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(f"const unsigned char gImage[{len(values)}]"+" = {\n")
            for i in range(0, len(values), 16):
                hex_values = [f"0x{value:02X}" for value in values[i:i+16]]
                line = ", ".join(hex_values)
                file.write(f"{line},\n")
            file.write("};\n")
        print(f"File {file_path} saved successfully")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'pandatree.bmp'
pixel_values, image2 = convert_to_2_level_grayscale(file_path)
#print(pixel_values)
packed_bytes = map_to_1bit_and_pack(pixel_values)
#print(packed_bytes)
list_to_hex_file(packed_bytes, 'pandatree2.c')

# Display the 2-level monochrome image
image2.show()
