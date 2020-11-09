import pandas as pd
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt


def importDataset(pathToDataset):
    dataset={}

    for noiseType in listdir(pathToDataset):

        datasOneNoise={}
        for file in listdir(f"{pathToDataset}/{noiseType}"):
            df=pd.read_csv(f"{pathToDataset}/{noiseType}/{file}",  header=None)
            df.index=["x","y"]

            datasOneNoise[file[0:-4]]=df.T # get rid of the extension


        dataset[noiseType]=datasOneNoise
    return dataset

if __name__ == "__main__":
    pathToDataset = "../dataset"
    dataset= importDataset(pathToDataset)

    #%% accessing the data
    dataset["Noise_1"]["Train_dataset"].plot()
    plt.show()

