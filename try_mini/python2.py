import bs4 as bs
import re
import nltk
import heapq


def summary(file):
# scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Machine_learning')
    scraped_data = open(file, 'r')
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article, 'lxml')
    # parsed_article = bs.BeautifulSoup(article, 'html.parser')
    # print(parsed_article)
    paragraphs = parsed_article.find_all('p')
    # print(paragraphs)
    article_text = ""

    for p in paragraphs:
        article_text += p.text
    # print(article_text)
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[\d*]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    sentence_list = nltk.sent_tokenize(article_text)

    # nltk.download("stopwords")
    stopwords_o = nltk.corpus.stopwords.words('english')
    # print(sentence_list)
    # # print(stopwords_o)

    word_frequencies = {}

    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords_o:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
        maximum_frequncy = max(word_frequencies.values())
    # print(word_frequencies)


    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)
        sentence_scores = {}

    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    print(sentence_scores)

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    # print(summary_sentences)
    summary = ' '.join(summary_sentences)

    print(summary)

    # print(len(article_text))
    # print(len(summary))
