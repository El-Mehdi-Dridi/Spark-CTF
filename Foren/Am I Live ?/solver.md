```
tshark -r challenge.pcap
-Y 'icmp and ip.src == 10.0.0.1' -T fields -e frame.time_epoch -e ip.ttl | sort -n | awk '{if ($2 >= 32 && $2 <= 126) printf "%c", $2} END {print ""}'
```
