import pandas as pd

class ScoreFuncPipeline:
    def __init__(self, **socre_func: dict) -> None:
        self.score_func = socre_func
    
    def fit(self, graph, *df:pd.DataFrame) -> None:
        # self.graph = graph
        # self.df = df
        pass