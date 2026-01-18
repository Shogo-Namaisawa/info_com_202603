from otree.api import *
import random


doc = """
最後通牒ゲーム（対人間・MAO方式）
応答者として、受諾する「最低金額（Minimum Acceptable Offer）」を事前に入力します。
相手は人間であることを想定したゲームです。
"""


class C(BaseConstants):
    NAME_IN_URL = 'ultimatum_human'
    PLAYERS_PER_GROUP = None  # 1人で行う
    NUM_ROUNDS = 1  # 1ラウンド
    ENDOWMENT = 20  # 初期保有額20ポイント
    OPPONENT_TYPE = '人間'  # 相手のタイプ


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # MAO（最低受諾額）
    mao = models.IntegerField(
        label='受諾する最低金額（0〜20の整数）',
        min=0,
        max=C.ENDOWMENT
    )
    
    # 実際に選ばれた提案額（ランダムに決定）
    actual_offer = models.IntegerField()
    # その提案に対する応答者の回答（提案額 >= MAO なら受諾）
    actual_response = models.BooleanField()


def compute(player: Player):
    # ランダムに提案額を決定（0〜20）
    player.actual_offer = random.randint(0, C.ENDOWMENT)
    
    # 提案額がMAO以上であれば受諾
    player.actual_response = (player.actual_offer >= player.mao)
    
    # 利得計算
    if player.actual_response:  # 受け入れた場合
        player.payoff = player.actual_offer
    else:  # 拒否した場合
        player.payoff = 0


# PAGES
class Page1_u(Page):
    """説明ページ"""
    pass


class Page2_u(Page):
    """MAO入力ページ"""
    form_model = 'player'
    form_fields = ['mao']


class Page3_u(Page):
    """回答確認ページ"""
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'mao_minus_1': max(0, player.mao - 1)
        }


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = False
    
    @staticmethod
    def after_all_players_arrive(group: Group):
        import time
        time.sleep(1)  # 1秒待機
        for player in group.get_players():
            compute(player)


class Page4_u(Page):
    """結果ページ"""
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'proposer_payoff': C.ENDOWMENT - player.actual_offer if player.actual_response else 0
        }


page_sequence = [Page1_u, Page2_u, Page3_u, ResultsWaitPage, Page4_u]
