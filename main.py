# Import Libraries
import virusEngine

# Path of folder to be checked
path = "C:\\Users\\rdev4\\OneDrive\\Desktop\\Portfolio Projects\\Python\\antivirus\\uni-bit antivirus\\viruses_maybe"

### Get all files path and viruses names if file is vulnerable on followed path
virusEngine.folderScan(path)
print(virusEngine.virusNames)

### remove all vulnerable files on followed path
# virusEngine.virusRemoval(path)

### Remove mostly files from temp, %temp%, Prefetch
# virusEngine.junkFileRemover()

### For cleaning all ram, just like through task bar
# virusEngine.ramBooster()






"""
Things can be done by now:
1. Virus and malware detection
2. Multi-files scanning
3. Junk file detection and removal
4. Ram Health manager
5. System activity manager
"""