# Steganography - Medium Difficulty
- Download the image and anlyse using exiftools
  - Nothing out of the ordinary is visible.
- Now, the question hints an MSB change.
  - Also, when we open the image, we can notice that major changes have been made to the image.
- So, we will now use a Significant Bits Decoder - https://github.com/Pulho/sigBits/tree/master
- Download and run the python script to obtain an output file. (Enter type as msb).
- We can use ```grep 'pico' <filename> | less```
  - A lot of text is present here.
  - Use the ```/``` operator to search through the ```less``` view for 'pico'
- The flag is present in the output file of the Significant Bit Decoder.
