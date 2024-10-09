# Steganography - Medium Difficulty
- Use exiftool to try and interpret the file type.
  - Exiftool indicates that the file might be a jpeg file.
  - Open file in hexview using ```xxd <filename> | less```.
- The header for a jpeg file must be - ```FF D8 FF E0```.
  - We can clearly see that this is not the case here.
  - But, we can see that it is jumbled -> ```E0 FF D8 FF``` is present instead.
- From all of this we can come up with a theory that we can obtain the original file if we either flip over the
  entire hexcode in this pattern or only the header.
- Editing only the editor using ```hexeditor``` does not do the job, so lets try the other way.
- Now, use this python code I created to do the conversion - [Forensics/8-bit-interchange-jpg.py](https://github.com/vivek-c07/Solved-CTF-Challenges/blob/397cd4d086801e46502dbaa54f0f890493edf24e/Forensics/8-bit-interchange-jpg.py)
  - Check and change filenames according to the code.
- Add a file extension to the new file (.jpg) and open it.
  - The flag is present in the form of an image.
