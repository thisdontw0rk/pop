import ansible_runner
import requests

def run_hello_playbook():
    r = ansible_runner.run(
        private_data_dir='.',  
        inventory='./hosts.yml',
        playbook='hello.yml'
    )


    
    verify_nodejs_response('http://127.0.0.1:3000/')
    verify_nodejs_response('http://127.0.0.1:3001/')
    verify_nodejs_response('http://127.0.0.1:3002/')
    verify_nodejs_response('http://127.0.0.1:80/')


def verify_nodejs_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Success! Received response from NodeJS server:", response.text)
        else:
            print("Failed to receive a successful response, status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error trying to reach the NodeJS server:", e)

if __name__ == "__main__":
    run_hello_playbook()
