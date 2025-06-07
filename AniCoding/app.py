from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from image_classification import labeling, is_anime
import csv
import os
import numpy as np

chrome_options = Options()

chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=chrome_options)

rankings_all = []
contests_all = []
ani_num_all = []

start = 10001
end = 12000
size = 1600
numbers = np.sort(np.random.choice(range(start, end+1), size, replace=False)) # size in start ~ end

for i in numbers:
    driver.get(f'https://leetcode.com/contest/globalranking/{i}')
    time.sleep(3)

    data_ranking = driver.find_elements(By.CSS_SELECTOR, '.ranking-row .ranking')
    data_contests = driver.find_elements(By.CSS_SELECTOR, '.ranking-row .info')
    data_avatar = driver.find_elements(By.CSS_SELECTOR, '.ranking-row .simp-avatar__mRN_')

    rankings = []
    contests = []
    ani_num = []

    for element in data_ranking:
        rankings.append(int(element.text))

    for element in data_contests:
        contest_text = element.text
        if contest_text == 'First time attending contest':
            contests.append(0)
        else:
            contest_number = contest_text.split()[0]
            contests.append(int(contest_number))

    for element in data_avatar:
        avatar_url = element.get_attribute('src')
        if avatar_url == 'https://assets.leetcode.com/users/default_avatar.jpg':
            ani_num.append(-1) # -1 if no profile picture
        else:
            ani_num.append(is_anime(avatar_url))

    rankings_all += rankings
    contests_all += contests
    ani_num_all += ani_num

filename = 'leetcode_data.csv'
file_exists = os.path.exists(filename)
with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    if not file_exists or os.path.getsize(filename) == 0:
        writer.writerow(['rankings', 'contests', 'ani_num'])

    for i in range(len(rankings_all)):
        row = [rankings_all[i], contests_all[i], ani_num_all[i]]
        writer.writerow(row)

driver.quit()