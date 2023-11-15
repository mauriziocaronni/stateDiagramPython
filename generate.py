import pygraphviz as pgv
from graphviz2drawio import graphviz2drawio
import pandas as pd
import os
import openpyxl
from openpyxl.styles import Border, Side
from datetime import datetime


def create_directory(dir_name):
    # Crea la directory se non esiste già
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def create_graph (processDir, processName):
    # Leggi il contenuto del file .dot
    with open(processDir + processName + '.dot', 'r') as file:
        diagram_code = file.read()

    # Crea un oggetto AGraph dal codice DOT
    graph = pgv.AGraph(string=diagram_code)

    # Salva il grafico come immagine o in un altro formato
    graph.draw( processDir + processName + '.svg', format='svg', prog='dot')
    
    # Salva il grafico come immagine o in un altro formato
    graph.draw( processDir + processName + '.json', format='json', prog='dot')



    return graph


def create_drawio (graph, processDir, processName):
    # Salva il grafico in formato .drawio
    xml = graphviz2drawio.convert(graph)
    # scrivi file xml
    with open(processDir + processName +'-drawio.xml', 'w') as file:
        # Scrivi la stringa nel file
        file.write(xml)


def write_excel (graph, processDir, processName):
    # Estrai gli stati di partenza, gli stati di arrivo e le etichette
    data = [(edge[0], edge.attr['label'], edge[1]) for edge in graph.edges()]

    # Crea un DataFrame da questi dati
    df = pd.DataFrame(data, columns=['Stato Corrente', 'Evento', 'Prossimo Stato'])

    # Scrivi il DataFrame in un file Excel
    df.to_excel(processDir + processName+'.xlsx', index=False)

    # aggiungi i bordi
    # Apri il file Excel con openpyxl
    wb = openpyxl.load_workbook(processDir + processName+'.xlsx')
    sheet = wb.active

    # Crea un bordo
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thin'))

    # Imposta la larghezza delle colonne A, B e C a 40 pixels
    for col in ['A', 'B', 'C']:
        sheet.column_dimensions[col].width = 30 

    # Applica il bordo alle celle nelle colonne A, B e C che contengono dati
    for row in sheet['A1':'C'+str(sheet.max_row)]:
        for cell in row:
            if cell.value is not None:
                cell.border = thin_border

    # Salva il workbook
    wb.save(processDir + processName+'.xlsx')

def main ():

    print("start", datetime.now())

 #   processName = "opening"
 #   processDir  = './' + processName + '/'
 #   print("Generating " + processName + " diagram...")
 #   graph = create_graph(processDir, processName)
 #   create_drawio(graph, processDir, processName)
#
    processName = "assessment"
    processDir  = './' + processName + '/'
    print("Generating " + processName + " diagram...")
    graph = create_graph(processDir, processName)
#    create_drawio(graph, processDir, processName)
    write_excel(graph, processDir, processName)
#
 #   processName = "expertise"
 #   processDir  = './' + processName + '/'
 #   print("Generating " + processName + " diagram...")
 #   graph = create_graph(processDir, processName)
 #   create_drawio(graph, processDir, processName)
 #   write_excel(graph, processDir, processName)
#
#    processName = "closing"
#    processDir  = './' + processName + '/'
#    print("Generating " + processName + " diagram...")
#    graph = create_graph(processDir, processName)
#    create_drawio(graph, processDir, processName)
#    write_excel(graph, processDir, processName)
#
    processName = "repair"
    processDir  = './' + processName + '/'
    print("Generating " + processName + " diagram...")
    graph = create_graph(processDir, processName)
 #   create_drawio(graph, processDir, processName)
    write_excel(graph, processDir, processName)

    processName = "global"
    processDir  = './global/' 
    print("Generating " + processName + " diagram...")
    graph = create_graph(processDir, processName)
    write_excel(graph, processDir, processName)   

    print("done!", datetime.now())
    

if __name__ == "__main__":
    main()