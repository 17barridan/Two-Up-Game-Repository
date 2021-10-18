""" A game of chance. The programs throws (virtually) two coins.

Have the player choose to gamble on:
 -  heads (obverse)
 - tails (reverse)
 - head + tail (Ewan)

 * If they guess correctly, they win. If not, they lose.
 * Make sure the coin tosses are actually random.

 Process:
 1. Notify the user that two coins have been thrown
 2. The player must input a guess as to whether it is heads, tails or both
 3. If the player is correct, the game informs the user they have won and vice versa for a loss.
 4. The coin toss must be randomised

 Possible program functions:
 1. Toss coins - 17Barridan
 2.Get guess - DEEBAZZ
 3.Generate coins result - 17Barridan
 4. Determine win/loss - DEEBAZZ

 Notes:
 * somehow you need to convert the user input to numbers relative to the possible results
"""

import random


def tossCoins():
    coinToss = random.randint(1, 3)
    return coinToss


def main():
    coinToss = tossCoins()
    print(coinToss)


if __name__ == "__main__":
    main()
