import os
from string import Template

for memory in ["SLCNAND", "RRAM", "STTRAM", "PCRAM"]:
  for opt in ["ReadLatency", "ReadDynamicEnergy", "ReadEDP", "Area"]:
    with open("nvsim.tmpl.cfg") as infile, open("reports/nvsim.%s.%s.rpt" % (memory, opt), "w") as rptfile:
      with open("configs/nvsim.%s.%s.cfg" % (memory, opt), "w") as outfile:
        outfile.write(Template(infile.read()).substitute(memory=memory, opt=opt))
      report = os.popen("./nvsim configs/nvsim.%s.%s.cfg" % (memory, opt)).read()
      print(report)
      rptfile.write(report)
