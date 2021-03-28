import os
import os.path


class Transfer:
    """
    @author:syd
    @time:2020/2/10
         @content: Convert the specified .ui file to a .py file
    """
    def __init__(self):
        # The path where the UI file is located
        self.Dir = './'
        # File storage list
        self.list = []

        self.listUIFile()

    def listUIFile(self):
        """
                 @content: List all UI files in the directory and store them in the list list
        """
        files = os.listdir(self.Dir)
        for filename in files:
            # print(dir + os.sep + f)
            # print(filename)
            if os.path.splitext(filename)[1] == '.ui':
                self.list.append(filename)

    @staticmethod
    def transPyFile(filename):
        """
                 @content: Change the file with the extension .ui to the file with the extension .py
        """
        return os.path.splitext(filename)[0] + '.py'

    def printUI(self):
        """
                 @content: Display the names and serial numbers of all .ui files in the directory
        """
        id = range(1, len(self.list) + 1, 1)
        zipped = zip(id, self.list)
        for id, uifile in zipped:
            print(str(id) + ': ' + uifile)

    def excuteAll(self):
        """
                 content: Convert all .ui files to .py files
        """
        try:
            for uifile in self.list:
                pyfile = self.transPyFile(uifile)
                cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=uifile)
                print(cmd)
                os.system(cmd)
            print("All files converted successfully")
        except Exception as ex:
            print("An error occurred during the conversion process, the reason for the error:" + str(ex))

    def excuteSingle(self, id):
        """
                 @content: Convert a single .ui file to a .py file
        """
        if id < 1 or id > len(self.list):
            print("Not found" + str(id) + "File Number")
            return -1
        try:
            uifile = self.list[id - 1]
            pyfile = self.transPyFile(uifile)
            cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile, uifile=uifile)
            print(cmd)
            os.system(cmd)
            return 1
        except Exception as ex:
            print(ex)

    def runMain(self):
        """
                 @content: Call system commands to convert UI files to python files
        """
        files = input("Please enter the serial number of the file to be converted:")
        files = files.strip()
        if files == "All" or files == "all":
            self.excuteAll()
        else:
            try:
                id = files.split(' ')
                flag = 1
                for i in id:
                    if self.excuteSingle(int(i)) == -1:
                        flag = -1
                if flag == 1:
                    print("Single file executed successfully")
            except Exception as ex:
                print("An error occurred while processing a single file, the reason for the error:" + str(ex))
    
    def consolidate(self):
        '''
            Moves all generated py files up one.
        '''
        for uifile in self.list:
            pyfile = self.transPyFile(uifile)
            cmd = 'mv {pyfile} ../generated_ui/dev_ui'.format(pyfile=pyfile)
            print(cmd)
            os.system(cmd)


if __name__ == "__main__":
    """
         @tips: If you want to convert all .ui to .py files, just enter "all";
                         If you want to convert some of the .ui files into .py files, enter the serial number before the corresponding file name in turn,
                         And every two serial numbers can be separated by a space. Example: 1 2 3 4
    """
    transfer = Transfer()
    transfer.printUI()
    transfer.runMain()
    transfer.consolidate()

