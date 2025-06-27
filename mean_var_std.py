import numpy as np

def calculate(list):
    if len(list)!=9:
        print('List must contain nine numbers.')
        return

    arr=np.array(list).reshape(3,3)
    mean1=[np.mean(arr[:,i]) for i in range(len(arr))]
    mean2=[np.mean(arr[i]) for i in range(len(arr))]
    mean_fla=np.mean(arr)
    var1=[np.var(arr[:,i]) for i in range(len(arr))]
    var2=[np.var(arr[i]) for i in range(len(arr))]
    var_fla=np.var(arr)
    std1=[np.std(arr[:,i]) for i in range(len(arr))]
    std2=[np.std(arr[i]) for i in range(len(arr))]
    std_fla=np.std(arr)
    max1=[np.max(arr[:,i]) for i in range(len(arr))]
    max2=[np.max(arr[i]) for i in range(len(arr))]
    max_fla=np.max(arr)
    min1=[np.min(arr[:,i]) for i in range(len(arr))]
    min2=[np.min(arr[i]) for i in range(len(arr))]
    min_fla=np.min(arr)
    sum1=[np.sum(arr[:,i]) for i in range(len(arr))]
    sum2=[np.sum(arr[i]) for i in range(len(arr))]
    sum_fla=np.sum(arr)
    calculations={'mean':[mean1,mean2,mean_fla],
    'variance':[var1,var2,var_fla],
    'standard deviation':[std1,std2,std_fla],
    'max':[max1,max2,max_fla],
    'min':[min1,min2,min_fla],
    'sum':[sum1,sum2,sum_fla],
    }
    
    
    
    return calculations
    
