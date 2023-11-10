import pygraphviz as pgv

def dfs(graph, start, path=None):
    if path is None:
        path = []

    path.append(start)

    for edge in graph.out_edges(start):
        node = edge[1]
        label = graph.get_edge(*edge).attr['label']
        if node not in path:
            path.append(f"{node} (Transition: {label})")
            dfs(graph, node, path)

    return path



def main ():
    processName = "global"
    processDir  = './global/'

    print("Testing " + processDir + processName + ".dot"  + "\n")
    # Leggi il contenuto del file .dot

    with open(processDir + processName + '.dot', 'r') as file:
        diagram_code = file.read()

    # Crea un oggetto AGraph dal codice DOT
    graph = pgv.AGraph(string=diagram_code)
    
    
    # Utilizza la funzione
    start_state = 'InizializzazioneIncarico'
    
    # Ottieni tutti i percorsi possibili
    all_paths = []
    for node in graph.nodes():
        all_paths.append(dfs(graph, node))
    
# Apri il file in modalità scrittura
    with open('output.txt', 'w') as file:
     # Stampa tutti i percorsi nel file
        for path in all_paths:
         file.write(' -> '.join(path) + '\n')


    print("Done!")


if __name__ == "__main__":
    main()