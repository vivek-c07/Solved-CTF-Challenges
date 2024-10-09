## Medium Difficulty Question
- Download and unzip disk image using ```gunzip <filename>```
- use command ```mmls <disk_image>``` to view allocation within image.
- Now, use ```fls -o <offset_number> -r <disk_image>``` to view all directories and subfiles and subdirectories.
  - Change offset until the partition has system files in it appears.
  - pipe the output to ```grep 'flag'``` using the ```|``` command.
- Now, use ```icat -o <offset_number> <disk_image> <inode>``` to print contents of the required file.
- The answer flag will appear in stdout.
