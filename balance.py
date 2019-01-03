#!/usr/bin/env python3

import datetime
from datetime import timedelta

accounts = {
    'cache': {
        'name':'cache',
        'balance': 42902,
    },
    'suica': {
        'name':'suica',
        'balance': 8525,
    },
    'sumisei_fund': {
        'name':'sumisei_fund',
        'balance': 7351,
    },
    'jibun_bank': {
        'name':'jibun_bank',
        'balance': 0,
    },
    'joyo_bank': {
        'name':'joyo_bank',
        'balance': 37242,
    },
    'sumisin_sbi_bank': {
        'name':'sumisin_sbi_bank',
        'balance': 20000,
    },
    'mufg_bank': {
        'name':'mufg_bank',
        'balance': 165960,
    },
    'mufg_card_visa': {
        'name':'mufg_card_visa',
        'balance': -162662,
    },
    'mufg_card_jcb': {
        'name':'mufg_card_jcb',
        'balance': 0,
    },
    'rakuten_card': {
        'name':'rakuten_card',
        'balance': -2410,
    },
}

start_date = datetime.date(2019, 1, 2)
end_date = datetime.date(2021, 1, 2)

print("hello")

