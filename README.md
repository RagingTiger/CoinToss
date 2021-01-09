## About
Simple `coin toss` simulator written in our good friend `Python 3`.

## Installation
```
git clone https://github.com/RagingTiger/CoinToss.git && cd CoinToss
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
The `command line interface` portion of this module uses the
[fire](https://github.com/google/python-fire.git) library, which generates the
below documentation by running `python cointoss.py` as follows:
```
NAME
    cointoss.py - A class with various methods for simulating a coin toss.

SYNOPSIS
    cointoss.py COMMAND

DESCRIPTION
    A class with various methods for simulating a coin toss.

COMMANDS
    COMMAND is one of the following:

     simulate
       Run coin toss simulation with heads considered wins (i.e. 1) and tails
       considered losses (i.e. 0).
```
To find out more about any of the `COMMANDS` shown above simply run the help
flag `--help` after the command. For example to learn about the `simulate`
command:
```
NAME
    cointoss.py simulate - Run coin toss simulation with heads considered wins
    (i.e. 1) and tails considered losses (i.e. 0).

SYNOPSIS
    cointoss.py simulate GAMES <flags>

DESCRIPTION
    Run coin toss simulation with heads considered wins (i.e. 1) and tails
    considered losses (i.e. 0).

POSITIONAL ARGUMENTS
    GAMES
        Number of coin toss games to play.

FLAGS
    --probability=PROBABILITY
        Probability of coin toss resulting in heads.

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
