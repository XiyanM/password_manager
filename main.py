import json
from cryptography.fernet import Fernet
import os


def get_vault(path = "pass.json"):
      if not os.path.exists(path):
            return {}
      else:
            with open(path, "r") as f:
                  return json.load(f)
        
      
      

def get_fernet(path = "key.key"):
     if not os.path.exists(path):
           key = Fernet.generate_key()
           with open("key.key", "wb") as f:
                f.write(key)

     else:
           with open("key.key", "rb") as f:
                 key = f.read()
     return Fernet(key)
          

def encrypt(vault, fernet):
      for platform in vault:
          ptpassword = vault[platform]["password"]
          if not ptpassword.startswith("gAAAA"):
             token = fernet.encrypt(ptpassword.encode("utf-8"))
             vault[platform]["password"] = token.decode("utf-8")
      with open("pass.json", "w") as f:
         json.dump(vault, f, indent=4)

def add(service, username, password, fernet, path = "pass.json"):
     vault = get_vault()
     vault[service] = {"username": username, "password": password}
     with open(path, "w") as f:
          json.dump(vault, f, indent=4)
     encrypt(vault, fernet)
          
          

def main():
     fernet = get_fernet()
     userinput = input("Actions: add get list update delete\n")
     if userinput == "add":
          line = input("Format: service username password").strip()
          items = line.split()
          if len(items) != 3:
               return print("Please input exactly 3 fields.")
          service, username, password = items
          add(items[0], items[1], items[2], fernet)

          
     
main()






    
    