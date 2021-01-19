#this is life WITHOUT regular expressions
def isPhoneNumber(text):
    if len(text) != 12:
        return False  #not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal(): 
            return False  # no area code
    if text[3] != '-':
        return False  # no dash
    for i in range(4, 7): 
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False # missing 2nd dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('could not find number')
