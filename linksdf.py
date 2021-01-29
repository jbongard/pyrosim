from pyrosim.inertialsdf     import INERTIAL_SDF

from pyrosim.geometrysdf     import GEOMETRY_SDF

from pyrosim.collisionsdf    import COLLISION_SDF

from pyrosim.visualsdf       import VISUAL_SDF

from pyrosim.commonFunctions import Save_Whitespace

class LINK_SDF:

    def __init__(self,name,pos,size):

        self.name = name

        self.depth = 2

        self.inertial  = INERTIAL_SDF()

        self.geometry = GEOMETRY_SDF(size)

        self.collision = COLLISION_SDF(self.geometry)

        self.visual    = VISUAL_SDF(self.geometry)

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.inertial.Save(f)

        self.collision.Save(f)

        self.visual.Save(f)

        self.Save_End_Tag(f)

# ------------------- Private methods -----------------

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</link>\n')

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<link name="' + self.name + '">\n')
