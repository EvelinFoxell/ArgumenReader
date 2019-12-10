import sys, getopt

class ArgumentReader:
	acceptedArgs = ['help', 'debug']
	optionsList = [("-h", "--help"), ("-d", "--debug")]
	debug = False

	def __init__(self, args):
		self.validateArgs(args)
		self.runInDebug(args)
		self.setUpAcceptedArgs(args)
		self.acceptedArgs = self.acceptedArgs + args
		self.debug("args:")
		self.debug(self.acceptedArgs)

	def runInDebug(self, submittedArgs):
		debug = True

	def debug(self, stringMsg):
		if self.debug:
			print(stringMsg)

	def setUpAcceptedArgs(self, args):
		fullArgsList = []
		for arg in args:
			fullArgsList.append(("-" + arg[0], "--" + arg[:-1]))
		self.debug("Full Args: ")
		self.debug(fullArgsList)
		self.optionsList = self.optionsList + fullArgsList

	def getShortArgs(self):
		arglist = ""
		args = self.acceptedArgs
		for index, arg in enumerate(args):
			argument = arg[0]
			if arg[-1:] == '=':
				argument = argument + ":"
			arglist = arglist + argument
		self.debug("arglist: " + arglist)
		return arglist

	def getArgs(self):
		opts = []
		shortArgs = self.getShortArgs()
		arginp = sys.argv[1:]
		print("Argument input: ", arginp)
		try:
			opts, args = getopt.getopt(arginp, shortArgs, self.acceptedArgs)
			print("Options", opts)
			print("First Option: " + opts[0][0])
			self.printHelp()
		except getopt.GetoptError as getErr:
			self.printUnknownCommand(getErr)
		except Exception as e:
			print("Something went wrong! please try again! Or type -h or --help to see list of commands")
			print(e)
		
		return opts

	def printHelp(self):
		helpMessage = \
		" ___ ____ ____ _  _ _   _ ___ __  _ _____ \n" + \
		"|   |    |  __| || |  V  | __|  \\| |_   _| \n" + \
		"| ' | ' _| |  | || |  _  | __|     | | | \n" + \
		"|_|_|_|\\_\\____'____'_| |_|___|_|\\__| |_| \n" + \
		"                         ____ ___ ___ __  ___ ____ \n" + \
		"                        |    | __|   |  '. __|    | \n" + \
		"                        | ' _| __| ' | | | __| '  | \n" + \
		"                        |_|\\_\\___|_|_|__.'___|_|\\_\\ \n" + \
		"=====================================================\n\n" + \
		"You have the following options in using this script:\n" + \
		"--------------------------------------------------------\n" + \
		"shorthand      long argument        description \n" + \
		"-------------------------------------------------------- \n"
		for argset in self.optionsList:
			option = \
			argset[0] + "             " + argset[1] + "\n"
			helpMessage = helpMessage + option

		print(helpMessage)
		sys.exit(0)

	def printUnknownCommand(self, getoptError):
		print(str(getoptError) + ". Please try again! Or type -h or --help to see list of commands")
		sys.exit(0)

	def validateArgs(self, submittedArgs):
		for arg in submittedArgs:
			for option in self.optionsList:
				if option[0][1] == arg[0]:
					print("There is already an argument starting with " + option[0][1] + "!\n"\
						"Please refer to ArgumentReader's documentation on how to implement the module!")
					sys.exit(0)
		print('Arguments supplied are valid!')
		