# encoding: utf-8
def load_dict_from_file(filepath):
	_dict = {}
	try:
		with open(filepath, 'r') as dict_file:
			for line in dict_file:
				(key, value) = line.strip().split('\t')
				_dict[int(key)] = value
	except IOError as ioerr:
		print ("文件 %s 不存在" % (filepath))

	return _dict

def save_dict_to_file(_dict, filepath):
	try:
		with open(filepath, 'w') as dict_file:
			for (key,value) in _dict.items():
				dict_file.write('%s\t%s\n' % (key, value))
	except IOError as ioerr:
		print ("文件 %s 无法创建" % (filepath))

NameDict = load_dict_from_file ('namedict.txt')
PosDict = load_dict_from_file ('posdict.txt')
print(PosDict)

def getStreetName(streetid):
    return NameDict.get(streetid)

def getStreetPosition(streetid):
    return PosDict.get(streetid)

print(getStreetName(21))

#print(getStreetPosition(21)[0])
 
# if __name__ == '__main__' :
# 	_dict = load_dict_from_file ('dict.txt')
# 	print (_dict)
# 	#save_dict_to_file(_dict, 'dict_copy.txt')
# 	f2=open("output.txt",'w')
# 	with open ('input.txt','r') as f1:
# 		for line in f1:
# 			str1=line.split()
# 			for i in range(1,len(str1)):
# 				if str1[i].isupper():
# 					str1[i]='/ '+str(_dict.get(str1[i]))+' /'
# 					print (str1[i])
# 			f2.write(' '.join(str1)+'\n')
# 	# f2=open("output.txt",'w')
# 	# with open ('all_py.txt','r') as f1:
# 		# for line in f1:
# 			# str1=line.split()
# 			# for i in range(1,len(str1)):
# 				# str1[i]=str(_dict.get(str1[i]))
# 				#print str1[i]
# 			# f2.write(' '.join(str1)+'\n')