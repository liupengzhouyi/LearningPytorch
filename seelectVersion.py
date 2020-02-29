import torch

print(torch.__version__)

x = torch.empty(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3, 4, 5])
print(x)

















