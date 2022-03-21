import csv


parsed = []
with open('../datasets/education.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    key = 1

    for row in csv_reader:
        if line_count % 13 == 2:
            country = [[0 for i in range(15)] for i in range(16)]
            year = 2005
            country_name = row[0]

            primarySchoolEnrollment_index = 0
            for c in country:
                # init
                c[0] = key
                c[1] = country_name
                c[2] = year

                year += 1
                key += 1
                # School enrollment, primary (% gross)'
                primarySchoolEnrollment = row[primarySchoolEnrollment_index+4]
                primarySchoolEnrollment_index += 1
                if primarySchoolEnrollment == "..":
                    c[3] = 'null'
                else:
                    c[3] = float(primarySchoolEnrollment)

        if line_count % 13 == 3:
            secondarySchoolEnrollment_index = 0
            for c in country:
                # School enrollment, secondary (% gross)
                secondarySchoolEnrollment = row[secondarySchoolEnrollment_index+4]
                secondarySchoolEnrollment_index += 1
                if secondarySchoolEnrollment == "..":
                    c[4] = 'null'
                else:
                    c[4] = float(secondarySchoolEnrollment)

        if line_count % 13 == 4:
            femalePrimaryCompletionRate_index = 0
            for c in country:
                # Primary completion rate, female (% of relevant age group)
                femalePrimaryCompletionRate = row[femalePrimaryCompletionRate_index+4]
                femalePrimaryCompletionRate_index += 1
                if femalePrimaryCompletionRate == "..":
                    c[5] = 'null'
                else:
                    c[5] = float(femalePrimaryCompletionRate)

        if line_count % 13 == 5:
            malePrimaryCompletionRate_index = 0
            for c in country:
                # Primary completion rate, male (% of relevant age group)
                malePrimaryCompletionRate = row[malePrimaryCompletionRate_index+4]
                malePrimaryCompletionRate_index += 1
                if malePrimaryCompletionRate == "..":
                    c[6] = 'null'
                else:
                    c[6] = float(malePrimaryCompletionRate)

        if line_count % 13 == 6:
            adultFemaleLiteracyRate_index = 0
            for c in country:
                # Literacy rate, adult female (% of females ages 15 and above)
                adultFemaleLiteracyRate = row[adultFemaleLiteracyRate_index+4]
                adultFemaleLiteracyRate_index += 1
                if adultFemaleLiteracyRate == "..":
                    c[7] = 'null'
                else:
                    c[7] = float(adultFemaleLiteracyRate)

        if line_count % 13 == 7:
            adultMaleLiteracyRate_index = 0
            for c in country:
                # Literacy rate, adult male (% of males ages 15 and above)
                adultMaleLiteracyRate = row[adultMaleLiteracyRate_index+4]
                adultMaleLiteracyRate_index += 1
                if adultMaleLiteracyRate == "..":
                    c[8] = 'null'
                else:
                    c[8] = float(adultMaleLiteracyRate)

        if line_count % 13 == 8:
            youthFemaleLiteracyRate_index = 0
            for c in country:
                # Literacy rate, youth female (% of females ages 15-24)
                youthFemaleLiteracyRate = row[youthFemaleLiteracyRate_index+4]
                youthFemaleLiteracyRate_index += 1
                if youthFemaleLiteracyRate == "..":
                    c[9] = 'null'
                else:
                    c[9] = float(youthFemaleLiteracyRate)

        if line_count % 13 == 9:
            youthMaleLiteracyRate_index = 0
            for c in country:
                # Literacy rate, youth male (% of males ages 15-24)
                youthMaleLiteracyRate = row[youthMaleLiteracyRate_index+4]
                youthMaleLiteracyRate_index += 1
                if youthMaleLiteracyRate == "..":
                    c[10] = 'null'
                else:
                    c[10] = float(youthMaleLiteracyRate)

        if line_count % 13 == 10:
            femaleChildrenOutOfPrimarySchool_index = 0
            for c in country:
                # Children out of school, female (% of female primary school age)
                femaleChildrenOutOfPrimarySchool = row[femaleChildrenOutOfPrimarySchool_index+4]
                femaleChildrenOutOfPrimarySchool_index += 1
                if femaleChildrenOutOfPrimarySchool == "..":
                    c[11] = 'null'
                else:
                    c[11] = float(femaleChildrenOutOfPrimarySchool)

        if line_count % 13 == 11:
            maleChildrenOutOfPrimarySchool_index = 0
            for c in country:
                # Children out of school, male (% of male primary school age)
                maleChildrenOutOfPrimarySchool = row[maleChildrenOutOfPrimarySchool_index+4]
                maleChildrenOutOfPrimarySchool_index += 1
                if maleChildrenOutOfPrimarySchool == "..":
                    c[12] = 'null'
                else:
                    c[12] = float(maleChildrenOutOfPrimarySchool)
        if line_count % 13 == 12:
            femaleAdolescentsOutOfPrimarySchool_index = 0
            for c in country:
                # Adolescents out of school, female (% of female primary school age)
                femaleAdolescentsOutOfPrimarySchool = row[femaleAdolescentsOutOfPrimarySchool_index+4]
                femaleAdolescentsOutOfPrimarySchool_index += 1
                if femaleAdolescentsOutOfPrimarySchool == "..":
                    c[13] = 'null'
                else:
                    c[13] = float(femaleAdolescentsOutOfPrimarySchool)

        if line_count % 13 == 0:
            maleAdolescentsOutOfPrimarySchool_index = 0
            for c in country:
                # Adolescents out of school, male (% of male primary school age)
                maleAdolescentsOutOfPrimarySchool = row[maleAdolescentsOutOfPrimarySchool_index+4]
                maleAdolescentsOutOfPrimarySchool_index += 1
                if maleAdolescentsOutOfPrimarySchool == "..":
                    c[14] = 'null'
                else:
                    c[14] = float(maleAdolescentsOutOfPrimarySchool)

            parsed.append(country)
        line_count += 1
print(parsed[0])


with open('../parsedDataset/parsedEducation.csv', mode='w') as country_file:
    country_writer = csv.writer(
        country_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    country_writer.writerow(["id","country","year", "primarySchoolEnrollment", "secondarySchoolEnrollment", "femalePrimaryCompletionRate",
                             "malePrimaryCompletionRate",
                             "adultFemaleLiteracyRate", "adultMaleLiteracyRate", "youthFemaleLiteracyRate",
                             "youthMaleLiteracyRate", "maleChildrenOutOfPrimarySchool", "femaleChildrenOutOfPrimarySchool",
                             "femaleAdolescentsOutOfPrimarySchool", "maleAdolescentsOutOfPrimarySchool"])
    for country in parsed:
        for row in country:
            country_writer.writerow(row)
