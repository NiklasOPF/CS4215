from sympy import * 

def evaluate(l):
	ss=simplify(l)
	return ss 

def partial_evaluate(s):
	final=""
	x=""
	for el in s:
		if(el!=';'):
			if(el=='\n' or el==' '):
				if(x[-1]!='\n' and x[-1]!=' '):
					x+=' '
			


			else:
				x+=el
		else:
			x+=";\n"
	for line in x.splitlines():

		final+=str(evaluate(line[:-1]))
		final+=';\n'
	print(final)



