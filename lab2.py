import sys
def print_arguments():
    name = sys.argv[0]
    args = ' '.join(sys.argv[1:])
    print("Script name:", name)
    print("Script name and arguments:", script_name, arguments)
#function call
print_arguments()
def helloWorld():
	print("Hello World")

helloWorld()
