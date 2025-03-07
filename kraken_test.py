import requests

# Fungsi untuk mendapatkan daftar pasangan perdagangan dari Kraken
def fetch_kraken_pairs():
    url = "https://api.kraken.com/0/public/AssetPairs"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            return {pair: data["result"][pair]["altname"] for pair in data["result"]}
    print(f"❌ Gagal mendapatkan pair Kraken: {response.text}")
    return {}

# Fungsi untuk mendapatkan harga ticker dari Kraken
def fetch_kraken_ticker(pair):
    url = f"https://api.kraken.com/0/public/Ticker?pair={pair}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            pair_key = list(data["result"].keys())[0]  # Dapatkan kunci pair
            price = float(data["result"][pair_key]["c"][0])  # Harga terakhir
            return price
    print(f"❌ Gagal mendapatkan harga untuk {pair}: {response.text}")
    return None

# **Coba Fetch Data**
kraken_pairs = fetch_kraken_pairs()
print(f"✅ Kraken Pair Map: {kraken_pairs}")

# **Coba Ambil Harga untuk BTC/USD (XXBTZUSD)**
if "XXBTZUSD" in kraken_pairs:
    btc_price = fetch_kraken_ticker("XXBTZUSD")
    print(f"✅ Harga BTC/USD di Kraken: {btc_price}")
else:
    print("❌ BTC/USD tidak ditemukan di Kraken pairs!")
