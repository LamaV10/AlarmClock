# Alarm Clock 

This is a simple alarm clock written in python. After a given time it will play your music. 

# Usage

In order to have working music you have to create a folder named "Music" inside of "Source/" and then put your music in there (mp3, WAV).
After that you can execute the setup.sh script and choose "1", which will bring you to the module responsible for the music (music.py) after you have choosen your editor.
Neovim, Vim, Vi, Nano and Vscode/ium are supported in this script.
Let me know which editors you want to be added!
Now you can put your titel into the line 7.

# Linux 

If you are on Linux, you can also copy the alarmClock.sh file into the /bin directory. 
Before copying it you should rename the file to something like "alarmClock", so the command will later be "alarmClock" and not "alarmClock.sh".  
Then you have to modify the path from the "alarmClock" script (originally alarmClock.sh) to cd to your "AlarmClock" folder location. 


This is an example of how your file could look like:
cd /home/*your_username/folder/location*/Source/
python main.py

Dont forget to make the script executable with chmod.
Now you should be able to directly type the command "alarmClock" into your terminal.
(This is just experimental! It may be also possible on MacOS.) 

# Requirements

- Python with the dependencies from requirements.txt installed
- Bash to execute the scripts (but it's also possible to do it all manually)
