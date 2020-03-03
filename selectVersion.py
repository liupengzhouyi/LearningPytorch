import torch

print(torch.__version__)

# 构造一个随机初始化的矩阵
x = torch.empty(5, 3)
print(x)

# 构造一个填充零且dtype long的矩阵
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

# 直接从数据构造张量
x = torch.tensor([5.5, 3, 4, 5])
print(x)






