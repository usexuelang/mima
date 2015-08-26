def replace(line="",replaceOld="",replaceNews=[]):
	lines=[]
	for r in replaceNews:
		lines.append(line.replace(replaceOld,r))
	return lines
def replacelines(lines=[],replaceOlds=[],replaceNews=[]):
	newlines=[]
	for line in lines:
		newlines.append(replaceline(line,replaceOlds,replaceNews))
	return newlines
def replacelineM(line="",replaceOlds=[],replaceNews=[]):
	lines=[]
	if len(replaceOlds)!=len(replaceNews):
		return lines
	for i in range(0,len(replaceOlds)):
		lines=lines+replace(line,replaceOlds[i],replaceNews[i])
	return lines
def replaceline(line="",replaceOlds=[],replaceNews=[]):
	if len(replaceOlds)!=len(replaceNews):
		return line
	for i in range(0,len(replaceOlds)):
		line=line.replace(replaceOlds[i],replaceNews[i])
	return line
def replacefile(username_file="in.txt",output_file="out.txt",replaceOlds=[],replaceNews=[]):
	f=open(username_file,"r")
	o=open(output_file,"w")
	lines=replacelines(f.readlines(),replaceOlds,replaceNews)
	for line in lines:
		o.write(line)
	f.close()
	o.close()
	return lines
#print replacefile("username.txt","out.txt",["%username%"],["123"])
print replacelineM("%username%123",["%username%"],[["guang","jia"]])
