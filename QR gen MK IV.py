# in this version of the code we are assigning a path to save all images in a folder within the project to make it less off a cluster

import qrcode
import os

# Define the folder to save QR codes inside the QRCG project
save_folder = "QRCG project/QR_codes"

# Ensure the save folder exists
os.makedirs(save_folder, exist_ok=True)

# User input for the link and filename
data = input("Enter the link to generate the QR code: ")
file_name = input("Enter the name to save the QR code (without extension): ") + ".png"

# Full path to save the QR code
file_path = os.path.join(save_folder, file_name)

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

# Save the final QR code image in the specified folder
img.save(file_path)

print(f"QR code generated and saved as '{file_path}'")



#this code creates a new folder called QRCG_Project/QR_code and stores the QR in that
# So in the next version the goal is to make sure that it stores in the same folder it is generating in 
