import requests
import argparse
from config import EMAIL, PASS

print(EMAIL, PASS)
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", help="Add some information", action="store_true")
parser.add_argument("-l", "--listinfo", help="List all informations", action="store_true")
parser.add_argument("-t", "--gettoken", help="Get token", action="store_true")



class ApiCaller:
    
    def __init__(self, email, passw):
        self.email = email
        self.passw = passw
        self.base_url = "https://questions-api-ivan.herokuapp.com/"
        # self.base_url = "http://localhost:8000/"

    def get_token(self):
        url = self.base_url + "users/api-token-auth/"
        response = requests.post(url, data={"username": self.email, "password": self.passw})
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
        print(response)
        return response.status_code

    def list_info(self):
        token = self.get_token()
        headers = {"Authorization": f"Token {token}"}
        url = self.base_url + "info/"
        response = requests.get(url, headers=headers)
        print(response.json())
        return response


if __name__ == "__main__":
    args = parser.parse_args()
    ac = ApiCaller(email=EMAIL, passw=PASS)
    if args.add:
        ac.add_info()
    elif args.listinfo:
        ac.list_info()
    else:
        print("Please enter some argument, use -h for help")

