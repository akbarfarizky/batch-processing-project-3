import pandas as pd
from sqlalchemy import create_engine
import os

file_path = r"D:/batch-processing-project-3/source/users_w_postal_code.csv"
file_name = os.path.basename(file_path).split(".")[0]

df = pd.read_csv(file_path, sep=',')
df['email'] = df['email'].apply(lambda x: x.split('@')[1])

engine = create_engine('postgresql://postgres:123jomblo@localhost:5432/postgres')
df.to_sql(file_name,engine)
