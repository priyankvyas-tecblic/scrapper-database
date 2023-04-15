import pandas as pd
import os
from scrapper_app.models import CompanyList

def dumping_company_data():
    relative_path = os.path.dirname(os.path.realpath(__file__))
    fname = "company_list.xlsx"
    df = pd.read_excel(fname)
    print(df.columns)
    print(df.shape)
    i = 0

    while i < 2000:
        print("in while")
        CompanyList.objects.create(company_urls = df.iloc[i][0])
        i += 1