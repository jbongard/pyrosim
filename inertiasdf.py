from pyrosim.commonFunctions import Save_Whitespace


class INERTIA_SDF: 

    def __init__(self):

        self.depth = 4 

        self.string1 = '<inertia>'

        self.string2 = '    <ixx>0.083</ixx>'

        self.string3 = '    <ixy>0.0</ixy>'

        self.string4 = '    <ixz>0.0</ixz>'

        self.string5 = '    <iyy>0.083</iyy>'

        self.string6 = '    <iyz>0.0</iyz>'

        self.string7 = '    <izz>0.083</izz>'

        self.string8 = '</inertia>'


    def Save(self,f):

        Save_Whitespace(self.depth,f)
        f.write(self.string1 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string2 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string3 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string4 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string5 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string6 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string7 + '\n')

        Save_Whitespace(self.depth,f)
        f.write(self.string8 + '\n')

