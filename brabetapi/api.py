import requests, uuid
from brabetapi.headers import headers

red_numbers = [1, 2, 3, 4, 5, 6, 7]
black_numbers = [8, 9, 10, 11, 12, 13, 14]

class BrabetAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.api_url = 'https://api.brabetxl4oq.com/'
        self.get_token()

    def send_request(self, url, method='GET', json_data=None):
        try:
            response = self.session.request(method, self.api_url + url, json=json_data)
            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
            
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

    def get_token(self):
        json_data = {
            'mainVer': 1,
            'subVer': 1,
            'pkgName': 'h5_client',
            'nativeVer': 0,
            'deviceid': f'PC_{uuid.uuid4()}',
            'pixelid': '',
            'kwai_id': '',
            'kwai_pixel_id': '',
            'kwai_click_id': '',
            'skyads_click_id': '',
            'skyads_pixel_id': '',
            'skyads_utm_source': '',
            'google_id': 'G-M36ZXGX5X0',
            'tiktok_id': '',
            'gtm_id': '',
            'oks_pixel_id': '',
            'oks_pixel_click_id': '',
            'oks_utm_source': '',
            'fbclid': '',
            'facebook_pix_id_server': '',
            'domain': 'https://www.brabet.com',
            'appsflyer_id': None,
            'appsflyer_key': None,
            'loadLocation': 'https://www.brabet.com/',
            'source': '10',
            'Type': 101,
            'os': 'Windows',
            'isShell': 0,
            'ioswebclip': 0,
            'login_source': 0,
            'report_type': 3,
            'lat': None,
            'lng': None,
            'language': 'pt-pt',
            'sys_api_version': 1,
        }

        response = self.send_request('login/visitor_login', method='POST', json_data=json_data)
        self.token = response['data']['token']

    def get_double_history(self, limit: int=12, result_type: int=3):
        json_data = {
            'limit': limit,
            'token': self.token,
            'type': result_type,
            'language': 'pt-pt',
            'sys_api_version': 1,
        }

        response = self.send_request('goldGame/double_history', method='POST', json_data=json_data)
        return response['data']

    def get_crash_history(self):
        json_data = {
            'type': 2,
            'uid': 0,
            'language': 'pt-pt',
            'sys_api_version': 1,
        }

        response = self.send_request('Goldgame/bd_history', method='POST', json_data=json_data)
        return response['data']

    def format_double_history(self, history):
        formatted_history = []
        for roll in history:
            roll = int(roll)
            color = 'black' if roll in black_numbers else 'red' if roll in red_numbers else 'white'
            formatted_history.append({
                'roll': roll,
                'color': color,
            })
        return formatted_history