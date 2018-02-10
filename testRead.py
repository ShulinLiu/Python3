dicFile = open('dict.txt', 'r')#打开数据  
# print ('开始装载数据...')
txtDict = {}#建立字典  
while True:  
    line = dicFile.readline()  
    if line == '':  
        break  
    index = line.find('\t')#以tab键为分割 
    endindex = line.find('\n') 
    key = line[:index]  
    value = line[index+1:endindex]  
    txtDict[key] = value#加入字典  

print(txtDict)
dicFile.close() 

# ##查找字典  
# srcFile = open('train1.txt', 'r')#要匹配的key  
# destFile = open('match.txt', 'w')#符合字典的写入里面 
# badFile = open('notmatch.txt', 'w') 
# while True:  
#     line = srcFile.readline()  
#     if line == '':  
#         break  
#     index = line.find(' ')  
#     key = line[:index]  
#     if txtDict.get(key) != None:      
#         destFile.write(key)  
#         destFile.write(txtDict[key])         
#     else:  
#         badFile.write(key)  
#         badFile.write('\n')  
# print ('全部完成！')  
# destFile.close()  
# srcFile.close()
# badFile.close() 
