Password Manager 

A simple command-line password manager built in Python.
Passwords are encrypted using Fernet (symmetric encryption) from the cryptography library and stored securely in a local JSON file.

⸻

 Features
	•	Add new credentials (service, username, password)
	•	Get stored password (decrypted at runtime)
	•	List all saved services
	•	Update existing credentials
	•	Delete a service (with confirmation)
	•	Quit to exit the program
	•	Hidden password input with getpass

⸻

 How It Works
	•	Credentials are stored in pass.json
	•	Passwords are encrypted using a key stored in key.key
	•	Only encrypted values are stored; decryption happens when retrieving

⸻

 • Installation

Clone the repo and set up a virtual environment:

git clone https://github.com/XiyanM/password_manager.git

cd password_manager

 • create virtual environment
 
python -m venv .venv

source .venv/bin/activate         # mac/linux

.venv\Scripts\activate            # windows

 • install dependencies
 
pip install -r requirements.txt


⸻

 • Usage

Run the program:

python main.py

 • Example interaction:

Actions: add get list update delete quit
add

Service: gmail

Username: johndoe

Password (input hidden): ******

Added successfully.


⸻

• Project Structure
```
password_manager/
│── main.py          # main program
│── pass.json        # vault (auto-created, ignored in git)
│── key.key          # encryption key (auto-created, ignored in git)
│── requirements.txt # dependencies
│── .gitignore
│── README.md
```

⸻

 • Future Improvements
	•	Copy password to clipboard (pyperclip)
	•	Multi-user support
	•	GUI version (Tkinter / Flask webapp)
	•	Automatic password generation

⸻

 • Security Note

This is a learning project. Don’t use it as your only password manager for sensitive accounts.

⸻
