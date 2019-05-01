import pandas as pd

ALERT = 'alert'
WARNING = 'warning'
STABLE = 'stable'
SUSTAINABLE = 'sustainable'


def discretize_decision_value(file_path, target_file_path):
    df = pd.read_excel(file_path)
    total_score_list = df['Total'].tolist()
    tag_list = []
    for index in range(len(total_score_list)):
        score = total_score_list[index]
        if 90.0 <= score <= 120.0:
            tag_list.append(ALERT)
        elif 60.0 <= score <= 89.9:
            tag_list.append(WARNING)
        elif 30.0 <= score <= 59.9:
            tag_list.append(STABLE)
        else:
            tag_list.append(SUSTAINABLE)
    df.insert(4, 'classification', tag_list)
    # print(df.info())
    # print(df['category'])
    df.drop(['Year', 'Rank'], axis=1, inplace=True)
    # df.to_json(target_file_path)
    df.to_csv(target_file_path)


def append_new_features(fsi_file_path, new_features_file_path, target_file_path):
    df_new_features = pd.read_csv(new_features_file_path)
    co2_dict = {}
    debt_dict = {}
    pm_dict = {}
    secondary_school_dict = {}
    high_school_dict = {}
    total_tax_dict = {}
    for index, row in df_new_features.iterrows():
        co2_dict[row['Country']] = row['co2']
        debt_dict[row['Country']] = row['debt']
        pm_dict[row['Country']] = row['PM2.5']
        secondary_school_dict[row['Country']] = row['secondary_school']
        high_school_dict[row['Country']] = row['high_school']
        total_tax_dict[row['Country']] = row['total_tax']

    df = pd.read_csv(fsi_file_path)
    country_list = df['Country'].tolist()
    co2_list = []
    for index in range(len(country_list)):
        country = country_list[index]
        if (country in co2_dict.keys()):
            co2_list.append(co2_dict[country])
        else:
            co2_list.append(round(sum(co2_dict.values()) / len(co2_dict), 2))

    debt_list = []
    for index in range(len(country_list)):
        country = country_list[index]
        if (country in debt_dict.keys()):
            debt_list.append(round(debt_dict[country], 2))
        else:
            debt_list.append(round(sum(debt_dict.values()) / len(debt_dict), 2))

    pm_list = []
    for index in range(len(country_list)):
        country = country_list[index]
        if (country in pm_dict.keys()):
            pm_list.append(round(pm_dict[country], 2))
        else:
            pm_list.append(round(sum(pm_dict.values()) / len(pm_dict), 2))

    secondary_school_list = []
    for index in range(len(country_list)):
        country = country_list[index]
        if (country in secondary_school_dict.keys()):
            secondary_school_list.append(round(secondary_school_dict[country], 2))
        else:
            secondary_school_list.append(round(sum(secondary_school_dict.values()) / len(secondary_school_dict), 2))

    high_school_list = []
    for index in range(len(country_list)):
        country = country_list[index]
        if (country in high_school_dict.keys()):
            high_school_list.append(round(high_school_dict[country], 2))
        else:
            high_school_list.append(round(sum(high_school_dict.values()) / len(high_school_dict), 2))

    total_tax_list = []
    for index in range(len(country_list)):
        country = country_list[index]
        if (country in total_tax_dict.keys()):
            total_tax_list.append(round(total_tax_dict[country], 2))
        else:
            total_tax_list.append(round(sum(total_tax_dict.values()) / len(total_tax_dict), 2))
    print(df.info())
    # df.insert(df.shape[1], 'co2', co2_list)
    # df.insert(df.shape[1], 'debt', debt_list)
    # df.insert(df.shape[1], 'pm2.5', pm_list)
    # df.insert(df.shape[1], 'secondary_school', secondary_school_list)
    # df.insert(df.shape[1], 'high_school', high_school_list)
    # df.insert(df.shape[1], 'total_tax', total_tax_list)
    # df.to_csv(target_file_path)


def pre_process_new_features(file_path, target_file_path):
    df = pd.read_excel(file_path)
    print(df.info())
    df.fillna(df.mean(), inplace=True)
    print(df.info())
    df.to_csv(target_file_path)


if __name__ == '__main__':
    # discretize_decision_value('./dataset/fsi-2012.xlsx', './dataset/fsi_2012.csv')
    # discretize_decision_value('./dataset/fsi-2013.xlsx', './dataset/fsi_2013.csv')
    # discretize_decision_value('./dataset/fsi-2014.xlsx', './dataset/fsi_2014.csv')
    # pre_process_new_features('./dataset/new_features_2012.xlsx', './dataset/features_2012.csv')
    # pre_process_new_features('./dataset/new_features_2013.xlsx', './dataset/features_2013.csv')
    # pre_process_new_features('./dataset/new_features_2014.xlsx', './dataset/features_2014.csv')
    append_new_features('./dataset/fsi_2012.csv', './dataset/features_2012.csv', './dataset/fsi-new-2012.csv')
    # append_new_features('./dataset/fsi_2013.csv', './dataset/features_2013.csv', './dataset/fsi-new-2013.csv')
    # append_new_features('./dataset/fsi_2014.csv', './dataset/features_2014.csv', './dataset/fsi-new-2014.csv')
