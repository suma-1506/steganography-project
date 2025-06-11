from PIL import Image

def binary_to_text(binary):
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)

def xor_decrypt(text, password):
    return ''.join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(text))

def reveal_text(image_path, password=None):
    img = Image.open(image_path)
    binary_data = ""
    
    pixels = list(img.getdata())
    for pixel in pixels:
        for color in pixel[:3]:  # RGB
            binary_data += str(color & 1)
    
    eof_index = binary_data.find('1111111111111110')
    if eof_index == -1:
        raise ValueError("No hidden message found.")

    binary_data = binary_data[:eof_index]
    text = binary_to_text(binary_data)

    if password:
        text = xor_decrypt(text, password)
    
    return f"🔓 Hidden message: {text}"
