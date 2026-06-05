class Analisi:

    def outliers_iqr_per_col(self):
        result = {}

        numeric_cols = self.data.select_dtypes(include=np.number).columns

        for col in numeric_cols:
            Q1 = self.data[col].quantile(0.25)
            Q3 = self.data[col].quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outliers_count = self.data[(self.data[col] < lower) | (self.data[col] > upper)].shape[0]
            result[col] = outliers_count

        return result
    
    def outliers_zscore_per_col(self, threshold=3):
        result = {}

        numeric_cols = self.data.select_dtypes(include=np.number).columns

        for col in numeric_cols:
            col_data = self.data[col].dropna()

            if col_data.std() == 0:
                result[col] = 0
                continue

            z_scores = zscore(col_data)

            outliers_count = np.sum(np.abs(z_scores) > threshold)
            result[col] = int(outliers_count)

        return result
    
    def valori_stringhe(self):
        cat_cols = self.data.select_dtypes(include=["object","string"]).columns

        for col in cat_cols:
            print(f"\n{col} ({self.data[col].nunique()} valori unici):")
            print(self.data[col].unique())

    



