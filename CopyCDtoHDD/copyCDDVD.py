# copy from H: drive to the anime folder on the F:drive
# F5 to run

#TO DO: if file already exists, skip and copy remaining files
import shutil, os

sourceList = os.listdir('H:\\')

destination = 'F:\\anime\\azumanga daioh\\'  #UPDATE THE SAVE DESTINATION
destinationList = os.listdir(destination)   

for i in range(len(sourceList)):
    sourceCopy = 'H:\\\\' + sourceList[i]   
    if sourceList[i] in destinationList:    #check if file already exists in destination
        i = i + 1
    else: 
        print('Now copying...' + sourceList[i])
        shutil.copy(sourceCopy, destination)    # actual copy line

print('CD/DVD files copied to ' + destination + '. you may eject the tray now')
