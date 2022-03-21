import csv


parsed = []
with open('../datasets/health_and_quality_of_life.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    key = 1

    for row in csv_reader:
        if line_count % 30 == 2:
            country = [["null" for i in range(22)] for i in range(10)]
            year = 2005
            country_name = row[0]

            for c in country:
                # init
                c[0] = key
                c[1] = country_name
                c[2] = year

                year += 1
                key += 1

        if line_count % 30 == 7:
            domesticHealthExpenditure_index = 0
            for c in country:
                # Domestic general government health expenditure (% of GDP)
                domesticHealthExpenditure = row[domesticHealthExpenditure_index+4]
                domesticHealthExpenditure_index += 1
                if domesticHealthExpenditure == "..":
                    c[3] = 'null'
                else:
                    c[3] = float(domesticHealthExpenditure)

        if line_count % 30 == 8:
            hospitalBeds_index = 0
            for c in country:
                # Hospital beds (per 1,000 people)
                hospitalBeds = row[hospitalBeds_index+4]
                hospitalBeds_index += 1
                if hospitalBeds == "..":
                    c[4] = 'null'
                else:
                    c[4] = float(hospitalBeds)

        if line_count % 30 == 2:
            immunizationDPT_index = 0
            for c in country:
                # Immunization, DPT (% of children ages 12-23 months)
                immunizationDPT = row[immunizationDPT_index+4]
                immunizationDPT_index += 1
                if immunizationDPT == "..":
                    c[5] = 'null'
                else:
                    c[5] = float(immunizationDPT)

        if line_count % 30 == 3:
            immunizationHepB3_index = 0
            for c in country:
                # Immunization, HepB3 (% of one-year-old children)
                immunizationHepB3 = row[immunizationHepB3_index+4]
                immunizationHepB3_index += 1
                if immunizationHepB3 == "..":
                    c[6] = 'null'
                else:
                    c[6] = float(immunizationHepB3)

        if line_count % 30 == 4:
            immunizationHib3_index = 0
            for c in country:
                # Immunization, Hib3 (% of children ages 12-23 months)
                immunizationHib3 = row[immunizationHib3_index+4]
                immunizationHib3_index += 1
                if immunizationHib3 == "..":
                    c[7] = 'null'
                else:
                    c[7] = float(immunizationHib3)

        if line_count % 30 == 5:
            immunizationPol3_index = 0
            for c in country:
                # Immunization, Pol3 (% of one-year-old children)
                immunizationPol3 = row[
                    immunizationPol3_index+4]
                immunizationPol3_index += 1
                if immunizationPol3 == "..":
                    c[8] = 'null'
                else:
                    c[8] = float(immunizationPol3)

        if line_count % 30 == 6:
            immunizationMeasles_index = 0
            for c in country:
                # Immunization, measles (% of children ages 12-23 months)
                immunizationMeasles = row[immunizationMeasles_index+4]
                immunizationMeasles_index += 1
                if immunizationMeasles == "..":
                    c[9] = 'null'
                else:
                    c[9] = float(immunizationMeasles)

        if line_count % 30 == 9:
            numberOfSurgicalProcedures_index = 0
            for c in country:
                # Number of surgical procedures (per 100,000 population)
                numberOfSurgicalProcedures = row[numberOfSurgicalProcedures_index+4]
                numberOfSurgicalProcedures_index += 1
                if numberOfSurgicalProcedures == "..":
                    c[10] = 'null'
                else:
                    c[10] = float(numberOfSurgicalProcedures)

        if line_count % 30 == 11:
            numberOfDeathInfant_index = 0
            for c in country:
                # Number of infant deaths
                numberOfDeathInfant = row[numberOfDeathInfant_index+4]
                numberOfDeathInfant_index += 1
                if numberOfDeathInfant == "..":
                    c[11] = 'null'
                else:
                    c[11] = float(numberOfDeathInfant)

        if line_count % 10 == 0:
            numberOfDeathStillbirths_index = 0
            for c in country:
                # Number of stillbirths
                numberOfDeathStillbirths = row[numberOfDeathStillbirths_index+4]
                numberOfDeathStillbirths_index += 1
                if numberOfDeathStillbirths == "..":
                    c[12] = 'null'
                else:
                    c[12] = float(numberOfDeathStillbirths)


        if line_count % 30 == 12:
            numberOfDeathElderly_index = 0
            for c in country:
                # Number of deaths ages 5-9 years
                numberOfDeathElderly = row[numberOfDeathElderly_index+4]
                numberOfDeathElderly_index += 1
                if numberOfDeathElderly == "..":
                    c[13] = 'null'
                else:
                    c[13] = float(numberOfDeathElderly)

        if line_count % 30 == 13:
            numberOfHealthProfessionals_index = 0
            for c in country:
                # Community health workers (per 1,000 people)
                numberOfHealthProfessionals = row[numberOfHealthProfessionals_index+4]
                numberOfHealthProfessionals_index += 1
                if numberOfHealthProfessionals == "..":
                    c[14] = 'null'
                else:
                    c[14] = float(numberOfHealthProfessionals)


        if line_count % 30 == 14:
            contraceptivePrevalenceMarried_index = 0
            for c in country:
                # Contraceptive prevalence, any modern method (% of married women ages 15-49)
                contraceptivePrevalenceMarried = row[contraceptivePrevalenceMarried_index+4]
                contraceptivePrevalenceMarried_index += 1
                if contraceptivePrevalenceMarried == "..":
                    c[15] = 'null'
                else:
                    c[15] = float(contraceptivePrevalenceMarried)

        if line_count % 30 == 15:
            contraceptivePrevalenceUnmarried_index = 0
            for c in country:
                # Contraceptive prevalence, any modern method (% of sexually active unmarried women ages 15-49)
                contraceptivePrevalenceUnmarried = row[contraceptivePrevalenceUnmarried_index+4]
                contraceptivePrevalenceUnmarried_index += 1
                if contraceptivePrevalenceUnmarried == "..":
                    c[16] = 'null'
                else:
                    c[16] = float(contraceptivePrevalenceUnmarried)


        if line_count % 30 == 16:
            diabetesPrevalence_index = 0
            for c in country:
                # Diabetes prevalence (% of population ages 20 to 79)
                diabetesPrevalence = row[diabetesPrevalence_index+4]
                diabetesPrevalence_index += 1
                if diabetesPrevalence == "..":
                    c[17] = 'null'
                else:
                    c[17] = float(diabetesPrevalence)

        if line_count % 30 == 17:
            prevalenceOfAnemiaAmongChildren_index = 0
            for c in country:
                # Prevalence of anemia among children (% of children ages 6-59 months)
                prevalenceOfAnemiaAmongChildren = row[prevalenceOfAnemiaAmongChildren_index+4]
                prevalenceOfAnemiaAmongChildren_index += 1
                if prevalenceOfAnemiaAmongChildren == "..":
                    c[18] = 'null'
                else:
                    c[18] = float(prevalenceOfAnemiaAmongChildren)

        if line_count % 30 == 18:
            prevalenceOfOverweight_index = 0
            for c in country:
                # Prevalence of overweight (% of adults)
                prevalenceOfOverweight = row[prevalenceOfOverweight_index+4]
                prevalenceOfOverweight_index += 1
                if prevalenceOfOverweight == "..":
                    c[19] = 'null'
                else:
                    c[19] = float(prevalenceOfOverweight)

        if line_count % 30 == 19:
            prevalenceHIVAdults_index = 0
            for c in country:
                # Adults (ages 15+) living with HIV
                prevalenceHIVAdults = row[prevalenceHIVAdults_index+4]
                prevalenceHIVAdults_index += 1
                if prevalenceHIVAdults == "..":
                    c[20] = 'null'
                else:
                    c[20] = float(prevalenceHIVAdults)

        if line_count % 30 == 20:
            childrenWithHIV_index = 0
            for c in country:
                # Children (0-14) living with HIV
                childrenWithHIV = row[childrenWithHIV_index+4]
                childrenWithHIV_index += 1
                if childrenWithHIV == "..":
                    c[21] = 'null'
                else:
                    c[21] = float(childrenWithHIV)
            parsed.append(country)

        line_count += 1

with open('../parsedDataset/parsedHealth.csv', mode='w') as QOF_file:
    QOL_writer = csv.writer(
        QOF_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    QOL_writer.writerow(["id", "country", "year", "domesticHealthExpenditure", "hospitalBeds", "immunizationDPT",
                         "immunizationHepB3", "immunizationHib3", "immunizationPol3", "immunizationMeasles", "numberOfSurgicalProcedures",
                         "numberOfDeathInfant", "numberOfDeathStillbirths", "numberOfDeathElderly", "numberOfHealthProfessionals", "contraceptivePrevalenceMarried",
                         "contraceptivePrevalenceUnmarried", "diabetesPrevalence", "prevalenceOfAnemiaAmongChildren", "prevalenceOfOverweight",
                         "adultsWithHIV", "childrenWithHIV"])
    for country in parsed:
        for row in country:
            QOL_writer.writerow(row)
