f = open("array.asm","r")
def searchlabel(arr,label):
	for i in arr:
		if i[0]==label:
			i[6]='D'
			return 0
	return 1
t =[]
size =0
for line in f:
	if ".bss" in line:
		break
	if "\"" in line:	
		m = line.strip().split("\"")
		
		t.append([(str(m[0]).split(" "))[0]]+[m[1]]+[1]+[len(m[1])]+[1*len(m[1])]+['S']+['D']+[size])
		size +=1*len(m[1])
		
	elif "dd" in line:
		m = line.strip().split(" ")
		vlen = len(str(m[2]).split(","))
		t.append([m[0]]+[m[2]]+[4]+[vlen]+[vlen*4]+['S']+['D']+[size])
		size+=4*vlen

lineno =0
tt=[]
for line in f:
	lineno+=1
	if ":" in line:
		m=(line.split(":"))[0]
		if searchlabel(tt,m):
			tt.append([m]+['-']+['-']+['-']+['-']+['L']+['U']+[lineno])
	elif "jnz" in line or "jmp" in line or "jz" in line:
		m=(line.strip().split(" "))[1]
		if searchlabel(tt,m):
			tt.append([m]+['-']+['-']+['-']+['-']+['L']+['U']+['-'])
print(t)
print(tt)
