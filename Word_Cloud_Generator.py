# Word Cloud generator in Python

# A Import libraries
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# B Generating data and cleaning it
dataset = open("Dataset.txt", "r").read()
comment_words = ''
stopwords = set(STOPWORDS)
# Iterate through the txt file
for val in dataset:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens) + " "

# C fn to plot wordcloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    plt.axis("off");

# D Import image to np array
mask = np.array(Image.open('upvote.png'))

# E generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='viridis',contour_width=5,contour_color='black', collocations=False, stopwords = STOPWORDS, mask=mask).generate(dataset)

# F plot
plot_cloud(wordcloud)

# G Save image
wordcloud.to_file("wordcloud11.png")
