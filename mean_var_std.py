import numpy as np
def calculate(array):
    
    arr = np.array(array).reshape([3,3])
    
    dictionary= {
      'mean': [[],[],[]],
      'variance': [[],[],[]],
      'standard deviation': [[],[],[]],
      'max': [[],[],[]],
      'min': [[],[],[]],
      'sum': [[],[],[]]
    }


    for i in range(3):
      dictionary['mean'][0].append(np.mean(arr[i]))
      dictionary['mean'][1].append(np.mean(arr.T[i]))

      dictionary['variance'][0].append(np.var(arr[i]))
      dictionary['variance'][1].append(np.var(arr.T[i]))

      dictionary['standard deviation'][0].append(np.std(arr[i]))
      dictionary['standard deviation'][1].append(np.std(arr.T[i]))

      dictionary['max'][0].append(np.max(arr[i]))
      dictionary['max'][1].append(np.max(arr.T[i]))

      dictionary['min'][0].append(np.min(arr[i]))
      dictionary['min'][1].append(np.min(arr.T[i]))
      
      dictionary['sum'][0].append(np.sum(arr[i]))
      dictionary['sum'][1].append(np.sum(arr.T[i]))
      
    dictionary['mean'][2].append(np.mean(arr.flat))
    dictionary['variance'][2].append(np.var(arr.flat))
    dictionary['standard deviation'][2].append(np.std(arr.flat))
    dictionary['max'][2].append(np.max(arr.flat))
    dictionary['min'][2].append(np.min(arr.flat))
    dictionary['sum'][2].append(np.sum(arr.flat))

    return dictionary
    
    
    