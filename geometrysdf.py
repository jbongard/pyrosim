from pyrosim.commonFunctions import Save_Whitespace

class GEOMETRY_SDF: 

    def __init__(self,type,size):

        self.depth   = 4

        self.string1 = '<geometry>'

        if type == 'cube':

            sizeString = str(size[0]) + " " + str(size[1]) + " " + str(size[2])

        elif type == 'sphere':

            radiusString = str(size)

        if type == 'cube':

            self.string2 = '   <box>'

            self.string3 = '      <size>' + sizeString + '</size>'

            self.string4 = '   </box>'

        elif type == 'sphere':

            self.string2 = '   <sphere>'

            self.string3 = '      <radius>' + radiusString + '</radius>'

            self.string4 = '   </sphere>'

        self.string5 = '</geometry>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string4 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string5 + '\n' )
