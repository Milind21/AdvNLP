import pandas as pd

#Read the exixting dataframes
augmented_df = pd.read_csv("./augmented_df.csv")
split_df = pd.read_csv("./split_df.csv")
newGPT_df = pd.read_csv("./newGPT_df.csv")


print("----APPENDING PARAPHARSED DATA----")

#Iterate over the augmented_df to get all paraphrased data
for index, row in augmented_df.iterrows():
    if index%2==0:
        continue
    category = row["category"]
    text = row["text"]
    split_df.loc[len(split_df)] = [category, text]

print("\n----APPENDING NEW GPT3 DATA----")

#Iterate over the newGPT_df to get newly generated data
for index, row in newGPT_df.iterrows():
    if index%2==0:
        continue
    category = row["category"]
    text = row["text"]
    split_df.loc[len(split_df)] = [category, text]

split_df.to_csv('./mixed_df.csv', index=False)