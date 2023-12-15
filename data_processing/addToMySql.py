# #SQL Script trong Django
# import pandas as pd
# import pymysql
# from sqlalchemy import create_engine

# hostname = "localhost"
# database = "football"
# username = "root"
# password = "1234"

# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))

# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="football",
# )

# dataframes_dict = {
#     #"tablename":"path",
#     "matchs_dataset_model": "./dataset_model/matchs_dataset_model.csv",
#     "fbref_matchgoals_modified": "./fbref_modified/fbref_matchgoals_modified.csv",
#     "fbref_matchinfos_modified": "./fbref_modified/fbref_matchinfos_modified.csv",
#     "fbref_matchplayerstats_modified": "./fbref_modified/fbref_matchplayerstats_modified.csv",
#     "fbref_matchsquad_modified": "./fbref_modified/fbref_matchsquad_modified.csv",
#     "fbref_matchstats_modified": "./fbref_modified/fbref_matchstats_modified.csv",
#     "matchsquad_players": "./merge/matchsquad_players_completed.csv",
#     "sofifa_players_attr_modified": "./sofifa_modified/sofifa_players_attr_modified.csv",
#     "sofifa_players_infos_modified": "./sofifa_modified/sofifa_players_infos_modified.csv"
# }

# for df_name, file_path in dataframes_dict.items():
#     df = pd.read_csv(file_path)
#     df.to_sql(df_name, engine, if_exists="replace", index=False)

# connection.close()
# engine.dispose()

import pandas as pd
import pymysql
from sqlalchemy import create_engine
from concurrent.futures import ThreadPoolExecutor

hostname = "localhost"
database = "football"
username = "root"
password = "1234"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=database, user=username, pw=password))

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="football",
)

dataframes_dict = {
    # "tablename":"path",
    "matchs_dataset_model": "./dataset_model/matchs_dataset_model.csv",
    "fbref_matchgoals_modified": "./fbref_modified/fbref_matchgoals_modified.csv",
    "fbref_matchinfos_modified": "./fbref_modified/fbref_matchinfos_modified.csv",
    "fbref_matchplayerstats_modified": "./fbref_modified/fbref_matchplayerstats_modified.csv",
    "fbref_matchsquad_modified": "./fbref_modified/fbref_matchsquad_modified.csv",
    "fbref_matchstats_modified": "./fbref_modified/fbref_matchstats_modified.csv",
    "matchsquad_players": "./merge/matchsquad_players_completed.csv",
    "sofifa_players_attr_modified": "./sofifa_modified/sofifa_players_attr_modified.csv",
    "sofifa_players_infos_modified": "./sofifa_modified/sofifa_players_infos_modified.csv"
}

def process_dataframe(df_name, file_path):
    df = pd.read_csv(file_path)
    df.to_sql(df_name, engine, if_exists="replace", index=True,index_label="id")

# Create a ThreadPoolExecutor with the desired number of threads
executor = ThreadPoolExecutor(max_workers=4)

# Submit each dataframe processing task to the executor
futures = [executor.submit(process_dataframe, df_name, file_path) for df_name, file_path in dataframes_dict.items()]

# Wait for all tasks to complete
for future in futures:
    future.result()

connection.close()
engine.dispose()