# **Practice of Social Media Analytics CS5128701**

This is a code written for the ***Practice of Social Media Analytics*** course.  

The code was written by [@李享紝 - Hsiang-Jen Li](https://github.com/hsiangjenli), but there is no guarantee that all algorithms are error-free. Therefore, users need to assume their own risk when using these code.

## **Project structure**

```yaml
.
├── ./00_demo_usage.ipynb # 使用演算法範例
├── ./01_degree_random.ipynb # 資料前處理 + 特徵工程 + Ensemble Voting Predict
├── ./Data
│   ├── ./Data/new_test_data.csv  # 訓練用資料
│   ├── ./Data/new_train_data.csv # 測試用資料
│   └── ./Data/sample_submit.csv
├── ./README.md
├── ./core
│   ├── ./core/__init__.py
│   ├── ./core/base.py # 基本 Graph 的 attributes
│   ├── ./core/graph.py # 主要 Graph + scoring function
│   ├── ./core/pipeline.py # 方便建立 scoring function(feature engineering) 的 PIPELINE
│   ├── ./core/score_func.py # 所有 scoring function (JC, CN, PA....)
│   └── ./core/sparsification.py # 稀疏化的模組 (Degree-Based, Random-Walk)
```
## **Create documentation from source code**
```shell
IMAGE=https://hsiangjenli.github.io/hsiangjenli/static/image/ntust.png
pdoc core -o ./docs --favicon "$IMAGE" --logo "$IMAGE" --docformat "numpy"
```


