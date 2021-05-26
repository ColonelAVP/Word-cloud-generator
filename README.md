# Word-cloud-generator
## Introduction
In this project, you'll be making a word cloud generator using dataset.
A word cloud is a visual representation of text data. Words are usually single words, and the importance of each is shown with font size or color. Python fortunately has a wordcloud library allowing to build them.

>Concept used:
* Visual Representation

>Tools and technology used:
* Python
* Matplotlib 
* WordCloud
* numpy
* Pillow

>Installation Guide
``pip install matplotlib``
``pip install wordcloud``
``pip install numpy``
``pip install Pillow``

## Steps
```Python
Step1: Import Required libraries
Step2: Generate Data for wordcloud
Step3: Clean Data 
      - Use stopwords to remove words like 'is','but','and',etc
      - Remove spaces as well
Step4: write function to plot wordcloud using matplotlib  
Step5: Import a shaped image to np array
Step6: Generate wordcloud using WordCloud. Add features such as;
      - width
      - height 
      - background color
      - contour color
      - mask
      - collocations
Step7: Plot the Wordcloud
Step8: Save Image
```
>Note 

You can used any dataset consisting of words or numbers.
To get accurate shape use large datasets like lyrics of songs or wikipedia paragraphs.
I have used a song by Eminem as [Dataset](https://github.com/ColonelAVP/Word-cloud-generator/blob/master/Dataset.txt).
You can use that as well. 
Also You can generate data directly by importing wikipedia and then scraping from wikipedia page.
Use png format images.

I have provided sample images for masks. Click [sample masks](https://github.com/ColonelAVP/Word-cloud-generator/tree/master/Sample)

## Reference
* [Word-cloud-generator](https://towardsdatascience.com/simple-wordcloud-in-python-2ae54a9f58e5)
* [Word Cloud Docs](https://github.com/ColonelAVP/Word-cloud-generator/blob/master/wordcloud.py)

## Contributions
Contributions are always welcomed. Make sure you check [Contribution info](https://github.com/ColonelAVP/Word-cloud-generator/blob/master/Contribution.md) before making pull requests.

## Screenshots
>***Word-cloud of a Upvote***

![alt tag](https://user-images.githubusercontent.com/78366601/119533464-7da1b280-bda3-11eb-8f97-52fa1fb6f0ca.png)

>***Word-cloud of Donald Trump***

![alt_tag](https://user-images.githubusercontent.com/78366601/119533463-7d091c00-bda3-11eb-8741-a57ef774d841.png)

>***Word-cloud of James Bond***

![alt tag](https://user-images.githubusercontent.com/78366601/119533460-7bd7ef00-bda3-11eb-950d-86c66dbf33e2.png)





