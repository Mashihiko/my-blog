from mysite.settings import *
DEBUG = True
SECRET_KEY = 'b+x@!a%rgmpw%s#5@f_xtc1i9i!@fn0ldcx!)2=)y7cs*3-_xj'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { #ログ出力の形式を設定
        'production': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "%(asctime)s",
                "%(name)s.%(funcName)s:%(lineno)s",
                "%(message)s",
            ])
        },
    },
    'handlers': {    #ログの出力先の設定
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'django.log',  #環境に合わせて変更
            'formatter': 'production',
            'level': 'INFO',
    },
          'console': { # どこに出すかの設定をもう一つ、こちらの設定には`console`という名前
            'level': 'INFO',
            # こちらは標準出力に出してくれるクラスを指定
            'class': 'logging.StreamHandler', 
            'formatter': 'production'
        },

    },
    'loggers': {#
        # 自作したログ出力
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Djangoの警告・エラー
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'blog.views': {
            'handlers': ['file','console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

