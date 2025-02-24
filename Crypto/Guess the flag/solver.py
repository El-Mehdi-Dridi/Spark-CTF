from pwn import *
from randcrack import RandCrack
conn = remote('tcp.espark.tn', 6543)
rc = RandCrack()
for _ in range(624):
    conn.sendlineafter("Enter your choice: ", "1")
    line = conn.recvline().decode().strip()
    if "Here is the next number:" in line:
        number = int(line.split(": ")[1])
        rc.submit(number)
for _ in range(100):
    predicted_number = rc.predict_randrange(0, 6969)
    conn.sendlineafter("Enter your choice: ", "2")
    conn.sendline(str(predicted_number))
    response = conn.recvline().decode().strip()
    print(response)  
conn.interactive()
