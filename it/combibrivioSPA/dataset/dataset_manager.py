import pandas as pd
from ucimlrepo import fetch_ucirepo
from dataset_analisi import DatasetAnalisi
from grafici import Grafici

class DatasetManager:
    def __init__(self):
        self.__dataset = None
        self.__data_ana = DatasetAnalisi()
        self.__grafici = Grafici()

    def load(self):
        # fetch dataset
        mushroom = fetch_ucirepo(id=73)

        # data (as pandas dataframes)
        X = mushroom.data.features
        y = mushroom.data.targets

        dataset = pd.concat((X, y), axis=1)
        self.__dataset = dataset

    def analisi(self):
        val_nan = self.__data_ana.val_nan(self.__dataset)
        val_strani = self.__data_ana.val_strani(self.__dataset)
        outliers = self.__data_ana.outlier(self.__dataset)
        return {
            "val_nan": val_nan,
            "val_strani": val_strani,
            "outliers": outliers
        }

    def normality(self):
        norm = self.__data_ana.normality(self.__dataset)
        return {
            "normality": norm
        }

    def grafici(self):
        grafic = self.__grafici.correlazione(self.__dataset)
        return {
            "grafic": grafic
        }

    def clean(self):
        self.__data_ana.clean(self.__dataset)

