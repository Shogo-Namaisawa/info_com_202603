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
    # 感想3問
    q_survey1 = models.IntegerField(
        initial=None,
        choices=[
            [1, '全くそう思わない'],
            [2, 'あまりそう思わない'],
            [3, 'どちらともいえない'],
            [4, 'ややそう思う'],
            [5, '非常にそう思う']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">この実験は興味深かったですか？</span>',
        widget=widgets.RadioSelect
    )
    
    q_survey2 = models.IntegerField(
        initial=None,
        choices=[
            [1, '全く理解できなかった'],
            [2, 'あまり理解できなかった'],
            [3, 'どちらともいえない'],
            [4, 'やや理解できた'],
            [5, '非常に理解できた']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">実験の内容は理解しやすかったですか？</span>',
        widget=widgets.RadioSelect
    )
    
    q_survey3 = models.IntegerField(
        initial=None,
        choices=[
            [1, '全く真剣に取り組めなかった'],
            [2, 'あまり真剣に取り組めなかった'],
            [3, 'どちらともいえない'],
            [4, 'やや真剣に取り組めた'],
            [5, '非常に真剣に取り組めた']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">実験中、真剣に取り組むことができましたか？</span>',
        widget=widgets.RadioSelect
    )
    
    # AI認識に関する質問
    q_ai_awareness = models.IntegerField(
        initial=None,
        choices=[
            [1, '全く感じなかった'],
            [2, 'あまり感じなかった'],
            [3, 'どちらともいえない'],
            [4, 'やや感じた'],
            [5, '非常に感じた']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">実験中、対戦相手がAIエージェントであるとどの程度感じましたか？</span>',
        widget=widgets.RadioSelect
    )
    
    # 自由記述
    q_free_comment = models.LongStringField(
        initial=None,
        blank=True,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">この実験について、ご意見やご感想があればご自由にお書きください。</span>'
    )


# PAGES
class Survey(Page):
    """実験後アンケートページ"""
    form_model = 'player'
    form_fields = ['q_survey1', 'q_survey2', 'q_survey3', 'q_ai_awareness', 'q_free_comment']


class Results(Page):
    pass


page_sequence = [Survey, Results]
