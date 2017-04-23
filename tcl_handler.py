def flatten_tcl(tclfiles):
    ''' This function takes a tcl file and rewrites it to a temporary file.
    The new temporary file will be flattened, meaning all expressions are
    replaced with their evaluated value (as a float)
    '''
    import os

    variables = {} # a disctionary of variables set in the tcl file
    tempfiles = [] # a list of the temporary files created
    ns = {'__builtins__':None} # create empty namespace to use eval() safely

    for tclfile in tclfiles:
        tempfiles.append(tclfile[:-4]+'_temp.tcl')


        with open(tclfile) as f_in, open(tempfiles[-1], 'w') as f_out:
            for line in f_in:
                # For lines that define variable, add that variable to dictionary
                if line[:3] == 'set':
                    # If the line has 3 words, the variable is set directly and we
                    #  can add it to our dictionary of variable values
                    if len(line.split()) == 3:
                        variables['$'+line.split()[1]] = float(line.split()[2])
                        f_out.write(line)
                    # If the thrid word is an expression, evaluate before write
                    elif '[expr' in line.split()[2]:
                        expr = line[line.find('[expr ')+6:line.find(']')]
                        for variable in variables:
                            if variable in expr:
                                # If variables in expr, replace with value
                                expr = expr.replace(variable,
                                                    str(variables[variable]))
                        # Replace expression with evaluated value of expression
                        expr = eval(expr, ns)
                        variables['$'+line.split()[1]] = float(expr)
                        f_out.write(' '.join(('set', line.split()[1], str(expr))))
                # For lines that don't define variable, eval expressions and print
                else:
                    for variable in variables:
                        line = line.replace(variable, str(variables[variable]))
                    if '[expr' in line: # evaluate any expressions, then print
                        expr = line[line.find('[expr ')+6:line.find(']')]
                        line = line.replace('[expr '+expr+']', str(eval(expr, ns)))
                    f_out.write(line)

    # Combine all _temp tcl files into one messy one
    with open('temp.tcl', 'w') as f:
        for tempfile in tempfiles:
            with open(tempfile, 'r') as temp:
                for line in temp:
                    f.write(line)
            os.remove(tempfile)

    return 'temp.tcl'
