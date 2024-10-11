# Steganography - Medium
- Upon using ```exiftool <image>```, we can see that the file is a 'png' image.
  - But, exiftool also tells us that there is some trailer data in the image, indicating the presence of a hidden file.
- We can use ```binwalk``` to confirm out suspicions.
  - Use ```binwalk <image>```, which tells us that there are compressed files among the file.
  - So, use ```binwalk -e <image>``` to decompress the compressed data.
- Open the directory created by binwalk output.
- Here, there is a directory called secret which contains an image.
  - This image contains the flag.
