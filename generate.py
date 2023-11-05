import pygraphviz as pgv
from graphviz2drawio import graphviz2drawio
import pandas as pd
import os

def create_directory(dir_name):
    # Crea la directory se non esiste già
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


processName = "opening"
processDir  = processName



# Leggi il contenuto del file .dot
with open('./'+processDir + '/' + processName + '.dot', 'r') as file:
    diagram_code = file.read()

# Crea un oggetto AGraph dal codice DOT
graph = pgv.AGraph(string=diagram_code)

# Salva il grafico come immagine o in un altro formato
graph.draw('./'+processDir + '/' + processName + '.svg', format='svg', prog='dot')


xml = graphviz2drawio.convert(graph)
# Apri il file in modalità scrittura ('w')
with open('./'+processDir + '/'+processName +'-drawio.xml', 'w') as file:
    # Scrivi la stringa nel file
    file.write(xml)



# Estrai gli stati di partenza, gli stati di arrivo e le etichette
data = [(edge[0], edge.attr['label'], edge[1]) for edge in graph.edges()]

# Crea un DataFrame da questi dati
df = pd.DataFrame(data, columns=['Corrente', 'Evento', 'Prossimo'])

# Scrivi il DataFrame in un file Excel
df.to_excel('./'+processDir + '/'+processName+'.xlsx', index=False)