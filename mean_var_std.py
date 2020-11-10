import numpy as np

def calculate(list):
  try:
    lst = np.reshape(np.array(list), (3, 3))
  except ValueError as ve:
    print('List must contain nine numbers.')
    return ve     
 
  calculations = {}
 
  calculations['mean'] = [lst.mean(axis = 0).tolist(), lst.mean(axis = 1).tolist(), lst.mean()]
  calculations['variance'] = [lst.var(axis = 0).tolist(), lst.var(axis = 1).tolist(), lst.var()]
  calculations['standard deviation'] = [lst.std(axis = 0).tolist(), lst.std(axis = 1).tolist(), lst.std()]
  calculations['max'] = [lst.max(axis = 0).tolist(), lst.max(axis = 1).tolist(), lst.max()]
  calculations['min'] = [lst.min(axis = 0).tolist(), lst.min(axis = 1).tolist(), lst.min()]
  calculations['sum'] = [lst.sum(axis = 0).tolist(), lst.sum(axis = 1).tolist(), lst.sum()]

  return calculations