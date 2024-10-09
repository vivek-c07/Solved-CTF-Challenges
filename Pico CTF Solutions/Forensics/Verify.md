# Steps Invloved :
  - Connect to server instance using ssh (command provided in challenge).
  - Extract checksum of each file in the server and store in txt file using -
      ```sha256 <directoryname>/* > checksums.txt```
  - Search for required checksum using ```grep <checksum> checksums.txt```
  - Feed this file into the python program present in the server to obtain flag :)
