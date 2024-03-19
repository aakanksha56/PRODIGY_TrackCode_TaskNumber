
def encrypt_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.load()
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            encrypted_r = g
            encrypted_g = b
            encrypted_b = r
            pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)
    
    encrypted_image_path = 'encrypted_' + image_path
    image.save(encrypted_image_path)
    
    return encrypted_image_path

def decrypt_image(encrypted_image_path):
    image = Image.open(encrypted_image_path)
    width, height = image.size
    pixels = image.load()
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            decrypted_r = b
            decrypted_g = r
            decrypted_b = g
            pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)
    
    decrypted_image_path = 'decrypted_' + encrypted_image_path
    image.save(decrypted_image_path)
    
    return decrypted_image_path