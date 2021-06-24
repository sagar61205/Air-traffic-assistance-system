from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics  import r2_score
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from xgboost import XGBRegressor

class Model_Finder:
    """
                This class shall  be used to find the model with best accuracy and AUC score.
                Written By: iNeuron Intelligence
                Version: 1.0
                Revisions: None

                """

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.clf = RandomForestRegressor()
        self.xgb = XGBRegressor()

    def get_best_params_for_random_forest(self,train_x,train_y):
        """
                                Method Name: get_best_params_for_random_forest
                                Description: get the parameters for Random Forest Algorithm which give the best accuracy.
                                             Use Hyper Parameter Tuning.
                                Output: The model with the best parameters
                                On Failure: Raise Exception

                                Written By: iNeuron Intelligence
                                Version: 1.0
                                Revisions: None

                        """
        self.logger_object.log(self.file_object, 'Entered the get_best_params_for_random_forest method of the Model_Finder class')
        try:
            # initializing with different combination of parameters
            self.param_grid = {"n_estimators": [100,500,700], "criterion": ['mse'],
                               "max_depth": [4,6,8], "max_features": ['auto','log2'], "min_samples_leaf": [5,7,9]}

            #Creating an object of the Grid Search class
            self.grid = GridSearchCV(estimator=self.clf, param_grid=self.param_grid, cv=5,  verbose=3)
            #finding the best parameters
            self.grid.fit(train_x,train_y)

            #extracting the best parameters
            self.criterion = self.grid.best_params_['criterion']
            self.max_depth = self.grid.best_params_['max_depth']
            self.max_features = self.grid.best_params_['max_features']
            self.n_estimators = self.grid.best_params_['n_estimators']
            self.min_samples_leaf = self.grid.best_params_['min_samples_leaf']

            #creating a new model with the best parameters
            self.clf = RandomForestRegressor(n_estimators=self.n_estimators, criterion=self.criterion,
                                              max_depth=self.max_depth, max_features=self.max_features,min_samples_leaf=self.min_samples_leaf,n_jobs=-1)
            # training the mew model
            self.clf.fit(train_x,train_y)
            self.logger_object.log(self.file_object,
                                   'Random Forest best params: '+str(self.grid.best_params_)+'. Exited the get_best_params_for_random_forest method of the Model_Finder class')

            return self.clf
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_params_for_random_forest method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Random Forest Parameter tuning  failed. Exited the get_best_params_for_random_forest method of the Model_Finder class')
            raise Exception()


    def get_best_params_for_xgboost(self,train_x,train_y):

        """
                                        Method Name: get_best_params_for_xgboost
                                        Description: get the parameters for XGBoost Algorithm which give the best accuracy.
                                                     Use Hyper Parameter Tuning.
                                        Output: The model with the best parameters
                                        On Failure: Raise Exception

                                        Written By: iNeuron Intelligence
                                        Version: 1.0
                                        Revisions: None

                                """
        self.logger_object.log(self.file_object,
                               'Entered the get_best_params_for_xgboost method of the Model_Finder class')
        try:
            # initializing with different combination of parameters
            self.param_grid_xgboost = {                 # Entire hyper parameter tuning is done in the
                                                        # EDA section in the jupyter notebook.
                                                        # The selected values are written here just to save computational time
                'learning_rate': [0.1,0.01,0.05,0.2],
                'max_depth': [2,4,6,8],
                'n_estimators': [500,700],
                'min_child_weight': [7,8,9],
                'subsample': [0.5,0.7,0.8],
                'colsample_bytree': [0.5,0.7,0.8],
                'reg_lambda': [0.001,0.005],
                'reg_alpha': [0.001,0.005]
            }



            # Creating an object of the Grid Search class
            self.grid = GridSearchCV(estimator=self.xgb,param_grid=self.param_grid_xgboost, verbose=3,cv=5,n_jobs=-1)
            # finding the best parameters
            self.grid.fit(train_x,train_y)

            # extracting the best parameters
            self.learning_rate = self.grid.best_params_['learning_rate']
            self.max_depth = self.grid.best_params_['max_depth']
            self.n_estimators = self.grid.best_params_['n_estimators']
            self.min_child_weight = self.grid.best_params_['min_child_weight']
            self.subsample = self.grid.best_params_['subsample']
            self.colsample_bytree = self.grid.best_params_['colsample_bytree']
            self.reg_lambda = self.grid.best_params_['reg_lambda']
            self.reg_alpha = self.grid.best_params_['reg_alpha']

            # creating a new model with the best parameters
            self.xgb = XGBRegressor(learning_rate=self.learning_rate, max_depth=self.max_depth, n_estimators=self.n_estimators,
                                     min_child_weight=self.min_child_weight,subsample=self.subsample,
                                    colsample_bytree=self.colsample_bytree,reg_lambda=self.reg_lambda,reg_alpha=self.reg_alpha,n_jobs=-1
                                    )
            # training the mew model
            self.xgb.fit(train_x,train_y)
            self.logger_object.log(self.file_object,
                                   'XGBoost best params: ' + str(
                                       self.grid.best_params_) + '. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            return self.xgb
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_params_for_xgboost method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'XGBoost Parameter tuning  failed. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            raise Exception()


    def get_best_model(self,train_x,train_y,test_x,test_y):
        """
                                                Method Name: get_best_model
                                                Description: Find out the Model which has the best AUC score.
                                                Output: The best model name and the model object
                                                On Failure: Raise Exception

                                                Written By: iNeuron Intelligence
                                                Version: 1.0
                                                Revisions: None

                                        """
        self.logger_object.log(self.file_object,
                               'Entered the get_best_model method of the Model_Finder class')
        # create best model for KNN
        try:

            self.clf= self.get_best_params_for_random_forest(train_x, train_y)
            self.prediction_Random_Forest_reg = self.clf.predict(test_x) # Predictions using the decisionTreeReg Model
            self.prediction_Random_Forest_Reg_error = r2_score(test_y,self.prediction_Random_Forest_reg)



         # create best model for XGBoost
            self.xgboost = self.get_best_params_for_xgboost(train_x, train_y)
            self.prediction_xgboost = self.xgboost.predict(test_x)  # Predictions using the XGBoost Model
            self.prediction_xgboost_error = r2_score(test_y,self.prediction_xgboost)


            #comparing the two models
            if(self.prediction_Random_Forest_Reg_error <  self.prediction_xgboost_error):
                return 'XGBoost',self.xgboost
            else:
                return 'RandomForestReg',self.clf

        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_model method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Model Selection Failed. Exited the get_best_model method of the Model_Finder class')
            raise Exception()

