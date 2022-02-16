import snscrape.modules.twitter as sntwitter
import pandas as pd


tweets_list2 = []

# text='Is Xanalia secure since:2020-01-01 until:2021-05-31'
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Metaverse since:2018-01-01 until:2021-01-31').get_items()):
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Metaverse').get_items()):
    if i>1000:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content])
    
                                                                      
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text'])
tweets_df2.to_csv('metaverse_tweets-2.csv', index=False,)


# snscrape --max-results 100 twitter-hashtag Metaverse

# You ought to acquire MetaMask. 
# # Wait until Ultraman NFT drops.
   
   