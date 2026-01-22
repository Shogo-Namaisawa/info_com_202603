from os import environ
import dj_database_url

SESSION_CONFIGS = [
    dict(
        name='former_game_sequence',
        display_name='Former Game Sequence',
        app_sequence=['instruction', 'demographics', 'bigfive', 'dictator_human', 'dictator_ai', 'ultimatum_human', 'ultimatum_ai', 'closing'],
        num_demo_participants=1,
    ),
    dict(
        name='latter_game_sequence',
        display_name='Latter Game Sequence',
        app_sequence=['instruction', 'demographics', 'dictator_human', 'dictator_ai', 'ultimatum_human', 'ultimatum_ai', 'bigfive', 'closing'],
        num_demo_participants=1,
    ),
    dict(
        name='bigfive_test',
        display_name='BigFive (テスト用)',
        app_sequence=['bigfive'],
        num_demo_participants=1,
    ),
    dict(
        name='dictator_ai_test',
        display_name='Dictator AI (テスト用)',
        app_sequence=['dictator_ai'],
        num_demo_participants=1,
    ),
    dict(
        name='dictator_human_test',
        display_name='Dictator Human (テスト用)',
        app_sequence=['dictator_human'],
        num_demo_participants=1,
    ),
    dict(
        name='ultimatum_ai_test',
        display_name='Ultimatum AI (テスト用)',
        app_sequence=['ultimatum_ai'],
        num_demo_participants=1,
    ),
    dict(
        name='ultimatum_human_test',
        display_name='Ultimatum Human (テスト用)',
        app_sequence=['ultimatum_human'],
        num_demo_participants=1,
    ),
    dict(
        name='closing_test',
        display_name='Closing (テスト用)',
        app_sequence=['closing'],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9433999788057'

# データベース設定（PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'otree_db',      # ステップ1でつけた名前
        'USER': 'postgres',      # pgAdmin接続時のユーザー名
        'PASSWORD': 'ange0827',          # Postgres.appなら空欄で動くことが多いですが、設定していればそのパスワード
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# settings.py の一番下の行に追加
