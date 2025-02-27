# In this code we have enhanced the code by 
# allowing the user to save what ever he wants for his PNG file 
# also to addition to that based on the data input the 
# code will automatically change its size mentioned in the line 25 of the code 

import qrcode
from PIL import Image

# User input for the filename
file_name = input("Enter the name to save the QR code (without extension): ") + ".png"

# Data to encode in the QR code
data = "Enter the link you want to generate the QR for"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction to accommodate the logo
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white').convert("RGBA")

# Load the club logo
logo_path = "club_logo.png"  # Ensure you have a logo image in the same directory
try:
    logo = Image.open(logo_path)

    # Resize logo to fit in the center of the QR code
    qr_width, qr_height = img.size
    logo_size = qr_width // 5  # Adjust the logo size (1/5th of QR width)
    logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

    # Calculate position to place the logo at the center
    logo_x = (qr_width - logo_size) // 2
    logo_y = (qr_height - logo_size) // 2

    # Paste the logo onto the QR code (with transparency support)
    img.paste(logo, (logo_x, logo_y), logo)

    print("Logo added successfully.")

except FileNotFoundError:
    print("Logo file not found. Generating QR without a logo.")

# Save the final QR code image with the custom filename
img.save(file_name)

print(f"QR code generated and saved as '{file_name}'")
