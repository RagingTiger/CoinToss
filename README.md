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
```
cointoss [-i] <games>
cointoss [-i]
```

## Example
### Basic: Instance Mode
Running a single instance of 10 games (i.e. coin tosses or flips):
```
$ python cointoss.py 10
Heads(1) = 46
Tails(0) = 54
Total(1+0) = 100
Percentage Heads = 46.0%
Percentage Edge = -4.0%
```

### Advanced: Interactive Mode
Whereas the basic usage is only single instances with no saved state, the
advanced usage drops into an interactive interpreter that saves state between
sets of games. For example:
```
$ python cointoss.py -i
> run 10
Heads(1) = 5
Tails(0) = 5
Total(1+0) = 10
Percentage Heads = 50.0%
Percentage Edge = 0.0%

> run 100
Heads(1) = 38
Tails(0) = 62
Total(1+0) = 100
Percentage Heads = 38.0%
Percentage Edge = -12.0%

> run 1000
Heads(1) = 511
Tails(0) = 489
Total(1+0) = 1000
Percentage Heads = 51.1%
Percentage Edge = 1.1000000000000014%

> run 10000
Heads(1) = 5083
Tails(0) = 4917
Total(1+0) = 10000
Percentage Heads = 50.83%
Percentage Edge = 0.8299999999999983%

> run 100000
Heads(1) = 49882
Tails(0) = 50118
Total(1+0) = 100000
Percentage Heads = 49.882%
Percentage Edge = -0.1180000000000021%

> run 10000000
Heads(1) = 5000164
Tails(0) = 4999836
Total(1+0) = 10000000
Percentage Heads = 50.00164%
Percentage Edge = 0.0016400000000018622%
```
In the above example you can see we are increasing the number of games using
the **interactive** command `run`, but there are a few other commands we can
use while in the **interpreter**:
```
> help
run [<games>] Runs the simulation with inputs
total                Prints running total
help                 Prints this help message

> total
Total Heads = 5055683
Total Tails = 5055427
Total Percentage Heads = 50.00126593420505%
Total Percentage Edge = 0.0012659342050511668%

> run
Heads(1) = 5002020
Tails(0) = 4997980
Total(1+0) = 10000000
Percentage Heads = 50.0202%
Percentage Edge = 0.02020000000000266%

> run
Heads(1) = 4998799
Tails(0) = 5001201
Total(1+0) = 10000000
Percentage Heads = 49.987989999999996%
Percentage Edge = -0.012010000000003629%

> run 10000000000000
Heads(1) = 4999998400491
Tails(0) = 5000001599509
Total(1+0) = 10000000000000
Percentage Heads = 49.99998400491%
Percentage Edge = -1.599509000271837e-05%
```

While the `help` command should be self-explanatory, the other commands could
benefit from some clarification:

+ The `total` command just lets us
  see the current running totals for heads, tails, the percentage of coin tosses
  that are heads (overall) and precent edge (i.e. the difference in probability
  of heads vs. tails).

+ The `run` command can **optionally** except an argument (e.g. the number of
  games of coin toss to be played). Without an argument it will repeat the same
  simulations with the previous argument values for `<games>`.
