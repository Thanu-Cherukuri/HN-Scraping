'''Python script to scrap the hacker news website and customize the hackernews'''
import requests
from bs4 import BeautifulSoup


def extract_url_pg_data(url_pg_list):
    all_links = []
    all_subtexts = []
    for url in url_pg_list:
        response = requests.get(url)
        web_in_html = BeautifulSoup(response.text, 'html.parser')
        # Extract elements/tags from html:
        links = web_in_html.select('.titleline > a')
        all_links.extend(links)
        # pprint.pprint(f'{response}\n ************ \n {web_in_html} \n *************** \n {links}')
        subtext = web_in_html.select('.subtext')
        all_subtexts.extend(subtext)
        # votes = web_in_html.select('.score')
        # pprint.pprint(f'{subtext}\n ************ \n {votes}')

    return all_links, all_subtexts


def sort_articles_by_votes(ls_hn_data):
    return sorted(ls_hn_data, key=lambda k: k['votes'], reverse=True)


def customize_hn_data(ls_links, ls_subtext):
    hn_data = []
    for idx, item in enumerate(ls_links):
        article_title = item.getText()
        article_link = item.get('href', None)
        upvotes = ls_subtext[idx].select('.score')
        if len(upvotes):
            points = int(upvotes[0].getText().replace(' points', ''))
            if points > 99:
                hn_data.append(
                    {'title': article_title, 'link': article_link, 'votes': points})
    return sort_articles_by_votes(hn_data)
