# mapIt.py - Launch a google maps in the browser using an address 
#     from the command line  or clipboard (command line empty)


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get the address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # TODO: Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
