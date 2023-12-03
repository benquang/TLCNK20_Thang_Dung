import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from functions import *
import pandas as pd
from kafka import KafkaProducer
import json
import csv
def crawlUpComingMatch():
    data = {
        'match_date': [],
        'league': [],
        'home_team': [],
        'away_team': [],
        'home_player1': [],
        'home_player2': [],
        'home_player3': [],
        'home_player4': [],
        'home_player5': [],
        'home_player6': [],
        'home_player7': [],
        'home_player8': [],
        'home_player9': [],
        'home_player10': [],
        'home_player11': [],
        'away_player1': [],
        'away_player2': [],
        'away_player3': [],
        'away_player4': [],
        'away_player5': [],
        'away_player6': [],
        'away_player7': [],
        'away_player8': [],
        'away_player9': [],
        'away_player10': [],
        'away_player11': []
    }

    df = pd.DataFrame(data)
    leauge = ['Premier Leauge']

    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.sportsgambler.com/lineups/football/england-premier-league/")
    print(driver.title)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[./span[text()='Predicted Lineups']]"))
        )
        predicted_lineup_buttons = driver.find_elements(By.XPATH, "//a[./span[text()='Predicted Lineups']]")
        for predicted_lineup_button in predicted_lineup_buttons:
            driver.execute_script("arguments[0].click();", predicted_lineup_button)
        dates = driver.find_elements(By.XPATH,"//div[@class='content-block team-news-container']//h3[@class = 'date-headline']")
        dates = [CustomFuncs.UCM_convert_date(date.text) for date in dates]
        time.sleep(7)
        for index_date,date in enumerate(dates):
            number_of_match_in_dates = len(driver.find_elements(By.XPATH,"//div[@class = 'content-block team-news-container']\
                                                                         //div[@class='fxs-table table-for-lineups'][{}]\
                                                                        //div[@class='table-row-loneups' and \
                                                                        .//span[text() = 'Predicted Lineups']]".format(index_date+1)))
            if (number_of_match_in_dates == 0):
                continue
            
            for index_match in range(number_of_match_in_dates):
                xpath_infor_row = "//div[@class = 'content-block team-news-container']//div[@class='fxs-table table-for-lineups'][{}]\
                                                                                        //div[@class='table-row-loneups' and .\
                                                                                        //span[text() = 'Predicted Lineups']][{}]"\
                                                                                        .format(index_date+1,index_match+1)
                home_team = driver.find_element(By.XPATH,xpath_infor_row+"//span[@class='fxs-team home']").text
                away_team = driver.find_element(By.XPATH,xpath_infor_row+"//span[@class='fxs-team']").text
                xpath_home_lineup = "(//div[@class = 'content-block team-news-container']//div[@class='fxs-table table-for-lineups'][{}]\
                                                                                        //div[@class='table-row-loneups' and \
                                                                                        .//span[text() = 'Predicted Lineups']]\
                                                                                        //div[@class='lineups-home reverse'])[{}]"\
                                                                                        .format(index_date+1,index_match+1)
                xpath_away_lineup = "(//div[@class = 'content-block team-news-container']//div[@class='fxs-table table-for-lineups'][{}]//div[@class='table-row-loneups' and .//span[text() = 'Predicted Lineups']]//div[@class='lineups-away'])[{}]".format(index_date+1,index_match+1)
                home_kits = driver.find_elements(By.XPATH,xpath_home_lineup+"//span[@class = 'player-profile']")
                home_kits = [kit.text for kit in home_kits]
                away_kits = driver.find_elements(By.XPATH,xpath_away_lineup+"//span[@class = 'player-profile']")
                away_kits = [kit.text for kit in away_kits]
                home_player_names = driver.find_elements(By.XPATH,xpath_home_lineup+"//span[@class = 'player-name']")
                home_player_names = [name.text for name in home_player_names]
                away_player_names = driver.find_elements(By.XPATH,xpath_away_lineup+"//span[@class = 'player-name']")
                away_player_names = [name.text for name in away_player_names]
                print(away_player_names)
                
                row_data = data = {
                    'match_date': date,
                    'league': 'Premier Leauge',
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_player1': [home_player_names[0]],
                    'home_player2': [home_player_names[1]],
                    'home_player3': [home_player_names[2]],
                    'home_player4': [home_player_names[3]],
                    'home_player5': [home_player_names[4]],
                    'home_player6': [home_player_names[5]],
                    'home_player7': [home_player_names[6]],
                    'home_player8': [home_player_names[7]],
                    'home_player9': [home_player_names[8]],
                    'home_player10': [home_player_names[9]],
                    'home_player11': [home_player_names[10]],
                    'away_player1': [away_player_names[0]],
                    'away_player2': [away_player_names[1]],
                    'away_player3': [away_player_names[2]],
                    'away_player4': [away_player_names[3]],
                    'away_player5': [away_player_names[4]],
                    'away_player6': [away_player_names[5]],
                    'away_player7': [away_player_names[6]],
                    'away_player8': [away_player_names[7]],
                    'away_player9': [away_player_names[8]],
                    'away_player10': [away_player_names[9]],
                    'away_player11': [away_player_names[10]],
                    'home_kit1': [home_kits[0]],
                    'home_kit2': [home_kits[1]],
                    'home_kit3': [home_kits[2]],
                    'home_kit4': [home_kits[3]],
                    'home_kit5': [home_kits[4]],
                    'home_kit6': [home_kits[5]],
                    'home_kit7': [home_kits[6]],
                    'home_kit8': [home_kits[7]],
                    'home_kit9': [home_kits[8]],
                    'home_kit10': [home_kits[9]],
                    'home_kit11': [home_kits[10]],
                    'away_kit1': [away_kits[0]],
                    'away_kit2': [away_kits[1]],
                    'away_kit3': [away_kits[2]],
                    'away_kit4': [away_kits[3]],
                    'away_kit5': [away_kits[4]],
                    'away_kit6': [away_kits[5]],
                    'away_kit7': [away_kits[6]],
                    'away_kit8': [away_kits[7]],
                    'away_kit9': [away_kits[8]],
                    'away_kit10': [away_kits[9]],
                    'away_kit11': [away_kits[10]],
                }
                df = pd.concat([df, pd.DataFrame(row_data, index=[0])], ignore_index=True)
    finally:
        #Header:
            #match_date,league,home_team,away_team,home_player1,home_player2,home_player3,home_player4,home_player5,
            # home_player6,home_player7,home_player8,home_player9,home_player10,home_player11,away_player1,away_player2,
            # away_player3,away_player4,away_player5,away_player6,away_player7,away_player8,away_player9,away_player10,
            # away_player11,home_kit1,home_kit2,home_kit3,home_kit4,home_kit5,home_kit6,home_kit7,home_kit8,home_kit9,
            # home_kit10,home_kit11,away_kit1,away_kit2,away_kit3,away_kit4,away_kit5,away_kit6,away_kit7,away_kit8,
            # away_kit9,away_kit10,away_kit11
        df.to_csv('data.csv', index=False, encoding='utf-8-sig',header=False)
        driver.quit()

def kafka_producer():
    producer = KafkaProducer(
            bootstrap_servers = 'localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8-sig')
        )
    with open('data.csv', 'r',encoding='utf-8-sig') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            producer.send('UpComingMatch_Topic',row)
            producer.flush() # Đợi cho tất cả message cho queue được gửi đi
            print(row)

def main():
    # crawlUpComingMatch()
    kafka_producer()

if __name__ == "__main__":
    main()

