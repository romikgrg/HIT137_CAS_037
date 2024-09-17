# Chapter 1 : The Gatekeeper
from PIL import Image
import numpy as np
import time

def modify_image_and_calculate_red_sum(image_path, output_path, n):
    # Load the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Modify the image by adding 'n' to each pixel's RGB values
    modified_image_array = np.clip(image_array + n, 0, 255) 

    # Create a new Image from the modified array
    modified_image = Image.fromarray(modified_image_array.astype('uint8'))

    # Save the modified image
    modified_image.save(output_path)

    # Calculate the sum of all red values in the modified image
    red_sum = np.sum(modified_image_array[:, :, 0])
    
    return red_sum

# Calculate 'n' based on the current time
current_time = int(time.time())
n = (current_time % 100) + 50
if n % 2 == 0:
    n += 10

# File paths
image_path = "chapter1.jpg"  
output_path = "chapter1out.png"  

# Process the image and get the red sum
red_sum = modify_image_and_calculate_red_sum(image_path, output_path, n)
print(f"The sum of all red pixel values is: {red_sum}")

# Chapter 2 : The chamber of strings

def process_string(s):
    numbers = ''.join([char for char in s if char.isdigit()])
    letters = ''.join([char for char in s if char.isalpha()])
    
    even_numbers_ascii = [ord(char) for char in numbers if int(char) % 2 == 0]
    uppercase_letters_ascii = [ord(char) for char in letters if char.isupper()]
    
    return even_numbers_ascii, uppercase_letters_ascii

example_string = '56aAwl98Aksttr23527QaYmni4557S85fqsq31D0'
even_numbers_ascii, uppercase_letters_ascii = process_string(example_string)
print("ASCII Values of Even Numbers:", even_numbers_ascii)
print("ASCII Values of Uppercase Letters:", uppercase_letters_ascii)

# decrypting the cipher text using ROT13
def decrypt_caesar_cipher(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((ord(char) - shift_base + shift) % 26) + shift_base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

cryptogram = " VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypted_message = decrypt_caesar_cipher(cryptogram, 13)
print("Decrypted Message:", decrypted_message)
