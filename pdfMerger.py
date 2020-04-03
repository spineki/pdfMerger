import subprocess
import os
import sys
import shutil
import argparse


def cmd_exists(cmd):
    """
    Function that verify if a command is usable in the current OS
    """
    return (shutil.which(cmd) is not None)

def verify_directory_name():
    verif = True
    while (verif):
        directory_name = input("Enter a valid absolute directory path containing the pdf files: ")
        if os.path.isdir(directory_name):
            return directory_name
        else:
            print("This path is not a directory, Please ", end = " ")

def verify_output_name():
    default = "merged_document.pdf"
    print("\n\n " + "*" * 20)
    output_name = input("Enter the name of the output file, default name is " + default + ". Just press enter to keep it")
    if len(output_name) <= 4: # no even .pdf
        return default
    elif output_name[-3:] != "pdf": # need pdf extension
        return output_name + ".pdf"
    else:
        return output_name


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
        print(gs_command, " for GhostSript command found")
    return gs_command

def get_pdf_files_from_folder(directory_path, verbose=True):
    doc_in_directory = os.listdir(directory_path)
    pdf_in_directory = [ "\"" + os.path.join(directory_path,doc)+"\"" for doc in doc_in_directory if len(doc)>4 and doc[-3:] == "pdf"]
    pdf_to_merge_sorted = sorted(pdf_in_directory)
    if verbose:
        print("*" *20, "\nPDF files found, that will be merged in the following order:")
        i = 1
        for file in pdf_to_merge_sorted:
            print(i, "-> ", file)
            i+=1
    return pdf_to_merge_sorted

# CREATING THE COMMAND ----------------------------------------------------------------------------
def create_command(list_files,  gs_command, output_path, verbose = True):
    """ Return the ghostScript command to merge the pdf in the folder 'directory_path'
		needed
	"""
    template = """ {0} -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile={1}"""
    pdf_to_merge_sorted = list_files
    # output_path = os.path.join(directory_path, ouput_file)
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

    if len(sys.argv) == 1: # if some options are parsed, regular simplified mode for non cli users: only folder mode working to avoid the user to have to choose
        gs_command = find_gs_name(True)
        directory = verify_directory_name()
        list_files = get_pdf_files_from_folder(directory, verbose=True)
        ouput_name = verify_output_name()
        ouput_path = os.path.join(directory, ouput_name)
        print(ouput_path)
        command = create_command(list_files,gs_command, ouput_path, verbose = True)
        execute_command(command, verbose=True)

    else:
        parser = argparse.ArgumentParser(description='Process pdf files')
        
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument( "-d", "--directory", type=str,   help="Set the path of the directory where are the pdf files to process", default=None)
        group.add_argument( "-f", "--file",      nargs="+",  help="Specify list of files to merge. The order of the name is the order of the merge", default=None)
        
        parser.add_argument('-o', "--output",    type=str,   help='Output name of the file with .pdf name', default="merged_document.pdf")
        parser.add_argument("-v", "--verbose",   type=bool,  help="set the level of verbosity: True-> verbose, False-> quiet", default = False)

        args = parser.parse_args()
        
        gs_command = find_gs_name(verbose=args.verbose)

        list_files= []
        output_name  = ""
        if args.file is not None:
            list_files = args.file
            output_name = args.ouput
        else:
            list_files = get_pdf_files_from_folder(args.directory, verbose=args.verbose)
            output_name = os.path.join(args.directory, args.output)

        command = create_command(list_files, gs_command, output_path=output_name, verbose=args.verbose)
        execute_command(command, verbose=args.verbose)
    
    input("\n\nPress enter to finish!")