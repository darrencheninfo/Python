cat_names = []

while True:
    print ('Input the cat ' + str(len(cat_names)+1) + ' or input nothing to break')
    name = input()
    if name == '':
        break
    else:
        cat_names = cat_names + [name]

if not cat_names:
    print ("You have no cats")
else: 
    print ("Now you have cats with these names: ")
    # for i in range(len(cat_names)):
    #     print ("The cat " + str(i) + " is " + cat_names[i])
    for name in cat_names:
        print (name)
