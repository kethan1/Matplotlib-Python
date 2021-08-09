import matplotlib.pyplot as plt

topic_percentages = list(map(int, input('Enter the topic amounts for general news, finance, sports, movies: ').split(', ')))
topics_list = ['general news', 'finance', 'sports', 'movies']
colorlist = ['green', 'blue', 'red', 'yellow']
plt.pie(
    topic_percentages, labels=topics_list, colors=colorlist, startangle=90,
    shadow=True, explode=(0, 0.1, 0, 0), autopct="%1.1f%%"
)
plt.show()
