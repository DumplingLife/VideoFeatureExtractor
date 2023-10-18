import pickle

with open('actionsense_features.pickle', 'rb') as f:
    print(pickle.load(f))