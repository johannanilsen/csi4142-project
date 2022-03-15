#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS country (
            id SERIAL PRIMARY KEY,
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
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS month (
            MonthKey SERIAL PRIMARY KEY,
            Name varchar(255) NOT NULL,
            Quarter integer NOT NULL,
            Year integer NOT NULL,
            Decade integer NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS education (
            EducationKey SERIAL PRIMARY KEY,
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
        )
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