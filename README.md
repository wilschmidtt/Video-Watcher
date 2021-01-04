# viewBot
Bot that generates views on a YouTube video(s) of choice.

![gif](gif/viewbot.gif)

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
   - The 'requirements.txt' file contains all of the necessary libraries. It is recommended that you install them onto a fresh environment
* 2560 x 1080 Display Resolution
   - During the running of the bot, a Python library called 'PyAutoGUI' executes mouse clicks on the screen according to hard-coded coordinates
   - I created this project on a 21:9 2560 x 1080 display, so the coordinates for the mouse clicks are aligned to this resolution. With any other resolution, the relative location of the pixels will be different, so the mouse clicks will not execute in the proper location, ultimately causing the program to fail
   - To fix this, you will need to go into your system's display settings and change the resolution to 2560 x 1080

### viewBot Explained
* In order to simulate human interaction on a YouTube video, the viewBot utilizes a variety of randomly chosen actions
* In addition, the viewBot continually cycles through different proxies so that a suspicious amount of activity can't be detected from your IP address
* All forms of interaction that the viewBot uses are randomly chosen to avoid the bot being detected
* It is virtually impossible for the same seires of clicks to be repeated twice by the viewBot
* The layers of randomness selected in each iteration by the viewBot are as follows:
   - A randomly chosen proxy
   - A randomly chosen number of tabs to open
   - A random number of clicks to execute on each tab
   - A randomly chosen on-screen button to select with each mouse click
   - A randomly chosen part of the on-screen button to press
   - A randomly chosen number of seconds to pause after each click
   - A randomly chosen number of seconds to watch the video for during each iteration
* All together, there are seven layers of randomness. Hypothetically, if there were 1,000 possible choices in each layer, then there would be 1,000^7, or 1,000,000,000,000,000,000,000 different combinations of actions that the viewBot can perform. This is a hypothetical scenario though; layers such as the proxy layer and the number of tabs to open are limited. But layers such as the button to click and what part of this button to press have thousands of different possibilities
* The emphasis on randomness ensures that behaviors characteristic of a 'bot' aren't displayed, and no detectable pattern is left behind by the viewBot

### Running the viewBot
* Once you have set up the environment, navigate to the directory where you have saved the 'src' folder and run: ```$ python .\viewbot.py -h```
* There are four commands that need to be supplied prior to running the program. They are as follows:
    * -s SEARCH_STRING, --search_string SEARCH_STRING
                        phrase to search on YouTube
    * -n NUM_RUNS, --num_runs NUM_RUNS
                        number of times to run the viewBot in total
    * --max MAX             max amount of seconds to watch video for
    * --min MIN             min amount of seconds to watch video for
* Example command: ```$ python .\viewBot.py -s "Best way to sleep on a flight" -n 150 --max 35 --min 5```
    * -s "Best way to sleep on a flight"
       - Name of the YouTube video that will be loaded and watched by the bot
    * -n 150
       - Number of iterations that the bot will cycle through. Each iteration generates between 1-5 views, so 150 iterations will generate between 150-750 views
    * --max 35
       - The max number of seconds that the bot will pause for during each iteration (to simulate "watching" the video). This value will be a randomly chosen number between the range of --min and --max. In this case, the maximum amount of time that a video can be watched for during each iteration is 35 seconds
    * --min 5
       - The min number of seconds that the bot will pause for during each iteration (to simulate "watching" the video). This value will be a randomly chosen number between the range of --min and --max. In this case, the minimum amount of time that a video can be watched for during each iteration is 5 seconds
       
### Inspiration
* I have a friend who is into film and recently uploaded one of his self-made films onto YouTube. He mentioned that it would be cool if he could get the video to 10,000 views, so I created this bot to help get his video get there in a matter of days.

### Author
* **William Schmidt** - [Wil's LikedIn](https://www.linkedin.com/in/william-schmidt-152431168/)
