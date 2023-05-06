import pandas as pd
import openai
import time
# openai.api_key = "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"
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

# Set the maximum number of tokens to generate in the response
max_tokens = 2000

#Read the exixting dataframe df2
df = pd.read_csv("./df.csv")

#Initialise a new dataframe
newGPT3_df = pd.read_csv("./newGPT_df.csv")

#Iterate over the dataframe df
for index, row in df.iterrows():
    if index <= 1427:
        continue
    category = row["category"]
    text = row["text"]
    prompt = "Can you provide some details about the signs & symptoms of the following plant disease: {}. Provide details in a parapgraph.".format(category)
    newGPT3_df.loc[len(newGPT3_df)] = [category, text]
    # Generate a response
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    new_text = completion.choices[0].message.content
    print(new_text)
    new_text = new_text.replace("\n","")
    newGPT3_df.loc[len(newGPT3_df)] = [category, new_text]
    print("{}/{} Done".format(index+1, len(df)))
    newGPT3_df.to_csv('./newGPT_df.csv', index=False)
    time.sleep(18)
