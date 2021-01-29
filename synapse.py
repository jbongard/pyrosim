import math

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class SYNAPSE: 

    def __init__(self,line):

        self.Determine_Source_Neuron_Name(line)

        self.Determine_Target_Neuron_Name(line)

        self.Determine_Weight(line)

    def Get_Source_Neuron_Name(self):

        return self.sourceNeuronName

    def Get_Target_Neuron_Name(self):

        return self.targetNeuronName

    def Get_Weight(self):

        return self.weight

# -------------------------- Private methods -------------------------

    def Determine_Source_Neuron_Name(self,line):

        if "sourceNeuronName" in line:

            splitLine = line.split('"')

            self.sourceNeuronName = splitLine[1]

    def Determine_Target_Neuron_Name(self,line):

        if "targetNeuronName" in line:

            splitLine = line.split('"')

            self.targetNeuronName = splitLine[3]

    def Determine_Weight(self,line):

        if "weight" in line:

            splitLine = line.split('"')

            self.weight = float( splitLine[5] )
