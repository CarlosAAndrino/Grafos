grafo = {
    'Oradea' : ['Zerind', 'Sibiu'],
    'Zerind' : ['Oradea', 'Arad'],
    'Arad' : ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara' : ['Arad', 'Lugoj'],
    'Lugoj' : ['Timisoara', 'Mehadia'],
    'Mehadia' : ['Lugoj', 'Dobreta'],
    'Dobreta' : ['Mehadia', 'Craiova'],
    'Sibiu' : ['Oradea', 'Arad', 'RimnicuVilcea', 'Fagaras'],
    'Fagaras' : ['Sibiu', 'Bucharest'],
    'RimnicuVilcea' : ['Sibiu', 'Craiova', 'Pitesti'],
    'Craiova' : ['Dobreta', 'RimnicuVilcea', 'Pitesti'],
    'Pitesti' : ['RimnicuVilcea', 'Craiova', 'Bucharest'],
    'Bucharest' : ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu' : ['Bucharest'],
    'Urziceni' : ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova' : ['Urziceni', 'Eforie'],
    'Eforie' : ['Hirsova'],
    'Vaslui' : ['Urziceni', 'Iasi'],
    'Iasi' : ['Vaslui', 'Neamt'],
    'Neamt' : ['Iasi'],
}

visited = set()

def dfs(visitados, grafo, estado_inicial, estado_final): 
    if estado_inicial not in visitados:
        print(estado_inicial)
        if estado_inicial == estado_final:
            exit()
        visitados.add(estado_inicial)
        for vizinho in grafo[estado_inicial]:
            dfs(visitados, grafo, vizinho, estado_final)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, grafo, 'Oradea', 'Timisoara')