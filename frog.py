import requests
import json
import argparse

# credentials #

product = "https://emmanuell.jfrog.io/artifactory/"
username = "emmanuell2000@gmail.com"
token = "eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJFbkFYRHRXZ1h6T3ZaaDBNd3Y3VVpscU1JS3h0dG5ra3RkWS1HbWNNejJrIn0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZndkYnE3ZGNrZ2hkMTJkdzQ3d2YxbmJ6XC91c2Vyc1wvZW1tYW51ZWxsMjAwMEBnbWFpbC5jb20iLCJzY3AiOiJhcHBsaWVkLXBlcm1pc3Npb25zXC91c2VyIiwiYXVkIjoiKkAqIiwiaXNzIjoiamZmZUAwMDAiLCJleHAiOjE2NzczNDQyNDksImlhdCI6MTY0NTgwODI0OSwianRpIjoiMzczNDkxYWUtNjdlOS00MDY3LWI1OWMtNmJhZWRlOWU3YjFmIn0.gjG_hgwrtech3k8S_Ez_FZknVKCM2puiyvxpSwtc8qetxkUhGbvqcFIqykntF_vsctf0sWh8fJPHC7lTG17R8LP4-TXx9pgDgdsLdZgJUS9hvii7QdauwQeLOSHVFxo6HZXdnWA9USnolitLp7CmJwD02-e1vF6XKUP5P2pBRI-7rIdT9E6njha6xAFqyDgPhEdUz4eihrhjsSrE6UB24KjrjS2t2JwYjlqBQWV8CoglSwKqA6YwVcA66_df2Yxk6R4PRPFwMQXV03UfO2Cm2iPxpmaq0R4tTTCpUYX61RhVUWdmgfKjTPljwMWXq6dz6OyXql9uJrbuB6HaN1ZATw"


# 1 System Ping #

def ping():
    api = "api/system/ping"
    url = product + api
    response = requests.get(url, auth=(username, token))
    #  response.raise_for_status()
    if response:
        print(response.text)
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 2 System Version #

def version():
    api = "api/system/version"
    url = product + api
    response = requests.get(url, auth=(username, token))

    if response:
        print(response.json()['version'])
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 3 Create User -

def create_user(userName, passwd):
    api = f"api/security/users/{userName}"
    url = product + api
    payload = {

        "email": f"{userName}@jfrog.com",
        "password": f"{passwd}",

    }
    response = requests.put(url, json=payload, auth=(username, token))

    if response:
        print(f"user {userName} created")
        print(response.status_code)
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 4 Delete User #

def delete_user(name):
    api = f"api/security/users/{name}"
    url = product + api
    response = requests.delete(url, auth=(username, token))

    if response:
        print(response.text)
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 5 Get Storage Info #

def storage():
    api = "api/storageinfo"
    url = product + api
    response = requests.get(url, auth=(username, token))

    if response:
        print(response.json())
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 6 Create Repository

def create_repo(repoKey):
    api = f"api/repositories/{repoKey}"
    url = product + api
    payload = {"rclass": "local"}
    response = requests.put(url, json=payload, auth=(username, token))

    if response:
        print(response.text)
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 7 Delete Repository #

def delete_repo(repoKey):
    api = f"api/repositories/{repoKey}"
    url = product + api
    response = requests.delete(url, auth=(username, token))

    if response:
        print(response.text)
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 8 Update Repository #
# possible oversight in API docs that fits only for cURL: -H 'Content-Type: application/json'" ?

def update_repo(repoKey):
    api = f"api/repositories/{repoKey}"
    url = product + api
    payload = {"rclass": "local", }
    response = requests.post(url, json=payload, auth=(username, token))

    if response:
        print(response.text)
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 9 List Repositories #  list only "url" entry ?

def list_repo():
    api = "api/repositories/"
    url = product + api
    response = requests.get(url, auth=(username, token))

    if response:
        print(response.json())
    else:
        print('Response Failed')
        print(response.text)
        print(response.url)


# 10 Change Credentials #

def change_creds():
    choice = int(input("what do you wish to change?-\n 1.user name\n 2.access token"))
    if choice == 1:
        global username
        username = str(input("enter a name\n"))

    elif choice == 2:
        global token
        token = str(input("enter a token\n"))


# selection from the above functions ^ #

def opts_select():
    while True:
        try:
            user_input = int(input("""
            Please select your desired action:

            1.Perform System Ping
            2.Check System Version
            3.Create a User
            4.Delete a User
            5.Get Storage Info
            6.Create a Repository
            7.Delete a Repository
            8.Update a Repository
            9.List Repositories
            10.Change your Credentials
            11: Exit the program
            """))
            if user_input > 11 or user_input < 1:
                raise ValueError()
        except ValueError:
            print("please enter 1-11 only")
            continue

        if user_input == 1:
            ping()
        elif user_input == 2:
            version()
        elif user_input == 3:
            create_user(*input("enter a name followed by a password\n").split())
        elif user_input == 4:
            delete_user(input("enter a name\n"))
        elif user_input == 5:
            storage()
        elif user_input == 6:
            create_repo(input("enter a repository name\n"))
        elif user_input == 7:
            delete_repo(input("enter a repository name\n"))
        elif user_input == 8:
            update_repo(input("enter a repository name\n"))
        elif user_input == 9:
            list_repo()
        elif user_input == 10:
            change_creds()
        elif user_input == 11:
            print('Goodbye')
            break


parser = argparse.ArgumentParser(prog='frog', conflict_handler='resolve',
                                 description="""Emmanuell's Jfrog Artifactory CLI manager help menu""",
                                 epilog="""~Imagine There’s No Version.~""")
parser.add_argument('--help''-h', help="""This is my first help menu ever, I think the action selection menu is pretty self explenatory.
                                        there are probably things that could be expanded like sending more json payload data
                                        and then giving info on how to do those actions.
                                        More info regarding Artifactory API can be found at : https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API""")

args = parser.parse_args()

opts_select()
