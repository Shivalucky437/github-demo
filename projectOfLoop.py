#run program,for better understanding of working

class choice:
	a=1
	def prg1(self):
		for i in range(10):
			print('{}) Bright It Career'.format(i+1))
		return ''
		
	def prg2(self):
		print('printing nums from 1 to 20 are: ')
		n=1
		while n<=20:
			print(n,end=" ")
			n+=1
		return ''
		
	def prg3(self):
		print('even and odd nums btw 1 to 20 are: ')
		n=20
		print('Even num : ',end=' ')
		for i in range(2,n+1,2):
			print(i,end=' ')
		print()
		print(' odd num : ',end=' ')
		for i in range(1,n,2):
			print(i,end=' ')
		return ''
	def prg4(self):
		print('welcome to largest of among 3 nums prgm: ')
		n1,n2,n3=list(map(int,input('enter 3 nums in a b c format ').split()))
		lrgnum=0
		for i in list((n1,n2,n3)):
			if i>lrgnum:
				lrgnum=i
				
		return 'largest among {} , {} and {} is :'.format(n1,n2,n3)+str(lrgnum)
		
	def prg5(self):
		print('welcome to even nums btw a and b program ')
		n,m=list(map(int,input('enter nums in a b format ').split()))
		print('even nums btw {} and {} :'.format(n,m),end=" ")
		while n<=m:
			print(n,end=" ")
			n+=2
		return ''
			
		
	def prg6(self):
		print('welcome to printing 1 to n nums prgm')
		print()
		maxval=int(input('enter a num: '))
		def do(n):
			n+=1
			return n
		n=0
		print('nums are :',end=' ')
		while n<=maxval:
			print(do(n),end=" ")
			n+=1
		return ''

		
	def prg7(self):
		print('welcome to armstrong num check prgm ')
		n=input('enter a num : ')
		sum=0
		for i in n:
			sum+=pow(int(i),3)
		if sum==n:
				print(n+' is a armstrong num')
		else:
				print(n+' is not a armstrong num')
		return '' 
		

	def prg8(self):
		print('welcome to palindrome num check prgm ')
		a=input('enter a num ')
		s=''
		for i in range(-1,-len(a)-1,-1):
			s+=a[i]
		if s==a:
			print(str(a)+' is a palindrome')
		else:
			print(str(a)+' is not a palindrome')
			
		return ''
		
		
		
	def prg9(self):
		print('welcome to prime num check prgm ')
		n=int(input('enter a num '))
		if n==2:
			return '2 is a prime'
		for i in range(1,n):
			if i**2>=n:
				num=i
		for j in range(2,num+1):
			if n%j==0:
				print(str(n)+' is not a prime')
				break
		else:
				print(str(n)+' is a prime')
		return ''
		
		
		
	def prg10(self):
		print('welcome to odd or even num check prgm ')
		val=int(input('enter a value '))
		switcher={
		 1:'ODD NUM', 0:'EVEN NUM'}
		print('{} : '.format(val),end="")
		print(switcher.get(val%2,'default'))
		return ''
		
		
		
	def prg11(self):
		print('welcome to gender check prgm')
		gendercheck={ 'M':'male','F':'female'}
		print(gendercheck.get(input('enter first char of ur gender ').upper(),'transgender'))
		return ''
	


print('              welcome to loop Assignment!!')
print()
print('enter 1 for printing Bright It Career as 10 tyms ')
print()
print('enter 2 for printing 1 to 20 nums using while')
print()
print('enter 3 for even and odd nums')
print()
print('enter 4 for largest among 3 nums')
print()
print('enter 5 for even nums btw 10 to 20')
print()
print('enter 6 for 1 to 10 using do while statement')
print()
print('enter 7 for Armstrong num check')
print()
print('enter 8 for Palindrome num check')
print()
print('enter 9 for prime num check ')
print()
print('enter 10 for even or Odd num check')
print()
print('enter 11 for gender check ')
print()

m=11
for i in range(m):
	n=int(input('enter a value '))
	print()
	obj=choice()
	if n==1:
		print(obj.prg1())
	elif n==2:
		print(obj.prg2())
	elif n==3:
		print(obj.prg3())
	elif n==4:
		print(obj.prg4())
	elif n==5:
		print(obj.prg5())
	elif n==6:
		print(obj.prg6())
	elif n==7:
		print(obj.prg7())
	elif n==8:
		print(obj.prg8())
	elif n==9:
		print(obj.prg9())
	elif n==10:
		print(obj.prg10())
	elif n==11:
		print(obj.prg11())
	else:
		print('entered wrng num so prgm terminated')
		break
	print()

	

