from pyrosim.commonFunctions import Save_Whitespace

class COLLISION_URDF: 

    def __init__(self,origin,geometry):

        self.origin = origin

        self.geometry = geometry
 
        self.depth = 2

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.origin.Save(f)

        self.geometry.Save(f)

        self.Save_End_Tag(f)

# ------------------ Private methods ------------------

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</collision>\n')

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<collision>\n')
