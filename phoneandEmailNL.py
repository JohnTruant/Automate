#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard. 

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\(0\d{1,3}\)|0\d{1,3}) #06 of regiocode
    (\s|\-)?    # ruimte
    (\d{6,8})   # telefoonnummer
    )''', re.VERBOSE)

# Create email regex. 
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})           #dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text. 
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = ''.join([groups[1], groups[2], groups[3]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')