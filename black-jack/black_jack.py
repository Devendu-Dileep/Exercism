"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    return (10 if card in ['J','K','Q'] else 1 if card == 'A' else int(card))


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    higher_cards=['J','Q','K','10']
    if card_one in higher_cards and card_two in higher_cards:
        return card_one,card_two
    elif card_one in higher_cards and card_two not in higher_cards:
        return card_one
    elif card_one not in higher_cards and card_two in higher_cards:
        return card_two
    else:
        card_one= value_of_card(card_one)
        card_two= value_of_card(card_two)
        if card_one == card_two:
            if card_one == 1:
               return 'A','A'
            return str(card_one),str(card_two)
        elif card_one> card_two:
            return str(card_one)
        else:
            return str(card_two)




def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
        
    card_one= value_of_card(card_one)
    card_two= value_of_card(card_two)
    
    return (1 if card_one==1 or card_two==1 else 11 if card_one+card_two<=10 else 1)
 

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    first_hand=['A']
    second_hand=['10','K','Q','J']
    return (card_one in first_hand and card_two in second_hand) or (card_one in second_hand and card_two in first_hand)
    
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one)==value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    return value_of_card(card_one) + value_of_card(card_two) in [9,10,11]
