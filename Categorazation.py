import sqlite3
from openai import OpenAI
import csv
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np
from ast import literal_eval
import matplotlib.pyplot as plt
import matplotlib
import random
import array
from collections import defaultdict
import os
import subprocess




# api_key=''
# client = OpenAI(api_key=api_key)

# def get_embedding(text, model="text-embedding-3-large"):
#    text = text.replace("\n", " ")
#    return client.embeddings.create(input = [text], model=model).data[0].embedding

# words = ["Apparel & Accessories","Baby, Kids & Maternity","Beauty & Personal Care","Business Services","Education","Financial Services","Food & Beverage","Games","Health","Home Improvement","Household Products","Life Services","News & Entertainment","Pets","Sports & Outdoor","Tech & Electronics","Travel","Vehicle & Transportation"]

# with open('/Users/peternyman/Clips/word_embedding.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Word', 'Embedding'])
#     for word in words:
#         print(word)
#         embedding = get_embedding(word) 
#         writer.writerow([word, embedding])


connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()


results = []


cursor.execute("SELECT videoId, start_time, end_time, embedding FROM TKcuts")
tkcuts_rows = cursor.fetchall()


for row in tkcuts_rows:
    videoID = row[0]
    start_time = row[1]
    end_time = row[2]
    embedding_blob = row[3]

    embedding_array = array.array('d')
    embedding_array.frombytes(embedding_blob)


    embedding = embedding_array.tolist()

    cursor.execute("SELECT title FROM YTVideos WHERE video_id = ?", (videoID,))
    title_row = cursor.fetchone()
    
    if title_row:  
        title = title_row[0]

        results.append([title, embedding,[videoID,start_time,end_time]])


connection.close()


def parse_embeddings(embedding_str):
    return np.array(eval(embedding_str))

datafile_path = "/Users/peternyman/Clips/word_embedding.csv"
df1 = pd.read_csv(datafile_path)
df1['Embedding'] = df1['Embedding'].apply(parse_embeddings)
df2 = pd.DataFrame(results, columns=['Word', 'Embedding','VSE'])
pd.set_option('display.max_rows', None)  













embeddings1 = np.vstack(df1['Embedding'])
words1 = df1['Word'].values
embeddings2 = np.vstack(df2['Embedding'])
words2 = df2['Word'].values



closest_words = []
howMany = {}
for x in words1:
    howMany[x] = 0

for i, embedding2 in enumerate(embeddings2):
    similarities = cosine_similarity([embedding2], embeddings1)[0]
    # Find the index of the closest word
    closest_index = np.argmax(similarities)
    closest_word = words1[closest_index]
    closest_words.append((words2[i], closest_word))
    howMany[closest_word] += 1

results_df = pd.DataFrame(closest_words, columns=['Word in df2', 'Closest Word in df1'])
print(results_df)
print(10*"\n")
for words in list(howMany.keys()):
    print(f"{words}: --> {howMany[words]}")






numPerGroup = 8
num_clusters = len(df2) // numPerGroup


kmeans = KMeans(n_clusters=num_clusters, random_state=random.randint(1,42))
kmeans.fit(df2['Embedding'].to_list())

clusters = kmeans.labels_



cluster_groups = defaultdict(list)

for i, cluster_id in enumerate(kmeans.labels_):
    cluster_groups[cluster_id].append([df2['Embedding'].to_list()[i],df2['VSE'].to_list()[i]])



final_groups = []

for cluster_id, group in cluster_groups.items():
    for i in range(0, len(group), numPerGroup):
        chunk = group[i:i + numPerGroup]
        final_groups.append(chunk)



for idx, group in enumerate(final_groups):
    print(f"idx: {idx}")
    print(len(group))
for vse in [x[1] for x in final_groups[random.randint(0,len(final_groups))]]:
    clipsOutputPath = f"/Users/peternyman/Clips/Clips/YT={vse[0]}S={vse[1]}E={vse[2]}.mp4"
    subprocess.run(['open', clipsOutputPath], check=True)


# df = pd.concat([df1, df2], ignore_index=True)
# words = df['Word'].tolist()
# matrix = np.array(df.Embedding.apply(literal_eval).to_list())


# tsne = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)
# print(tsne)
# vis_dims = tsne.fit_transform(matrix)


# x = [x for x,y in vis_dims]
# y = [y for x,y in vis_dims]


# plt.scatter(x, y, alpha=0.3)
# for i, label in enumerate(words):
#     plt.annotate(label, (x[i], y[i]))

# plt.show()



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# connection = sqlite3.connect('local_database.db')
# cursor = connection.cursor()


# results = []



# cursor.execute("SELECT videoId, start_time, end_time, embedding FROM TKcuts")
# tkcuts_rows = cursor.fetchall()


# for row in tkcuts_rows:
#     videoID = row[0]
#     start_time = row[1]
#     end_time = row[2]
#     embedding_blob = row[3]

#     embedding_array = array.array('d')
#     embedding_array.frombytes(embedding_blob)


#     embedding = embedding_array.tolist()

#     cursor.execute("SELECT title FROM YTVideos WHERE video_id = ?", (videoID,))
#     title_row = cursor.fetchone()
    
#     if title_row:  
#         title = title_row[0]

#         results.append([[videoID,start_time,end_time], embedding])
        


# connection.close()
# results = results[:10]

# groupsOf = 2

# distance = defaultdict(dict)

# for i in results:
#     for j in results:
#         if i[0] != j[0]:
#             j_key = tuple(j[0])
#             i_key = tuple(i[0])
            
#             if j_key in distance and i_key in distance[j_key]:
#                 pass
#             else:
#                 distance[i_key][j_key] = cosine_similarity((np.array(i[1]).reshape(1, -1)),np.array(j[1]).reshape(1, -1))[0][0]
        

# all_combinations = list(combinations([x[0] for x in results] , groupsOf))
# allCombinationsDistence = {}
# lengg = len(all_combinations)
# for xi, combo in enumerate(all_combinations):
#     print(lengg,xi)
#     totalDistance = 0
#     for r,i in enumerate(combo):
#         for j in combo[r+1:]:
#             j_key = tuple(j)
#             i_key = tuple(i)

#             totalDistance += distance[i_key][j_key] 

#     allCombinationsDistence[tuple(map(tuple, combo))] = totalDistance


# maxTotalDistance = [0]

# lengg = comb(len(all_combinations), len(results) // groupsOf)
# for xi, combs in enumerate(combinations(all_combinations, len(results)//groupsOf)):
#     print(lengg,xi)
#     totalDistance = 0
#     usedElements = []
#     valid = True
    
#     for comb in combs:

#         for element in comb:
#             if element not in usedElements:
#                 usedElements.append(element)
#             else:
#                 valid = False
#                 break
    
#     if valid:
#         for comb in combs:
#             totalDistance += allCombinationsDistence[tuple(map(tuple, combo))]
#         if maxTotalDistance[0] < totalDistance:
#             maxTotalDistance = [totalDistance,combs]
#         print(combs)

# print(maxTotalDistance)





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# l = ["a", "b", "c", "d", "e", "f", "g", "h"]
# groupsOf = 2

# distance = defaultdict(dict)



# for i in l:
#     for j in l:
#         if i != j:
#             if j in distance and i in distance[j]:
#                 pass
#             else:
#                 distance[i][j] = random.random()  
        

# all_combinations = list(combinations(l, groupsOf))
# allCombinationsDistence = {}
# for combo in all_combinations:
#     totalDistance = 0
#     for r,i in enumerate(combo):
#         for j in combo[r+1:]:
#             totalDistance += distance[i][j] 

#     allCombinationsDistence[combo] = totalDistance


# maxTotalDistance = [0]
# for combs in combinations(all_combinations, len(l)//groupsOf):
#     totalDistance = 0
#     usedElements = []
#     valid = True
    
#     for comb in combs:

#         for element in comb:
#             if element not in usedElements:
#                 usedElements.append(element)
#             else:
#                 valid = False
#                 break
    
#     if valid:
#         for comb in combs:
#             totalDistance += allCombinationsDistence[comb]
#         if maxTotalDistance[0] < totalDistance:
#             maxTotalDistance = [totalDistance,combs]
#         print(combs)

# print(maxTotalDistance)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


