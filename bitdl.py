import requests
import re

base = 'http://s21.bitdl.ir/A-B/Hacked/Attack.on.Titan.2.PS4-DUPLEX/'
r = requests.get(base)

files = re.findall(r'<a href="(.*?)" title="\1"', r.text, "base")

for f in files:
    fr = requests.get(base + f)
    print(f'Starting download of {f}.')
    with open(f, 'wb') as binfile:
        binfile.write(fr.content)
    print(f'Downloading {f} finished.')