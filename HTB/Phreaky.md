# Packet Analysis - Medium
- Download the zip file and open using password - 'hackthebox'.
- Now, there are 15 SMTP/IMF, with each one containing a zip file.
- Download said files using the 'export objects' button. (15 files)
- Now, download the zip files from each of these eml files.
- The passwords for extracting these zip files lies in each of the respective SMTP/IMF packet's TCP Stream.
  - So, for each zip file, go to the respective SMTP/IMF packet's TCP Stream and retrieve password for extraction.
- After extracting all the zip files, we obtain 15 parts of a pdf.
  - We need to assemble these parts to obtain a full pdf.
- Use this python program to first combine the names of all pdf parts - [Python Code](https://github.com/vivek-c07/Solved-CTF-Challenges/blob/d476836bbb622075999f1ccf8d4f06192ecf5b1d/HTB/Assemble_filenames.py).
- Now, run this file and store output to another file using ```python3 print.py > files.txt```.
- Use this bash code to assemble all pdfs using pdf names from the previous output file - [Bash Code](https://github.com/vivek-c07/Solved-CTF-Challenges/blob/c56514ab3d77b14ffadca018e58cdef3419d9368/HTB/Pdf-Assembly.sh).
- Use ```chmod +x <bash_file>``` to give the file execution permissions and then run the file using ```./<bash_file>```.
- Now, open the assembled final pdf and the flag is visible at the end of the pdf.
