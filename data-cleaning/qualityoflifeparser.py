

import csv


parsed = []
with open('datasets/health_and_quality_of_life.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    key = 1

    for row in csv_reader:
        if line_count % 30 == 2:
            country = [["null" for i in range(16)] for i in range(16)]
            year = 2005
            country_name = row[0]

            for c in country:
                # init
                c[0] = key
                c[1] = country_name
                c[2] = year

                year += 1
                key += 1

        if line_count % 30 == 21:
            peopleUsingSafeDrinkingWaterServices_index = 0
            for c in country:
                # People using safely managed drinking water services (% of population)
                peopleUsingSafeDrinkingWaterServices = row[peopleUsingSafeDrinkingWaterServices_index+4]
                peopleUsingSafeDrinkingWaterServices_index += 1
                if peopleUsingSafeDrinkingWaterServices == "..":
                    c[3] = 'null'
                else:
                    c[3] = float(peopleUsingSafeDrinkingWaterServices)

        if line_count % 30 == 22:
            peopleUsingBasicDrinkingWaterServices_index = 0
            for c in country:
                # People using at least basic drinking water services, urban (% of urban population)
                peopleUsingBasicDrinkingWaterServices = row[peopleUsingBasicDrinkingWaterServices_index+4]
                peopleUsingBasicDrinkingWaterServices_index += 1
                if peopleUsingBasicDrinkingWaterServices == "..":
                    c[4] = 'null'
                else:
                    c[4] = float(peopleUsingBasicDrinkingWaterServices)

        if line_count % 30 == 23:
            peoplePracticingOpenDefecation_index = 0
            for c in country:
                # People practicing open defecation (% of population)
                peoplePracticingOpenDefecation = row[peoplePracticingOpenDefecation_index+4]
                peoplePracticingOpenDefecation_index += 1
                if peoplePracticingOpenDefecation == "..":
                    c[5] = 'null'
                else:
                    c[5] = float(peoplePracticingOpenDefecation)

        if line_count % 30 == 24:
            peopleUsingBasicSanitationServices_index = 0
            for c in country:
                # People using at least basic sanitation services (% of population)
                peopleUsingBasicSanitationServices = row[peopleUsingBasicSanitationServices_index+4]
                peopleUsingBasicSanitationServices_index += 1
                if peopleUsingBasicSanitationServices == "..":
                    c[6] = 'null'
                else:
                    c[6] = float(peopleUsingBasicSanitationServices)

        if line_count % 30 == 25:
            peopleUsingSafeSanitationServices_index = 0
            for c in country:
                # People using safely managed sanitation services (% of population)
                peopleUsingSafeSanitationServices = row[peopleUsingSafeSanitationServices_index+4]
                peopleUsingSafeSanitationServices_index += 1
                if peopleUsingSafeSanitationServices == "..":
                    c[7] = 'null'
                else:
                    c[7] = float(peopleUsingSafeSanitationServices)

        if line_count % 30 == 26:
            ruralPeopleUsingBasicSanitationServices_index = 0
            for c in country:
                # People using at least basic sanitation services, rural (% of rural population)
                ruralPeopleUsingBasicSanitationServices = row[
                    ruralPeopleUsingBasicSanitationServices_index+4]
                ruralPeopleUsingBasicSanitationServices_index += 1
                if ruralPeopleUsingBasicSanitationServices == "..":
                    c[8] = 'null'
                else:
                    c[8] = float(ruralPeopleUsingBasicSanitationServices)

        if line_count % 30 == 27:
            urbanPeopleUsingBasicSanitationServices_index = 0
            for c in country:
                # People using at least basic sanitation services, urban (% of urban population)
                urbanPeopleUsingBasicSanitationServices = row[
                    urbanPeopleUsingBasicSanitationServices_index+4]
                urbanPeopleUsingBasicSanitationServices_index += 1
                if urbanPeopleUsingBasicSanitationServices == "..":
                    c[9] = 'null'
                else:
                    c[9] = float(urbanPeopleUsingBasicSanitationServices)

        if line_count % 30 == 28:
            peopleWithBasicHandwashingFacilities_index = 0
            for c in country:
                # People with basic handwashing facilities including soap and water (% of population)
                peopleWithBasicHandwashingFacilities = row[peopleWithBasicHandwashingFacilities_index+4]
                peopleWithBasicHandwashingFacilities_index += 1
                if peopleWithBasicHandwashingFacilities == "..":
                    c[10] = 'null'
                else:
                    c[10] = float(peopleWithBasicHandwashingFacilities)

        if line_count % 30 == 29:
            ruralPeopleWithBasicHandwashingFacilities_index = 0
            for c in country:
                # People with basic handwashing facilities including soap and water, rural (% of rural population)
                ruralPeopleWithBasicHandwashingFacilities = row[
                    ruralPeopleWithBasicHandwashingFacilities_index+4]
                ruralPeopleWithBasicHandwashingFacilities_index += 1
                if ruralPeopleWithBasicHandwashingFacilities == "..":
                    c[11] = 'null'
                else:
                    c[11] = float(ruralPeopleWithBasicHandwashingFacilities)

        if line_count % 30 == 0:
            yearsOfMaternalLeave_index = 0
            for c in country:
                # Maternal leave benefits (% of wages paid in covered period)
                yearsOfMaternalLeave = row[
                    yearsOfMaternalLeave_index+4]
                yearsOfMaternalLeave_index += 1
                if yearsOfMaternalLeave == "..":
                    c[15] = 'null'
                else:
                    c[15] = float(yearsOfMaternalLeave)
            parsed.append(country)

        line_count += 1

with open('datasets/unemployment.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    country_index = 0
    for row in csv_reader:

        if line_count != 1 and row != []:
            country = parsed[country_index]

            if line_count % 2 == 0:
                femaleUnemploymentRate_index = 0

                for c in country:

                    # People using at least basic sanitation services (% of population)
                    femaleUnemploymentRate = row[femaleUnemploymentRate_index+4]
                    femaleUnemploymentRate_index += 1
                    if femaleUnemploymentRate == "..":
                        c[12] = 'null'
                    else:
                        c[12] = float(femaleUnemploymentRate)
            if line_count % 2 == 1:
                maleUnemploymentRate_index = 0
                for c in country:
                    # People using at least basic sanitation services (% of population)
                    maleUnemploymentRate = row[maleUnemploymentRate_index+4]
                    maleUnemploymentRate_index += 1
                    if maleUnemploymentRate == "..":
                        c[13] = 'null'
                    else:
                        c[13] = float(maleUnemploymentRate)
                country_index += 1
        line_count += 1

with open('parsedQualityOfLife.csv', mode='w') as QOF_file:
    QOL_writer = csv.writer(
        QOF_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    QOL_writer.writerow(["id", "name", "year", "peopleUsingBasicDrinkingWaterServices", "peoplePracticingOpenDefecation", "peopleUsingBasicSanitationServices",
                         "peopleUsingSafeSanitationServices", "ruralPeopleUsingBasicSanitationServices", "urbanPeopleUsingBasicSanitationServices", "peopleWithBasicHandwashingFacilities", "ruralPeopleWithBasicHandwashingFacilities",
                         "urbanPeopleWithBasicHandwashingFacilities", "maleUnemploymentRate", "femaleUnemploymentRate", "totalUnemploymentRate", "yearsOfMaternalLeave"])
    for country in parsed:
        for row in country:
            QOL_writer.writerow(row)
