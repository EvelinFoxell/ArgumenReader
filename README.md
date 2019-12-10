# Argument Reader

This  is a small nifty little module that helps you automate a small UI for your python script.

### Supported Version

This script supports Python 3.

## Implementation

Add the script file to the same folder as your script. 

```
root
   |_your_script.py
   |_argumentReader.py
```

Import the reader in your script:

```
from argumentReader import ArgumentReader
```

Make an array of your desired argument's long option. Add a `=` to indicate if the argument accepts a value or not.

```
accepted_args = ['url=', 'file=', 'short']
```

Create an instance of your ArgumentReader with the desired arguments as an argument.

```
argumentReader = ArgumentReader(accepted_args)
```

To get the submitted arguments call for `getArgs()`

```
args = argumentReader.getArgs()
```

Done!

## Usage

The script has two flags built in to it; help and debug.

The `help` command can be triggered by inputting the `-h` alternatively `--help` flag into a script that implements the module.

```
python3 your_script.py -h
```

This outputs the menu of the different options the user can interact with.

The `debug` command debugs the script itself.


## Development

You can debug the script by adding `self.debug(str)` to a place inside the object and sending a `-d` flag into the script implementing it.