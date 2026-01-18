from otree.api import *
import time


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'dicator_trial'
    PLAYERS_PER_GROUP = None   #1人で行う
    NUM_ROUNDS = 1  #1ラウンド
    ENDOWMENT = cu(20)  #初期保有額20
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 半角数字入力形式（0〜ENDOWMENTまで）
    proposal = models.IntegerField(
        min=0,
        max=20,
        label='プレイヤー2に渡す金額を入力してください（0〜20）'
    )


def compute(player: Player):
    # プレイヤーは必ず贈与者側
    # payoffは 初期保有額 - 分配額
    player.payoff = C.ENDOWMENT - player.proposal

# PAGES
class Page1_d(Page):
    pass

class Page2_d(Page):
    form_model = 'player'
    form_fields = ['proposal']

class AlibiWaitPage(WaitPage):
    wait_for_all_groups = False
    
    @staticmethod
    def after_all_players_arrive(group: Group):
        time.sleep(1)  # 1秒待機
        for player in group.get_players():
            compute(player)

class Page3_d(Page):
    pass


page_sequence = [Page1_d, Page2_d, AlibiWaitPage, Page3_d]
