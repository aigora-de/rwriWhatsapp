from typing import Set, Any, List

import pandas as pd
from whatsapp_chat_parser import get_messages
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import ngrams, FreqDist
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


class WhatsAppParser:
    """
    A class that uses whatsapp_chat_parser to parse _chat.txt (WhatsApp export) into
    'author', 'message', and 'timestamp'.
    """

    @staticmethod
    def run():
        messages = get_messages("../data/_chat.txt")
        for message in messages["chats"]:
            print(message["author"])
            print(message["message"])
            print(message["timestamp"])

        for descriptive_message in messages["descriptive_messages"]:
            print(descriptive_message)

        df = pd.DataFrame(messages['chats'])
        df_by_author = df.groupby("author")
        df_by_author.size().sort_values(ascending=False).plot(kind='bar', use_index=False, logy=False, xticks=None)
        plt.xticks([])
        plt.show()
        df_by_author.size().sort_values(ascending=False)[0:50].plot(kind='bar', use_index=True, logy=False)
        plt.show()

        df_raphael = df[df['author'] == 'Arie Harza']
        df_raphael.head()

        cloud_words = RWRIWordCloud().get_word_cloud(df_raphael['message'])
        text = df['message'].str.cat(sep=' ')
        word_cloud = WordCloud(max_words=200).generate(text=cloud_words)
        # Display the generated image:
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

        WhatsAppParser().ngram_frequency(cloud_words)

    def ngram_frequency(self, words: List[str]):
        """

        :param words:
        :return:
        """
        all_counts = dict()
        for size in 1, 2, 3, 4, 5:
            all_counts[size] = FreqDist(ngrams(words, size))
        top_50_words = all_counts[1].most_common(50)
        #word_cloud_1_50 = WordCloud.generate_from_frequencies(top_50_words)
        top_50_bigrams = all_counts[2].most_common(50)


class RWRIWordCloud:
    """
    Generate a word cloud from the message content of a WhatsApp chat.
    """
    # stop_words is a static attribute shared by all instances of the class.
    stop_words: Set[Any] = set(stopwords.words('english'))
    stop_words.add('Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.')

    def get_word_cloud(self, messages: pd.Series) -> list:
        """
        Generate a word cloud.
        :rtype: list
        :param messages: a pandas Series object containing string items.
        :return: a word cloud object.
        """
        # Concatenate the Series containing messages into a single large string.
        cloud_input = messages.str.cat(sep=' ')
        words = cloud_input.split()
        cloud_words = []
        for word in words:
            if not word in self.stop_words:
                cloud_words.append(word)
        #print(cloud_words)
        return ' '.join(cloud_words)
