# Image Compression and Resizing Script

This Python script allows you to compress and resize JPG images to achieve a target file size, using the Pillow library.

## Project Structure

The project directory contains the following files and directories:

- `compress_image.py`: The main Python script for compressing and resizing images.
- `README.md`: This file, which provides an overview of the project.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `LICENSE.txt`: The license file for the project.
- `examples/`: A directory containing example images (original and compressed).

## Requirements

- Python 3.12.2
- Pillow 10.2.0 or later

## Installation

1. Clone the repository or download the script file.

2. Install the required Python libraries using pip:

```sh
pip install -r requirements.txt
```

3. Run the script using Python:

```sh
python compress_image.py
```

## Usage

### Compress and Resize an Image

The script `compress_image.py` compresses and resizes a JPG image to achieve a target file size. By default, it aims for 1 MB (1,024 KB) but you can adjust this as needed.

### Script

The script is located in `compress_image.py`:

```python
from PIL import Image
import os
from typing import Tuple

def compress_image_to_size(input_path: str, output_path: str, target_size_kb: int = 1024, resize_factor: float = 0.5) -> None:
    """
    Compress and resize a JPG image to achieve a target file size.

    Parameters:
    - input_path (str): Path to the input JPG image.
    - output_path (str): Path to save the compressed and resized image.
    - target_size_kb (int): Desired target file size in kilobytes (default is 1024 KB).
    - resize_factor (float): Factor by which to resize the image dimensions (default is 0.5).

    This function attempts to compress and resize the image iteratively until the file size
    is less than or equal to the target size. It starts with a quality setting of 85 and
    reduces it by 5 in each iteration until the target size is achieved.
    """
    try:
        with Image.open(input_path) as img:
            # resize the image
            width, height = img.size
            new_dimensions: Tuple[int, int] = (int(width * resize_factor), int(height * resize_factor))
            img = img.resize(new_dimensions, Image.LANCZOS)

            # initialize quality and save image until target size is reached
            quality: int = 85
            img.save(output_path, format="JPEG", quality=quality, optimize=True)
            while os.path.getsize(output_path) / 1024 > target_size_kb:
                quality -= 5
                img.save(output_path, format="JPEG", quality=quality, optimize=True)
                print(f"Reducing quality to {quality}, current size: {os.path.getsize(output_path) / 1024:.2f} KB")

            print(f'Image saved as {output_path} with size {os.path.getsize(output_path) / 1024:.2f} KB')

    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == '__main__':
    # example usage: see in 'examples' folder
    input_image_path: str = 'path/to/your/image.jpg'
    output_image_path: str = 'path/to/your/compressed_image.jpg'
    
    compress_image_to_size(input_image_path, output_image_path)
```

### Example

The script is set up with example usage inside the `if __name__ == '__main__':` block. You can replace the paths in the example with your own file paths.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Contact

If you have any questions, feedback, or would like to collaborate, feel free to reach out:

- **Email**: edgarruiztovar@gmail.com
- **GitHub Profile**: [eruiz1996](https://github.com/eruiz1996)
- **LinkedIn**: [eruiz1996](https://www.linkedin.com/in/eruiz1996)

Your feedback and contributions are welcome!