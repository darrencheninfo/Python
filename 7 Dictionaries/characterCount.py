import pprint   #The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output.

#this will count the letters in a string 'message'  
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print (count)  #standard print
pprint.pprint(count) # this will return a more readable list of the character count
