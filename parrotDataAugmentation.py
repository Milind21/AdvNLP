from parrot import Parrot
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from paraphraser import paraphrase

#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

#Read the exixting dataframe df2
df = pd.read_csv("./df.csv")

#Initialise a new dataframe
augmented_df = pd.DataFrame(columns=["category", "text"])

#Iterate over the dataframe df
for index, row in df.iterrows():
    category = row["category"]
    text = row["text"]
    augmented_df.loc[len(augmented_df)] = [category, text]
    phrase = text
    para_phrases = parrot.augment(input_phrase=text,
                                  adequacy_threshold=0.70,
                                  fluency_threshold=0.50)
    sentences = paraphrase(text)
    print(sentences)
    # for para_phrase in para_phrases:
    #     print(para_phrase)
    #     # new_text = para_phrase[0]
    #     # augmented_df.loc[len(augmented_df)] = [category, new_text]
    break

augmented_df.to_csv('./augmented_df.csv', index=False)





#phrases = ["Ceratocystis fimbriata is an ascomycete fungal pathogen. The species as a whole can infect a wide variety of hosts, but particular strains are host-specific."]

#
# for phrase in phrases:
#   print("-"*100)
#   print("Input_phrase: ", phrase)
#   print("-"*100)
#   para_phrases = parrot.augment(input_phrase=phrase,
#                                 diversity_ranker="levenshtein",
#                                 max_return_phrases=4,
#                                 adequacy_threshold=0.90,
#                                 fluency_threshold=0.80)
#   for para_phrase in para_phrases:
#    print(para_phrase[0])