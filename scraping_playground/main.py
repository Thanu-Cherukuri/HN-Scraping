import pprint
from scraping import extract_url_pg_data, customize_hn_data
import sys


def main():
    with open('URLs_list.txt', 'r') as file:
        url_pg_ls = [line.rstrip() for line in file.readlines()]
        # print(url_pg_ls)
    links_list, subtext_list = extract_url_pg_data(url_pg_ls)
    hn_articles = customize_hn_data(links_list, subtext_list)
    pprint.pprint(hn_articles)


if __name__ == "__main__":
    main()
    sys.exit()
