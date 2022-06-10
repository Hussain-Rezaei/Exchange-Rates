url = 'https://api.exchangerate.host/latest'


rules = {
    'archive': True,
    'send_mail': True,
    # preferred default is None
    # 'preferred': None
    'preferred': ['BTC', "USD", "CAD", "AED"]
}