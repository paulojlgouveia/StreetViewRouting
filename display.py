
class Color:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	ITALIC = '\x1B[3m'
	
	END = '\033[0m'
	

def purple(string): return Color.PURPLE + string + Color.END
def blue(string): return Color.BLUE + string + Color.END
def cyan(string): return Color.CYAN + string + Color.END
def green(string): return Color.GREEN + string + Color.END
def red(string): return Color.RED + string + Color.END
def yellow(string): return Color.YELLOW + string + Color.END

def italic(string): return Color.ITALIC + string + Color.END
def underline(string): return Color.UNDERLINE + string + Color.END
def bold(string): return Color.BOLD + string + Color.END



def print_stack(stack, name = ""):
	
	if name is None:
		for n in stack:
			print(n)
		
	else:
		print(name)
		for n in stack:
			print("\t" + n)


def print_numbered_list(bag):	
	if isinstance(bag, dict):
		for k, v in sorted(bag.items()):
			print(" " + str(k).rjust(3) + "  " + v[1])
		
	elif isinstance(bag, list):
		for t in range(len(bag)):
			print(" " + str(t).rjust(3) + "  " + bag[t])


def get_unic_strs(bag):
	output = []
	seen = set()
	
	for thing in bag:
		if str(thing) not in seen:
			output.append(str(thing))
			seen.add(str(thing))
	
	return output


def print_file(filePath):
	
	try:
		print("\n" + filePath)
		with open(filePath, 'r') as fp:
			ln = 1
			for line in fp:
				print(" {}: {}".format(str(ln).rjust(2), line.strip('\n')))
				ln = ln + 1
			
	except IOError as e:
		print(e)


