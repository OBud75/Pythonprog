from datetime import datetime, timedelta

# D'une manière générale on préfère l'anglais
def date_moin_6_jours():
    aujourd_hui = datetime.now()
    il_y_a_6_jours = aujourd_hui - timedelta(days=6)
    return il_y_a_6_jours.strftime('%Y-%m-%d')

# Exemple d'utilisation
print("La date d'il y a 6 jours était :", date_moin_6_jours())

# Si on devait améliorer le code (pas demandé ici), voila un exemple de ce qui me vient en tête:
def date_x_days_ago(days, format='%Y-%m-%d'):
    return (datetime.now() - timedelta(days=days)).strftime(format=format)
