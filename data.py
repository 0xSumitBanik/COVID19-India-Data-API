from bs4 import BeautifulSoup
import requests as rq

def covidCountryData():
  URL = 'https://www.mygov.in/corona-data/covid19-statewise-status'
  page_content = rq.get(URL).content
  soup = BeautifulSoup(page_content,'html.parser')


  last_updated = (soup.find(class_='field field-name-field-covid-india-as-on field-type-text field-label-above')).text[19:]
  passengers_screened = (soup.find(class_='field field-name-field-passenger-screened-format field-type-text field-label-above')).text[31:]
  active_cases = (soup.find(class_='field field-name-field-total-active-case field-type-number-integer field-label-above')).text[14:]
  recovered_cases = (soup.find(class_='field field-name-field-total-cured-discharged field-type-number-integer field-label-above')).text[18:]
  migrated_cases = (soup.find(class_='field field-name-field-migrated-counts field-type-text field-label-above')).text[10:]
  death_cases = (soup.find(class_='field field-name-field-total-death-case field-type-number-integer field-label-above')).text[8:]

  country_data = {
    'last_updated' : last_updated,
    'passengers_screened' : passengers_screened,
    'active_cases':int(active_cases),
    'recovered_cases':int(recovered_cases),
    'migrated_cases':int(migrated_cases),
    'death_cases':int(death_cases)
  }

  return country_data



  
