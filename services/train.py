import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import joblib

from config.env_variables import settings
from config.database import engine
from config.jre_utils import clean_text


class TrainJobRecommendationModel:
    nbrs = NearestNeighbors(n_neighbors=1)
    vectorizer = TfidfVectorizer()

    def __init__(self, config=settings, db_engine=engine):
        self.job_df = None
        self.job_id = None
        self.tfidf = None
        self.model = None
        self.config = settings
        self.db_engine = db_engine
        self.model_path = None

    def load_data(self):
        self.job_df = pd.read_sql("SELECT * FROM job_table", con=self.db_engine)
        self.job_id = list(self.job_df["job_id"])

    def pre_process(self):
        self.job_df["ProcessedText"] = self.job_df['job_title'] + " " + \
                                       self.job_df['industry'] + " " + self.job_df['sector'] + \
                                       self.job_df['location'] + " " + self.job_df['job_description']

        self.job_df["ProcessedText"].apply(clean_text)

    def train(self):
        self.tfidf = self.vectorizer.fit_transform(self.job_df["ProcessedText"])
        self.model = self.nbrs.fit(self.tfidf)

    def save_model(self):
        # filepath = os.path.dirname(settings.model_path)
        joblib.dump([self.job_id, self.vectorizer, self.model], settings.model_path, compress=1)
        # print(os.path.join(filepath, "jre_model.joblib"))

    def begin(self):
        self.load_data()
        self.pre_process()
        self.train()
        self.save_model()


a = TrainJobRecommendationModel()
a.begin()
print("Success!")
