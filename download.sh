# download file from google sheet
curl "https://docs.google.com/spreadsheets/d/1O3wnaFYSZCgY3Ih4yDw3EIH2SC_-vjhyHwrCQSy0J7M/export?gid=0&format=csv" -o conferences.csv

# convert csv to yaml
python3 gsheet2yaml.py
