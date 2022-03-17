import os
import platform

userDirectory = os.path.expanduser("~")
osType = platform.system()
InvAttFolderWin = "\\InventoryAttachments"
InvAttFolderOth = "/InventoryAttachments"

class DefinePath:
    #Method to set the true path to your machine's main directory C:\\Users\User in Windows
    #Returns the path unique to your machine's OS
    def setPath(self):
        if(osType=='Windows'):
            userDirectory = os.path.expanduser("~") + InvAttFolderWin
            isExist = os.path.exists(userDirectory)
            if(isExist):
                truepath = userDirectory
            else:
                os.makedirs(userDirectory)
                truepath = userDirectory
        else:
            userDirectory = os.path.expanduser("~") + InvAttFolderOth
            isExist = os.path.exists(userDirectory)
            if(isExist):
                truepath = userDirectory
            else:
                os.makedirs(userDirectory)
                truepath = userDirectory
        return truepath
    
    #Method to determine whether the user's machine is on Windows or not
    #Returns boolean true or false
    def guessWindows(self):
        if(osType=='Windows'):
            return True
        else:
            return False

