import csv

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
year = 2005

parsed = []
id = 0
while year < 2021:
    for month in months:
        id += 1
        m = []
        m.append(id)
        m.append(month)
        if month == "January" or month == "February" or month == "March":
            m.append(1)
        elif month == "April" or month == "May" or month == "June":
            m.append(2)
        elif month == "July" or month == "August" or month == "September":
            m.append(3)
        else:
            m.append(4)
        m.append(year)
        if year < 2010:
            m.append("2000")
        elif year < 2020:
            m.append("2010")
        else:
            m.append("2020")
        parsed.append(m)

    year += 1


with open('../parsedDataset/parsedMonth.csv', mode='w') as month_file:
    month_writer = csv.writer(
        month_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    month_writer.writerow(["id", "name", "quater", "year", "decade"])
    for row in parsed:
        month_writer.writerow(row)
