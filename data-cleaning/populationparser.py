import csv


parsed = []
with open('../datasets/population.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    key = 1
    i = 0
    for row in csv_reader:
        if i == 1:
            country = [["null" for i in range(14)] for i in range(14)]
            year = 2005
            country_name = row[0]

            for c in country:
                # init
                c[0] = key
                c[1] = country_name
                c[2] = year

                year += 1
                key += 1
            i += 1
        else:
            if i > 2:
                year_index = 0
                for c in country:
                    value = row[year_index+4]
                    year_index += 1
                    if value == "..":
                        c[i] = 'null'
                    else:
                        c[i] = float(value)

            if i == 13:
                parsed.append(country)
                i = 0

            i += 1

with open('../parsedDataset/parsedPopulation.csv', mode='w') as population_file:
    population_writer = csv.writer(
        population_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    population_writer.writerow(["id", "country", "year", "femaleLifeExpectancy", "maleLifeExpectancy", "totalLifeExpectancy",
                                "netMigration", "ageDependencyRatio", "povertyHeadcountRatio", "populationGrowth", "ruralPopulationGrowth",
                                "urbanPopulationGrowth", "populationSize", "averageAge", "infantMortalityRate"])
    for country in parsed:
        for row in country:
            population_writer.writerow(row)
