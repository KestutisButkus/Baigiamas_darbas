from bs4 import BeautifulSoup
import requests

def get_15min_news():
    news = []
    source_15min = requests.get("https://www.15min.lt/naujienos")
    source_15min.encoding = 'utf-8'
    soup_15min = BeautifulSoup(source_15min.text, "html.parser")
    item_data_15min = soup_15min.find_all("h4", class_="vl-title item-no-front-style")
    for item in item_data_15min[:2]:
        items_15min = item.get_text(strip=True)
        news.append(items_15min)
    return '\n'.join(news)

def get_lrt_news():
    news = []
    source_lrt = requests.get("https://www.lrt.lt")
    source_lrt.encoding = "utf-8"
    soup_lrt = BeautifulSoup(source_lrt.text, "html.parser")
    item_data_lrt = soup_lrt.find_all("h3", class_="news__title")
    for item in item_data_lrt[:2]:
        items_lrt = item.get_text(strip=True)
        news.append(items_lrt)
    return '\n'.join(news)

def get_delfi_news():
    news = []
    source_delfi = requests.get("https://www.delfi.lt/paieska")
    soup_delfi = BeautifulSoup(source_delfi.text, "html.parser")
    item_data_delfi = soup_delfi.find_all("h5", class_="headline-title headline-title--size-h4 headline-title--size-sm-h6")
    for item in item_data_delfi[:2]:
        items_delfi = item.get_text(strip=True)
        news.append(items_delfi)
    return '\n'.join(news)

def get_vz_news():
    news = []
    source_vz = requests.get("https://www.vz.lt/")
    source_vz.encoding = "utf-8"
    soup_vz = BeautifulSoup(source_vz.text, "html.parser")
    item_data_vz = soup_vz.find_all("ul", class_="ordered-articles col")
    count = 0
    for item in item_data_vz:
        articles = item.find_all("a")
        for article in articles:
            title = article.get_text(strip=True)
            link = article['href']
            if not link.startswith('http'):
                link = f"https://www.vz.lt{link}"
            news.append(title)
            count += 1
            if count == 2:
                break
        if count == 2:
            break
    return '\n'.join(news)

if __name__ == "__main__":
    print("15min naujienos:\n", get_15min_news())
    print("\nLRT naujienos:\n", get_lrt_news())
    print("\nDelfi naujienos:\n", get_delfi_news())
    print("\nVerslo žinios naujienos:\n", get_vz_news())
