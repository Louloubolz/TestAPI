from fastapi import FastAPI
import ast

app = FastAPI()



@app.get("/add")
async def get_add(a: int, b: int):
    return {"result": a + b}

@app.get("/calcul_entre")
async def get_calcul_entree(taux_entree_ptf1_actifs : float, total_pop : int, table_taux_entree : str): 
    """
    taux_entree_ptf1_actifs : taux définit
    total_po : effectif d'une population 
    table_taux_entrée : liste composé de taux d'entrées
    
    """
    table_taux_entree = ast.literal_eval(table_taux_entree)
    # Créer une nouvelle liste en multipliant chaque élément par le produit du total_pop et taux_entree_ptf1_actifs
    result_list = [entry * total_pop * taux_entree_ptf1_actifs for entry in table_taux_entree]

    return result_list
