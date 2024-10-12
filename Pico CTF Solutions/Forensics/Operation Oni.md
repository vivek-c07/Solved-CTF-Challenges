# Disk Analysis - Medium Difficulty
- Extract disk image from download using `gunzip <filename>`.
- Now, use `mmls <disk_image>` to view partitions of the disk.
- Now, string searches for common keywords give a lot of results.
  - There is a high chance that the 'key_file' is hidden in the Linux partitions.
- The final Linux partition is a proper filesystem.
- Start by saerching folders such as 'root' and 'home'.
  - See directory contents using `fls -o <offset_number> <disk_image> <inode>`.
  - Read file contents using `icat -o <offset_number> <disk_image> <inode>`.
- Now, the root folder contains a dirtectory called ssh.
  ![image](https://github.com/user-attachments/assets/ff221d80-acef-4473-902e-c551e6f4f31a).
  <br/>
- See files inside this directory. <br/>
  ![image](https://github.com/user-attachments/assets/aa1c1de1-193b-431d-9cad-2cb93d06d94f)
- Read both the files
  ![image](https://github.com/user-attachments/assets/ac2eb358-5a77-4593-aceb-41dc57f8e2dd)
  ![image](https://github.com/user-attachments/assets/e5b9b6bc-24fa-4b4c-b91e-159f90dac2e2)
- Now, copy the contents of the first file (The one with the Private Key)
  - ```<Command to read file> > <savefile_name>```
- We need to remove permissions for the group and others.
  - So, use ```chmod 600 <key_file>``` to give r,w permissions only to user/owner.
- Now, login to the remote server by copying the command from the challenge
  - Change the input file to that of your saved file which contains the key.
- You have now gained access into the ssh server.
- Now, use ```ls``` to see all files in the server.
- Read contents of the one and only file in the server using ```cat 'filename'```.
- The flag can be found in stdout.
