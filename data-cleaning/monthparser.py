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
            m.append("Q1")
        elif month == "April" or month == "May" or month == "June":
            m.append("Q2")
        elif month == "July" or month == "August" or month == "September":
            m.append("Q3")
        else:
            m.append("Q4")
        m.append(year)
        if year < 2010:
            m.append("2000s")
        elif year < 2020:
            m.append("2010s")
        else:
            m.append("2020s")
        parsed.append(m)

    year += 1


with open('../parsedMonth.csv', mode='w') as month_file:
    month_writer = csv.writer(
        month_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    month_writer.writerow(["id", "name", "quater", "year", "decade"])
    for row in parsed:
        month_writer.writerow(row)
