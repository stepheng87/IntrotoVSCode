import pandas as pd

default_path=r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\IntrotoVSCode'

codes={'A':'%','a':'9','B':'@','b':'19','C':'#','c':'14','D':'$','d':'4','E':'&','e':'3','F':'*','f':'15','G':'(','g':'7','H':')','h':'8','I':'-','i':'1','J':'+','j':'16','K':',','k':'17','L':'.','l':'18','M':'/','m':'20','N':'0','n':'21','O':':','o':'67','P':';','p':'23','Q':'<','q':'24','R':'=','r':'25','S':'>','s':'83','T':'?','t':'27','U':'@','u':'32','V':'A','v':'!@','W':'B','w':'30','X':'C','x':'31','Y':'D','y':'98','Z':'E','z':'56'}

with open(default_path+r'\info_security-1.txt','r') as file:
    text=file.read()

encrypted_text=""
for char in text:
    if char in codes: encrypted_text+=codes[char]
    else: encrypted_text+=char

print(encrypted_text)

with open(default_path+r'\encrypted.txt','w') as file:
    file.write(encrypted_text)