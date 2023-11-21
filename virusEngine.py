"""
Decrypt file to hash md5(more hash collision), and check with viruses hashs. If similar then file has virus else not!
We use sha-256 hash to minimize hash collisions
"""
###* Extract hash of file
import hashlib
import os


###* Global Variables
    # Open databases of viruses
malware_hashes = list(open("DataBase\\virusHash.unibit", "r").read().split('\n')) 
    # We need to know what virus is it. So,
virusInfo = list(open('DataBase\\virusInfo.unibit', 'r').read().split('\n'))
    # Path of folder to be scanned
# path = "C:\\Users\\rdev4\\OneDrive\\Desktop\\Portfolio Projects\\Python\\antivirus\\uni-bit antivirus\\viruses_maybe"


###* Get file Hash SHA-256
def sha256_hash(filename):
    try:
        with open(filename, "rb") as f:
            bytes = f.read()
            sha256hash = hashlib.sha256(bytes).hexdigest()
            f.close()
        return sha256hash
    except:
        # There are some files which can't be read with user permission. So, we use try and except to control that error.
        return 0


###* Malware detection using Hash
def malware_identification_checker_one(pathOfFile):
    global malware_hashes
    global virusInfo

    hash_malware_check = sha256_hash(pathOfFile) # extract hash value of file to be checked
    counter = 0

    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1
    return 0
###### ###### print(malware_identification_checker_one(path))


###* Malware detection for folder scan (Deep Scanning)
virusNames = [] # Stores all vulnerable files name and paths (both)
virusPath = [] # Stores all vulnerable files paths
def folderScan(path):
    dir_list = list()
    for (dirpath, dirname, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]

    for i in dir_list:
        ###### ###### print(i)
        if malware_identification_checker_one(i) != 0:
            virusNames.append(malware_identification_checker_one(i)+ " :: File Path :: "+i)
            virusPath.append(i)
###### ###### folderScan()
###### ###### print(virusNames)


###* Virus Removal
def virusRemoval(path):
    folderScan(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0
###### ###### virusRemoval(path)


###* Remove Junk/Temp file (only currenlty used file can't be deleted)
def junkFileRemover():
    temp_list = list()

    # Windows username finder
    username = os.environ.get('USERNAME').upper().split(" ")

    for (temppath, tempname, filenames) in os.walk("C:\\windows\\Temp"):
        temp_list += [os.path.join(temppath, file) for file in filenames]
        temp_list += [os.path.join(temppath, file) for file in tempname]
    for (temppath, tempname, filenames) in os.walk("C:\\Users\\{}\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(temppath, file) for file in filenames]
        temp_list += [os.path.join(temppath, file) for file in tempname]
    for (temppath, tempname, filenames) in os.walk("C:\\windows\\Prefetch"):
        temp_list += [os.path.join(temppath, file) for file in filenames]
        temp_list += [os.path.join(temppath, file) for file in tempname]

    print(temp_list)

    if temp_list:
        for i in temp_list:
            print(i)
            try:
                os.remove(i)
            except:
                pass
            try:
                os.rmdir(i)
            except:
                pass
    else:
        return 0


###* Ram Cleaner
def ramBooster():
    taskList = ["notepad.exe", "chrome.exe", "msedge.exe"]

    for i in taskList:
        # Task killing 
        os.system(f'taskkill /f /im {i}')
