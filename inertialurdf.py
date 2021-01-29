from pyrosim.massurdf    import MASS_URDF

from pyrosim.inertiaurdf import INERTIA_URDF

from pyrosim.commonFunctions import Save_Whitespace

class INERTIAL_URDF:

    def __init__(self,origin):

        self.depth = 2

        self.origin = origin

        self.mass = MASS_URDF()

        self.inertia = INERTIA_URDF()

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.Save_Elements(f)

        self.Save_End_Tag(f)

# --------------------------- Private ------------------

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<inertial>\n')

    def Save_Elements(self,f):

        self.origin.Save(f)

        self.mass.Save(f)

        self.inertia.Save(f)

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</inertial>\n')
