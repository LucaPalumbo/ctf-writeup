import torch, random
import torch.nn
import numpy as np

flag = "A"*24

def floatify(ip):
	flag = [float(ord(i)) for i in ip]
	normalized = torch.tensor([flag], dtype=torch.float32)
	return normalized

def tf(_in,_out):
	weight = np.round(np.random.uniform(-1, 1, (_out, _in)).astype(np.float32),2)
	bias = np.round(np.random.uniform(-1, 1, _out).astype(np.float32),2)
	return torch.from_numpy(weight), torch.from_numpy(bias)

np.random.seed(0x544350)
model = torch.nn.Sequential(
	torch.nn.Linear(24, 450),
)

layer_shapes = [(24, 450)]

for i, (input_dim, output_dim) in enumerate(layer_shapes):
	weight, bias = tf(input_dim, output_dim)
	model[i].weight.data = weight
	model[i].bias.data = bias

original_out = [i.detach().numpy().tolist() for i in model(floatify(flag))[0]]
print(original_out)

######
A = original_out - model[0].bias.data.numpy()
B = np.linalg.pinv(model[0].weight.data.numpy())
C = np.round( np.dot(B, A), 2).tolist()
print( ''.join([chr(int(i)) for i in C]) ) 
#print(C)
#
#print( floatify(flag).numpy().squeeze() )


#print(predic_out)
#print()
#print(original_out)

#print( np.allclose(predic_out, original_out) )
# Output:
# [38883.9140625, 18747.87890625, -15371.05078125, 12231.2080078125, -56379.48046875, -33719.13671875, 9454.150390625, 9346.9814453125, 1701.4693603515625, -6380.3759765625, 12019.501953125, -4850.94140625, 14421.296875, 44332.0390625, -11196.283203125, -19712.0859375, -36390.265625]