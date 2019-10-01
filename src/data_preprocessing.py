import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt


def get_news_final(min_popu = 1000):
    news_final = pd.read_csv("../data/News_Final.csv")
    news_final = news_final[news_final["Facebook"]>=min_popu].dropna()
    return news_final

def get_plat_topic(min_popu = 1000, plats = ['Facebook'], topics = ['Economy', 'Microsoft', 'Obama', 'Palestine']):
    plat_topic_dict = {}
    for p in plats:
        for t in topics:
            name = p + '_' + t
            df = pd.read_csv(f"../data/{name}.csv")
            df = df[df["TS144"]>=min_popu]
            plat_topic_dict[name] = df
    return plat_topic_dict

def process_news_final(df):
    df_encode = pd.DataFrame(index = df["IDLink"])
    onehot_columns = ['Source','Topic']
    stdscaler_columns = ['SentimentTitle', 'SentimentHeadline']
    
    enc = OneHotEncoder(sparse=False, handle_unknown = 'ignore') 
    onehot_values = enc.fit_transform(df[onehot_columns])
    onehot_catos = enc.categories_
    idx = 0
    for i in range(len(onehot_columns)):
        column = onehot_columns[i]
        catos = onehot_catos[i]
        for j in range(len(catos)):
            name = column + '_' + catos[j]
            df_encode[name] = onehot_values[:,idx]
            idx += 1
            
    scaler = StandardScaler()
    for i in stdscaler_columns:
        df_encode[i] = scaler.fit_transform(df[[i]])
    return df_encode


def process_ts(df):
    df_norm = df.set_index("IDLink")
    print(df_norm.head())
    df_norm = df_norm.div(df_norm["TS144"],0)
    print(df_norm.head())
    return df_norm


if __name__ == '__main__':
    news_final = get_news_final()
    fb_econ = get_plat_topic()["Facebook_Economy"]
    print(process_news_final(news_final).head())
    print(process_ts(fb_econ).head())


