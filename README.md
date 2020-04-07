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
**ICMR Lab Details**
```
      {
      government_labs: [
      {
      address: " ICMR-Regional Medical Research Centre, Post Bag 13, Dollygunj, Port Blair, Andaman and Nicobar Islands 744103",
      name: " ICMR-Regional Medical Research Centre, Port Blair"
      }
      ],
            state_or_UT: "Andaman & Nicobar Island"
      },
      {
      collection_sites: [
      {
      address: "National Highway 52A, Old Assembly Complex, Naharlagun, Arunachal Pradesh 791110",
      name: "Tomo Riba Institute of Health & Medical Sciences, Naharlagun"
      }
      ],
            state_or_UT: "Arunachal Pradesh"
      },
```
**Helpline Numbers**
```
      contact_details: [
      {
            helpline_number: "0866-2410978",
            state_or_UT: "Andhra Pradesh"
      },
      {
            helpline_number: "9436055743",
            state_or_UT: "Arunachal Pradesh"
      },
```
___________________________________________________________________________________________________________

Visit the [website](https://covid-19india-api.herokuapp.com/) to know more.
