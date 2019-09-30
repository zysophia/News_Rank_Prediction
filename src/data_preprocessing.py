import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

news_final = pd.read_csv("data/News_Final.csv")

def get_plat_topic(plats = ['Facebook'], topics = ['Economy', 'Microsoft', 'Obama', 'Palestine']):
    plat_topic_dict = {}
    for p in plats:
        for t in topics:
            name = p + '_' + t
            plat_topic_dict[name] = pd.read_csv(f"data/{name}.csv")
    return plat_topic_dict

def process_news_final(news_final):
    onehot_columns = ['Source','Topic']
    mmscaler_columns = ['age','hours-per-week']


if __name__ == '__main__':
    print(news_final["PublishDate"])
