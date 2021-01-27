class ROBOT:

    def __init__(self):

        pass

    def Save_Start_Tag(self,f):

        f.write('<robot name="robot">\n')

    def Save_End_Tag(self,f):

        f.write("</robot>")
