import json
import time
import requests


base_url = "http://192.168.1.73:8000/api/v1/hardware/"
current_session_url = base_url + "session/current/"
session_detail_url = base_url + "session/"
hardware_info_url = base_url + "info/1/"

while True:
    hardware_info_response = requests.get(hardware_info_url).json()
    automatic_process = hardware_info_response['is_process_started']
    print(f'automatic - {automatic_process} ---------')


    if automatic_process:
        print('Here-----------')
        
        current_session_response = requests.get(current_session_url).json() 
        current_session_id = current_session_response['id']
        print(f'{current_session_id} 00000000000000++++++++')

        if current_session_response['is_image_capture']:
            print('===========Capturing Image')
            time.sleep(5)
            set_image_capture = {
                'is_image_capture': False
            }
            response = requests.patch(f'{session_detail_url}{current_session_id}/', json=set_image_capture)
            print(f'++++++++++++++++++ Image CAptured ')
            response_dict = json.loads(response.text)
            print(response_dict['is_image_capture'])

    time.sleep(1)