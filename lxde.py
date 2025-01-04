import os

print("updating...")
os.system("sudo apt-get update")
os.system("clear")
print("installing lxde...")
os.system("sudo apt install lxde -y")
os.system("clear")
print("installing crd...")
os.system("wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb && sudo apt install ./chrome-remote-desktop_current_amd64.deb")
print("visit https://remotedesktop.google.com/headless, get the debian code and paste it here. (you need to configure a 6 digit pin)")