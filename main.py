import yfinance as yf
import json
import numpy as np

def convert_to_native_type(value):
    if isinstance(value, np.int64):
        return int(value)
    return value

def get_all_symbols():
    try:
        url = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
        data = pd.read_csv(url)
        return data['Symbol'].tolist()
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None

def get_stock_info(symbol):
    try:
        data = yf.download(symbol, period="1d", interval="1m")
        if not data.empty:
            stock_info = {
                "Action": symbol,
                "Open": convert_to_native_type(data["Open"].iloc[-1]),
                "High": convert_to_native_type(data["High"].iloc[-1]),
                "Low": convert_to_native_type(data["Low"].iloc[-1]),
                "Volume": convert_to_native_type(data["Volume"].iloc[-1])
            }
            return stock_info
        else:
            print(f"Informations introuvables pour le symbole {symbol}")
            return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None

symbols = ["AAPL", "GOOGL", "TSLA"]
result_json = []

for symbol in symbols:        
    stock_info = get_stock_info(symbol)

    if stock_info is not None:
        result_json.append(stock_info)

if result_json:
    print("Résultats sous forme de JSON :")
    print(json.dumps(result_json, indent=2))
else:
    print("Aucun résultat disponible.")
