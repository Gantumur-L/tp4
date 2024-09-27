def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    if len(chaine) == 0:
       return 0
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel

    for i in range(len(chaine)): # 0, 1, 2 ..., len(chaine)-1
        if chaine[1] == chaine[-1]: # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
    else: # si la lettre actuelle est egale est  
        if lg_actuelle > lg_max:
           lg_max = lg_actuelle 
        lg_actuelle = 1
    if lg_actuelle > lg_max: # cas de dernier plateau
     lg_max = lg_actuelle

    return lg_max

def test_plus_long_plateau():
    assert plus_long_plateau("aaaa") == len("aaaa")
    assert plus_long_plateau("dgdfffffhthhh") == 5 # il y a 4f
    assert plus_long_plateau("") == 0 # pas de parameteres

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]
