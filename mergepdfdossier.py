import subprocess
import os
import shutil


def cmd_exists(cmd):
    """
    Function that verify if a command is usable in the current OS
    """
    return (shutil.which(cmd) is not None)

# FIRST: FINDING if it's a gs or gswin64 executable -----------------------------------------------
def find_gs_name(verbose = True):
    gs_command = ""
    if (cmd_exists("gswin64")):
        gs_command = "gswin64"
    elif cmd_exists("gs"):
        gs_command = "gs"
    else:
        print("No ghostscript executable found. (gs or gswin64). Please make sure to download ghostScript and include it in your PATH")
        exit(1)
    if verbose:
        print(gs_command)
    return gs_command

# CREATING THE COMMAND ----------------------------------------------------------------------------
def create_command(directory_path,  gs_command, ouput_file = "merged_document.pdf", verbose = True):
    """ Return the ghostScript command to merge the pdf in the folder 'directory_path'
		needed
	"""
    template = """ {0} -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile={1}"""
    doc_in_directory = os.listdir(directory_path)
    pdf_in_directory = [ "\"" + os.path.join(directory_path,doc)+"\"" for doc in doc_in_directory if len(doc)>4 and doc[-3:] == "pdf"]
    pdf_to_merge_sorted = sorted(pdf_in_directory)
    if verbose:
        print("*" *20, "\nPDF files found, that will be merged in the following order:")
        for file in pdf_to_merge_sorted:
            print(file)
    output_path = os.path.join(directory_path, ouput_file)
    command = template.format(gs_command, output_path) +" " + " ".join(pdf_to_merge_sorted)
    return command

# EXECUTING THE COMMAND ---------------------------------------------------------------------------
def execute_command(command, verbose = True):
    """Execute a command, return it's value: Print ouput if verbose is True"""
    if verbose:
        print("Executing the command:\n", command)

    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if verbose:
        print("OUTPUT:\n")
        if p.stdout is not None:
            for line in p.stdout.readlines():
                print(line)

    if p.stderr is not None:
        for line in p.stderr.readlines():
            print(line)

    retval = p.wait()
    return retval

if __name__ == '__main__':
    gs_command = find_gs_name()

    directory_path = input("enter here your directory containing pdf files")
    command = create_command(directory_path, gs_command)
    execute_command(command)