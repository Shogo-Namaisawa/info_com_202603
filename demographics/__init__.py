from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models.IntegerField(
        initial=None,
        choices=[
            [0, '男性'],
            [1, '女性'],
            [2, 'その他']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">1. あなたの性別を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_age = models.IntegerField(
        initial=None,
        choices=[
            [0, '19歳以下'],
            [1, '20-29歳'],
            [2, '30-39歳'],
            [3, '40-49歳'],
            [4, '50-59歳'],
            [5, '60-69歳'],
            [6, '70歳以上']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">2. あなたの年代を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_area = models.IntegerField(
        initial=None,
        choices=[
            [0, '北海道'],
            [1, '東北地方'],
            [2, '関東地方'],
            [3, '中部地方'],
            [4, '近畿地方'],
            [5, '中国地方'],
            [6, '四国地方'],
            [7, '九州地方'],
            [8, '回答しない']
        ], 
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">3. お住まいの地方を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_education = models.IntegerField(
        initial=None,
        choices=[
            [0, '中学校卒業'],
            [1, '高等学校卒業'],
            [2, '専門学校卒業'],
            [3, '短期大学卒業'],
            [4, '大学卒業'],
            [5, '大学院修了'],
            [6, 'その他']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">4. あなたの最終学歴を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_device = models.IntegerField(
        initial=None,
        choices=[
            [0, 'パソコン'],
            [1, 'タブレット'],
            [2, 'スマートフォン'],
            [3, 'それ以外']
        ], 
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">5. 現在お使いの回答端末を教えてください。</span>',
        widget=widgets.RadioSelect
    )


# PAGES
class DemographicPage(Page):
    """デモグラフィック情報収集ページ"""
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_area', 'q_education', 'q_device']


page_sequence = [DemographicPage]
