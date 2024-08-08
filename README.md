# Web Content Scraper and QR Code Generator

## Overview

This project contains two Python scripts:

1. **`main.py`**: Scrapes website content using Apify, processes the content with Langchain, and generates a detailed description prompt for image generation.
2. **`qr.py`**: Creates a QR code with an optional logo overlay.

## Requirements

Ensure you have the following dependencies installed:

- `opencv-python`
- `numpy`
- `langchain`
- `langchain-openai`
- `python-dotenv`
- `qrcode`
- `Pillow`

You can install them using `pip`:

```bash
pip install opencv-python numpy langchain langchain-openai python-dotenv qrcode Pillow
```

## Environment Variables
 Create a `.env`file in the root directory of your project and add the following lines with your respective API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
ACTIVELOOP_TOKEN=your_activeloop_token
APIFY_API_TOKEN=your_apify_api_token
```
## Usage
`main.py`
1. This script uses Apify to scrape content from a specified website.
2. It then processes the content using Langchain's embeddings and stores it in DeepLake.
3. It generates a detailed description for image generation based on the content.

To run the script:
```bash
python main.py
```
`qr.py`
1. This script creates a QR code for a given URL.
2. It allows for the inclusion of a logo in the center of the QR code.


To run the script:
```bash
python qr.py
```
Ensure you have a file named `logo.png` in the same directory as `qr.py` to use as the logo.

## Output
`main.py`: Outputs the generated image prompt to the console.
`qr.py`: Generates a QR code image named qr_with_logo.png with an optional logo

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```bash
MIT License

Copyright (c) 2024 Johnny463

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
