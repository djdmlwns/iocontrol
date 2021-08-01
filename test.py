import os
from ioclass import iocontrol

ioclass = iocontrol('MyFirstScript.tcl', 'MyFirstScript2.tcl', 'set val 22', 'set val 40')
ioclass.changeinput()

os.system('wish MyFirstScript.tcl')
                    
        


# line = line.strip() --> Remove all white spaces and new line symbol
    