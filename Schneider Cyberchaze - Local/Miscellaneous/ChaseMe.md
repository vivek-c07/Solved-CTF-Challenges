# Forensics - Easy Difficulty
- A file has been provided - [Challenge File](https://github.com/vivek-c07/Solved-CTF-Challenges/blob/86445a98339d836956335a522473ee56e65704af/Schneider%20Cyberchaze%20-%20Local/Miscellaneous/ChaseMe0x03)
- Download the file and extract using ```binwalk -e ChaseMe0x03```
- Binwalk output tells us that the files inside are `zlib` compressed.
  Keep this in mind.
- Now, search through the extracted file for the 'cyber' keyword.
  - Use ```grep -r 'cyberc' _ChaseMe0x03.extracted/```.
    - We get a match with a particular filename.
    - Now, we need to search that file for the flag.
- Use ```srch_strings -a _ChaseMe0x03.extracted/ADEB | grep 'cyber'```.
  - We have the flag - ```cyberchase{IceCreamIsLove}``` in stdout.
