import csv
external_info = {"Argentina": ["Spanish", "South America", "Argentine peso", "Buenos Aires"],
                 "Canada": ["French and English", "North America", "Canadian dollar", "Ottawa"],
                 "United States": ["French and English", "North America", "U.S. Dollar", "Washington D.C."],
                 "Mali": ["French", "Africa", "West African CFA franc", "Bamako"],
                 "Mexico": ["Spanish", "North America", "Mexican peso", "Mexico City"],
                 "Niger": ["French", "Africa", "West African CFA franc", "Niamey"],
                 "Nigeria": ["English", "Africa", "Nigerian naira", "Abuja"],
                 "Ethiopia": ["Amharic", "Africa", "Ethiopian birr", "Addis Ababa"],
                 "Pakistan": ["English and Urdu", "Asia", "Pakistani rupee", "Islamabad"],
                 }
parsed = []
with open('../datasets/country.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    key = 1

    for row in csv_reader:

        if line_count % 7 == 2:
            country = [[0 for i in range(12)] for i in range(16)]
            year = 2005
            country_name = row[0]
            gdp_index = 0
            for c in country:
                # init
                c[0] = key
                c[1] = country_name
                c[2] = year
                c[3] = external_info[country_name][0]
                c[4] = external_info[country_name][1]
                c[5] = external_info[country_name][2]
                c[6] = external_info[country_name][3]

                year += 1
                key += 1
                # GDP
                gdp = row[gdp_index+4]
                gdp_index += 1
                c[11] = float(gdp)

        if line_count % 7 == 3:
            br_index = 0
            for c in country:
                # brith rate
                br = row[br_index+4]
                br_index += 1
                if br == "..":
                    c[8] = 'null'
                else:
                    c[8] = float(br)

        if line_count % 7 == 4:
            dr_index = 0
            for c in country:
                # death rate
                dr = row[dr_index+4]
                dr_index += 1
                if dr == "..":
                    c[9] = 'null'
                else:
                    c[9] = float(dr)

        if line_count % 7 == 4:
            fr_index = 0
            for c in country:
                # Fertility rate, total (births per woman)
                fr = row[fr_index+4]
                fr_index += 1
                if fr == "..":
                    c[10] = 'null'
                else:
                    c[10] = float(fr)

        if line_count % 7 == 0:
            population_index = 0
            for c in country:
                # Total reserves (% of total external debt)
                population = row[population_index+4]
                population_index += 1
                if population == "..":
                    c[7] = 'null'
                else:
                    c[7] = float(population)

            parsed.append(country)
        line_count += 1


with open('../parsedDataset/parsedCountry.csv', mode='w') as country_file:
    country_writer = csv.writer(
        country_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    country_writer.writerow(["id", "year", "name", "language", "continent", "currency",
                             "capital", "totalPopulation", "birthRate", "deathRate", "fertilityRate", "GDP"])
    for country in parsed:
        for row in country:
            country_writer.writerow(row)
