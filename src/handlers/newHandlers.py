__author__ = 'ksotala'

from base_handler import *
from random import sample
import datetime

class TopicHandler(BaseHandler):
    def get(self):
        self.application.form_new_keywords_information()
        self.application.analyzer.reset_current()
        # defines the number of the keywords received by the front end
        self.topics_no = 10
        self.topics = sample(self.application.keywords_set, self.topics_no)

        self.message_list = []

        for i in range(0, len(self.topics)):
            keyword_list = (self.application.corpus_keywords[self.topics[i]]).split()
            keyword_dict_list = []
            for j in range(0, len(keyword_list)):
                newdict = {"label": keyword_list[j], "weight": 0.2}
                keyword_dict_list.append(newdict)
            dict = {"id": self.topics[i],
                  "keywords": keyword_dict_list,
                  "weight": 0.1,
                }
            self.message_list.append(dict)

        self.message = {"topics": self.message_list}

        print self.message
        self.json_ok(self.message)

    def post(self):
        pass

class TopicArticleHandler(BaseHandler):
    def get(self, key):
        message_list = []

        for i in range(0,5):
            message_list.append({
                "title": 'Lorem',
                "authors": 'Lorem, Ipsum, Dolor',
                "abstract": 'Lorem ipsum',
                "weight": 0.5
            })

        message = {"articles": message_list}

        print message
        self.json_ok(message)

    def post(self):
        pass


class FeedbackHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        def sort_keywords(scores):
            """Sorts the keywords according to their scores. Will also filter out the keywords contained in
            the already experienced keywords.

            @params scores: scores of the keywords, the order is the same as in self.application keywords
            @return: sorted keyword pairs
            """

            # sort keywords according to their scores
            combined_pairs = zip(scores, self.application.keywords_info)
            # print self.application.experienced_keywords
            # filter out the keyword info if keyword's text is in experienced_keywords
            combined_pairs = filter(lambda x: x[1]["text"] not in self.application.experienced_keywords, combined_pairs)

            sorted_pair = zip(*sorted(combined_pairs))
            return sorted_pair[1]

        def update_keywords_info(scores):
            """Update information stored in the self.application.keywords_info

            @params Scores is a list of tuples. First element of tuple stores exploitation rate of the keyword.
                    Second element of tuple stores exploration rate of the keyword.
            """
            for i in xrange(len(self.application.keywords_info)):
                self.application.keywords_info[i]["exploitation"] = scores[i][0]
                self.application.keywords_info[i]["exploration"] = scores[i][1]

        # add experienced word, this word will not appear any in selection process
        self.application.experienced_keywords.extend([keyword["text"] for keyword in self.application.keywords])

        # load the data from the front end
        data = json.loads(self.request.body)

        # keywords info consists a list of tuples. It stores name of keyword and weight of keyword
        keywords_info = [(keyword["text"], keyword["weight"]) for keyword in data["topics"]]
        # Decompose the keywords_info array to two arrays.
        # One of them contains keywords, another of them contains weights of keywords
        keywords, weights = zip(*keywords_info)
        # increase the iteration number
        self.application.iter_num += 1

        # get scores of all the keywords ordered in list order
        before = datetime.datetime.now()
        scores = self.application.analyzer.analyze(keywords, self.application.corpora, weights)
        after = datetime.datetime.now()
        print "Time Consumption of Function Analyzer: ", after - before
        scores_sum = [sum(score) for score in scores]

        # update information if self.application.keywords_info
        update_keywords_info(scores)
        self.application.ranked_keywords = sort_keywords(scores_sum)

        # get the keywords that has highest score.
        self.application.keywords = (self.application.ranked_keywords[-self.application.keywords_number:])[::-1]

        # sort the persons
        keywords_id = [keyword["id"] for keyword in self.application.keywords]

        def sort_persons(person):
            return len(set(person["keywords"]) & set(keywords_id))

        persons_info = self.application.corpora_user_id.values()
        persons = sorted(persons_info, key=sort_persons, reverse=True)

        self.topics = [keyword for keyword in self.application.keywords]
        self.message_list = []

        for i in range(0, len(self.topics)):
            keyword_list = (self.application.corpus_keywords[self.topics[i]]).split()
            keyword_dict_list = []
            for j in range(0, len(keyword_list)):
                newdict = {"label": keyword_list[j], "weight": 0.2}
                keyword_dict_list.append(newdict)
            dict = {"id": self.topics[i],
                  "keywords": keyword_dict_list,
                  "weight": 0.1,
                }
            self.message_list.append(dict)

        self.message = {"topics": self.message_list}

        print self.message
        self.json_ok(self.message)



