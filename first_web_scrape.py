from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')  

table = soup.find_all('table')[1]
world_titles = table.find_all('th')

world_table_titles = []
for title in world_titles:
    world_table_titles.append(title.text.strip())


df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

excel_path = '/Users/tylercorrell/desktop/excel/company_revenues.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(excel_path, index=False)