from os import walk
print("-------------------------------------------------")

with open("Root/lev2_Root_0/lev3_Root_00/file_0.in") as fd:
    data = fd.read()
    
# 1
myDict = {}
for dirpath, dirnames, filenames in walk('Root'):
    levels = dirpath.split('\\')
    if len(levels) == 3:
        key = (levels[0], levels[1])
        for filename in filenames:
            full_path = levels[0] + '/' + levels[1] + '/' + levels[2] + '/' + filename
            value = (levels[2], full_path)
            if  key in myDict:
                myDict[key].append(value)
            else:
                myDict[key] = [value]
        
# 2
mx = 0
for key in myDict:
    value = myDict[key]
    newvalue = {}
    for foldername, fullpath in value:
        filenamewithoutext = fullpath.split('/')[-1].split('.')[0]     
        with open(fullpath) as fr:
            arr = [x for x in fr.read().split() if len(x) == 9]
            mx = max(mx, len(arr))
        newvalue[(foldername, filenamewithoutext)] = arr
    myDict[key] = newvalue
    
# 3
for key in myDict:
    for key1 in myDict[key]:
        if len(myDict[key][key1]) == mx:
            print("key: ", key, " key1: ", key1, "#3 kvelaze meti 9 ert listshi: ", mx)

# 4
def fun(a) :
    s = str(a)
    arr = [s[i] for i in range(1, len(s), 2)]
    sortedArr = sorted(arr, reverse=True)
    return sortedArr == arr
    
# 5
maxx = 0
res = []
for key in myDict:
    for key1 in myDict[key]:
        co = 0
        for num in myDict[key][key1]:
            if(fun(num)):
                co += 1
        if(co > maxx):
            maxx = co
            res = [(key, key1)]
        elif co == maxx and co > 0:
            res.append((key, key1))
        

            