#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS factTable;
        """,
        """
        DROP TABLE IF EXISTS country;
        """,
        """
        DROP TABLE IF EXISTS country;
        """,
        """
        DROP TABLE IF EXISTS month;
        """,
        """
        DROP TABLE IF EXISTS education;
        """,
        """
        DROP TABLE IF EXISTS health;
        """,
        """
        DROP TABLE IF EXISTS qualityOfLife;
        """,
        """
        DROP TABLE IF EXISTS population;
        """,
        """
        DROP TABLE IF EXISTS event;
        """,
        """
        CREATE TABLE country (
            countryKey SERIAL PRIMARY KEY,
            name varchar(255) NOT NULL,
            region varchar(255) NOT NULL,
            continent varchar(255) NOT NULL,
            currency varchar(255),
            capital varchar(255) NOT NULL,
            totalPopulation integer,
            birthRate float,
            deathRate float,
            fertilityRate float,
            GDP float
        );
        """,
        """
        CREATE TABLE month (
            monthKey SERIAL PRIMARY KEY,
            name varchar(255) NOT NULL,
            quarter integer NOT NULL,
            year integer NOT NULL,
            decade integer NOT NULL
        );
        """,
        """
        CREATE TABLE education (
            educationKey SERIAL PRIMARY KEY,
            primarySchoolEnrollment float,
            secondarySchoolEnrollment float,
            femalePrimaryCompletionRate float,
            malePrimaryCompletionRate float,
            totalPublicSpendingOnEducation float,
            adultFemaleLiteracyRate float,
            adultMaleLiteracyRate float,
            youthFemaleLiteracyRate float,
            youthMaleLiteracyRate float,
            maleChildrenOutOfPrimarySchool integer,
            femaleChildrenOutOfPrimarySchool integer,
            femaleAdolescentsOutOfPrimarySchool integer,
            maleAdolescentsOutOfPrimarySchool integer
        );
        """,
        """
        CREATE TABLE health (
            healthKey SERIAL PRIMARY KEY,
            domesticHealthExpenditure float,
            hospitalBeds integer,
            immunizationDPT float,
            immunizationHepB3 float,
            immunizationHib3 float,
            immunizationPol3 float,
            immunizationMeasles float,
            numberOfSurgicalProcedures integer,
            numberOfDeathInfant integer,
            numberOfDeathStillbirths integer,
            numberOfDeathElderly integer,
            numberOfHealthProfessionals integer,
            contraceptivePrevalence float,
            diabetesPrevalence float,
            prevalenceHIVTotal float,
            prevalenceOfAnemiaAmongChildren float,
            prevalenceOfOverweight float,
            adultsWithHIV float,
            childrenWithHIV float
        );
        """,
        """
        CREATE TABLE qualityOfLife (
            qualityOfLifeKey SERIAL PRIMARY KEY,
            peopleUsingSafeDrinkingWaterServices integer,
            peopleUsingBasicDrinkingWaterServices integer,
            peoplePracticingOpenDefecation integer,
            peopleUsingBasicSanitationServices integer,
            peopleUsingSafeSanitationServices integer,
            ruralPeopleUsingBasicSanitationServices integer,
            urbanPeopleUsingBasicSanitationServices integer,
            peopleWithBasicHandwashingFacilities integer,
            ruralPeopleWithBasicHandwashingFacilities integer,
            urbanPeopleWithBasicHandwashingFacilities integer,
            maleUnemploymentRate float,
            femaleUnemploymentRate float,
            totalUnemploymentRate float,
            yearsOfMaternalLeave float
        );
        """,
        """
        CREATE TABLE population (
            populationKey SERIAL PRIMARY KEY,
            femaleLifeExpectancy float,
            maleLifeExpectancy float,
            totalLifeExpectancy float,
            netMigration integer,
            ageDependencyRatio float,
            povertyHeadcountRatio float,
            populationGrowth float,
            ruralPopulationGrowth float,
            urbanPopulationGrowth float,
            populationSize integer,
            averageAge float,
            infantMortalityRate float
        );
        """,
        """
        CREATE TABLE event (
            eventKey SERIAL PRIMARY KEY,
            name varchar(255) NOT NULL,
            description text,
            startDate date,
            endDate date,
            startMonth integer,
            endMonth integer,
            outcome text,
            casualties integer,
            economicDamage float
        );
        """,
        """
        CREATE TABLE factTable (
            key SERIAL PRIMARY KEY,
            qualityOfLifeIndex float,
            developmentIndex float,
            humanDevelopmentIndex float,
            countryKey SERIAL,
            monthKey SERIAL,
            educationKey SERIAL,
            healthKey SERIAL,
            qualityOfLifeKey SERIAL,
            populationKey SERIAL,
            eventKey SERIAL,
            CONSTRAINT fk_country
                  FOREIGN KEY(countryKey)
            	        REFERENCES country(countryKey),
            CONSTRAINT fk_month
                  FOREIGN KEY(monthKey)
            	        REFERENCES month(monthKey),
            CONSTRAINT fk_education
                  FOREIGN KEY(educationKey)
            	        REFERENCES education(educationKey),
            CONSTRAINT fk_health
                  FOREIGN KEY(healthKey)
            	        REFERENCES health(healthKey),
            CONSTRAINT fk_qualityOfLife
                  FOREIGN KEY(qualityOfLifeKey)
            	        REFERENCES qualityOfLife(qualityOfLifeKey),
            CONSTRAINT fk_population
                  FOREIGN KEY(populationKey)
            	        REFERENCES population(populationKey),
            CONSTRAINT fk_event
                  FOREIGN KEY(eventKey)
            	        REFERENCES event(eventKey)
        );
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def load_countries():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('parsedCountry.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'country', sep=',')
    conn.commit()


if __name__ == '__main__':
    create_tables()
#     load_countries()