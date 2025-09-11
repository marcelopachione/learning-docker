import requests
from datetime import date
from config import API_URL
from date_utils import generate_date_range

def fetch_data_for_dates(start_date, end_date):
    dates = generate_date_range(start_date, end_date)
    data = []

    for d in dates:
        try:
            r = requests.get(f'{API_URL}{d}', timeout=10)
            r.raise_for_status()
            resp_json = r.json()
            if 'data' not in resp_json or not resp_json['data']:
                continue
            intensity = resp_json['data'][0].get('intensity', {})
            forecast = intensity.get('forecast')
            actual = intensity.get('actual')
            index = intensity.get('index')
            if None in (forecast, actual, index):
                continue
            data.append({
                "search_date": date.today().strftime("%Y-%m-%d"),
                "prevision_date": d,
                "index": index,
                "actual": actual,
                "forecast": forecast
            })
        except (requests.RequestException, ValueError) as e:
            print(f"Erro ao buscar/precessar dados para {d}: {e}")
    return data