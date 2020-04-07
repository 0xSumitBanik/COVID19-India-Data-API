from bs4 import BeautifulSoup
import requests as rq
from icmr_labs import labs_list

class Country:
    def __init__(self, URL):
        self.URL = URL

    def covidCountryData(self):
        page_content = rq.get(self.URL).content
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
            'passengers_screened': passengers_screened,
            'active_cases': int(active_cases),
            'recovered_cases': int(recovered_cases),
            'migrated_cases': int(migrated_cases),
            'death_cases': int(death_cases)
        }
        return country_data

    def state_data(self):
        page_content = rq.get(self.URL).content
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
                    'State': state_name,
                    'Confirmed': confirmed_case,
                    'Cured': cured,
                    'Death': death
                }
                json_data.append(st_data)

        state_data={
            'source':self.URL,
            'state_data':json_data
        }
        return state_data


    def icmrLabDetails(self):
        return labs_list