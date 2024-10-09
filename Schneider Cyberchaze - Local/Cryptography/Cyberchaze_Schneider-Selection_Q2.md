# Schneider Electric Cyberchaze Selection Round Question 2
- We have to analyze the provided network capture file.
- Check for any discrepancies or elements that stand out.
- In a HTTP POST request, check out all fields
  - Right Click and select Follow Stream and choose either TCP or HTTP option.
  - Here, there is a password field which contains ```cyberchaze%7BY0u_g0t_1t_c0rrect%7D```.
  - Now, '%7B' and '%7D' are URL encoded characters that denote curled brackets.
  - So, we now have our answer flag - ```cyberchaze{7BY0u_g0t_1t_c0rrect}```.
