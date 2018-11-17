import numpy
import pandas
import statsmodels.api as sm


def simple_heuristic(file_path, param):
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.

    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models 
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted

    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the 
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data. 

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic disaster.

    You prediction should be 78% accurate or higher.

    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.

    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survied or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0

    You can also look at the Titantic data that you will be working with
    at the link below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    predicted = []

    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']

        def is_woman(passenger):
            return passenger['Sex'] == 'female'
        def is_young(passenger):
            return passenger['Age'] < 18
        def is_rich_and_bold(passenger):
            return passenger['Pclass'] < 3
        def paid_much_for_ticket(passenger):
            val = 0
            # return passenger['SibSp'] > 0
            ##single fathers
            # return (passenger['Sex'] == 'male') and (passenger['Parch'] == 1 and passenger['SibSp'] > 0)
            ## all kids
            # return (passenger['Age'] in range(0,16))
            ## no-kid husbands
            # return (passenger['Sex'] == 'male') and (passenger['Parch'] == 0 and passenger['SibSp'] == 1)
            ## kid with siblings
            # val = passenger['Age'] < 7
            ## alone singe young man
            # val2 = passenger['Age'] < 30 and (passenger['Parch'] == 0 and passenger['SibSp'] > 0)
            # val = val or val2
            # expensive tickets
            val = passenger['Fare'] > 270
            ## young father
            ## only having wife/sibling, no kids
            # val = passenger['SibSp'] == 1 and passenger['Parch'] == 0
            return val

        if is_woman(passenger) or (is_young(passenger) and is_rich_and_bold(passenger)) or paid_much_for_ticket(passenger):
            predictions[passenger_id] = 1
            predicted.append(1)
        else:
            predictions[passenger_id] = 0
            predicted.append(0)

    df['predicted'] = predicted


    return predictions, df

if __name__ == '__main__':
    path = "c:\\Users\\lukasz\\Documents\\udacity\\titanic_data.csv"

    (predictions, df) = simple_heuristic(path, param=None)
    df['valid'] = df['predicted'] == df['Survived']
    prediction_failed_df = df[df['valid'] == False]
    # print(prediction_failed_df.head())
    prediction_failed_df.to_csv('prediction_failed.csv')
    prediction_succeeded_df = df[df['valid'] == True]
    succeeded = len(prediction_succeeded_df.index)
    total = len(df.index)
    # print(f'Total {total}'
    #       f', succeded for {succeeded}'
    #       f', failed for {len(prediction_failed_df.index)}')
    print(f'Succeded for percent {succeeded/total}')
    # print(predictions)
    # survived = list(n for n in predictions.items() if n[1] == 1)
    # print(f'Survived {len(survived)} from total {len(predictions)}')

