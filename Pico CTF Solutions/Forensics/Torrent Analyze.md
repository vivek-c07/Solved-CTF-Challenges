# Packet Analysis - Medium Difficulty
- Download the pcap file and open it using wireshark
- Now, we need to find the name of the torrent file.
  - Metadata such as name, file length, etc in a torrent are associated to an attribute called info_hash.
  - info_hash is the hash value of all these metadata combined together.
- Let us search for `info_hash` under string_search in wireshark.
- We obtain a lot of results.
- Now, all over the torrent, we notice a local ip address in both the source and destination columns
  - The `192.168.73.132` ip address is most likely to be the host ip address.
- Add a filter `ip.src == 192.168.73.132`, because we need the host is sending a download request that most
  probably contains the info_hash with the file's metadata.
- Now, we can notice that under these conditions, all packets have the same hash_info, which upon googling reveals
  the filename - `ubuntu-19.10-desktop-amd64.iso`.<br/>
![image](https://github.com/user-attachments/assets/aabc647e-2f60-4784-8395-3da2c0a54ae4)

- Use `pico{<filename>}`, which is our flag to be submitted.
