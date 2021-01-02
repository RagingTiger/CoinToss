#!/usr/bin/env python

"""
Description: Coin toss simulator for command line
References:
Usage:
    cointoss [-i] <games>
    cointoss (-i)
"""

# libs
import sys
import random
import readline
import termcolor
import numpy

# funcs
def ctxt(txt, color='yellow'):
    """Print out colored text to stdout."""
    return termcolor.colored(txt, color)


def warn(txt, exit=True):
    """Print exit message and exit."""
    if exit:
        sys.exit(ctxt(txt, color='red'))
    else:
        print(ctxt(txt, color='red'))


# classes
class CoinToss(object):
    """A class with various methods for simulating a coin toss."""
    def __init__(self, clargs):
        # startup readline
        readline.parse_and_bind("tab: complete")

        # store clargs
        self.clargs = clargs

        # get user prompt
        self.prompt = '> '

        # get totals
        self.record = {'heads': 0, 'tails': 0}

        # command dictionary
        self.commands = {'run': self.run,
                         'total': self.total,
                         'help': self.print_help
                         }

    @staticmethod
    def simulate(params):
        """Run coin toss simulation with heads considered wins (i.e. 1) and
           tails considered losses (i.e. 0).
        """
        # init heads and tails counters (wins and losses respectively)
        heads = 0
        tails = 0

        # init random number generator
        rand_gen = numpy.random.default_rng()

        # get number of heads (i.e. 1s) with 1/2 probability
        heads = rand_gen.binomial(params['games'], params['probability'])

        # calculate tails/tails by subtracting heads/heads from total
        tails = params['games'] - heads

        # return heads/tails
        return {'heads': heads, 'tails': tails, 'games': params['games']}

    def interpreter(self):
        """Starts interactive session to store state of games."""
        while True:
            try:
                cmd = input(self.prompt)
                self.execute_cmd(cmd)
            except EOFError:
                warn('\nClosing interactive session')
            except KeyboardInterrupt:
                print('')

    def parse_cmd(self, cmd):
        """Parse commands for interactive mode."""
        # first split
        return cmd.split()

    def execute_cmd(self, command):
        """Execute commands passed in interactive mode."""
        # first parse
        cmd_list = self.parse_cmd(command)

        # now execute
        try:
            self.commands[cmd_list[0]](cmd_list)
        except KeyError:
            warn('Unknown command {0}'.format(cmd_list[0]), exit=False)

    def print_help(self, args):
        """Prints help message."""
        help_msg = ('run [<games>] Runs the simulation with inputs\n'
                    'total                Prints running total\n'
                    'help                 Prints this help message\n')

        # print help
        print(ctxt(help_msg, color='red'))

    @staticmethod
    def print_results(results):
        # Basic formula for calculating percentage
        percentage = (float(results['heads']) / results['games']) * 100

        # Print statements #
        print(ctxt("Heads(1) = " + str(results['heads'])))
        print(ctxt("Tails(0) = " + str(results['tails'])))
        print(ctxt("Total(1+0) = " + str(results['games'])))
        print(ctxt("Percentage heads = " + str(percentage) + "%"))
        print(ctxt("Percentage Edge = " + str(percentage - 50.00) + "%\n"))

    def total(self, args):
        """Calculates and prints running total."""
        # calculate totals
        heads = self.record['heads']
        tails = self.record['tails']
        percent_heads = (float(heads) / (heads + tails)) * 100
        edge = percent_heads - 50.00

        # get format string
        total_string = (
            'Total Heads = {0}\n'
            'Total Tails = {1}\n'
            'Total Percentage Heads = {2}%\n'
            'Total Percentage Edge = {3}%\n'
        ).format(heads, tails, percent_heads, edge)

        # print totals
        print(ctxt(total_string))

    def run(self, cmd_list):
        """Sets up the parameters for the simulation and executes it."""
        # get parameters
        try:
            params = {'games': int(cmd_list[1]), 'probability': 0.5}

            # now update clargs
            self.clargs['<games>'] = params['games']

        except IndexError:
            if self.clargs['<games>']:
                params = {
                          'games': int(self.clargs['<games>']),
                          'probability': 0.5
                         }
            else:
                print('Usage Error: Type \'help\' for more details')
                return

        # execute simulation
        results = self.simulate(params)

        # print out results
        self.print_results(results)

        # update total
        self.record['heads'] += results['heads']
        self.record['tails'] += results['tails']


# executable only
if __name__ == '__main__':

    # libs
    from docopt import docopt

    # get args
    args = docopt(__doc__)

    # check interactive
    if args['-i']:
        # we need to store state
        game = CoinToss(args)

        # start interactive
        game.interpreter()

    else:
        # parameters
        params = {'games': int(args['<games>']), 'probability': 0.5}

        # execute simulation
        results = CoinToss.simulate(params)

        # print out results
        CoinToss.print_results(results)
