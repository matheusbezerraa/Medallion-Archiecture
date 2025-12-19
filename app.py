import os
import pandas as pd
from db import DB


db = DB(host="localhost", port=5432, database="postgres", user="postgres", password="postgres")

for file in os.listdir("02-silver-normalized"):
    df = pd.read_parquet(f"02-silver-normalized/{file}")
    db.create_table(
        file.replace(".parquet", ""),
        df.columns.tolist()
        )
    
    db.insert_data(
        file.replace(".parquet", ""),
        df
    )

