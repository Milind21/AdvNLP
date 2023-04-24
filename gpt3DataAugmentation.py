import pandas as pd
import openai
openai.api_key = "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"
model_engine = "text-davinci-003"

# Set the maximum number of tokens to generate in the response
max_tokens = 2048

#Read the exixting dataframe df2
df = pd.read_csv("./df.csv")

#Initialise a new dataframe
augmented_df = pd.read_csv("./augmented_df.csv")

#Iterate over the dataframe df
for index, row in df.iterrows():
    if index <= 1710:
        continue
    category = row["category"]
    text = row["text"]
    prompt = "paraphrase the paragraph and give results. Do not shorten the paragraph. Paragraph is as follows : {}".format(text)
    augmented_df.loc[len(augmented_df)] = [category, text]
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    new_text = completion.choices[0].text
    new_text = new_text.replace("\n","")
    augmented_df.loc[len(augmented_df)] = [category, new_text]
    print("{}/{} Done".format(index+1, len(df)))
    augmented_df.to_csv('./augmented_df.csv', index=False)



