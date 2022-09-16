import torch
from mode import BasicModel

PATH = "saved_model"

model = BasicModel()
model.load_state_dict(torch.load(PATH))
print(model.forward(torch.zeros((10))))