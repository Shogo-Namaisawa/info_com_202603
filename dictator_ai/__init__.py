from otree.api import *
import time


doc = """
独裁者ゲーム（対AI）
相手はAIであることを想定したゲームです。
"""


class C(BaseConstants):
    NAME_IN_URL = 'dictator_ai'
    PLAYERS_PER_GROUP = None   # 1人で行う
    NUM_ROUNDS = 1  # 1ラウンド
    ENDOWMENT = cu(20)  # 初期保有額20
    OPPONENT_TYPE = 'AI'  # 相手のタイプ


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
    
    # 理解度確認の問題（初期保有20、20渡した場合の自分の利得）
    comprehension_answer = models.IntegerField(
        label='あなたの利得（ポイント）',
        choices=[
            [0, '0ポイント'],
            [5, '5ポイント'],
            [13, '13ポイント'],
            [20, '20ポイント'],
        ],
        widget=widgets.RadioSelect
    )


def compute(player: Player):
    # プレイヤーは必ず贈与者側
    # payoffは 初期保有額 - 分配額
    player.payoff = C.ENDOWMENT - player.proposal


# PAGES
class Page1_d_ai(Page):
    pass


class Check_d_ai(Page):
    form_model = 'player'
    form_fields = ['comprehension_answer']


class Answer_d_ai(Page):
    pass


class Page2_d_ai(Page):
    form_model = 'player'
    form_fields = ['proposal']


class AlibiWaitPage(WaitPage):
    wait_for_all_groups = False
    
    @staticmethod
    def after_all_players_arrive(group: Group):
        time.sleep(1)  # 1秒待機
        for player in group.get_players():
            compute(player)


class Page3_d_ai(Page):
    pass


page_sequence = [Page1_d_ai, Check_d_ai, Answer_d_ai, Page2_d_ai, AlibiWaitPage, Page3_d_ai]
