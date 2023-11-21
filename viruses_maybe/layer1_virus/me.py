deff = list(open('VirusDataBaseHash.bav', 'r').read().split('\n'))

for i in deff:
    xyz = open('virusHash.txt', 'a').writelines(i[0:64]+"\n")
    abc = open('virusInfo.txt', 'a').writelines(i[65:len(i)]+"\n")