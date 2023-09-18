
def print_hello(num: int):
	
	for i in range(num):
		if num%2==0:
			print(f'{i}번쨰 안녕')

if __name__=='__main__':
	print_hello(10)
