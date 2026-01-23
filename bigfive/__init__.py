from otree.api import *


doc = """
Big Five 29項目短縮版
変数名規則: big5_[因子][番号][_R]
- 因子: E(外向性), N(情緒不安定性), O(開放性), C(誠実性), A(協調性)
- _R: 逆転項目
"""


class C(BaseConstants):
    NAME_IN_URL = 'bigfive'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # 回答選択肢
    BIG5_CHOICES = [
        [1, '1：全く当てはまらない'],
        [2, '2：ほとんど当てはまらない'],
        [3, '3：あまり当てはまらない'],
        [4, '4：どちらでもない'],
        [5, '5：やや当てはまる'],
        [6, '6：かなり当てはまる'],
        [7, '7：非常に当てはまる'],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # ===== 外向性 (Extraversion) - 5項目 =====
    # E1: 話好き (正転)
    big5_E1 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">話好き</span>',
        widget=widgets.RadioSelect()
    )
    # E2: 無口な (逆転)
    big5_E2_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">無口な</span>',
        widget=widgets.RadioSelect()
    )
    # E3: 陽気な (正転)
    big5_E3 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">陽気な</span>',
        widget=widgets.RadioSelect()
    )
    # E4: 外向的 (正転)
    big5_E4 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">外向的</span>',
        widget=widgets.RadioSelect()
    )
    # E5: 社交的 (正転)
    big5_E5 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">社交的</span>',
        widget=widgets.RadioSelect()
    )

    # ===== 情緒不安定性 (Neuroticism) - 5項目 =====
    # N1: 不安になりやすい (正転)
    big5_N1 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">不安になりやすい</span>',
        widget=widgets.RadioSelect()
    )
    # N2: 心配性 (正転)
    big5_N2 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">心配性</span>',
        widget=widgets.RadioSelect()
    )
    # N3: 弱気になる (正転)
    big5_N3 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">弱気になる</span>',
        widget=widgets.RadioSelect()
    )
    # N4: 緊張しやすい (正転)
    big5_N4 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">緊張しやすい</span>',
        widget=widgets.RadioSelect()
    )
    # N5: 憂鬱な (正転)
    big5_N5 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">憂鬱な</span>',
        widget=widgets.RadioSelect()
    )

    # ===== 開放性 (Openness) - 6項目 =====
    # O1: 独創的な (正転)
    big5_O1 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">独創的な</span>',
        widget=widgets.RadioSelect()
    )
    # O2: 多才の (正転)
    big5_O2 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">多才の</span>',
        widget=widgets.RadioSelect()
    )
    # O3: 進歩的 (正転)
    big5_O3 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">進歩的</span>',
        widget=widgets.RadioSelect()
    )
    # O4: 頭の回転の速い (正転)
    big5_O4 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">頭の回転の速い</span>',
        widget=widgets.RadioSelect()
    )
    # O5: 興味の広い (正転)
    big5_O5 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">興味の広い</span>',
        widget=widgets.RadioSelect()
    )
    # O6: 好奇心が強い (正転)
    big5_O6 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">好奇心が強い</span>',
        widget=widgets.RadioSelect()
    )

    # ===== 誠実性 (Conscientiousness) - 7項目 =====
    # C1: いい加減な (逆転)
    big5_C1_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">いい加減な</span>',
        widget=widgets.RadioSelect()
    )
    # C2: ルーズな (逆転)
    big5_C2_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">ルーズな</span>',
        widget=widgets.RadioSelect()
    )
    # C3: 怠慢な (逆転)
    big5_C3_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">怠慢な</span>',
        widget=widgets.RadioSelect()
    )
    # C4: 成り行きまかせ (正転)
    big5_C4 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">成り行きまかせ</span>',
        widget=widgets.RadioSelect()
    )
    # C5: 計画性のある (正転)
    big5_C5 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">計画性のある</span>',
        widget=widgets.RadioSelect()
    )
    # C6: 軽率な (逆転)
    big5_C6_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">軽率な</span>',
        widget=widgets.RadioSelect()
    )
    # C7: 几帳面な (正転)
    big5_C7 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">几帳面な</span>',
        widget=widgets.RadioSelect()
    )

    # ===== 協調性 (Agreeableness) - 6項目 =====
    # A1: 温和な (正転)
    big5_A1 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">温和な</span>',
        widget=widgets.RadioSelect()
    )
    # A2: 短気 (逆転)
    big5_A2_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">短気</span>',
        widget=widgets.RadioSelect()
    )
    # A3: 怒りっぽい (逆転)
    big5_A3_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">怒りっぽい</span>',
        widget=widgets.RadioSelect()
    )
    # A4: 寛大な (正転)
    big5_A4 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">寛大な</span>',
        widget=widgets.RadioSelect()
    )
    # A5: 親切な (正転)
    big5_A5 = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">親切な</span>',
        widget=widgets.RadioSelect()
    )
    # A6: 自己中心的 (逆転)
    big5_A6_R = models.IntegerField(
        initial=None,
        choices=C.BIG5_CHOICES,
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">自己中心的</span>',
        widget=widgets.RadioSelect()
    )

    # 各因子の合計得点
    Gaiko = models.IntegerField()       # 外向性 (E)
    Shinkei = models.IntegerField()     # 情緒不安定性 (N)
    Kaiho = models.IntegerField()       # 開放性 (O)
    Kinben = models.IntegerField()      # 誠実性 (C)
    Kyocho = models.IntegerField()      # 協調性 (A)


# PAGES
class BigFivePage1(Page):
    """BigFive心理調査ページ1（前半15問）"""
    form_model = 'player'
    # 因子がバラバラになるよう固定順で並び替え（前半）
    form_fields = [
        'big5_E1',      # 1. 話好き (外向性)
        'big5_N1',      # 2. 不安になりやすい (情緒不安定性)
        'big5_O1',      # 3. 独創的 (開放性)
        'big5_C1_R',    # 4. いい加減 (誠実性・逆転)
        'big5_A1',      # 5. 温和な (協調性)
        'big5_E2_R',    # 6. 無口な (外向性・逆転)
        'big5_N2',      # 7. 心配性 (情緒不安定性)
        'big5_O2',      # 8. 多才な (開放性)
        'big5_C2_R',    # 9. ルーズな (誠実性・逆転)
        'big5_A2_R',    # 10. 短気 (協調性・逆転)
        'big5_E3',      # 11. 陽気な (外向性)
        'big5_N3',      # 12. 弱気になる (情緒不安定性)
        'big5_O3',      # 13. 進歩的 (開放性)
        'big5_C3_R',    # 14. 怠慢な (誠実性・逆転)
        'big5_A3_R',    # 15. 怒りっぽい (協調性・逆転)
    ]


class BigFivePage2(Page):
    """BigFive心理調査ページ2（後半14問）"""
    form_model = 'player'
    # 因子がバラバラになるよう固定順で並び替え（後半）
    form_fields = [
        'big5_E4',      # 16. 外向的 (外向性)
        'big5_N4',      # 17. 緊張しやすい (情緒不安定性)
        'big5_O4',      # 18. 頭の回転が速い (開放性)
        'big5_C4',      # 19. 成り行きまかせ (誠実性)
        'big5_A4',      # 20. 寛大な (協調性)
        'big5_E5',      # 21. 社交的 (外向性)
        'big5_N5',      # 22. 憂鬱な (情緒不安定性)
        'big5_O5',      # 23. 興味が広い (開放性)
        'big5_C5',      # 24. 計画性のある (誠実性)
        'big5_A5',      # 25. 親切な (協調性)
        'big5_O6',      # 26. 好奇心が強い (開放性)
        'big5_C6_R',    # 27. 軽率な (誠実性・逆転)
        'big5_A6_R',    # 28. 自己中心的 (協調性・逆転)
        'big5_C7',      # 29. 几帳面な (誠実性)
    ]


page_sequence = [BigFivePage1, BigFivePage2]
