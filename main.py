
import pandas as pd
url='https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'
shark_df=pd.read_excel(url)
print(shark_df)

shark_df.rename(columns={"Fatal Y/N": "Fatal"}, inplace=True)
shark_df