from collect import crawler
from analysis import analizer
from visualize import visualize

pagename = "jtbcnews"
from_date = "2018-05-21"
to_date = "2018-05-23"

if __name__ == "__main__":
    # 수집
    postList = crawler.fb_get_post_list(pagename, from_date, to_date)
    print(postList)

    # 분석
    dataString = analizer.json_to_str("D:/javaStudy/facebook/jtbcnews.json", "message_str")
    count_data = analizer.count_wordfreq(dataString)
    print(count_data)
    dictWords = dict(count_data)

    # 그래프
    # 시각화
    # 데이타 가공
    dictWords = dict(count_data.most_common(30))
    # 막대그래프
    visualize.show_graph_bar(dictWords)

    # 워드 클라우드
    visualize.wordcloud(dictWords, pagename)