from pyrosim.commonFunctions import Save_Whitespace

class MASS_URDF: 

    def __init__(self):

        self.string =  '<mass value="1" />'

        self.depth = 3

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write(self.string + '\n' )
