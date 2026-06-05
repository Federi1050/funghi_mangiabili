import numpy as np
from scipy.stats import zscore

class DatasetAnalisi:

    def outliers_iqr_per_col(self, data):
        result = {}
        numeric_cols = data.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outliers_count = data[(data[col] < lower) | (data[col] > upper)].shape[0]
            result[col] = outliers_count
        return result
    
    def outliers_zscore_per_col(self, data, threshold=3):
        result = {}
        numeric_cols = data.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            col_data = data[col].dropna()
            if col_data.std() == 0:
                result[col] = 0
                continue
            z_scores = zscore(col_data)
            outliers_count = np.sum(np.abs(z_scores) > threshold)
            result[col] = int(outliers_count)
        return result
    
    def valori_stringhe(self, data):
        cat_cols = data.select_dtypes(include=["object","string"]).columns
        string = ""
        for col in cat_cols:
            string += f"\n{col} ({data[col].nunique()} valori unici): {data[col].unique()}"
        string = string.strip()
        return string

    def valori_nulli(self, data):
        return data.isnull().sum().sort_values(ascending=False)

    def clean_data(self, data):
        data.drop_duplicates()
        # gestione outlier   
        # elimina caratteri strani
        # gestire nan 
        data.replace('?', np.nan)
        data["stalk-root"]=data["stalk-root"].fillna(data["stalk-root"].mode()[0])
        data.loc[data["poisonous"].isin(["unknown edibility", "not recommended"]), "poisonous"] = "definitely poisonous"
        return data
    
