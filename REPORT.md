# **Report**
## **Implementation of 6 Algorithms**

1. CommonNeighbors
2. JaccardCoefficient
3. AdamicAdar
4. ShortestPath
5. KatzScore
6. PreferentialAttachment

## **Basic Understand of Dataset**
### **Train set**
![Image](https://i.imgur.com/G2Vhl3v.png)

### **Test Set**
![Image](https://i.imgur.com/PcgtEzd.png)

## **Flow Chart**

### **pseudocode**

1. Create Graph using train data where label is 1
1. Sparsify the Graph using Degree-Based and RandomWalk methods
1. Generate new features (CN, JC, AA, PA) using ScoreFunc based on new graphs and train/test data
1. Train a small model on the new train data (excluding node1 and node2)
1. Use the trained models to predict test data (excluding node1 and node2) and perform voting

### **Preprocessing**
- **Node Out** : The number of edges pointing from Node1 to other nodes.
- **Node In** : The number of edges pointing to Node1 from other nodes.
- **Node All** : Refers to an undirected graph.

![Image](https://i.imgur.com/Rd0Ioln.png)

### **Modeling**
![Image](https://i.imgur.com/eKciysF.png)

## **Result**
|Test Name|Node Direction|ScoreFunc|Model|Accuracy|Note|
|:-------:|--------------|---------|-----|--------|----|
|2023_04_22 test_01-test_jc_pa|Node Out|JC & PA|RandomForest Classifier|0.52333|    |
|2023-04-28-test-02|Node Out|Neighbor Size & CN & JC & AA|RandomForestClassifier, XGBClassifier, LogisticRegression|0.52916|Use a voting method to make predictions based on the predicted results from RFC, XGB, LR|
|2023-04-30 test-08|Node Out & In|Neighbor Size & CN & JC & PA|Logistic Regression|0.67194|    |
|2023_05_07 test_02_rw_db_lr|Node Out & In|Neighbor Size & CN & JC & PA|Logistic Regression|**0.67305**|<li>Degree-based Sparsification</li><li>Random-Walk Sparsification</li><li>Train logistic regression models with different parameters on the training set</li><li>Use a voting method to make predictions based on the predicted results (if more than half predict 1, then it is considered as 1)</li>|

1. Here are some results from a few tests, as we ran too many tests and are uncertain about which parameters were used
1. In terms of model performance, LogisticRegression clearly performed better than RandomForestClassifier
1. Regarding the direction of nodes, using all three types of direction (In, Out, All) did not result in better performance than using just In and Out
1. For FuncScore, using all values did not improve model accuracy, whereas using Neighbor Size, CN, JC, and PA yielded relatively better results
1. The accuracy on the final test set was about 67%