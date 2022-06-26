import json
import complements
def graph():
    Loc = [(10, 10), (10, 24), (23, 22), (22, 11),(10, 34), (30,27)]
    #Loc = complements.coordenadas()
    G=complements.grafoTraficoAlto()
    
    """"  
    G = [[(1, 2), (3, 1)],
         [(2, 3)],
         [(3, 3)],
         []] """ 

    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    #bestpath = [-1, 0, 1, 0]
    bestpath=complements.rutaTraficoBajo()
    path1 = [-1, 0, 1, 0]
    path2 = [-1, 0, 1, 0]

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)