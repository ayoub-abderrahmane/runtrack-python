def phare_calculator (nb ,h):
    metre = h / 100
    trajet = metre * nb
    allez_retour = trajet * 2
    journée = allez_retour * 5
    semaine = journée * 7
    result = semaine
    print ("Pour",nb ,"marches de" ,h ,"cm,le gardien parcourt" ,result ,"m par semaine")

phare_calculator (5 ,5)
    