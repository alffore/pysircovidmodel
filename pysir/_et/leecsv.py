import csv

archivo = '/Users/alfonso/devel/datoscovid-19/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

with open(archivo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
