import os
import platform

userDirectory = os.path.expanduser("~")
osType = platform.system()
InvAttFolderWin = "\\InventoryAttachment"
InvAttFolderOth = "/InventoryAttachment"

class DefinePath:
    def setPath(self):
        if(osType=='Windows'):
            userDirectory = os.path.expanduser("~") + InvAttFolderWin
            isExist = os.path.exists(userDirectory)
            print(isExist)
            if(isExist):
                truepath = userDirectory
            else:
                os.makedirs(userDirectory)
                truepath = userDirectory
        else:
            userDirectory = os.path.expanduser("~") + InvAttFolderOth
            isExist = os.path.exists(userDirectory)
            print(isExist)
            if(isExist):
                truepath = userDirectory
            else:
                os.makedirs(userDirectory)
                truepath = userDirectory
        return truepath

