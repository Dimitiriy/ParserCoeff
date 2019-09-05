from django.shortcuts import render
from django.http import HttpResponse
from .models import PariMatch
from django_tables2 import SingleTableView
from .tables import PariMatchTable

class MatchesListView(SingleTableView):
    model = PariMatch
    table_class = PariMatchTable
    template_name = 'parser_app/index.html'

def index(request):
    PariMatchs = PariMatch.objects.all()
    context = {'PariMatch':PariMatchs,}
    return render(request, 'parser_app/index.html', context)

from selenium import webdriver
import time
from lxml import html
from bs4 import BeautifulSoup
from .defs import printProgressBar

def update(request):
    count_saved = 0
    count_not_saved = 0
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print('\n\n\n[DEBUG]: Чищу модель PariMatch', end=' ')
    try:
        PariMatch.objects.all().delete()
        print(' - ok')
    except:
        print(' - ошибка')
    print('[DEBUG]: Запускаю ChromeDriver', end=' ')
    try:
        driver = webdriver.Chrome(chrome_options=options)
        driver.set_window_size(1024, 6000)
        print(' - ok')
    except:
        print(' - ошибка')
    print('[DEBUG]: Подключаюсь к parimatch.ru', end=' ')
    try:
        driver.get('https://www.parimatch.ru/live')
        print(' - ok')
    except:
        print(' - ошибка')
    print('[DEBUG]: Загружаю страницу')
    for i in range(10):
        time.sleep(1)
        printProgressBar(i + 1, 10, prefix = '[DEBUG]:', suffix = ' Процесс', length = 50)
    print('[DEBUG]: получаю HTML страницы', end=' ')
    try:
        html = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html, 'html.parser')
        print(' - ok')
    except:
        print(' - ошибка')
    print('[DEBUG]: Парсю HTML:')
    live_group_container = soup.find(class_='live-group-container')
    live_groups = live_group_container.findAll(class_='live-group')
    for live_group in live_groups:
        live_block_head_title_text = live_group.find(class_='live-block-head-title__text')
        print('[DEBUG]: | [' + live_block_head_title_text.string + ']')
        live_group_item = live_group.find(class_='live-group-item')
        live_block_championships = live_group.findAll(class_='live-block-championship')
        for live_block_championship in live_block_championships:
            championship_name_title = live_block_championship.find(class_='championship-name-title__text')
            print('[DEBUG]: | - ' + championship_name_title.string)
            live_blocks = live_block_championship.findAll(class_='live-block-row')
            for live_block in live_blocks:
                competitor_name = live_block.find(class_='competitor-name')
                total = live_block.find(class_='total')
                total_group_header = total.find(class_='total-group-header')
                outcome_coeffs = total.findAll(class_='outcome__coeff')
                try:
                    print('[DEBUG]: |   - ' + competitor_name.string, end=' ')
                except:
                    print('[DEBUG]: |   - NULL', end=' ')
                try:
                    print('[total = ' + total_group_header.string + ']', end=' ' )
                except:
                    print('[total = NULL]', end=' ')
                try:
                    print('[outcome = ' + outcome_coeffs[0].string + ']', end=' ')
                except:
                    print('[outcome = NULL]', end=' ')
                try:
                    print('[outcome = ' + outcome_coeffs[1].string + ']', end=' ')
                except:
                    print('[outcome = NULL]', end=' ')
                print()
                try:
                    PariMatch.objects.create(game=competitor_name.string, league=championship_name_title.string, total=float(total_group_header.string), more=float(outcome_coeffs[0].string), less=float(outcome_coeffs[1].string))
                    count_saved += 1
                except:
                    count_not_saved += 1
    print('[DEBUG]: Сохранено ' + str(int(count_saved*100/(count_saved+count_not_saved))) + '% (' + str(count_saved) + '/' + str(count_saved+count_not_saved) + ')\n\n\n')
    return render(request, 'parser_app/update.html', context=None)
