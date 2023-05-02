# %% Import necessary packages
from chore import *
from core import Graph
import warnings

warnings.filterwarnings("ignore")

# %% Load the data
train, test = load_data()

# %% Create a graph from the training data
graph_out, graph_in, graph_all = Graph(), Graph(), Graph()

for _, row in train[train['label'] == 1].iterrows():
    # Graph_out is the graph with edges from node1 to node2
    graph_out.add_edge(row['node1'], row['node2'])
    
    # Graph_in is the graph with edges from node2 to node1
    graph_in.add_edge(row['node2'], row['node1'])
    
    # Graph_all is the graph with edges from node1 to node2 and from node2 to node1
    graph_all.add_edge(row['node1'], row['node2'])
    graph_all.add_edge(row['node2'], row['node1'])

# %% Calculate the score functions
cal_fun_score(df=train, graph_data=graph_out, direction='out')
cal_fun_score(df=train, graph_data=graph_in, direction='in')
cal_fun_score(df=train, graph_data=graph_all, direction='out')

cal_fun_score(df=test, graph_data=graph_out, direction='out')
cal_fun_score(df=test, graph_data=graph_in, direction='in')
cal_fun_score(df=test, graph_data=graph_all, direction='out')

# %% Save the data
# train.to_csv(r'Data/preprocessing/new_train_data.csv', index=False)
# test.to_csv(r'Data/preprocessing/new_test_data.csv', index=False)

degree_based = {
    "N1_GTOD": "{mode}.node1_out > graph_out.get_average_degree",
}

from sklearn.linear_model import LogisticRegression

x_col = train.columns[3:].to_list()
y_col = 'label'

for group_id, operation in degree_based.items():
    lr = LogisticRegression()
    train_op = eval(operation.format(mode='train'))
    test_op =  eval(operation.format(mode='test'))

    lr.fit(train[train_op][x_col], train[train_op][y_col])

    train[group_id] = ''
    test[group_id] = ''

    train[train_op][group_id] = lr.predict(train[train_op][x_col])
    test[test_op][group_id] = lr.predict(test[test_op][x_col])

print(train.columns)