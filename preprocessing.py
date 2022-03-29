import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder


def decision_tree(X_train, X_test, y_train, y_test, path):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    predicted_y = clf.predict(X_test)
    # tn, fp, fn, tp = confusion_matrix(y_test, predicted_y).ravel()
    print(metrics.confusion_matrix(y_test, predicted_y))
    print(metrics.classification_report(y_test, predicted_y))

    report = metrics.classification_report(y_test, predicted_y, output_dict=True)
    df = pd.DataFrame(report).transpose()
    df.to_csv(os.path.join(path, 'decision_tree.csv'))


def gradient_boost(X_train, X_test, y_train, y_test, path):
    clf = GradientBoostingClassifier(n_estimators=25, learning_rate=1.0, max_depth=20, random_state=0)
    clf.fit(X_train, y_train)

    predicted_y = clf.predict(X_test)
    # tn, fp, fn, tp = confusion_matrix(y_test, predicted_y).ravel()
    print(metrics.confusion_matrix(y_test, predicted_y))
    print(metrics.classification_report(y_test, predicted_y))

    report = metrics.classification_report(y_test, predicted_y, output_dict=True)
    df = pd.DataFrame(report).transpose()
    df.to_csv(os.path.join(path, 'gradient_boost.csv'))


def random_forest(X_train, X_test, y_train, y_test, path):
    clf = RandomForestClassifier(random_state=314)
    clf.fit(X_train, y_train)
    predicted_y = clf.predict(X_test)
    # tn, fp, fn, tp = confusion_matrix(y_test, predicted_y).ravel()
    print(metrics.confusion_matrix(y_test, predicted_y))
    print(metrics.classification_report(y_test, predicted_y))

    report = metrics.classification_report(y_test, predicted_y, output_dict=True)
    df = pd.DataFrame(report).transpose()
    df.to_csv(os.path.join(path, 'random_forest.csv'))


def summarization(og_df, graphs_dir):
    countries = ["Argentina", "United States", "Canada", "Mexico", "Mali", "Nigeria", "Pakistan", "Niger", "Ethiopia"]

    for country in countries:
        if 'name' in og_df:  # Select the country
            df = og_df.loc[og_df['name'] == country]
        else:
            df = og_df.loc[og_df['country'] == country]

        # Effect of year changes on country's GDP
        if 'GDP' in df:  # Country dataset
            plt.plot(df['year'], df['GDP'])
            plt.xlabel("Year")
            plt.ylabel("GDP")
            plt.title("GDP of " + country + " over time")
            plt.savefig(graphs_dir + '\\GDP\\' + country + '_GDP.png')

        # Effect of year changes on country's literacy rate
        if 'adultFemaleLiteracyRate' in df:  # Education dataset
            plt.plot(df['year'], df['adultFemaleLiteracyRate'],
                     label="adult female literacy rate")

            plt.plot(df['year'], df['adultMaleLiteracyRate'],
                     label="adult male literacy rate")

            plt.xlabel("Year")
            plt.ylabel("Literacy rate")
            plt.legend()
            plt.title("Literacy rate of " + country + " over time")
            plt.savefig(graphs_dir + '\\literacy_rate\\' + country + '_literacy_rate.png')

        if 'immunizationDPT' in df:  # Health dataset
            plt.plot(df['numberOfDeathElderly'], df['immunizationHepB3'],
                     label="HepB3 immunization rate")

            plt.plot(df['numberOfDeathElderly'], df['immunizationHib3'],
                     label="Hip3 immunization rate")

            plt.xlabel("Elderly Deaths")
            plt.ylabel("Immunization Rates")
            plt.legend()
            plt.title("Effect of immunizations on elderly deaths in " + country)
            plt.savefig(graphs_dir + '\\immunizations\\' + country + '_immunizations.png')

        if 'totalLifeExpectancy' in df:  # Population dataset
            plt.plot(df['totalLifeExpectancy'], df['povertyHeadcountRatio'])

            plt.xlabel("Total life expectancy")
            plt.ylabel("Poverty Headcount")
            plt.legend()
            plt.title("Effect of poverty on life expectancy in " + country)
            plt.savefig(graphs_dir + '\\life_expectancy\\' + country + '_life_expectancy.png')

        plt.show()


def transformation(df):
    """Perform data preprocessing"""

    # Drop columns with majority null values
    if 'maleChildrenOutOfPrimarySchool' in df:  # In education dataset
        df = df.drop('maleChildrenOutOfPrimarySchool', 1)
        df = df.drop('femaleChildrenOutOfPrimarySchool', 1)
        df = df.drop('femaleAdolescentsOutOfPrimarySchool', 1)
        df = df.drop('maleAdolescentsOutOfPrimarySchool', 1)

    if 'numberOfHealthProfessionals' in df:  # In health dataset
        df = df.drop('numberOfHealthProfessionals', 1)
        df = df.drop('contraceptivePrevalenceMarried', 1)
        df = df.drop('contraceptivePrevalenceUnmarried', 1)

    # Fill in null values with mean value of the column for that country
    if 'name' in df:
        df = df.fillna(df.groupby('name').transform('mean'))

    if 'country' in df:
        df = df.fillna(df.groupby('country').transform('mean'))

    return df


def encode_df(dataframe):
    """Encode string values to integers"""
    le = LabelEncoder()
    for column in dataframe.columns:
        dataframe[column] = le.fit_transform(dataframe[column])
    return dataframe


def assign_label(i):
    if 0 <= i < 40:
        return 'low'
    if 40 <= i < 70:
        return 'medium'
    if 70 <= i <= 100:
        return 'high'


def classsification(df):
    # Predict which countries will have a Human Development Index less than 0.7
    X = df.drop(['developed_status'], axis=1).values
    y = df['developed_status'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, shuffle=True)

    X_train[np.isnan(X_train)] = 0  # Fill nan with 0
    X_test[np.isnan(X_test)] = 0  # Fill nan with 0

    y_train = ["medium" if x is None else x for x in y_train]  # Fill nan with medium
    y_test = ["medium" if x is None else x for x in y_test]  # Fill nan with medium

    results_dir = os.path.abspath(os.path.join(__file__, "../")) + "\\results"

    decision_tree(X_train, X_test, y_train, y_test, results_dir)
    gradient_boost(X_train, X_test, y_train, y_test, results_dir)
    random_forest(X_train, X_test, y_train, y_test, results_dir)


def main():
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parsedDataset'))
    graphs_dir = os.path.abspath(os.path.join(__file__, "../")) + "\\graphs"
    # removed events
    dimensions = ["parsedCountry", "parsedEducation", "parsedHealth", "parsedMonth",
                  "parsedPopulation", "parsedQualityOfLife", "parsedFactTable"]
    frames = []

    for dim in dimensions:
        file_path = data_dir + "\\" + dim + ".csv"
        df = pd.read_csv(file_path)

        df2 = transformation(df)
        # summarization(df2, graphs_dir)
        df3 = encode_df(df2)

        if 'name' not in df3:
            frames.append(df3)

    combined = pd.concat(frames)
    combined = combined[combined['humanDevelopmentIndex'].notna()]  # Drop null values for HDI

    #  Add labels for development status of the country: {low, med, high}
    combined['developed_status'] = combined['humanDevelopmentIndex'].apply(assign_label)

    classsification(combined)


if __name__ == "__main__":
    main()