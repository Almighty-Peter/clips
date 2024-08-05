
from openai import OpenAI
import csv
import pandas as pd
from sklearn.manifold import TSNE
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
import matplotlib.pyplot as plt
import matplotlib
import random


api_key='open ai key'
client = OpenAI(api_key=api_key)

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding









# words = ["Apparel & Accessories","Baby, Kids & Maternity","Beauty & Personal Care","Business Services","Education","Financial Services","Food & Beverage","Games","Health","Home Improvement","Household Products","Life Services","News & Entertainment","Pets","Sports & Outdoor","Tech & Electronics","Travel","Vehicle & Transportation"]

words = ["New VW Golf GTI review *EXCLUSIVE*", "600hp GR Yaris v Lambo Aventador SV: DRAG RACE", "Need For Speed 2014 full movie"]
# words = ["5 Self-Care tips that ACTUALLY work", "Assisting with Personal Care and Hygiene", "The Best & Worst Personal Care Products!","I Ate The World's Best Pizza" ]

with open('/Users/peternyman/Clips/word_embedding_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Word', 'Embedding'])
    # Write the word and vector
    for word in words:
        print(word)
        embedding = get_embedding(word) 
        writer.writerow([word, embedding])



datafile_path = "/Users/peternyman/Clips/word_embedding.csv"
df1 = pd.read_csv(datafile_path)

datafile_path = "/Users/peternyman/Clips/word_embedding_test.csv"
df2 = pd.read_csv(datafile_path)



# vector1 = np.array([[3, 2]])
# vector2 = np.array([[6, 4]])

# similarity = cosine_similarity(vector1, vector2)

# # Display the result
# print(similarity)


def parse_embeddings(embedding_str):
    # Convert the string representation of the list to a numpy array
    return np.array(eval(embedding_str))

# Apply the function to convert embeddings
df1['Embedding'] = df1['Embedding'].apply(parse_embeddings)
df2['Embedding'] = df2['Embedding'].apply(parse_embeddings)

# Extract embeddings and words
embeddings1 = np.vstack(df1['Embedding'])
words1 = df1['Word'].values
embeddings2 = np.vstack(df2['Embedding'])
words2 = df2['Word'].values

# Find closest words
closest_words = []

for i, embedding2 in enumerate(embeddings2):
    # Compute cosine similarity
    similarities = cosine_similarity([embedding2], embeddings1)[0]
    # Find the index of the closest word
    closest_index = np.argmax(similarities)
    closest_word = words1[closest_index]
    closest_words.append((words2[i], closest_word))

# Create a DataFrame with results
results_df = pd.DataFrame(closest_words, columns=['Word in df2', 'Closest Word in df1'])

# Display the results
print(results_df)



# df = pd.concat([df1, df2], ignore_index=True)
# words = df['Word'].tolist()
# # Convert to a list of lists of floats
# matrix = np.array(df.Embedding.apply(literal_eval).to_list())

# # Create a t-SNE model and transform the data
# tsne = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)
# print(tsne)
# vis_dims = tsne.fit_transform(matrix)


# x = [x for x,y in vis_dims]
# y = [y for x,y in vis_dims]


# plt.scatter(x, y, alpha=0.3)
# for i, label in enumerate(words):
#     plt.annotate(label, (x[i], y[i]))

# plt.show()





