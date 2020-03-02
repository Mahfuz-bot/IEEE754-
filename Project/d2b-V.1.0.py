def float_bin(number): 
	whole, dec = str(number).split(".")  
	whole = int(whole)  
	ndec = '.' + dec
	fraction = float(ndec)
	res = bin(whole).lstrip("0b") + "."
	lres = list(res)
	f_bin = []
	f_float = []
	t_bin = []
	
	#itr = len([int(ele) for ele in str(fraction) if ele.isdigit()]) -1
	count = 0
	for x in range(40):
	#while True:
		new_wholeFraction = (fraction * 2)
		nWhole, dFrac = str(new_wholeFraction).split(".")
		f_bin.append(nWhole)
		nFrac = '.' + dFrac
		fraction = float(nFrac)
		f_float.append(fraction)
	# 	if fraction in f_float:
	# 		count += 1
	#print(count)
	#print(f_float)
	#print(f"fraction: {f_bin}")
	t_bin = lres + f_bin
	# print(f"Total: {t_bin}")
	return t_bin

def listToString(s):  
    str1 = " "    
    return (str1.join(s)) 
    
def IEEE754(n):
	sign = 0
	if n < 0:
		sign = 1
		n = n * (-1)
	print("sign bit ",sign)
	orgDec = float_bin (n)
	dec = orgDec.copy()
	# print(f"old decimal {dec}")
	ct = dec.index(".")
	remove = dec.pop(ct)
	cdv = dec.index("1")
	cdvl = cdv+1
	# print(f"ct {ct}")
	# print(f"cdv {cdv}")
	# print(f"cdvl {cdvl}")
	# print(f"now new decimal aftr remv {dec}")
	newDec = dec.insert(cdvl, ".")
	print(f"new decimal added {newDec}")
	print(f"updqte decimal {dec}")
	dummyExp = ct - cdvl
	exponent = 127 + dummyExp
	# print(f"exp frst e koto {exponent}")
	expSbin = bin(exponent).lstrip("0b")
	exp_bin = list(expSbin)
	
	i = 0
	while exp_bin:
		if len(exp_bin) == 8:
			break
		else:
			exp_bin.insert(i, "0")
			i += 1

	exp_bit = exp_bin[0:9]
	exp_bit2S = listToString(exp_bit)
	idFrac = dec.index(".")
	# print(f"what is idFrac {idFrac}")
	afracPart = dec[idFrac+1:]
	lngth = len(afracPart)
	print(f"What is frac her means full: {afracPart}")
	fracPart = [] + afracPart[:23]
	print(f"What is frac her means: {fracPart}")

	fracPart2S = listToString(fracPart)

	print("Exponent_bin_bit: ")
	print(" ".join(exp_bit))
	print(f"Exponent_bin_length: {len(exp_bit)}")
	print("Fractional_part_bin_bit: ")
	print(fracPart2S)
	print(f"Fractional_part_length: {len(fracPart)}")
	# print("Final form of IEEE754: ")
	final = str(sign) + " " + exp_bit2S +  " " + fracPart2S 
	print(f"Final form of IEEE754 \n{final}")
	print(f"final length: {len(final)-31}")
	# return final

# if __name__ == "__main__":
# 	print(IEEE754(5.025))

n = float(input("Enter decimal value: "))
IEEE754(n)