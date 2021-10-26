import requests
import argparse
from config import EMAIL, PASS
from colors import bcolors

####
# ANtoher comment
#####


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", help="Add some information", action="store_true")
parser.add_argument("-l", "--listinfo", help="List all informations", action="store_true")
parser.add_argument("-t", "--gettoken", help="Get token", action="store_true")
parser.add_argument("-d", "--delete", help="Delete information", action="store_true")
parser.add_argument("-f", "--finish", help="Mark task as finished", action="store_true")


class ApiCaller:
    
    def __init__(self, email, passw):
        self.email = email
        self.passw = passw
        self.base_url = "https://questions-api-ivan.herokuapp.com/"
        # self.base_url = "http://localhost:8000/"

    def get_token(self):
        url = self.base_url + "users/api-token-auth/"
        response = requests.post(url, data={"username": self.email, "password": self.passw})
        # response = requests.post(url, data={"username": "admin@admin.com", "password": "django123"})
        if "token" not in response.json():
            raise ValueError(f"CREDIDENTIALS {self.email} ARE NOT VALID")
        auth_token = response.json()["token"]
        return auth_token

    def add_info(self):
        token = self.get_token()
        headers = {"Authorization": f"Token {token}"}
        title = input("Please enter a title for your information\n")
        description = input("Please enter a description for your info\n")
        url = self.base_url + "info/"
        response = requests.post(url, headers=headers, data={"title": title, "description": description})
        print(response.json())
        return response.status_code

    def list_info(self):
        token = self.get_token()
        headers = {"Authorization": f"Token {token}"}
        url = self.base_url + "info/"
        response = requests.get(url, headers=headers)
        data = response.json()
        for d in data:
            finish = f"{bcolors.WARNING}NOT FINISHED YET{bcolors.ENDC}"
            if d['finished']:
                finish = f"{bcolors.FAIL}FINISHED{bcolors.ENDC}"
            print(f"ID:{d['id']}\nTITLE:{bcolors.BOLD}{d['title']}{bcolors.ENDC}\nDESCRIPTION:{d['description']}\nDATE:{d['date']}\nFINISHED:{finish}")
            print(10 * "==")
        return response
    
    def delete_info(self):
        info_id = input("Please enter ID of the info you want to delete\n")
        token = self.get_token()
        headers = {"Authorization": f"Token {token}"}
        url = self.base_url + f"info/{info_id}/"
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print("Information deleted")
        else:
            print(response)
        return response.status_code

    def finish_info(self):
        info_id = input("Please enter ID of the info you finished\n")
        token = self.get_token()
        headers = {"Authorization": f"Token {token}"}
        url = self.base_url + f"info/{info_id}/finish/"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Task with ID: {info_id} marked as FINISHED")
        else:
            print(response)
        return response.status_code



if __name__ == "__main__":
    args = parser.parse_args()
    ac = ApiCaller(email=EMAIL, passw=PASS)
    if args.add:
        ac.add_info()
    elif args.listinfo:
        ac.list_info()
    elif args.delete:
        ac.delete_info()
    elif args.finish:
        ac.finish_info()
    else:
        print("Please enter some argument, use -h for help")

