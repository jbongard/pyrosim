from pyrosim.masssdf         import MASS_SDF

from pyrosim.inertiasdf      import INERTIA_SDF

from pyrosim.commonFunctions import Save_Whitespace

class INERTIAL_SDF:

    def __init__(self):

        self.depth = 3

        self.mass = MASS_SDF()

        self.inertia = INERTIA_SDF()

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.Save_Elements(f)

        self.Save_End_Tag(f)

# --------------------------- Private ------------------

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<inertial>\n')

    def Save_Elements(self,f):

        self.mass.Save(f)

        self.inertia.Save(f)

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</inertial>\n')
