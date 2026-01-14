from otree.api import *


doc = """
Closing page
"""


class C(BaseConstants):
    NAME_IN_URL = 'closing'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


page_sequence = [MyPage]
