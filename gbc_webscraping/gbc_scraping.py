from bs4 import BeautifulSoup
import requests
import pandas as pd


# Data extraction

def extract(year):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    url = f"https://www.georgebrown.ca/program-finder?search=computer&year={year}"

    r = requests.get(url, headers)
    # return r.status_code  
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

programs = []

# Data transformation

def transform(soup):
    trs = soup.find_all("tr", class_="program-row")
    divs = soup.find_all("div", class_="overview-content")
    
    for i in range(len(trs)):
        title = trs[i].find("a").text.strip()
        summary = divs[i].find("div", class_="program-overview-content overview").text.strip()
        duration = divs[i].find("div", class_="program-overview-content duration").text.strip()

        program = {"title": title, "summary": summary, "duration": duration}
        programs.append(program)

    return



# Data Loading

for year in range(2020, 2023):
    c = extract(year)
    transform(c)
    
df = pd.DataFrame(programs)

print(df.head())   
df.to_csv("programs.csv", index=False)

