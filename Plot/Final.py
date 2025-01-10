import os
import json
from dataclasses import dataclass, field
from typing import Any, List, Union

data_map = {}
name = "CIRCO"

inp = open(name + ".json", "r")
data = json.load(inp)
inp.close()

data_ans = []
for i in range(len(data)):
    if data[i]["Alpha"] == 0.9 and data[i]["Beta"] == 0.15:
        data_ans.append(data[i])


out = open(name + "threshold.json", "w")
json.dump(data_ans, out, indent = 4)
out.close()

    