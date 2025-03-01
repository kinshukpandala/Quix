# Changes made in this code are that once the code is running 
# The user needs to the enter the URL in the terminal to generate the QR Code

import qrcode

# User input for the link and filename
data = input("Enter the link to generate the QR code: ")
file_name = input("Enter the name to save the QR code (without extension): ") + ".png"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the final QR code image with the custom filename
img.save(file_name)

print(f"QR code generated and saved as '{file_name}'")
    