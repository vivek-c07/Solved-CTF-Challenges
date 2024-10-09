# Steps Involved - 
- Download the image.
- Try out various tools such as binwalk (search through binary file), xxd (view hex values), etc.
- Use command - ```exiftool <filename>```.
  - Here, the output includes a flag called *License* which has weird values, and looks like encoded text.
- Decode this text from Base64 encoding using an online tool called Cyberchef.
  - Open the Cyberchef Website and paste the License flag data as input.
  - Add *'From Base64'* filter to get the answer CTF Flag.
