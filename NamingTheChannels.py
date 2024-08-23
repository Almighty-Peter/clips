import json
import numpy as np
from scipy.spatial.distance import pdist, squareform
import subprocess
import sqlite3
import pandas as pd

import csv
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np
import random
import array
from collections import defaultdict
import os
import subprocess
import string


connection = sqlite3.connect('local_database.db')
cursor = connection.cursor()


cursor.execute("SELECT videoId, start_time, end_time, embedding, caption FROM TKcuts")
tkcuts_rows = cursor.fetchall()
tkCuts = []

for row in tkcuts_rows:
    embedding_blob = row[3]
    embedding_array = array.array('d') 
    embedding_array.frombytes(embedding_blob)
    embedding = embedding_array.tolist()
    tkCuts.append({
        'VSE': [row[0], row[1], row[2]], 
        'Embedding': embedding,
        'Caption': row[4]
    })

tkCuts = pd.DataFrame(tkCuts)
tkCuts.columns = ['VSE', 'Embedding', 'Caption']

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


closestChannel = {name: [] for name in tkChannels['Name']} 

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
    closestChannel[closest_channel].append(cut['Caption'])



captions_combined = {channel: ' '.join(captions) for channel, captions in closestChannel.items()}

from openai import OpenAI

api_key='open ai api key'
client = OpenAI(api_key=api_key)

channel_names = {}
for channel, captions in captions_combined.items():
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
            {"role": "system", "content": "You are a creative expert at naming TikTok channels. Only respond with the channel name and nothing else."},
            {"role": "user", "content": f"Based on the following captions: '{captions}', generate a trending, clickable TikTok channel name."}
        ]
    )
    channel_name = response.choices[0].message.content.strip()
    print(channel_name)  # To confirm the output is correct
    channel_names[channel] = channel_name


for channel, new_name in channel_names.items():
    cursor.execute("UPDATE tkChannel SET Name = ? WHERE Name = ?", (new_name, channel))
    connection.commit()

connection.close()
