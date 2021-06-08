#from file_handler.file_reader import CsvReader
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from file_handler.csv_reader import CsvReader
import country_converter as coco
FILE_ADDRESS="data/archive/LifeExpectancyData.csv"
FILE_NAME="LIFE_EXPECTANCY_DATA"
if __name__ == '__main__':

    reader = CsvReader(FILE_ADDRESS,FILE_NAME)
    df = reader.read_data()

    # First step: data preprocessing
    # one hot encodeing for countries and status
    dummy_df = pd.get_dummies(df, columns=["Country","Status"], prefix=["Country","Status"] )
    # Second step: do prediction
    y = dummy_df['Life expectancy ']
    X = dummy_df.drop('Life expectancy ',axis=1)

   # X.fillna(X.mean())
    xtrain,xtest,ytrain,ytest = train_test_split(X,y,random_state=42,test_size=0.2)
    LR = LinearRegression()
    # fitting the training data
    xtrain.fillna(xtrain.mean(), inplace=True)
    xtest.fillna(xtest.mean(), inplace=True)
    ytrain.fillna(ytrain.mean(), inplace=True)
    ytest.fillna(ytest.mean(), inplace=True)

    LR.fit(xtrain, ytrain)
    yprediction  = LR.predict(xtest)

    print(LR.coef_)
    score = r2_score(ytest, yprediction)
    print('r2socre is ', score)