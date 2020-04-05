# COVID19-India-Data-API
A Flask application which fetches the data from Ministry of Health and Family Welfare ( [MoFHW](https://www.mohfw.gov.in/) ) and returns a JSON object.

**Country Data**

```
      {
      active_cases: 2650,
      death_cases: 68,
      last_updated: "04 April 2020, 09:00 GMT+5:30",
      migrated_cases: 1,
      passengers_screened: "15,24,266",
      recovered_cases: 183
      }
```
**State Data**
```
      {
      Confirmed: "161",
      Cured: "1",
      Death: "1 ",
      State: "AndhraPradesh"
      },
      {
      Confirmed: "10",
      Cured: "0",
      Death: "0 ",
      State: "AndamanNicobar"
      },
```
To be added, soon:

- [ ] List of COVID19 Testing Laboratories
___________________________________________________________________________________________________________

Retrieve Country Data: [/api/v1.0/country_data](https://covid-19india-api.herokuapp.com/api/v1.0/country_data) <br>
Retrieve State Data:   [/api/v1.0/state_data](https://covid-19india-api.herokuapp.com/api/v1.0/state_data)
