#!/usr/bin/env python

# libs
import random
import numpy

# classes
class CoinToss(object):
    """A class with various methods for simulating a coin toss."""

    @staticmethod
    def simulate(games, probability=0.5):
        """Run coin toss simulation with heads considered wins (i.e. 1) and
           tails considered losses (i.e. 0).

        Args:
            games (int): Number of coin toss games to play.
            probability (float): Probability of coin toss resulting in heads.

        Returns:
            heads (float): Percent of coin tosses resulting in heads.
            tails (float): Percent of coin tosses resulting in tails.
            total (int): Total amount of games played.
            probability (float): Probability of coin toss resulting in heads.
        """
        # init heads and tails counters (wins and losses respectively)
        heads, tails = 0, 0

        # init random number generator
        rand_gen = numpy.random.default_rng()

        # get number of heads (i.e. 1s) with 1/2 probability
        heads = rand_gen.binomial(games, probability)

        # calculate tails by subtracting heads from total games
        tails = games - heads

        # return heads/tails
        return {
            'heads': heads / games,
            'tails': tails / games,
            'total': games,
            'probability': probability
        }


# executable only
if __name__ == '__main__':

    # libs
    import fire

    # bang bang
    fire.Fire(CoinToss)
