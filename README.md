# QR Code Generator

This is a Python-based QR Code Generator that allows you to create QR codes for text, URLs, or other data easily and efficiently.

## Features

- Generate QR codes from any text or URL.
- Save generated QR codes as image files.
- Customize QR code size and error correction levels.

## Prerequisites

Before using this project, ensure you have the following installed:

- Python (version 3.6 or later)
- Required Python libraries:
  - `qrcode`
  - `Pillow`

You can install the required libraries using pip:
```bash
pip install qrcode[pil]
```

## How to Use

1. Clone this repository or download the script to your local machine.

2. Run the script:
   ```bash
   python qrcode_generator.py
   ```

3. Input the data you want to encode in the QR code when prompted.

4. The QR code will be generated and saved as an image file (e.g., `qrcode.png`).

## Code Structure

The script consists of the following key steps:

1. **Input Data:** Accept user input for the text or URL to encode.
2. **QR Code Generation:** Use the `qrcode` library to create a QR code with the specified data.
3. **Customization:** Optional parameters like size and error correction level can be adjusted.
4. **Save Image:** Save the generated QR code as a PNG file using the `Pillow` library.

## Example

Here is an example of how the program works:

1. Run the script.
2. Enter the text or URL when prompted, for example:
   ```
   Enter the data for the QR code: https://example.com
   ```
3. The program will generate a QR code and save it as `qrcode.png` in the current directory.

## Customization

You can customize the QR code by modifying the following parameters in the script:

- **Box Size:** Adjust the size of the QR code boxes.
- **Border:** Change the thickness of the border.
- **Error Correction:** Set the error correction level (L, M, Q, H).

Example:
```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## Acknowledgements

- [qrcode Library](https://github.com/lincolnloop/python-qrcode)
- [Pillow Library](https://python-pillow.org/)

---

Enjoy using the QR Code Generator!

