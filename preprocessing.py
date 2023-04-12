import torch
import numpy as np
from transformers import BertTokenizer
import pandas as pd

#initialise a dataframe
df = pd.DataFrame(columns=["category", "text"])
labels = {} #this dictionary contains all labels and their associated index {"index1":0, "index2":1, ...}

#This open the dataset.txt file and stores all the data in the form of a list of strings (corpus)
with open('dataset_PName.txt', 'r') as file:
    corpus = file.read()
    corpus = corpus.split("\n")

#This loop iterates on each item in the list, and appends the data into the dataframe
for i, record in enumerate(corpus):
    data = record.split('\t') #Split to get label and its associated text
    category = data[-1].strip()
    text = data[0].strip()
    if len(category) > 0 and len(text) > 0:
        df.loc[len(df)] = [category, text] #Insert the record into the dataframe
        labels[category] = i

#Uncomment to see the generated df.
print(df)

#The BERT tokenizer used for tokenization.
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

#The dataset class that needs to be used further for training the data
class Dataset(torch.utils.data.Dataset):
    def __init__(self, df):
        self.labels = [labels[label] for label in df['category']]
        self.texts = [tokenizer(text, padding='max_length', max_length=512, truncation=True,
                                return_tensors="pt") for text in df['text']]

    def classes(self):
        return self.labels

    def __len__(self):
        return len(self.labels)

    def get_batch_labels(self, idx):
        # Fetch a batch of labels
        return np.array(self.labels[idx])

    def get_batch_texts(self, idx):
        # Fetch a batch of inputs
        return self.texts[idx]

    def __getitem__(self, idx):
        batch_texts = self.get_batch_texts(idx)
        batch_y = self.get_batch_labels(idx)
        return batch_texts, batch_y

#Code to split the data for training and validation
df_train, df_val, df_test = np.split(df.sample(frac=1, random_state=42),
                                     [int(.8*len(df)), int(.9*len(df))])
print(len(df_train), len(df_val), len(df_test))
df_train.to_csv("./train2.csv")
df_test.to_csv("./val2.csv")
df_val.to_csv("./test2.csv")
df.to_csv("./df2.csv")
print(len(df))