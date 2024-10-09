# Packet Analysis - Medium Difficulty
- Download the said packet and open it in wireshark.
- Now, search for any available objects under the export objects tab.
  - There is nothing we can find here.
- So, the flag has to be hidden somewhere.
- Manually inspect all packets. Now, make this easier by ordering them by protocol.
  - So, now we can look for protocols with less packets.
- Now, we can notice that there is a packet with the ```FTP``` protocol which has a username and a password.
  - But the username and password are useless to us and they do not contain any flags or traces of the flag.
- But, if we right-click on the flag and select Follow->TCP Stream and then close the window, we can see that
  there is one more packet with the same source and destination ip address.
  - This packet contains the flag under its ```Retransmitted TCP Segment Data```.
- We can right click on the ```Retransmitted TCP Segment Data``` and select copy->value.
  - Use cyberchef to obtain flag.

*Note - Alternatively, We can perform a string search on the entire file for the flag as well.*
