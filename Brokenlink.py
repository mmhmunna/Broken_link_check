from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
#input your webpage  link here
baseurl = ""
driver.get(baseurl)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)
link_tag = driver.find_elements_by_tag_name('a')
link_links = []
for link in link_tag:
    link_links.append(link.get_attribute("href"))

empty_or_None_Links = []
correct_link = []
broken_link =[]
total_link = len(link_links)
for link in range (total_link):
    if (link_links[link] == '' or link_links[link] == None):
        empty_or_None_Links.append(link_links[link])

    else:
        url = str(link_links[link])
        driver.get(url)
        time.sleep(2)
        title = driver.title
        if ("DashLite" in title):   #this "error" will be change as per as title
            correct_link.append(url)
        else:
            broken_link.append(url)


print('Total links' + ' ' + str(total_link))
print('Total empty or None links' + ' ' + str(len(empty_or_None_Links)))
print('Total Correct links' + ' ' + str(len(correct_link)))
print('Total Broken links' + ' ' + str(len(broken_link)))
print('Correct links are here:' + ' ' + str(correct_link))
print('Broken links are here:' + ' ' + str(broken_link))
