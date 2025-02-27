import qrcode

# Data to encode in the QR code
data = "https://docs.google.com/forms/d/e/1FAIpQLSdMuzYq41YsyQzQ6HgAsBl9gI-gS3FpKsfzXZJWksMieb1BEQ/viewform"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=2,  # Version 2, gives a 25x25 matrix
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction (default)
    box_size=10,  # Size of each box in pixels
    border=4,  # Border thickness around the QR code
)

# Add data to the QR code
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image file
img.save("qr_code_version2.png")

print("QR code generated and saved as 'qr_code_version2.png'")
