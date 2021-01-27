class SDF:

    def __init__(self):

        self.depth = 0

    def Save_Start_Tag(self,f):

        f.write('<sdf>\n')

    def Save_End_Tag(self,f):

        f.write("</sdf>")
