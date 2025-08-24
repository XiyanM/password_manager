import json
from cryptography.fernet import Fernet
import os
import getpass


def get_vault(path = "pass.json"):
      if not os.path.exists(path):
            return {}
      try:
            with open(path, "r") as f:
                  return json.load(f)
      except json.JSONDecodeError:
           return {}
           
        
      
      

def get_fernet(path = "key.key"):
     if not os.path.exists(path):
           key = Fernet.generate_key()
           with open(path, "wb") as f:
                f.write(key)

     else:
           with open(path, "rb") as f:
                 key = f.read()
     return Fernet(key)
          

def add(service, username, password, fernet, path = "pass.json"):
     vault = get_vault()
     vault[service] = {"username": username, "password": (fernet.encrypt(password.encode("utf-8"))).decode()}
     with open(path, "w") as f:
          json.dump(vault, f, indent=4)
          
          

def main():
     fernet = get_fernet()
     while True:
        userinput = input("Actions: add get list update delete quit\n")

        if userinput == "add":
            service = input("Service: ").strip()
            username = input("Username: ").strip()
            password = getpass.getpass("Password (input hidden): ")
            add(service, username, password, fernet)
            print("Added successfully.")
            continue

        elif userinput == "get":
            service = input("Service: ").strip()
            username = input("Username: ").strip()
            vault = get_vault()
            if service not in vault:
                print("No such service found.")
                continue
            if vault[service]["username"] != username:
                print("Username mismatch.")
                continue
            print((fernet.decrypt(vault[service]["password"].encode("utf-8"))).decode("utf-8"))
            continue

    
        elif userinput == "list":
            vault = get_vault()
            print("Platforms:")
            for service in vault:
                print(service)
            continue

        elif userinput == "update":
            service = input("Service: ").strip()
            username = input("Username: ").strip()
            password = getpass.getpass("Password (input hidden): ")
            vault = get_vault()
            if service not in vault:
                print("No such service found.")
                continue
            vault[service]["username"] = username
            vault[service]["password"] = (fernet.encrypt(password.encode("utf-8"))).decode("utf-8")

            with open("pass.json", "w") as f:
                json.dump(vault, f, indent=4)
            print("Information updated successfully.")
            continue

        elif userinput == "delete":
            line = input("Input which service to delete.\n").strip()
            vault = get_vault()
            if line not in vault:
                print("No such service found.")
                continue
            check = input(f"Delete {line}? (y/N) ").lower()
            if check == "y":
                del vault[line]
                with open("pass.json", "w") as f:
                    json.dump(vault, f, indent=4)
                print("Successfully deleted.")
                continue
            continue
        
        elif userinput == "quit":
            break


if __name__ == "__main__":
     main()     






    
    