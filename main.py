


macrodef = {}
arguments = {}

fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

lines = []

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""def scan(fin):
    global lines
    lines = fin.readlines()
    line_no = 0
    for line in lines:
        line_no += 1

        if "%macro" in line:
           
            stripex = line.split("%macro ", 1)[1].split("\n", 1)[0]    # remove "%expand " from line
            func = stripex.split(" ", 1)[0]

            
            
            
            while stripex[-1] == '\\':                                  # concatenate next line if multi-line macro
                stripex = stripex[:-1] + '\n' + lines[line_no].strip("\n")
                lines.remove(lines[line_no])
            
            

            if "(" in func:                                             # check if functional macro
                func_name = stripex.split("(", 1)[0]
                args[func_name] = func.split("(", 1)[1].split(")", 1)[0].split(',')
                macro[func_name] = stripex.split(" ", 1)[1]        
                #print(macro)
            else:
                macro[stripex.split(" ", 1)[0]] = stripex.split(" ", 1)[1]
 
"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def expand_macro(line):                                                 # expand macro if found
    for i in macrodef.keys():
        if i in line:
            if i in arguments:
                paralist = line.split(i + '(', 1)[1].split(')', 1)[0]	# get actual arguments
                para = paralist
                print(paralist)
                paralist = para.replace(' ', '').split(',')
                print(paralist)
                getmacro = macrodef[i]

                for k in range(len(paralist)):
                    getmacro = getmacro.replace(arguments[i][k], paralist[k])	# replace formal parameters with actual parameters

                line = line.replace(i + '(' + para + ')', ''.join(getmacro))

            else:
                line = line.replace(i, ''.join(macrodef[i]))

    return line

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def handle_macros():                                                    # handle various macros, strip comments
    global lines

    i = 0
    while i < len(lines):
        if "%macro" not in lines[i]:                                   # skip lines containing "%expand "
            if "//" in lines[i]:
                lines[i] = lines[i].split("//")[0] + '\n'

            if "%ex?" in lines[i]:                                      # handle conditional macros
                stripex = lines[i].split("%ex? ", 1)[1].split("\n", 1)[0]
                print(stripex) 
                if stripex in macrodef:                                    # check if macro is previously defined
                    while "%/ex?" not in lines[i]:
                        i += 1

                        if "%/ex?" not in lines[i]:
                            fout.write(expand_macro(lines[i]))
                    i += 1

                else:
                    while "%/ex?" not in lines[i]:
                        i += 1

                    i += 1

            fout.write(expand_macro(lines[i]))

        i += 1
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def scan(fin):
    global lines
    lines = fin.readlines()
    line_no = 0
    for line in lines:
        line_no += 1

        if "%macro" in line:
           
            stripex = line.split("%macro ", 1)[1].split("\n", 1)[0]    #remove "%macro " from line ;func stores the name of the macro for now with arguments or without till the next blank's encountered
            func = stripex.split(" ", 1)[0]    
            #print(func)
            
            
            
            while stripex[-1] == '\\':                                  # concatenate all the lines until stripex does not end with \ indicating multiline 
                stripex = stripex[:-1] + '\n' + lines[line_no].strip("\n")
                lines.remove(lines[line_no])
                print(stripex)
            

            if "(" in func:                                             # check if functional macro
                func_name = stripex.split("(", 1)[0]
                arguments[func_name] = func.split("(", 1)[1].split(")", 1)[0].split(',')
                macrodef[func_name] = stripex.split(" ", 1)[1]          #stripex contains the macro and definition 
                #print(macro)
            else:
                macrodef[stripex.split(" ", 1)[0]] = stripex.split(" ", 1)[1]     #name of macro will get assigned the definition 
                
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
scan(fin)
handle_macros()
