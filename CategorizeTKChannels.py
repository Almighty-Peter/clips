import json
import numpy as np
from time import time
from scipy.spatial.distance import pdist, squareform
import subprocess
import sqlite3
import pandas as pd

import csv
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np
from ast import literal_eval
import random
import array
from collections import defaultdict
import os
import subprocess
import string




def remove_closest_points(points, final_count):
    """Remove points based on proximity until only final_count points are left."""
    while len(points) > final_count:

        distances = squareform(pdist(points))
        np.fill_diagonal(distances, np.inf)  
        min_idx = np.unravel_index(np.argmin(distances, axis=None), distances.shape)
        point_to_remove = min_idx[0] if min_idx[0] < min_idx[1] else min_idx[1]
        points = np.delete(points, point_to_remove, axis=0)
    
    return points



connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()


def insert_point(coordinate):
    sql = '''INSERT INTO TkChannel(embedding, name) VALUES(?,?)'''

    cursor.execute(sql, (coordinate,''.join(random.choice(string.ascii_letters) for _ in range(11))))
    connection.commit()


def main(num_points, dimensions, final_count):


    points = np.random.rand(num_points, dimensions)
    remaining_points = remove_closest_points(points, final_count)
    
    
    try:
        sql_drop = 'DROP TABLE IF EXISTS TkChannel;'
        cursor.execute(sql_drop)
    except Exception as e:
        pass


    sql = '''
    CREATE TABLE IF NOT EXISTS TkChannel (
        id INTEGER PRIMARY KEY,
        name TEXT,
        embedding TEXT NOT NULL
    );'''

    cursor.execute(sql)

    for coordinate in remaining_points:
        embedding_bytes = array.array('d', coordinate).tobytes()
        insert_point(embedding_bytes)


dimensions = 3072 
num_points = 500  
final_count = 20 
# remaining_points = main(num_points, dimensions, final_count,)







cursor.execute("SELECT videoId, start_time, end_time, embedding FROM TKcuts")
tkcuts_rows = cursor.fetchall()
tkCuts = []

for row in tkcuts_rows:
    embedding_blob = row[3]
    embedding_array = array.array('d') 
    embedding_array.frombytes(embedding_blob)
    embedding = embedding_array.tolist()
    tkCuts.append({
        'VSE': [row[0], row[1], row[2]], 
        'Embedding': embedding
    })

tkCuts = pd.DataFrame(tkCuts)
tkCuts.columns = ['VSE', 'Embedding']


tkChannels = []
cursor.execute("SELECT name, embedding FROM TkChannel")
tkchannels_rows = cursor.fetchall()

for row in tkchannels_rows:
    embedding_blob = row[1]
    embedding_array = array.array('d') 
    embedding_array.frombytes(embedding_blob)
    embedding = embedding_array.tolist()
    tkChannels.append({
        'Name': row[0], 
        'Embedding': embedding
    })

tkChannels = pd.DataFrame(tkChannels)
tkChannels.columns = ['Name', 'Embedding']

howMany = {name: 0 for name in tkChannels['Name']}  # Initialize counting dictionary

for i, cut in tkCuts.iterrows():
    max_similarity = -1  # Initialize with a low value as cosine similarity ranges from -1 to 1
    closest_channel = None  # To keep track of which channel is closest

    # Extract cut embedding and reshape for cosine similarity computation
    cut_embedding_reshaped = np.array(cut['Embedding']).reshape(1, -1)

    for j, channel in tkChannels.iterrows():
        channel_embedding_reshaped = np.array(channel['Embedding']).reshape(1, -1)
        similarity = cosine_similarity(cut_embedding_reshaped, channel_embedding_reshaped)[0][0]

        # Check if this channel's similarity is greater than the max found so far
        if similarity > max_similarity:
            max_similarity = similarity
            closest_channel = channel['Name']  # Update closest channel

    # After checking all channels for a single cut, update the count for the closest channel
    howMany[closest_channel] += 1
    # if closest_channel == "WXLMayZkFSi":
    #     clipsOutputPath = f"/Users/peternyman/Clips/Clips/YT={cut['VSE'][0]}S={cut['VSE'][1]}E={cut['VSE'][2]}.mp4"
    #     subprocess.run(['open', clipsOutputPath])


# Print the counts for how many times each channel had the closest embedding
for word, count in howMany.items():
    print(f"{word}: --> {count}")
print("\n\n")


connection.close()

