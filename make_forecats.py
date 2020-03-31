from statsmodels.tsa.statespace.sarimax import SARIMAXResults
import pickle
forecast_model_train = SARIMAXResults.load('forecast_model_train.pkl')
# Make a forecast for the next 6 periods after the last period in the training set
future = forecast_model_train.forecast(steps=5)
print('Train forecats...')
print(future)

# Make a forecast for the next 6 periods after the last period in the test set
forecast_model_test = SARIMAXResults.load('forecast_model_test.pkl')
future = forecast_model_test.forecast(steps=5)
print('\nTest forecasts')
print(future)
