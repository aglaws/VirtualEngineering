from shutil import copyfile

def write_file_with_replacements(filename, replacements):

    # Provide the name of an unchanging backup file to read options from
    backup_filename = 'bkup_%s' % (filename)

    try:
        # If it already exists (i.e., we've run this code before) simply 
        # read its contents
        f_read = open(backup_filename, 'r')

    except:
        # If it doesn't exist (i.e., the code is being run for the first time)
        # copy the contents of the original file into a new backup
        # and read the contents from the new backup 
        copyfile(filename, backup_filename)
        f_read = open(backup_filename, 'r')

    # Create a separate pointer for reading and writing
    f_write = open(filename, 'w')

    for line in f_read:

        new_value = None

        # Find the definition of the variable we want to change
        for key, value in replacements.items():
            if key in line:
                new_value = value
                del replacements[key]
                break;

        if new_value is not None:
            # Split on whichever separator/assignment operator is found, and 
            # preserve the left-hand side variable name while adding the
            # new value on the right-hand side
            if '=' in line:
                lhs = line.split('=')[0]
                new_line = '%s= %s' % (lhs, str(new_value))

            elif ':' in line:
                lhs = line.split(':')[0]
                new_line = '%s: %s' % (lhs, str(new_value))

            else:
                lhs = line.split()[0]
                new_line = '%s %s' % (lhs, str(new_value))

            # If the original line terminated with a semicolon, add one
            # to the new line as well
            if ';' in line:
                new_line = '%s;\n' % (new_line)
            else:
                new_line = '%s\n' % (new_line)

            # Replace the current line with the modified line
            line = new_line

        # Write the (possibly modified) line into the new file    
        f_write.write(line)

    # Close both files when finished
    f_read.close()
    f_write.close()
