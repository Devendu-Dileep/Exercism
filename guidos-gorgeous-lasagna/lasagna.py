"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2



def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time
    



def preparation_time_in_minutes(no_of_layers):
    """Calculate preparatopn time in minutes..

    :param no_of_layers: int - no of layers in lasgna.
    :return: int - sum of the preparation time for each layer based on Preparation Time.

    Function that takes the no_of_layers and calculate the time required to prepare for each
    layer and return the sum.
    """
    return no_of_layers*PREPARATION_TIME




def elapsed_time_in_minutes(no_of_layers,elapsed_bake_time):
    """Calculate the total time for preparation.

    :param no_of_layers: int - no of layers in lasgna.
    :param elapsed_bake_time: int - elapsed bake time in the making
    :return: int - sum of the preparation time for each layer and bake_time_remaining.

    Function that takes the no_of_layers and elapsed_bake_time and return total time    """
    return preparation_time_in_minutes(no_of_layers)+ elapsed_bake_time


