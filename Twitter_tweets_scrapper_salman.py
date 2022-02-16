# -*- coding: utf-8 -*-
import os
import csv
import time
import traceback
import unicodecsv
import uuid
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# target_username = input("Enter Username: ")
# # limit = int(input("Limit: "))

list=['''veve_official''' ]

# CryptoKitties
# TheSandboxGame
# SorareHQ
# CryptoKitties
# TheSandboxGame


for li in list:
	li=li.split('\n')
	for i in li:
		target_username=i.lstrip()
		# print 

		print("Scrapping ==>" +  target_username)

		# print(f"Scrapping ==> {target_username}")


		# def write_column_header(output_file):
		#     path = f"./scrapped_data/{target_username}_{file_name}.csv"
		#     column_header=['Tweets', 'Tweets_date', 'Likes', 'retweets', 'Comments', 'images_url']
		#     with open(path, 'ab') as fp:
		#         row = unicodecsv.writer(fp, delimiter=',',lineterminator='\n')
		#         row.writerow(column_header)

		# method for saving scrapped data in csv file
		def write_output(data, file_name, first_index=False):
			if not os.path.exists("./scrapped_data"):
				os.mkdir("./scrapped_data")

			path = f"./scrapped_data/{target_username}_{file_name}.csv"

			# if first_index:
			#     with open(path, mode="r") as csvFile:
			#         rd = csv.reader(csvFile)
			#         lines = list(rd)
			#         lines.insert(0, data)
			# else:
			with open(path, mode="ab") as csvFile:
				row = unicodecsv.writer(csvFile, delimiter=",", lineterminator="\n")
				row.writerow(data)

		# Initialize Driver
		options = Options()
		# options.add_argument('--headless')
		# options.add_argument('--disable-gpu')
		# driver = webdriver.Chrome('./chromedriver', chrome_options=options)
		driver = webdriver.Chrome('/home/jk/Downloads/chromedriver_linux64/chromedriver')
		driver.get("https://twitter.com")
		time.sleep(60)
		driver.get(f"https://twitter.com/{target_username}")
		driver.maximize_window()
		time.sleep(10)


		# Get Full Name
		full_name_xpath1 = driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-1awozwy r-xoduu5 r-18u37iz r-dnmrzs']")
		full_name_xpath2 = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/span[1]/span")
		full_name = full_name_xpath1 or full_name_xpath2
		full_name = full_name[0].text


		# Get Twitter Handle
		twitter_handle_xpath1 = driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-18u37iz r-1wbh5a2']")
		twitter_handle_xpath2 = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/span")
		twitter_handle = twitter_handle_xpath1 or twitter_handle_xpath2
		twitter_handle = twitter_handle[0].text

		try:
			# Get Location and joined date
			ld_ele = driver.find_elements_by_xpath("//span[@class='css-901oao css-16my406 r-14j79pv r-4qtqp9 r-poiln3 r-1b7u577 r-bcqeeo r-qvutc0']")
			location = ld_ele[0].text
			joined = ld_ele[1].text.replace("Joined ", "")
		except:
			pass


		# Get linked url
		try:
			linked_url_xpath1 = driver.find_elements_by_xpath("//div[@class='css-4rbku5 css-18t94o4 css-901oao css-16my406 r-13gxpu9 r-1loqt21 r-4qtqp9 r-poiln3 r-1b7u577 r-bcqeeo r-qvutc0']")
			linked_url_xpath2 = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/a")
			linked_url = linked_url_xpath1 or linked_url_xpath2
			linked_url = linked_url[0].text
			if "Following" in linked_url:
				linked_url = ''
		except:
			None


		# Get Bio
		bio_xpath1 = driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-1adg3ll r-6gpygo']")
		bio_xpath2 = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]")
		bio = bio_xpath1 or bio_xpath2
		bio = bio[0].text


		# Get Followers and Following
		following_xpath1 = driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-1mf7evn']")
		following_xpath2 = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[1]")
		following = following_xpath1 or following_xpath2
		following = following[0].text.replace(" Following", "")

		followers_xpath1 = driver.find_elements_by_xpath("//a[@class='css-4rbku5 css-18t94o4 css-901oao r-18jsvk2 r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0']")
		followers_xpath2 = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a")
		followers = [followers_xpath1[1]] if followers_xpath1 else followers_xpath2
		followers = followers[0].text.replace(" Followers", "")


		# Save Profile Info
		profile_data = [full_name, twitter_handle, location, followers, following, bio, linked_url]
		# write_output(profile_data, 'profile_info')



		# col_headings = ["Full Name", "Twitter Handle", "Location", "Joined", "Followers", "Following", "Bio", "Linked Url"]
		# write_output(col_headings, 'profile_info', first_index=True)

		# print(
		#     f"""
		#     Name: {full_name}
		#     Handle: {twitter_handle}
		#     Followers: {followers}
		#     Following: {following}
		#     Location: {location}
		#     Joined: {joined}
		#     Linked Url: {linked_url}
		#     Bio: {bio}
		#     """
		# )


		# Get All Tweets
		# scrapped_tweets_captions = []

		scrapped_tweets_captions = set()
		count = 0
		while True:
			try:
				found_new_tweet = False
				tweets = driver.find_elements_by_css_selector('div[class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
				all_tweets = driver.find_elements_by_xpath("//article[@data-testid='tweet']")
				for tweet,actual in zip(all_tweets,tweets):
					tweet_body = tweet.find_elements_by_xpath("./*")[0]
					tweet_date = tweet_body.find_element_by_tag_name("time").text
					try:
						# tweet_text = tweet_body.find_elements_by_class_name("css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")[4].text
						tweet_text = actual.text
					except:
						tweet_text = ''

					# get bottom handle
					bottom_handle = tweet_body.find_elements_by_class_name('css-1dbjc4n')[0].find_elements_by_class_name("css-1dbjc4n.r-18u37iz.r-1h0z5md")

					# if len(bottom_handle) != 4:
					#     continue

					likes = bottom_handle[3].text+' Likes'
					comments = bottom_handle[1].text+' comments'
					retweets = bottom_handle[2].text+' retweets'

					images = tweet_body.find_elements_by_tag_name("img")

					images_list = []
					if images:
						for img in images:
							images_list.append(img.get_attribute("src"))


					if tweet_text not in scrapped_tweets_captions:
						# scrapped_tweets_captions.append(tweet_text)
						scrapped_tweets_captions.add(tweet_text)
						found_new_tweet = True

						# Save tweet Data
						tweet_data = [tweet_text, tweet_date, likes, retweets, comments]
						# write_column_header(path)

						
						write_output(tweet_data, 'tweets_data')

					# print(f"""
					# ==================================
					# Text: {tweet_text}
					# Date: {tweet_date}
					# Likes: {likes}
					# Comments: {comments}
					# Retweets: {retweets}
					# Images: {images_list}
					# ==================================
					# """)
					
				print(f"Tweets Scrapped ==> {len(scrapped_tweets_captions)}")
				# if len(scrapped_tweets_captions) >= limit:
				#     driver.quit()
				#     break

				if not found_new_tweet: #found_new_tweet == False:
					# col_headings = ["Tweet Text", "Date", "Likes", "Comments", "Retweets", "Images"]
					# write_output(col_headings, 'tweets_data', first_index=True)
					count+=1


					driver.execute_script("scroll(0, 0);")
					# driver.refresh()
					time.sleep(1)
					for i in range(6):
						# driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
						driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;")
						time.sleep(2)
					time.sleep(3)

					# time.sleep(2)
					# if count > 100:
					if len(scrapped_tweets_captions) > 2300:
						print("Scrapping Done!")
						break
				else:
					for i in range(3):
						# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;")
						driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
						time.sleep(5)
					time.sleep(5)
			except:
				# tb = traceback.format_exc()
				# print(tb)
				# import pdb;pdb.set_trace()
				continue