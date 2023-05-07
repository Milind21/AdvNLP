import pandas as pd

#Read the exixting dataframes
augmented_df = pd.read_csv("./augmented_df.csv")
newGPT_df = pd.read_csv("./newGPT_df.csv")

print("\n----APPENDING NEW GPT3 DATA----")

#Iterate over the newGPT_df to get newly generated data
for index, row in newGPT_df.iterrows():
    if index%2==0:
        continue
    category = row["category"]
    text = row["text"]
    augmented_df.loc[len(augmented_df)] = [category, text]

augmented_df.to_csv('./true_df.csv', index=False)