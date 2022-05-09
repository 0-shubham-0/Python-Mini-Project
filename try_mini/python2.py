import bs4 as bs
import re
import nltk
import heapq


def summaryText(text):
    article_text = text

    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[\d*]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    sentence_list = nltk.sent_tokenize(article_text)
    # output_sentence = 0
    # output_sentence == len(sentence_list)/2
    # if  percent == 50:

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

    return summary

    # print(len(article_text))
    # print(len(summary))


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

    return summary
    # print(len(article_text))
    # print(len(summary))

# summaryText("WASHINGTON - The Trump administration has ordered the military to start withdrawing roughly 7,000 troops from Afghanistan in the coming months, two defense officials said Thursday, an abrupt shift in the 17-year-old war there and a decision that stunned Afghan officials, who said they had not been briefed on the plans. President Trump made the decision to pull the troops - about half the number the United States has in Afghanistan now - at the same time he decided to pull American forces out of Syria, one official said. The announcement came hours after Jim Mattis, the secretary of defense, said that he would resign from his position at the end of February after disagreeing with the president over his approach to policy in the Middle East. The whirlwind of troop withdrawals and the resignation of Mr. Mattis leave a murky picture for what is next in the United States longest war, and they come as Afghanistan has been troubled by spasms of violence afflicting the capital, Kabul, and other important areas. The United States has also been conducting talks with representatives of the Taliban, in what officials have described as discussions that could lead to formal talks to end the conflict. Senior Afghan officials and Western diplomats in Kabul woke up to the shock of the news on Friday morning, and many of them braced for chaos ahead. Several Afghan officials, often in the loop on security planning and decision-making, said they had received no indication in recent days that the Americans would pull troops out. The fear that Mr. Trump might take impulsive actions, however, often loomed in the background of discussions with the United States, they said. They saw the abrupt decision as a further sign that voices from the ground were lacking in the debate over the war and that with Mr. Mattis resignation, Afghanistan had lost one of the last influential voices in Washington who channeled the reality of the conflict into the White House deliberations. The president long campaigned on bringing troops home, but in 2017, at the request of Mr. Mattis, he begrudgingly pledged an additional 4,000 troops to the Afghan campaign to try to hasten an end to the conflict. Though Pentagon officials have said the influx of forces - coupled with a more aggressive air campaign - was helping the war effort, Afghan forces continued to take nearly unsustainable levels of casualties and lose ground to the Taliban. The renewed American effort in 2017 was the first step in ensuring Afghan forces could become more independent without a set timeline for a withdrawal. But with plans to quickly reduce the number of American troops in the country, it is unclear if the Afghans can hold their own against an increasingly aggressive Taliban. Currently, American airstrikes are at levels not seen since the height of the war, when tens of thousands of American troops were spread throughout the country. That air support, officials say, consists mostly of propping up Afghan troops while they try to hold territory from a resurgent Taliban.")
