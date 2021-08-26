import torch

x = torch.randn(5)
indices = torch.tensor(3)
result_1 = torch.randn([3])
result = torch.index_select(x, 0, indices,out=result_1)
print(x)
print(result)
print(result_1)