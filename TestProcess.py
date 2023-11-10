import pygraphviz as pgv
import random

def simulate_state_transition(dot_file, start_state):
    # Crea un oggetto AGraph dal file DOT
    graph = pgv.AGraph(dot_file)

    # Inizia dal primo nodo
    current_state = start_state

    while True:
        #print(f"Current state: {current_state}")

        # Ottieni tutti gli edge adiacenti al nodo corrente
        adjacent_edges = list(graph.out_edges(current_state, keys=True))

        # Se non ci sono edge adiacenti, termina la simulazione
        if not adjacent_edges:
            print("No more transitions possible. Ending simulation.")
            break

        # Scegli un nodo adiacente a caso come prossimo stato
        next_edge = random.choice(adjacent_edges)
       
        # Ottieni il nodo di destinazione e la label dell'edge
        next_state = next_edge[1]
        transition_label = graph.get_edge(*next_edge).attr['label']

        # Stampa la transizione e la label
        print(f"Current status: {current_state} \t-> Event: {transition_label} \t-> next: {next_state} ")


        # Aggiorna lo stato corrente
        current_state = next_state

# Utilizza la funzione
#dot_file = 'path_to_your_dot_file.dot'
#simulate_state_transition(dot_file)



def main ():
    processName = "Global"
    processDir  = './global/'

    print("Testing " + processDir + processName + ".dot"  + "\n")

    for i in range(1):
        print("\nSimulation " + str(i) + "\n")
        simulate_state_transition(processDir + processName + ".dot", "CreazioneManualeIncarico")

    print("Done!")


if __name__ == "__main__":
    main()