import time
import torch

cuda = torch.cuda.is_available()
num_device = torch.cuda.device_count()
id_device = torch.cuda.current_device()

name_device = torch.cuda.get_device_name(id_device)
serial_device = torch.cuda.device(id_device)

print("--------------- Cuda info ----------------")
print("cuda is available: {0}".format(cuda))
print("cuda device count: {0}".format(num_device))
print("cuda current device: {0}".format(id_device))
print("get device name: {0}".format(name_device))
print("cuda device: {0}".format(serial_device))
print("-----------------------------------------")

#Additional Info when using cuda
def additional_info(id_device: int): 
    if device.type == 'cuda': # type: ignore
        print(torch.cuda.get_device_name(id_device))
        print('Memory Usage:')
        print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
        #print('Allocated:', round(torch.cuda.memory_allocated(0), 'MB'))
        print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')
        #print('Cached:   ', round(torch.cuda.memory_reserved(0), 'MB'))

inicio_gpu = time.time()
print("---------------- GPU test ----------------")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()
additional_info(id_device)

print("-----------------------------------------")
tensor_gpu = torch.rand(22, 30, 1920, 1080, 3).to(device)
print("tensor: {0}".format(tensor_gpu.size()))
additional_info(id_device)

fin_gpu = time.time()

print("--------------- Execution time ------------")
print("Time: {0} seg".format(fin_gpu-inicio_gpu)) 


inicio_cpu = time.time()
print("---------------- cpu test ----------------")
device = 'cpu'
print('Using device:', device)

print("-----------------------------------------")
tensor_cpu = torch.rand(22, 30, 1920, 1080, 3).to(device)
print("tensor: {0}".format(tensor_cpu.size()))

fin_cpu = time.time()

print("--------------- Execution time ------------")
print("Time: {0} seg".format(fin_cpu-inicio_cpu))

