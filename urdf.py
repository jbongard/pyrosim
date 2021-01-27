class URDF:

    def __init__(self):

        self.depth = 0

    def Save_Start_Tag(self,f):

        f.write('<robot name = "robot">\n')

    def Save_End_Tag(self,f):

        f.write("</robot>")
