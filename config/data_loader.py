# import pandas as pd
# from config.database import engine
#
# data = pd.read_csv('C:\\Users\\SoftBD\\workstation\\practice\\job_recommender\\files\\jd_unstructured_data.csv')
#
# data.to_sql('job_db', con=engine, if_exists='append')
# print('success!')
# df = pd.read_sql('SELECT * FROM job_table', con=engine)
# df.set_index('job_id', inplace=True)
# print(df.index)