import sys
import requests
from bs4 import BeautifulSoup
import time

def fetch_dexonline(word):
    url = f"https://dexonline.ro/definitie/{word}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"[ERROR] dexonline.ro returned {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    meaning_div = soup.find("div", class_="meaning")
    if not meaning_div:
        return "[No Romanian definition found.]"

    definitions = []
    for span in meaning_div.find_all("span", class_="tree-def"):
        text = span.get_text(strip=True)
        if text:
            definitions.append(text)

    if not definitions:
        return "[No Romanian definition found.]"

    return " | ".join(definitions)
pass

def fetch_oxford(word):
    url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"[ERROR] Oxford returned {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    sense = soup.find("span", class_="def")
    if not sense:
        return "[No English definition found.]"

    return sense.get_text(strip=True)
pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python define.py <word>")
        sys.exit(1)

    word = sys.argv[1].strip()
    start_time = time.time()

    definition = fetch_dexonline(word)
    print(f"Romanian definition: {definition}")
    if definition.startswith("[No") or definition.startswith("[ERROR"):
        definition = fetch_oxford(word)

    elapsed = int((time.time() - start_time) * 1000)
    print(f"{elapsed}ms -> {definition}")

    definition_english = fetch_oxford(word)
    print(f"English definition: {definition_english}")
    if definition_english.startswith("[No") or definition_english.startswith("[ERROR"):
        print("No English definition found.")
    pass

if __name__ == "__main__":
    main()
