# Multipurpose-Macro-Preprocessor

Multipurpose Macro Pre-processor implemented in Systems Programming Lab
The implemented macro preprocessor is a one-pass macro preprocessor which 
supports single-line and multi-line macros, nested macros, comments and
conditional macros.

Keywords used:
%expand : Used to create macro definitions.

%ex?	: Used to implement conditional macros, where all the statements
%/ex?	: declared within the body are written to the output file only if the 
	  macro passed as argument is defined previously.

Files used:
Macro.py   : Python program that implements the macro preprocessor.
code.txt   : Code containing macro definitions and invocations; taken as input 
	     file to the program.
excode.txt : Code containing expanded macros; taken as output file to the
	     program.

Run:
In the terminal, enter the command "python2 Macro.py". The input file should
be present in the same directory.

Implementation:
The program contains global definitions 'macro', 'args', 'fin', 'fout' and 
'lines':
- 'macro' is a dictionary containing the macro names as the key and its 
  definition as the value.
- 'args' is a dictionary containing the macro names as the key and its formal
  arguments as the value. This list is only populated if the preprocessor
  identifies the macro as a functional macro.
- 'fin' is a file pointer containing the input file.
- 'fout' is a file pointer containing the output file.
- 'lines' is a list which contains the code from the input file separated by
  each line

The program runs by calling the procedure scan(fin) and handle_macros().

The procedure scan(fin) scans the input file for macro definitions and
populates the 'macro' dictionary and 'args' dictionary accordingly.

The procedure handle_macros() strips all the macro definitions and the comments
from the input file. All macro invocations are expanded using the helper
procedure expand_macro(line). The procedure expand_macro(line) takes the
current line of the input file (which is passed by handle_macros()) and checks
the line for any macro invocations. All macro invocations are then expanded in 
the current line and is returned back to the caller function. The procedure 
handle_macros() writes this modified line to the output file, and this process
is repeated till the last line of the input file is encountered.
