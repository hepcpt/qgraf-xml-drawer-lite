import xml.etree.ElementTree as ET
from propagator import *
from leg import *
from xmlItemSort import *

INPUT = "model1_output"
pt = {"L": "fermion", "L_star": "fermion", "lr": "fermion", "lr_star": "fermion", "nr": "fermion", "nr_star": "fermion", "F": "fermion", "F_star": "fermion", "H": "charged scalar", "H_star": "charged scalar", "S1": "charged scalar", "S1_star": "charged scalar", "S2": "charged scalar", "S2_star": "charged scalar" }

GRAPHS = ET.parse(INPUT)
DIAGRAMS = GRAPHS.find("diagrams")

file = open("diagrams.tex","w+")

for diagram in list(DIAGRAMS):
    DiagID = diagram.find("id").text
    print("Doing diagram: "+DiagID)
    file.write(DiagID+"~\\feynmandiagram[]{\n")
    NOpropagators = list(diagram.find("propagators"))
    LegsSort = itemSort(diagram.find("legs"), "vertex")
    NOlegs = list(LegsSort)
    propagators = []
    for p in NOpropagators:
        propagators.append(propagator(p))
    for p in propagators:
        p.texprint(file, pt)
    legs = []
    for l in NOlegs:
        legs.append(leg(l))
    for l in legs:
        l.texprint(file, pt)
    file.write("};\n")
file.write("\n")