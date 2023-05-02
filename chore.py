import pandas as pd

def load_data(train_path=r'Data/new_train_data.csv', test_path=r'Data/new_test_data.csv'):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test

def cal_fun_score(df, graph_data, direction='out'):

    print(f'Calculating {direction} features...')
    
    if direction == 'out' or direction == 'all':
        node1 = 'node1'
        node2 = 'node2'
    else:
        node1 = 'node2'
        node2 = 'node1'
    
    df[f'node1_{direction}'] = df['node1'].apply(lambda node: graph_data.get_neighbors_size(node))
    df[f'node2_{direction}'] = df['node2'].apply(lambda node: graph_data.get_neighbors_size(node))
    
    df[f'node_cn_{direction}'] = df.apply(lambda row: graph_data.common_neighbors(row[node1], row[node2]), axis=1)
    df[f'node_jc_{direction}'] = df.apply(lambda row: graph_data.jaccard_coefficient(row[node1], row[node2]), axis=1)
    df[f'node_ks_{direction}'] = df.apply(lambda row: graph_data.katz_score(row[node1], row[node1]), axis=1)
    df[f'node_pa_{direction}'] = df.apply(lambda row: graph_data.preferential_attachment(row[node1], row[node2]), axis=1)
    df[f'node_aa_{direction}'] = df.apply(lambda row: graph_data.adamic_adar(row[node1], row[node2]), axis=1)