import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def check_dot(dot):
    if '・' in dot[0]:
        return dot.split(" ・")
    else:
        return dot.split


def web_scrape():
    driver = webdriver.Chrome("chromedriver.exe")
    search_url = "url"
    driver.get(search_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    side_bar = soup.find('ul', id="side_nav").find_all('a')

    headers = 'categories'
    data_list = []

    counter = 0

    items_name = "items"

    sub_title_list = []

    for s in side_bar:
        driver.find_element_by_link_text(s.text.strip()).click()
        time.sleep(2)
        box = f"box{side_bar.index(s)}"
        div_box = soup.find('div', id=box)
        box_zero = div_box.find_all(['h3', 'h4', 'p'])
        a_list = {
            "id": side_bar.index(s) + 1,
            "name": str(s.text.strip()),
            headers: []}
        item_thing = {}
        for i in box_zero:

            if i.name == 'h3':

                if item_thing:
                    a_list[headers].append(item_thing)

                header = i.text.strip()
                counter += 1
                item_thing = {
                    "id": counter,
                    "title": str(header)
                }

            elif i.name == 'h4':
                items_name = str(i.text.strip())
                sub_title_list.append(items_name)
            elif i.name == 'p':

                dot = " ・"

                value = str(i.text.strip()).split(dot)
                items_list = []
                for j in value:
                    word = j.rsplit()
                    if value[0] == j:

                        word = str(j.rsplit()[0])

                        word = word.replace("・", "")
                    elif len(word) > 1:
                        sub_word = word
                        lit = ''
                        for k in sub_word:
                            lit += k
                        word = lit

                    else:

                        word = str(j.rsplit()[0])
                    sub_item = {
                        "id": value.index(j) + 1,
                        "title": word
                    }

                    items_list.append(sub_item)

                y = items_list
                a = {items_name: y}

                items_name = "items"

                item_thing.update(a)
                if box_zero[-1] == i:
                    a_list[headers].append(item_thing)

        data_list.append(a_list)

    driver.close()
    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data_list, outfile, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    web_scrape()
