from pyrosim.commonFunctions import Save_Whitespace

class JOINT: 

    def __init__(self,name,parent,child,type,position):

        self.name = name

        self.parent = parent

        self.child  = child

        self.type   = type

        self.position = position

        self.depth = 1

    def Save(self,f):

        Save_Whitespace(self.depth,f)
        f.write('<joint name="' + self.name + '" type="' + self.type + '">' + '\n')

        Save_Whitespace(self.depth,f)
        f.write('   <parent link="' + self.parent + '"/>' + '\n')

        Save_Whitespace(self.depth,f)
        f.write('   <child  link="' + self.child  + '"/>' + '\n')

        Save_Whitespace(self.depth,f)
        originString = str(self.position[0]) + " " + str(self.position[1]) + " " + str(self.position[2])
        f.write('   <origin rpy="0 0 0" xyz="' + originString + '" />\n')

        Save_Whitespace(self.depth,f)
        f.write('   <axis xyz="0 1 0"/>\n')

        Save_Whitespace(self.depth,f)
        f.write('   <limit effort="0.0" lower="-3.14159" upper="3.14159" velocity="0.0"/>\n')

        Save_Whitespace(self.depth,f)
        f.write('</joint>' + '\n')

