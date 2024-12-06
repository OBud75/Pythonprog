import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

# Téléchargez les données d'Amazon
amazon_data = yf.download(
    tickers="AMZN", start="2020-06-01", end="2024-06-01"
)

# Vérifiez si les données sont vides
if amazon_data.empty:
    print("No data found. Please check the ticker or date range.")
else:
    # Aplatir les colonnes MultiIndex
    amazon_data.columns = ["_".join(col).strip() for col in amazon_data.columns.values]
    
    # Remettez l'index dans une colonne pour que "Date_" soit accessible
    amazon_data.reset_index(inplace=True)

    # Tracez les données
    plt.figure(figsize=(14, 7))
    sns.set_style(style="ticks")
    sns.lineplot(data=amazon_data, x="Date", y="Adj Close_AMZN", color="firebrick")
    sns.despine()

    plt.title(label="Amazon Stock Price", size="x-large", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()
