# Medium Difficulty
- Download the disk image and decompress it using ```gunzip <filename>```.
- Now, use command ```mmls <filename>``` on the decompressed file.
  - This command provides details about the memory location and size of the disk image.
  - Note down the size of the linux partition in the disk image.
- Launch Instance on the challenge page and copy the netcat command to connect to the instance server.
  - Enter the size of the linux partition found on the disk image to the question asked.
  - If the answer is right, the server prints the flag.

### Note
If the ```mmls``` command dosent work, install sleuthkit using ```sudo apt-get install sleuthkit```.
