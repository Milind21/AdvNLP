import pandas as pd

#Read the exixting dataframe df2
df = pd.read_csv("./df.csv")

#Initialise a new dataframe
# split_df = pd.read_csv("./split_df.csv")

split_df = pd.DataFrame(columns=["category", "text"])

#Iterate over the dataframe df
for index, row in df.iterrows():
    # if index <= 1710:
    #     continue
    category = row["category"]
    text = row["text"]
    split_df.loc[len(split_df)] = [category, text]
    split_text_list = text.split(".")
    for split_text in split_text_list:
        if len(split_text) > 10:
            split_df.loc[len(split_df)] = [category, split_text]
    print("{}/{} Done".format(index+1, len(df)))
split_df.to_csv('./split_df.csv', index=False)



