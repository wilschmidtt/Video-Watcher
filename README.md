# YouTube-viewBot
Bot that generates views on a YouTube video(s) of choice.

### Prerequisites
* Windows Operating System
   - viewBot calls commands that are configured for Windows
   - If you machine does not have Windows as its native OS, it is recommended that you set up a virtual Windows system using [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* NordVPN
   - viewBot utilizes a rotating proxy through the help of NordVPN
   - You can either purchase a NordVPN subscription or set up a trial at the [NordVPN website](https://nordvpn.com/?utm_expid=.CM-bHTe9S0iFcch8gLNeEA.0&utm_referrer=https%3A%2F%2Fwww.google.com%2F)
   - Without NordVPN, the viewBot will be unable to use the commands located within the '/src/proxy_list.txt' file and it is likely that YouTube will detect an unusually high traffic volume coming from the IP address your machine is using
   - NOTE: NordVPN must be added to path once installed. Without doing this, it won't be possible to interact with Nord through the command line
* Python 3.6.*
   - Any version of Python 3.6 will work 
   - The 'requirements'txt' file contains all of the necessary libraries. It is recommended that you install them onto a fresh environment
* 2560 x 1080 Display Resolution
   - During the running of the bot, a Python library called 'PyAutoGUI' executes mouse clicks on the screen according a set of coordinates
   - I created this project on a 21:9 2560 x 1080 display, so the coordinates for the mouse clicks are aligned to this resolution. With any other resolution, the relative location of the pixels will be different, so the mouse clicks will not execute in the proper location, ultimately causing the program to fail
   - To fix this, you will need to go into your system's display settings and change the resolution to 2560 x 1080

### Running the viewBot
* Once you have set up the environment, navigate to the directory where you have saved the 'src' folder and run: 
   ```$ python .\viewbot.py -h```
