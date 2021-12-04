def f(n):
	shrln=[]
	while not n in shrln:
		shrln.append(n)
		if n%2==0:
			n=int(n/2)
		else:
			n=n*3+1
	return shrln
	
def max(array):
	mn=0
	n=0
	for n in array:
		if n>mn:
			mn=n
	return mn
	
def avg(array):
	div=0
	n=0
	for i in range(len(array)):
		n+=array[i]
		div+=1
	return n/div

def sum(array):
	n=0
	for cm in array:
		n+=cm
	return n

def act(sequence):
	return max(sequence)*(avg(sequence)+10)
	
def alp(hex=False):
	if hex:
		alp="0123456789abcdef"
	else:
		alp="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\"'()*+,-./:;<=>?@[\\]^_`{|}~ "
	alp=list(alp)
	return alp
def alp_indexer(arg, hex=False):
	alph=alp(hex)
	if type(arg)==str:
		for i in range(len(alph)):
			if alph[i]==arg:
				return i
		print(f"Unable to find symbol '{arg}'. replacing with 0")
		return 0
	elif type(arg)==int:
		try:
			return alph[arg]
		except:
			print(f"Failed index {arg} access")
			return ""
		
def str_to_ints(str):
	str=list(str)
	for i in range(len(str)):
		str[i]=alp_indexer(str[i])
	return str

def ints_to_str(seq, hex=False):
	str=""
	for val in seq:
		str+=alp_indexer(val, hex)
	return str

def normalize(index, hex=False):
	alph=alp(hex)
	while index>len(alph)-1:
		index=index-len(alph)-1
	return index
	
def normalize_seq(seq, hex=False):
	for i in range(len(seq)):
		seq[i]=normalize(seq[i], hex)	
	return seq
def hash(string, salt=None, iterations=1):
	add=""
	if type(salt)==str:
		add=salt
	elif type(salt)==int:
		pass
	elif type(salt)==type(None):
		print("Salt weren't specified! Continuing hashing...")
	else:
		print(f"Unknow salt type: '{str(type(salt))}' only int or str can be used")
	seq1=str_to_ints(string+add)
	n=sum(seq1)
	if n%2==0:
		n=int(n/2)
	else:
		n=n+int(avg(seq1))
	if type(salt)==int:
		if salt%2==0:
			add=salt
		else:
			add=salt*3
	else:
		add=0
	seq2=normalize_seq(f(n+add), hex=True)
	string=ints_to_str(seq2, hex=True)
	while iterations>1:
		iterations-=1
		string=hash(string, salt)
	return string
if __name__=="__main__":
	print(hash(input("Test MPH: "), input("Salt: "), int(input("Iterations: "))))
