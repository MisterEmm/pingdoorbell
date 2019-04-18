# pingdoorbell
Basic code for the Raspberry Pi Video Doorbell project.

Project Writeups & Full Build Details:

Instructables:

Hackster:

Youtube:

# Raspberry Pi "PiNG" Video Doorbell

This project uses a Raspberry Pi and the Google Duo web app (https://duo.google.com/) to make video calls between a doorbell unit and a smartphone, tablet or PC. This code assumes the doorbell unit contains a button and LED, with either an amplified (eg battery powered) speaker or an audio HAT (for example the Phat Beat as used here). 

The code is very simple and essentially just programs the doorbell buton to perform a series of mouse clicks to control the Duo web app on screen. Except it's not really on screen as the Pi is running headless - more on that later.

# Prerequisites

From a fresh (full) installation of Raspbian it's best to first enable VNC server, and ideally log in / create a VNC account to make connecting to the Pi as straightforward as possible. This can be enabled under the Interfaces tab of Preferences > Raspberrty Pi Configuration. 

Because the Pi will be running headless we need to tell it to assume an HDMI monitor is connected, and set a resolution so that the mouse commands in the script line up with the elements on the web app. I chose option 19, 1280x720. 

Next we need to install PyUserInput from the terminal:

*pip3 install PyUserInput*

...and download the PiNG.py script to the Pi, I just popped it in the main Pi folder. 

To save having to start the script after each reboot it's worth setting it to autostart once the desktop has loaded, by editing the global autostart file:

*sudo nano /etc/xdg/lxsession/LXDE-pi/autostart*

...adding in the following line at the bottom to point at the script location:

*@python3 /home/pi/PiNG.py*

After a reboot the script should run automatically. 








