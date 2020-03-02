# 01000011010101000000000000000000
def list2string(s):  
    str1 = ""    
    return (str1.join(s)) 

def binary2dec(n):
	temp = list2string(n)
	res = int(temp, 2)
	return res

def IEEE754b2d(n):
	b_num = list(input("Input a binary number: \n"))[:n]
	# if n < len(b_num) or n > len(b_num):
	# 	break
	b_dup = b_num

	sign = pow(-1, int(list2string(b_dup[:1])))
	print(f"\nsign value {sign}")

	exp = b_dup[1:9]
	print(f"\nexp value {exp}\n") 

	exp_dec = binary2dec(exp)
	print(f"dec of exponent bin: {exp_dec}")

	dummy_exp = exp_dec - 127
	print(f"dec of dummy exponent: {dummy_exp}")

	mantisa = b_dup[9:32]
	print(f"\nmantisa {mantisa}")

	index = [i for i in range(1,24)] 
 
	idx=[]
	for i in range(len(index)):
		v = index[i] * (-1) 
		idx.append(v)

	t = []
	for i in range(len(mantisa)):
		v = int(list2string(mantisa[i])) * pow(2, idx[i])
		t.append(v)

	# print(f"\nmantisa list {t}")
	mantisa_dec = sum(t)
	print(f"\nSum of mantisa {mantisa_dec}")
	add_mantisa_dec = 1 + mantisa_dec
	print(f"\nNormalizing satate of man {add_mantisa_dec}")

	final = sign * add_mantisa_dec * pow(2, dummy_exp)
	# print(f"IEEE754 binary2dec: {final}")
	return final


n = int(input("Enter the size of list : "))

print(f"IEEE754 binary2dec: {IEEE754b2d(n)}")















