import requests
import json

from config import url, rules
from mail import send_smtp_email


def get_rates():
    api_response = requests.get(url)
    if api_response.status_code == 200:
        return json.loads(api_response.text)
    return None


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp, rates):
    subject = f'{timestamp} rates'

    if rules['preferred'] is not None:
        tmp = dict()
        for exc in rules['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp

    text = json.dumps(rates)

    send_smtp_email(subject, text)


if __name__ == "__main__":
    response = get_rates()
    if rules['archive']:
        archive(response['date'], response['rates'])

    if rules['send_mail']:
        send_mail(response['date'], response['rates'])
