# Disk Analysis - Medium Difficulty
- Open disk using Autopsy tool.
- Go to the 4th volume, which has system files.
- Search for anything that can contain a flag
  - Search for text files using ```.txt```.
  - Search for keywords such as 'flag' and 'pico'.
- We can see that we get hits for text files.
- There are some suspicious text files. Especially with 1 named ```innocuous-file.txt```.
  <img width="948" alt="image" src="https://github.com/user-attachments/assets/3027341e-1ce3-4f06-99b3-48e9dff78308">

- But this file or metadata dosent indicate anything.
  - There is another file in the folder - ```its-all-in-the-name```.
    - Hmm....lets try a global search on the disk using the string ```innocuous```.
- Go to the disk allotment which says raw data and perform a keyword search for ```innocuous```.
- We have multiple hits.
  - Upon close inspection of the file contents, we can come to the conclusion that the flag is scattered across a few of these files
    one after the other.
    <img width="884" alt="image" src="https://github.com/user-attachments/assets/67736248-d94e-4b2b-900c-a25d322cba78">
    <img width="875" alt="image" src="https://github.com/user-attachments/assets/d3ebb0da-0b72-46da-b98f-2e065842da3b">


- Read all hits and assemble the pieces of the flag one-by-one to obtain the full flag.
