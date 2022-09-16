import torch
from mode import BasicModel

if __name__ == "__main__":
    model = BasicModel()
    print(model.forward(torch.zeros((10))))
    torch.save(model.state_dict(),"saved_model")

