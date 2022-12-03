import os
import pandas as pd



def get_mean_std(loader):
        channels_sum, channels_square_sum, num_batches = 0, 0, 0
        for data, _ in loader:
            channels_sum += torch.mean(data.type(torch.FloatTensor), dim = [0,2,3])
            channels_square_sum += torch.mean(data.type(torch.FloatTensor)**2, dim = [0,2,3])
            num_batches += 1
        mean = channels_sum/num_batches
        std = (channels_square_sum/num_batches - mean**2)**0.5
        return mean, std
    mean, std = get_mean_std(testloader)
    print(mean, std)

        
