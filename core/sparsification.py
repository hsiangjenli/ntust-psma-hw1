from core.base import graph
import pandas as pd
import numpy as np

class DegreeBased:

    def __init__(self, 
                 graph: dict, 
                 train: pd.DataFrame, 
                 test: pd.DataFrame, 
                 x_col: list, y_col: str, 
                 models: list,
                 **index
        ):

        self.graph = graph
        self.index = index

        self.train = train
        self.test = test

        self.x_col = x_col
        self.y_col = y_col

        self.models = models
    
    # @property
    # def model(self):
    #     return self.__model
    
    def __sparsify(self, group_name: str, index):
        # print(index.format(*'train'))
        group_name = f'{group_name}_{self.model.__class__.__name__}'
        index_train = self.train.loc[eval(index.format(*['train' for e in range(10)]))].index.tolist()
        index_test = self.test.loc[eval(index.format(*['test' for e in range(10)]))].index.tolist()
        # train.loc[train['label'] > 0].index.tolist()
        train, model, x_col, y_col = self.train.loc[index_train], self.model, self.x_col, self.y_col
        print(train.label.value_counts())

        model.fit(train[x_col], train[y_col])
        self.train[group_name], self.test[group_name] = np.full(len(self.train), -1), np.full(len(self.test), -1)
        self.train.loc[index_train, group_name] = model.predict(self.train.loc[index_train][x_col])
        self.test.loc[index_test, group_name] = model.predict(self.test.loc[index_test][x_col])

    def fit(self):
        for self.model in self.models:
            for group_name, index in self.index.items():
                self.__sparsify(group_name, index)
