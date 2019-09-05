from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lxml import html
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(1024, 6000)
#driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('https://www.parimatch.ru/live')

def print_to_console(driver):
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    live_group_container = soup.find(class_='live-group-container')
    live_groups = live_group_container.findAll(class_='live-group')
    for live_group in live_groups:
        live_block_head_title_text = live_group.find(class_='live-block-head-title__text')
        print('[' + live_block_head_title_text.string + ']')
        live_group_item = live_group.find(class_='live-group-item')
        live_block_championships = live_group.findAll(class_='live-block-championship')
        for live_block_championship in live_block_championships:
            championship_name_title = live_block_championship.find(class_='championship-name-title__text')
            print('- ' + championship_name_title.string)
            live_blocks = live_block_championship.findAll(class_='live-block-row')
            for live_block in live_blocks:
                competitor_name = live_block.find(class_='competitor-name')
                total = live_block.find(class_='total')
                total_group_header = total.find(class_='total-group-header')
                outcome_coeffs = total.findAll(class_='outcome__coeff')
                try:
                    print('  - ' + competitor_name.string, end=' ')
                except:
                    print('  - NULL', end=' ')
                try:
                    print('[total = ' + total_group_header.string + ']', end=' ' )
                except:
                    print('[total = NULL]', end=' ')
                for outcome_coeff in outcome_coeffs:
                    try:
                        print('[outcome = ' + outcome_coeff.string + ']', end=' ')
                    except:
                        print('[total = NULL]', end=' ')
                print()
    print('--- end ---')
    driver.quit()

def save_to_sql(driver):
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    live_group_container = soup.find(class_='live-group-container')
    live_groups = live_group_container.findAll(class_='live-group')
    for live_group in live_groups:
        live_block_head_title_text = live_group.find(class_='live-block-head-title__text')
        #print('[' + live_block_head_title_text.string + ']')
        live_group_item = live_group.find(class_='live-group-item')
        live_block_championships = live_group.findAll(class_='live-block-championship')
        for live_block_championship in live_block_championships:
            championship_name_title = live_block_championship.find(class_='championship-name-title__text')
            League.objects.Create(name=championship_name_title.string)
            print('- ' + championship_name_title.string)
            live_blocks = live_block_championship.findAll(class_='live-block-row')
            for live_block in live_blocks:
                competitor_name = live_block.find(class_='competitor-name')
                total = live_block.find(class_='total')
                total_group_header = total.find(class_='total-group-header')
                outcome_coeffs = total.findAll(class_='outcome__coeff')
                try:
                    print('  - ' + competitor_name.string, end=' ')
                except:
                    print('  - NULL', end=' ')
                try:
                    print('[total = ' + total_group_header.string + ']', end=' ' )
                except:
                    print('[total = NULL]', end=' ')
                for outcome_coeff in outcome_coeffs:
                    try:
                        print('[outcome = ' + outcome_coeff.string + ']', end=' ')
                    except:
                        print('[total = NULL]', end=' ')
                print()
    print('--- end ---')
    driver.quit()

save_to_sql(driver)
