from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def xor_encrypt(text, password):
    return ''.join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(text))

def hide_text(image_path, output_path, secret_text, password=None):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Encrypt the message if password is given
    if password:
        secret_text = xor_encrypt(secret_text, password)
    
    binary_secret = text_to_binary(secret_text) + '1111111111111110'  # EOF marker
    binary_index = 0

    pixels = list(img.getdata())
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_secret):
            r = (r & ~1) | int(binary_secret[binary_index])
            binary_index += 1
        if binary_index < len(binary_secret):
            g = (g & ~1) | int(binary_secret[binary_index])
            binary_index += 1
        if binary_index < len(binary_secret):
            b = (b & ~1) | int(binary_secret[binary_index])
            binary_index += 1
        new_pixels.append((r, g, b))
    
    if binary_index < len(binary_secret):
        raise ValueError("Message is too long for this image.")

    img.putdata(new_pixels)
    img.save(output_path)
    print(f"✅ Secret text hidden and saved to '{output_path}'.")
