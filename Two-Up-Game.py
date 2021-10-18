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
 1. Toss coins - DEEBAZZ890
 2.Get guess - 17barridan
 3. Generate coins result - DEEBAZZ890
 4. Determine win/loss - DEEBAZZ890

"""

import random


def tossCoins():
    coinToss = random.randint(1, 3)
    return coinToss


def retrieveGuess():
    playerPrediction = input(
        "Please enter the corresponding letter pair to the bet you wish to place:\nHH - Both coins are Heads, "
        "TT - Both are tails, or HT - One of each\nEnter Bet --> ")
    playerPrediction.upper()
    if playerPrediction == "HH":
        playerBet = 1
    elif playerPrediction == "TT":
        playerBet = 2
    else:
        playerBet = 3
    return playerBet


def gameResult(playerBet, coinToss):
    if playerBet == coinToss:
        print("Congratulations, you win!")
    else:
        print("Tough luck, you have lost!")


def main():
    coinToss = tossCoins()
    playerBet = retrieveGuess()
    gameResult(playerBet, coinToss)


if __name__ == "__main__":
    main()