from textattack.augmentation import WordNetAugmenter
from textattack.augmentation import EmbeddingAugmenter
from textattack.augmentation import EasyDataAugmenter
from textattack.augmentation import CharSwapAugmenter
from textattack.augmentation import CheckListAugmenter
from textattack.augmentation import CLAREAugmenter

#The orignal text to be modified
text = "Ceratocystis fimbriata is an ascomycete fungal pathogen. The species as a whole can infect a wide variety of hosts, but particular strains are host-specific. One example is the Ipomoea form of the fungus, which is specific to sweet potato (Ipomea batatas) and wild morning glory. Symptoms can be found on the fleshy root or visible in plants. On sweet potato, Ceratocystis fimbriata causes a disease called 'black rot,' which displays firm and dry circular brown/black rots. Infected plants often show stunted growth, wilting, and yellowing. Wilting occurs because this pathogen can also travel through xylem and infect vascular system. During disease, white, fuzzy mycelia with long black perithecia grow out from the lesions. Additionally, research demonstrates that sweet potatoes infected with C. fimbriata demonstrate increased respiration which is partially due to the infection's influence on protein metabolism. Higher respiration rates cause dry weight loss in the tubers which poses a problem for marketability."
print("Orignal Text --> ", text)

#Wordnet augments text by replacing words with synonyms provided by WordNet.
wordnet_aug = WordNetAugmenter()
wordnet_aug_text = wordnet_aug.augment(text)
print("Word Net Augmentation --> ", wordnet_aug_text)

#Embedding augments text by replacing words with neighbors in the counter-fitted embedding space,
# with a constraint to ensure their cosine similarity is at least 0.8.
embed_aug = EmbeddingAugmenter()
embed_aug_text = embed_aug.augment(text)
print("Embedded Augmentation --> ", embed_aug_text)

#EDA augments text with a combination of word insertions, substitutions, and deletions.
eda_aug = EasyDataAugmenter()
eda_aug_text = eda_aug.augment(text)
print("EDA Augmentation --> ", eda_aug_text)

#It augments text by substituting, deleting, inserting, and swapping adjacent characters
char_aug = CharSwapAugmenter()
char_aug_text = char_aug.augment(text)
print("Char Swap Augmentation --> ", char_aug_text)

#It augments text by contraction/extension and by substituting names, locations and numbers.
check_aug = CheckListAugmenter()
check_aug_text = check_aug.augment(text)
print("Check List Augmentation --> ", check_aug_text)

#It augments text by replacing, inserting, and merging with a pre-trained masked language model.
# clare_aug = CLAREAugmenter()
# clare_aug_text = clare_aug.augment(text)
# print("Clare Augmentation --> ", clare_aug_text)



from textattack.augmentation import WordNetAugmenter
from textattack.augmentation import EmbeddingAugmenter
from textattack.augmentation import EasyDataAugmenter
from textattack.augmentation import CharSwapAugmenter
from textattack.augmentation import CheckListAugmenter
from textattack.augmentation import CLAREAugmenter


#The orignal text to be modified
text = "Ceratocystis fimbriata is an ascomycete fungal pathogen. The species as a whole can infect a wide variety of hosts, but particular strains are host-specific. One example is the Ipomoea form of the fungus, which is specific to sweet potato (Ipomea batatas) and wild morning glory. Symptoms can be found on the fleshy root or visible in plants. On sweet potato, Ceratocystis fimbriata causes a disease called 'black rot,' which displays firm and dry circular brown/black rots. Infected plants often show stunted growth, wilting, and yellowing. Wilting occurs because this pathogen can also travel through xylem and infect vascular system. During disease, white, fuzzy mycelia with long black perithecia grow out from the lesions. Additionally, research demonstrates that sweet potatoes infected with C. fimbriata demonstrate increased respiration which is partially due to the infection's influence on protein metabolism. Higher respiration rates cause dry weight loss in the tubers which poses a problem for marketability."
print("Orignal Text --> ", text)

#Wordnet augments text by replacing words with synonyms provided by WordNet.
wordnet_aug = WordNetAugmenter()
wordnet_aug_text = wordnet_aug.augment(text)
print("Word Net Augmentation --> ", wordnet_aug_text)

#Embedding augments text by replacing words with neighbors in the counter-fitted embedding space,
# with a constraint to ensure their cosine similarity is at least 0.8.
embed_aug = EmbeddingAugmenter()
embed_aug_text = embed_aug.augment(text)
print("Embedded Augmentation --> ", embed_aug_text)

#EDA augments text with a combination of word insertions, substitutions, and deletions.
eda_aug = EasyDataAugmenter()
eda_aug_text = eda_aug.augment(text)
print("EDA Augmentation --> ", eda_aug_text)

#It augments text by substituting, deleting, inserting, and swapping adjacent characters
char_aug = CharSwapAugmenter()
char_aug_text = char_aug.augment(text)
print("Char Swap Augmentation --> ", char_aug_text)

#It augments text by contraction/extension and by substituting names, locations and numbers.
check_aug = CheckListAugmenter()
check_aug_text = check_aug.augment(text)
print("Check List Augmentation --> ", check_aug_text)

#It augments text by replacing, inserting, and merging with a pre-trained masked language model.
# clare_aug = CLAREAugmenter()
# clare_aug_text = clare_aug.augment(text)
# print("Clare Augmentation --> ", clare_aug_text)



