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

# from it.combibrivioSPA.dataset.dataset_manager import DatasetManager
from it.combibrivioSPA.flask.flask_manager import FlaskManager
# from it.combibrivioSPA.machine_learning.regressione_logistica import RegLogistica
# from it.combibrivioSPA.machine_learning.random_forest import RndForest


app = FlaskManager()
app.run(host='0.0.0.0', port=5000, debug=True)

'''
print("Carico dataset")
ds_mg = DatasetManager()
print()

print("stampa dataset")
# ds_mg.stampa()
print()

print("Esplorazione del dataset")
# print(ds_mg.analisi())
print()

print("Visualizzazione grafici")
# ds_mg.grafici()
print()

print("pulisco dataset")
ds_mg.clean()
print()

print("stampa dataset dopo cleaning")
# ds_mg.stampa()
print()

print("correlazione")
# print(ds_mg.correlazione())
print()

print("creazione modello regressione logistica")
reg_log = RegLogistica(ds_mg.get_datatset())
print()

print("valutazione modello regressione logistica")
# print(reg_log.get_val())
print()

# print(ds_mg.get_datatset().loc[5].to_dict())

print("previsione per il dato")
oggetto = [
    ('cap-shape', 'x'), ('cap-surface', 'y'),('cap-color', 'y'), ('bruises', 't'),
    ('odor', 'a'), ('gill-attachment', 'f'), ('gill-spacing', 'c'), ('gill-size', 'b'),
    ('gill-color', 'n'), ('stalk-shape', 'e'), ('stalk-root', 'c'), ('stalk-surface-above-ring', 's'),
    ('stalk-surface-below-ring', 's'), ('stalk-color-above-ring', 'w'), ('stalk-color-below-ring', 'w'),
    ('veil-color', 'w'), ('ring-number', 'o'), ('ring-type', 'p'), ('spore-print-color', 'k'),
    ('population', 'n'), ('habitat', 'g')
]
# print(reg_log.prevedi(oggetto))
print()

print("creazione modello random forest")
rnd_forest = RndForest(ds_mg.get_datatset())
print()

print("valutazione modello random forest")
print(rnd_forest.get_val())
print()

print(ds_mg.get_datatset().loc[5].to_dict())

print("previsione per il dato")
oggetto = [
    ('cap-shape', 'x'), ('cap-surface', 'y'),('cap-color', 'y'), ('bruises', 't'),
    ('odor', 'a'), ('gill-attachment', 'f'), ('gill-spacing', 'c'), ('gill-size', 'b'),
    ('gill-color', 'n'), ('stalk-shape', 'e'), ('stalk-root', 'c'), ('stalk-surface-above-ring', 's'),
    ('stalk-surface-below-ring', 's'), ('stalk-color-above-ring', 'w'), ('stalk-color-below-ring', 'w'),
    ('veil-color', 'w'), ('ring-number', 'o'), ('ring-type', 'p'), ('spore-print-color', 'k'),
    ('population', 'n'), ('habitat', 'g')
]
print(rnd_forest.prevedi(oggetto))
print()
'''