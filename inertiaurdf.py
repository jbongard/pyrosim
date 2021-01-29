from pyrosim.commonFunctions import Save_Whitespace


class INERTIA_URDF: 

    def __init__(self):

        self.depth = 3 

        self.string1 = '<inertia ixx="100" ixy="0" ixz="0" iyy="100" iyz="0" izz="100" />'

    def Save(self,f):

        Save_Whitespace(self.depth,f)
        f.write(self.string1 + '\n')
