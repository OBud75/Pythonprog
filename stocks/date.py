from datetime import datetime, timedelta

def date_moin_6_jours():
    aujourd_hui = datetime.now()
    il_y_a_6_jours = aujourd_hui - timedelta(days=6)
    return il_y_a_6_jours.strftime('%Y-%m-%d')

# Exemple d'utilisation
print("La date d'il y a 6 jours était :", date_moin_6_jours())