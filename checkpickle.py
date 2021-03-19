import pickle
from Project import Project

filename = "test.ms"
with open(filename, 'rb') as f:
    proj = pickle.load(f)

panes = proj.get_panes()

print(panes)