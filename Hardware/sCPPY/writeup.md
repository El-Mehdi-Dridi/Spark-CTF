This is a hardware challenge hosted on Spark CTF 2025 

![image](https://github.com/user-attachments/assets/873c6380-781a-4a01-b8e7-59f696b83600)

The author provide us a file.sal to analyse it 

![image](https://github.com/user-attachments/assets/bd6c6fe9-3017-41be-92d3-38333a010be0)

The First thing to do is to sellect the protocol and in our situation it is `Async Serial`

know we must calculate the baudrate to get the data from the signal 

![image](https://github.com/user-attachments/assets/cd1156d2-53b0-42eb-8735-617dcbca79fd)

We can see different messages being sent at varying timing, length, and frequency.

![image](https://github.com/user-attachments/assets/8b43fd93-07cd-4f1d-ba57-ab0460d1226e)


By analyzing the bit duration, you can determine the correct baud rate for each signal.

In our case, the baud rates were:

First

![image](https://github.com/user-attachments/assets/ca3eb473-4501-4b39-97a7-24e855a5391a)

for the message 2 the baudrate was 2400 bauds

![image](https://github.com/user-attachments/assets/5a176f1b-3637-4e5c-94ab-8647f2de26c3)

Second

![image](https://github.com/user-attachments/assets/181f5a73-af8f-4c7b-9255-f8b4f3d2c230)

For the message one the baudrate was 230400

![image](https://github.com/user-attachments/assets/67698b9f-bb48-4b5e-a408-a6faa87cfca1)

Third

![image](https://github.com/user-attachments/assets/ffc4db60-9aae-4af8-a8ce-357175339ab3)

For the message 3 the baudrates was 19200

![image](https://github.com/user-attachments/assets/095da5db-3bd7-4ad8-99b2-f0646295df73)

After collecting data from file.sal 

We have this like 

https://wokwi.com/projects/423329261637485569

![image](https://github.com/user-attachments/assets/4693c1af-9908-485e-8d64-2af91cb68e13)

Opening this Wokwi project we found that there is a program that display images 

Looking into the description the author asked us to look for an image 

looking at the code, we notice a hidden section

```
const uint8_t  bitmap_icon_speed[] PROGMEM = {
	 0x00, 0x00, 0x00, 0x00, 0x77, 0x6e, 0x45, 0x44, 0x75, 0x64, 0x15, 0x45, 0x77, 0x45, 0x00, 0x05,
	 0x00, 0x00, 0x58, 0x10, 0x49, 0xd0, 0x59, 0x50, 0x49, 0x54, 0x19, 0xde, 0x00, 0x04, 0x00, 0x00
};

```

We used https://javl.github.io/image2cpp/ to decompile it 

![image](https://github.com/user-attachments/assets/1baa478d-36b6-4494-ac92-28909535ef54)

finaly we get the image 

![image](https://github.com/user-attachments/assets/bf273ff8-a45c-4397-85e8-fe6fcb03cd20)

And we found the flag 

SparkCTF{SOFT1034}


