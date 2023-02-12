# BotNet - Web automation
This repo is intended to gather the few bots I use(d) to automate some trivial tasks. 

## Requirements:
* python **3.10.9**, albeit a version of python **3.7+** should do the job.
* Selenium Webdriver **4.8.0**, install running:
```bash
pip3 install selenium
```
* Chromium (install [here](https://chromedriver.chromium.org/downloads)): match the version you decide to download with the version you are currently using for browsing. 
To check your Chrome version:
    * open Chrome
    * at the top right, look at more
    * click Help > About Chrome 

## Install:
This repo can be downloaded locally via SSH running this line command in your terminal:
```bash
git clone git@github.com:LucaFrat/BotNet.git
```

## Run:
To run a bot from your terminal you'll have to run:
```bash
python3 main.py
```

<br />
<br />

# Intern Bot

<br />
<br />
<br />

# Gym Book bot
This Bot is useful to either book a time slot at the gym (X TU Delft) or check its availability.

## Usage:
Before being able to properly run the code you'll have to customize a couple of things:
* in `constants.py` change the variable `CHROME_PATH` with the path to the chromium file `chromedriver.exec`
* change the variables `USERNAME_TUDELFT` and `PASSWORD_TUDELFT` defined in the file `constants.py`.

Be careful to set the variable `debug_mode` to `False` if you want to insert value manually after you run the program.
Once the program has being ran, you'll be asked to insert info from the terminal: 

<img src="images/gym_terminal.png" style=" width:500px ; height:200px ">


<br />
<br />
<br />

# Show Courses Bot
This Bot is useful to retreive and print in the terminal informations about the available Bachelor and Master courses, and about the PHD procedure, at the TU Delft.

## Usage:
Before running the code you'll have to customize a thing:
* in `constants.py` change the variable `CHROME_PATH` with the path to the chromium file `chromedriver.exec`

Once the program has being ran, you'll be asked to insert info from the terminal:

<img src="images/courses_terminal.png" style=" width:320px ; height:130px ">