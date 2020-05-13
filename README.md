# <p align="center">COVID19-India API<p>
This API contains the details of Country and State Cases, Worldwide Cases and COVID related updates. ⚡



<p align="center"> <a href="https://covid-19-apis.postman.com/" target="_blank"><img src="https://raw.githubusercontent.com/iSumitBanik/COVID19-India-Data-API/master/static/img/postman.png" height=130px>
</a>

<br>
</p>

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/iSumitBanik/COVID19-India-Data-API/graphs/commit-activity) ![GitHub language count](https://img.shields.io/github/languages/count/iSumitBanik/COVID19-India-Data-API) ![GitHub repo size](https://img.shields.io/github/repo-size/iSumitBanik/COVID19-India-Data-API)

### Response Demo
#### Country And States Data 
```

{
    active_cases: 47480,
    active_rate: 63.92,
    confirmed_cases: 74280,
    death_cases: 2415,
    death_rate: 3.25,
    delta_change_active_cases: 1472,
    delta_change_death_cases: 122,
    delta_change_recovered_cases: 1931,
    last_total_active_cases: 46008,
    last_total_death_cases: 2293,
    last_total_recovered_cases: 22454,
    last_updated: "13 May 2020, 08:00 IST (GMT+5:30)",
    migrated_cases: 1,
    passengers_screened: 1524266,
    recovered_cases: 24385,
    recovered_rate: 32.83
    },
{
    source: "myGov",
    state_data: [
    {
    active: 0,
    active_rate: 0,
    confirmed: 33,
    death_rate: 0,
    deaths: 0,
    recovered: 33,
    recovered_rate: 100,
    state: "Andaman and Nicobar"
    },
    {
    active: 988,
    active_rate: 47.27,
    confirmed: 2090,
    death_rate: 2.2,
    deaths: 46,
    recovered: 1056,
    recovered_rate: 50.53,
    state: "Andhra Pradesh"
    }, ....
```

#### Global Data
```
    {
    data: {
    confirmed_cases: "4394449",
    active_cases: "2461842",
    recovered_cases: "295696",
    death_cases: "1636911",
    active_rate: "56.02%",
    recovered_rate: "6.73%",
    death_rate: "37.25%",
    new_cases: "56847",
    new_deaths: "3245",
    serious_cases: "46120"
    },
    updates: [
    "8,985 new cases and 750 new deaths in the United States",
    "19 new cases and 4 new deaths in Israel",
    "159 new cases and 9 new deaths in Ireland",
    "653 new cases and 54 new deaths in Germany",
    "3,135 new cases and 231 new deaths in Brazil",
    "3,749 new cases and 136 new deaths in India",
    "12 new cases in Djibouti",
    "94 new cases in Morocco", ....
```

### Try this API: [Documentation](https://covid-19india-api.herokuapp.com/) ▶

### ✍🏻 Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Server Side Framework ⚡
* [Materialize CSS](materializecss.com) - Front-End CSS Framework 🎨

### 📜 License 
This project is licensed under the MIT license. You can read it in details out [here](https://github.com/iSumitBanik/COVID19-India-Data-API/blob/master/LICENSE)

### 🤝🏻 Feel free to contribute
Submit a Pull Request or drop an issue.

______________________________________________________________________________________________________________________________________
