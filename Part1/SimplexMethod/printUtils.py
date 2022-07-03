# Helper function to display in latex format
from IPython.display import display, Math

def print_matrix_nicely(array):
    data = ''
    for line in array:        
        if len(line) == 1:
            data += ' %.3f &'%line + r' \\'
            continue
        for element in line:
            data += ' %.3f &'%element
        data += r' \\'
    display(Math('\\begin{bmatrix} \n%s\end{bmatrix}'%data))

# get latex text
def getLatex(array):
    data = ''
    for line in array:        
        if len(line) == 1:
            data += ' %.3f &'%line + r' \\'
            continue
        for element in line:
            data += ' %.3f &'%element
        data += r' \\'
    return data