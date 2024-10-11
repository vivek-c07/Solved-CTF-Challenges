# Packet Analysis - Medium Difficulty
- Open pcap file. The zip file is password protected, so we have to try finding the password in the packet capture.
- 1 of the Ethernet II packets can be seen having a different color code.
  - Upon taking the value of this string and using Recipe 'From Base64' in Cyberchef, we obtain a partial flag.
- Now, there are various other strings found in the packet trace.
- After some trial and error, we can see that the partial flag itself is the password for the zip file.
- Once extracted, the zip file contains a file with the entire flag which can just be read using any text editor.
