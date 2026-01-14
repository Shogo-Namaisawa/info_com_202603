from otree.api import *


doc = """
Instruction page
"""


class C(BaseConstants):
    NAME_IN_URL = 'instruction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class StartPage(Page):
    pass


page_sequence = [StartPage]
