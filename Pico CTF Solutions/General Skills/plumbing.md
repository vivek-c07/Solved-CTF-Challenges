# Steps Involved : 
- use netcat to connect to server
  - ```nc jupiter.challenges.picoctf.org 14291```
- It is seen that output is not stored. So use -
  - ```nc jupiter.challenges.picoctf.org 14291 > output.txt```
  - This stores the output on your local machine as a text file - output.txt
- Now, search through the text file for the Pico Flag
  - ```grep "Pico" output.txt```
