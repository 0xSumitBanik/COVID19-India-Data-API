from bs4 import BeautifulSoup
import requests as rq
from helpline_numbers import helpline_numbers


class Country:
    def covidCountryData(self):
        URL = 'https://www.mygov.in/corona-data/covid19-statewise-status'

        page_content = rq.get(URL).content
        soup = BeautifulSoup(page_content, 'html.parser')
        last_updated = (soup.find(
            class_='field field-name-field-covid-india-as-on field-type-text field-label-above')).text[19:]
        passengers_screened = (soup.find(
            class_='field field-name-field-passenger-screened-format field-type-text field-label-above')).text[31:]
        active_cases = (soup.find(
            class_='field field-name-field-total-active-case field-type-number-integer field-label-above')).text[14:]
        recovered_cases = (soup.find(
            class_='field field-name-field-total-cured-discharged field-type-number-integer field-label-above')).text[18:]
        migrated_cases = (soup.find(
            class_='field field-name-field-migrated-counts field-type-text field-label-above')).text[10:]
        death_cases = (soup.find(
            class_='field field-name-field-total-death-case field-type-number-integer field-label-above')).text[8:]
        country_data = {
            'last_updated': last_updated,
            'passengers_screened': int(passengers_screened.replace(",","")),
            'active_cases': int(active_cases),
            'recovered_cases': int(recovered_cases),
            'migrated_cases': int(migrated_cases),
            'death_cases': int(death_cases),
            'confirmed_cases':int(active_cases)+int(recovered_cases)+int(death_cases),
            'death_rate': round((int(death_cases)/(int(active_cases)+int(recovered_cases)+int(death_cases))*100),2),
            'active_rate': round((int(active_cases)/(int(active_cases)+int(recovered_cases)+int(death_cases))*100),2),
            'recovered_rate': round((int(recovered_cases)/(int(active_cases)+int(recovered_cases)+int(death_cases))*100),2)

        }
        return country_data

    def state_data(self):
        URL = 'https://www.mygov.in/corona-data/covid19-statewise-status'

        page_content = rq.get(URL).content
        soup = BeautifulSoup(page_content, 'html.parser')
        datas = (soup.find(
            class_='field field-name-field-covid-statewise-data field-type-field-collection field-label-above').text).split('\n\n')
        datas.pop(0)
        json_data = []
        for data in datas:
            if data:
                state_name = data.split('\xa0')[1].split('Total')[0]
                confirmed_case = data.split('\xa0')[2].split('Cured')[0]
                cured = data.split('\xa0')[3].split('Death')[0]
                death = data.split('\xa0')[4]
                st_data = {
                    'state': state_name,
                    'confirmed_cases': int(confirmed_case),
                    'cured_cases': int(cured),
                    'death_cases': int(death),
                    'active_cases':int(confirmed_case)-int(death)-int(cured),
                    'active_rate':round(((int(confirmed_case)-int(death)-int(cured))/int(confirmed_case)*100),2),
                    'death_rate':round((int(death)/int(confirmed_case)*100),2),
                    'recovered_rate':round((int(cured)/int(confirmed_case)*100),2)
                }
                json_data.append(st_data)

        state_data={
            'source':'myGov',
            'state_data':json_data
        }
        return state_data


    def covidTestCount(self):
        URL = 'https://www.icmr.gov.in/'
        page_content = rq.get(URL).content
        soup = BeautifulSoup(page_content,'html.parser')

        test_count = int(soup.find(class_='counter').text)
        last_updated_test_count = soup.find('h2').text[22:].strip()

        test_count_dict = {
            'source':'ICMR',
            'last_updated':last_updated_test_count,
            'test_count':test_count
        }

        return test_count_dict


    def helplineNumbers(self):
        return helpline_numbers

    def headlines(self):
        URL_news = 'https://inshorts.com/en/read/Coronavirus'
        page_content_news = rq.get(URL_news).content

        soup_news = BeautifulSoup(page_content_news,'html.parser')

        headlines = soup_news('a',class_='clickable',href=True)
        headlines_list = []

        for i in headlines:
            headlines_list.append(i.text.strip())
            
        image_link = soup_news(class_='news-card-image',style=True)
        image_link_list = []

        for i in image_link:
            image_link_list.append(i.get('style')[23:-3])
            
        headlines_summary = soup_news('div',itemprop='articleBody')
        headlines_summary_list = []

        for i in headlines_summary:
            headlines_summary_list.append(i.text.strip())
            
            
        headlines_dict = {
            'source':'inshorts',
            'headlines':headlines_list,
            'headlines_summary':headlines_summary_list,
            'image_link':image_link_list
        }

        return headlines_dict
