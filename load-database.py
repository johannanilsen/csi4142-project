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
            year integer NOT NULL,
            language varchar(255) NOT NULL,
            continent varchar(255) NOT NULL,
            currency varchar(255),
            capital varchar(255) NOT NULL,
            population varchar(255),
            birthRate varchar(255),
            deathRate varchar(255),
            fertilityRate varchar(255),
            GDP varchar(255)
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
            country varchar(255),
            year integer NOT NULL,
            primarySchoolEnrollment varchar(255),
            secondarySchoolEnrollment varchar(255),
            femalePrimaryCompletionRate varchar(255),
            malePrimaryCompletionRate varchar(255),
            adultFemaleLiteracyRate varchar(255),
            adultMaleLiteracyRate varchar(255),
            youthFemaleLiteracyRate varchar(255),
            youthMaleLiteracyRate varchar(255),
            maleChildrenOutOfPrimarySchool varchar(255),
            femaleChildrenOutOfPrimarySchool varchar(255),
            femaleAdolescentsOutOfPrimarySchool varchar(255),
            maleAdolescentsOutOfPrimarySchool varchar(255)
        );
        """,
        """
        CREATE TABLE health (
            healthKey SERIAL PRIMARY KEY,
            country varchar(255),
            year integer,
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
            contraceptivePrevalenceMarried float,
            contraceptivePrevalenceUnmarried float,
            diabetesPrevalence float,
            prevalenceOfAnemiaAmongChildren float,
            prevalenceOfOverweight float,
            adultsWithHIV float,
            childrenWithHIV float
        );
        """,
        """
        CREATE TABLE qualityOfLife (
            qualityOfLifeKey SERIAL PRIMARY KEY,
            country varchar(255),
            year integer,
            peopleUsingBasicDrinkingWaterServices varchar(255),
            peoplePracticingOpenDefecation varchar(255),
            peopleUsingBasicSanitationServices varchar(255),
            peopleUsingSafeSanitationServices varchar(255),
            ruralPeopleUsingBasicSanitationServices varchar(255),
            urbanPeopleUsingBasicSanitationServices varchar(255),
            peopleWithBasicHandwashingFacilities varchar(255),
            ruralPeopleWithBasicHandwashingFacilities varchar(255),
            urbanPeopleWithBasicHandwashingFacilities varchar(255),
            maleUnemploymentRate varchar(255),
            femaleUnemploymentRate varchar(255),
            totalUnemploymentRate varchar(255),
            yearsOfMaternalLeave varchar(255)
        );
        """,
        """
        CREATE TABLE population (
            populationKey SERIAL PRIMARY KEY,
            country varchar(255),
            femaleLifeExpectancy float,
            maleLifeExpectancy float,
            totalLifeExpectancy float,
            netMigration float,
            ageDependencyRatio varchar(255),
            povertyHeadcountRatio float,
            populationGrowth varchar(255),
            ruralPopulationGrowth varchar(255),
            urbanPopulationGrowth varchar(255),
            populationSize float,
            averageAge float,
            infantMortalityRate float
        );
        """,
        """
        CREATE TABLE event (
            eventKey SERIAL PRIMARY KEY,
            country varchar(255) NOT NULL,
            name varchar(255) NOT NULL,
            description text,
            startDate date,
            endDate date,
            startMonth integer,
            endMonth integer,
            outcome text,
            casualties integer,
            economicDamage varchar(255)
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
    with open('parsedDataset/parsedCountry.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'country', sep=',')
    conn.commit()

def load_education():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('parsedDataset/parsedEducation.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'education', sep=',')
    conn.commit()

def load_month():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('parsedDataset/parsedMonth.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'month', sep=',')
    conn.commit()

def load_population():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('parsedDataset/parsedPopulation.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'population', sep=',')
    conn.commit()

def load_qualityOfLife():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('parsedDataset/parsedQualityOfLife.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'qualityoflife', sep=',')
    conn.commit()

def load_events():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    with open('parsedDataset/parsedEvents.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'event', sep=';')
    conn.commit()


if __name__ == '__main__':
    create_tables()
    load_countries()
    load_education()
    load_month()
    load_population()
    load_qualityOfLife()
    load_events()