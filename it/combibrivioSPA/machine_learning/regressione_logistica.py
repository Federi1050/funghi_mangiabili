from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

class RegLogistica:

    def __init__(self ,data):
        self.val_model = None
        self.set_mod(data)

    
    def set_mod(self, data):
        # Variabili esplicative e target
        y = data["poisonous"]
        
        # feature categoriche
        X = pd.get_dummies(
        data.drop(columns=["poisonous"]),
        drop_first=True
        )

        self.feature_columns = X.columns.tolist()

        # Suddivisione train/test
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )
        # Modello
        model = LogisticRegression(max_iter=1000)
        # Addestramento
        model.fit(X_train, y_train)

        self.model= model 
        y_pred = model.predict(X_test)

        self.val_model = {
            "predizioni": y_pred.tolist(),
            "coeff": self.model.coef_.tolist(),
            "intercetta": float(self.model.intercept_[0]),
            "Accuracy": accuracy_score(y_test, y_pred),
        }
        

    def get_val(self):
            return self.val_model
    
    def prevedi(self, osservazione):
    
        # se arriva lista di coppie -> dict
        if isinstance(osservazione, list):
            osservazione = dict(osservazione)

        df = pd.DataFrame([osservazione])

        # one-hot encoding identico al training
        df = pd.get_dummies(df, drop_first=True)

        # riallineamento colonne (PASSAGGIO FONDAMENTALE)
        df = df.reindex(columns=self.feature_columns, fill_value=0)

        return self.model.predict(df)

