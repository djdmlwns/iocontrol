import os

class iocontrol():
    def __init__(self, inputfile, outputfile, originalvalue, changedvalue, **kwargs):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.keywords = kwargs
        self.originalvalue = originalvalue
        self.changedvalue = changedvalue

    def changeinput(self):
        with open(self.inputfile, 'rt') as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if self.originalvalue in line:
                    for key, val in self.keywords.items():
                        if val == 'yes':
                            if key in line:
                                lines[index] = line.replace(self.originalvalue, self.changedvalue) 
                                continue
    
                        else:
                            if key not in line:
                                lines[index] = line.replace(self.originalvalue, self.changedvalue) 
                                continue
                            
                    print('Original value', self.originalvalue, ' is changed to', self.changedvalue)
                    lines[index] = line.replace(self.originalvalue, self.changedvalue)

        with open(self.outputfile, 'wt') as f:
            for line in lines:
                f.write(line)
            


# line = line.strip() --> Remove all white spaces and new line symbol
    