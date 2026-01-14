from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'bigfive'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    big5_1 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">1.活発で，外向的だと思う</span>',
                                widget=widgets.RadioSelect()
                                )

    big5_2 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">2.他人に不満をもち，もめごとを起こしやすいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_3 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">3.しっかりしていて，自分に厳しいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_4 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">4.心配性で，うろたえやすいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_5 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">5.新しいことが好きで，変わった考えをもつと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_6 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">6.ひかえめで，おとなしいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_7 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">7.人に気をつかう，やさしい人間だと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    # 不真面目回答者を抽出する項目, 
    big5_IMC =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">8.この選択肢では下から三番目を選択してください</span>',
                                widget=widgets.RadioSelect()
                                )

    big5_8 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">9.だらしなく，うっかりしていると思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_9 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">10.冷静で，気分が安定していると思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_10 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">11.発想力に欠けた，平凡な人間だと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    Gaiko = models.IntegerField()
    Kyocho = models.IntegerField()
    Kinben = models.IntegerField()
    Shinkei = models.IntegerField()
    Kaiho = models.IntegerField()


# PAGES
class BigFivePage(Page):
    """BigFive心理調査ページ"""
    form_model = 'player'
    form_fields = ['big5_1',
                   'big5_2',
                   'big5_3',
                   'big5_4',
                   'big5_5',
                   'big5_6',
                   'big5_7',
                   'big5_IMC', # 不適切回答者を抽出する項目
                   'big5_8',
                   'big5_9',
                   'big5_10']


page_sequence = [BigFivePage]
