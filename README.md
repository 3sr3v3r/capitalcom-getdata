# capitalcom-getdata
This repository provides python code to get data from the capital.com v1 REST API and write to .CSV
There are 2 main functions:
- download an overview of all the 'instruments' or EPICS from capital.com
- download historical data for an EPIC or list of EPICS.

historical data can be written in backtrader compatible OHLC format or in forextester format for backtesting.

The main file [capitalcom_historic_data.py] contains the variables to execute the API requests.

The API calls are based on this repository https://github.com/hootnot/oanda-api-v20 that was written for Oanda.
