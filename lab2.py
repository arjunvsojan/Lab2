import sys
def print_arguments():
    name = sys.argv[0]
    args = ' '.join(sys.argv[1:])
    print("Script name:", name)
    print("Script name and arguments:", script_name, arguments)
def helloWorld():
	print(‘Hello World’)

#function call
print_arguments()
helloWorld()
