import os
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from data.model_settings import cols_labels, frequence, intervalle, pourcentage_max, LP_filter


def recover_file():
    path = "Trials"
    file = os.listdir(path)
    if len(file) < 1:
        print("Aucun enregistrement à prédire")
    else:
        return file[len(file) - 1]


class Prediction:

    def __init__(self, model):
        self.model = model
        self.file = recover_file()

    def formatFile(self):
        new_shot_data = pd.read_csv(f"Trials/{self.file}", skiprows=range(0,1), usecols=range(8, 14))
        new_shot_data.columns = ["AccX", "AccY", "AccZ", "GyrX", "GyrY", "GyrZ"]
        new_shot_data = new_shot_data.dropna()
        maxX = np.max(new_shot_data["AccX"])
        seuil_max = maxX * pourcentage_max / 100
        AccX_peaks = find_peaks(new_shot_data["AccX"], height=seuil_max, distance=40)
        print(AccX_peaks[0])

    def predict(self):
        pass
