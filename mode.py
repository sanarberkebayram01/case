import torch.nn as nn

class BasicModel(nn.Module):
    def __init__(self):
        super().__init__();
        self.layer1 = nn.Linear(10,10)
    
    def forward(self,x):
        return self.layer1(x)