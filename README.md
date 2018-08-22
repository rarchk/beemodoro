Beeminder + Pomodoro = 🍅
=========================
Utilize the power of `Beeminder <http://beeminder.com/>`_ and `Pomodoro
<http://pomodorotechnique.com>`_. This little script runs a Pomodoro timer in
your terminal and increments your Beeminder goal counter when it's done. This
requires your project to count 1 Pomodoro per step.

It uses linux **notify-send** to use notifications as well. 

## Setup 
```bash
git clone https://github.com/rarchk/beemodoro
# It requires python > 3 
virtualenv bmdro -p python2.6
source bmdro/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
cd beemodoro
python __init.py__ "My first beemodoro session" [Custom time]
```

## BEEMINDER SETUP
-----------
1. I've Hardcoded the url in `__init__.py` 

  - ``BEEMINDER_KEY``: your Beeminder API key
  - ``BEEMINDER_USER``: your Beeminder username
  - ``BEEMINDER_GOAL``: your Beeminder goal slug name (can be found in your
    goal settings)

2. Run ``beemodoro "Work on secret project" [optional_custom_pomodoro_length]``
3. Work for 25 minutes
4. You just finished a Pomodoro! Yay! Take a break 🍅

Manual Goal Tracking
--------------------
``track_goal [comment]``

Requirements
---------------
- Python 3
- OS X say (for TTS output)
