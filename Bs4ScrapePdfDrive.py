
from re import S
from bs4 import BeautifulSoup
import SeleniumCallForPdfDrive
import requests

from SeleniumCallForPdfDrive import SeleniumScrape


url_links = ['https://www.pdfdrive.com/search?q=sports&pagecount=&pubyear=&searchin=&em=','https://www.pdfdrive.com/education-books.html','https://www.pdfdrive.com/food-books.html'
,'https://www.pdfdrive.com/animals-books.html','https://www.pdfdrive.com/blockchain-books.html']

for urlLink in url_links:
    request  = requests.get(urlLink)
    soup = BeautifulSoup(request.content,'html.parser')
    get_page_Div_list = soup.find_all('a', {'class','ai-search'})
    # print('get_page_Div_list = ',get_page_Div_list)
    for anchor in get_page_Div_list:
        print('anchor = ', anchor['href'])
        page_reaching_download_page = requests.get('https://www.pdfdrive.com/'+anchor['href'])
        reaching_download_page_soup = BeautifulSoup(page_reaching_download_page.content,'html.parser')
        reaching_download_page_anchor = reaching_download_page_soup.find('a',{"id":"download-button-link"})
        print('reaching_download_page_anchor = ', reaching_download_page_anchor['href'])
        seleniumScrape = SeleniumScrape()
        get_selenium_page_source = seleniumScrape.gettingDownloadingFile(reaching_download_page_anchor['href'])
        seleniumScrape.driver_quit()
        print('get_selenium_page_source = ',get_selenium_page_source)











