## Medium Question
- Download and extract disk image.
- Now, use ```mmls``` to find offset nummber of the Linux partition.
- Use command ```fls -o <offset_number> -r -p <disk_img> | grep <req_filename>```
  - Here, -p prints the absoulte path and -r searches through directories recursively.
- Copy the path of the file in stdout
- use ```icat -o <offset_number> <disk_img> <file_inode> | less```
  - This outputs the file contents to a command called less, which streamlines and arranges the output for better viewing.
  - Navigate through less using arrow keys and search using '/'.
