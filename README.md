# Sweatpad- the hackpad for sweats
I always found most gaming keyboards to be difficult to use and somewhat non ergonomic. This prompted me to create the sweatpad, a shortened keyboard with only the keys that you may need to play most fps games. It also features RGB lighting, a OLED display to show data/modes.

## Complete Assembly (without keys):
Some images of what the finished product should approximately look like. 

![Screenshot 2025-06-07 163622](https://github.com/user-attachments/assets/8be619e6-52e9-4de0-af66-681052f2a535)
![image](https://github.com/user-attachments/assets/54c41ae5-88ce-4b8d-b58d-8276979da1e4)

## PCB and Schematic

![Screenshot 2025-06-04 011038](https://github.com/user-attachments/assets/ea50e0de-978e-4b50-85ff-61949f200fd9) 
![Screenshot 2025-06-07 154958](https://github.com/user-attachments/assets/f6637263-afae-4b75-ae31-3ee854719555)
![image](https://github.com/user-attachments/assets/42634029-e826-41a4-bebe-b776546344a1)

## Case and Exploded View

![image](https://github.com/user-attachments/assets/9f46751c-6769-48c6-af54-ad63e62343ab)

## BOM 
- 1 SEEEDUINO XIAO RP2040
- 16x MX-Style switches (preferrably MX-Brown)
- 16x 1N4148 diodes
- 1x SSD1306 LED (I2C)
- 16 Blank DSA keycaps (White)
- 16x SK6812 MINI-E LEDs
- 4x M3x16mm screws, and corresponding nuts

## Notes
Although this project should have been really simple, i overcomplicated it by adding a bunch of switches because of my original idea for the project, but at least now it would be easier for me to design my full/60% keyboard. The PCB was larger than the 100x100 mm restriction, so i had to shorten it, leading to some unsightly changes in the case- but they shouldn't have any effect on the functionality. 
