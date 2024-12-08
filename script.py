from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINKS =  [
"https://adstransparency.google.com/advertiser/AR09120629959503642625/creative/CR12111454848667353089?political=&region=US",
"https://www.google.com/", # used to test a failing case
"https://adstransparency.google.com/advertiser/AR09120629959503642625/creative/CR08341379010604826625?political=&region=US",
"https://adstransparency.google.com/advertiser/AR07403452453460377601/creative/CR09203226887889879041?political=&region=US",
"https://adstransparency.google.com/advertiser/AR07403452453460377601/creative/CR12144248212462501889?political=&region=US",
"https://adstransparency.google.com/advertiser/AR03137232541803610113/creative/CR09180451518132781057?political=&region=US"
]

for link in LINKS:
	f = open("youtube_links.txt", "a")
	try:
		driver = webdriver.Chrome()
		driver.get(link)

		# arbitrary sleep, if ur internet is faster feel free to lower
		time.sleep(4)

		# the youtube link is like 3 iframes deep -_- .....
		id = driver.execute_script("""return document.querySelectorAll('iframe')[0].id""")
		iframe = driver.find_element(By.ID, id)
		driver.switch_to.frame(iframe)

		id2 = driver.execute_script("""return document.querySelectorAll('iframe')[0].id""")
		iframe2 = driver.find_element(By.ID, id2)
		driver.switch_to.frame(iframe2)

		# finally let's grab it!
		yt_link_embed = driver.execute_script("""return document.querySelectorAll('iframe')[0].src""")  
		yt_link = "https://www.youtube.com/watch?v=" + yt_link_embed[len("https://www.youtube.com/embed/"): yt_link_embed.index("?")]

		data_snatched = "Link: %s yt_link: %s\n" % (link, yt_link)
		print(data_snatched)
		f.write(data_snatched)

		driver.close()
	except:
		data_snatched = "ERROR: Link: %s has no YouTube vid\n" % (link)
		print(data_snatched)
		f.write(data_snatched)
	f.close()
		
