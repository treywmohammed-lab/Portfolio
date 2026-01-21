from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               company TEXT,
               location TEXT,
               link TEXT

               )
               
               """)

conn.commit()



URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)



soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

job_list = []

for job_card in python_job_cards:
    title = job_card.find("h2", class_="title").text.strip()
    company = job_card.find("h3", class_="company").text.strip()
    location = job_card.find("p", class_="location").text.strip()
    link = job_card.find_all("a")[1]["href"]

    job_list.append((title, company, location, link))



for j in job_list:
    cursor.executemany("""
    INSERT INTO jobs (
                   title, company, location, link)
                   VALUES(?,?,?,?)

                    """,job_list)
   

    
conn.commit()
conn.close()
print(f"{len(job_list)} convereted to your database.")    


df = pd.DataFrame(job_list, columns=['title' , 'company' , 'location' , 'link'])
df.to_csv('jobs.csv', index=False)

print(df)


