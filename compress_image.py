# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25th, 2024

@author: eruiz1996
"""
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
    input_image_path: str = r'C:\Users\ed_22\Documents\Image-compressor\examples\image.jpg'
    output_image_path: str = r'C:\Users\ed_22\Documents\Image-compressor\examples\compressed_image.jpg'
    
    compress_image_to_size(input_image_path, output_image_path)