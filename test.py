from functools import reduce
import operator

dataDict = {"/": {}}

maplist = ["/"]


reduce(operator.getitem, maplist, dataDict)["diid"] = {}
reduce(operator.getitem, maplist, dataDict)["kdjjfdf"] = {}


print(dataDict)
