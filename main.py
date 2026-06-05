'''
carica dataset

EDA
- individuazione outlaier
- indiduazione caratteri strani o nulli
- guarda grafici correlazione, simmetria (ogni attribuit)
- test normalità (funzione mat per vedere regolarita')

cleaning
- elimina duplicati
- elimina outlier
- sostituisci caratteri strani
- trasforma target in 0 1: dove 0 edibile 1 non

logistic regression per machine learning
implementa la random forset classification
- scrivi anche un breve spiegazione

flask
docker
'''
from it.combibrivioSPA.dataset.dataset_manager import DatasetManager

print("Carico dataset")
ds_mg = DatasetManager()
print()

print("stampa dataset")
ds_mg.stampa()
print()

print("Esplorazione del dataset")
print(ds_mg.analisi())
print()

print("Visualizzazione grafici")
ds_mg.grafici()
print()

print("pulisco dataset")
ds_mg.clean()
print()

print("stampa dataset dopo cleaning")
ds_mg.stampa()
print()