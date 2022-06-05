import requests
import json
from config import url


def get_rates():
    api_response = requests.get(url)
    if api_response.status_code == 200:
        return json.loads(api_response.text)
    return None


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


if __name__ == "__main__":
    response = get_rates()
    archive(response['date'], response['rates'])
