import json
import time
import requests
from run_motor import RunMotor, RunWaterPump, RunMotorReverse


base_url = "http://192.168.1.73:8000/api/v1/hardware/"
current_session_url = base_url + "session/current/"
session_detail_url = base_url + "session/"
hardware_info_url = base_url + "info/1/"

for i in range(5):
    # check if automatic process is true
    hardware_info_response = requests.get(hardware_info_url).json()
    automatic_process = hardware_info_response['is_process_started']
    print(f'automatic - {automatic_process} ---------')

    if automatic_process:
        current_session_response = requests.get(current_session_url).json()
        current_session_id = current_session_response['id']
        print(f'{current_session_id} 00000000000000++++++++')

        total_time_required = hardware_info_response['total_time']
        motor_running_time = hardware_info_response['motor_run_time']
        water_motor_running_time = hardware_info_response['water_motor_run_time']
        capture_image_delay_time = 3

        total_cycles = int(total_time_required / motor_running_time)
        print(f'total cycles - {total_cycles} +++++++++')

        for i in range(total_cycles):
            RunMotor(motor_running_time)

            # Set CaptureImage = True
            time.sleep(2)
            set_image_capture = {
                'is_image_capture': True
            }
            response = requests.patch(f'{session_detail_url}{current_session_id}/', json=set_image_capture)
            print(f'++++++++++++++++++')
            response_dict = json.loads(response.text)
            print(response_dict['is_image_capture'])
            
            response = requests.get(f'{session_detail_url}{current_session_id}/').json()
            while True:
                response = requests.get(f'{session_detail_url}{current_session_id}/').json()
                time.sleep(capture_image_delay_time)
                if response['is_image_capture'] is False:
                    break

            time.sleep(capture_image_delay_time)

            # Classify Image
            classified_result = "UnHealthy"
            if classified_result != "Healthy":
                RunWaterPump(water_motor_running_time)

            print('----------------- apple')

        # set automatic process = False
        print('-----------------')
        RunMotorReverse(motor_running_time * total_cycles)
        context = {
            'is_process_started': False
        }
        hardware_info_response = requests.patch(hardware_info_url, json=context)

        context_hardware_session = {
            'is_current_session': False,
            'is_completed': True
        }
        hardware_session_response = requests.patch(f'{session_detail_url}{current_session_id}/', json=context_hardware_session)
        # response_dict = json.loads(response.text)
        # print(response_dict['is_image_capture'])
        # print(f'at last automatic {response_dict} 0000000000')

    time.sleep(1)

