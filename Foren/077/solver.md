```
tshark -r 007.pcap
-Y 'http.user_agent and not (http.user_agent contains "Windows NT" or http.user_agent contains "Macintosh" or http.user_agent contains "Linux" or http.user_agent contains "Android")'
-T fields -e frame.time_epoch -e http.user_agent | sort -n | awk -F '[()]' '{print $2}' | tr -d '\n'
```
