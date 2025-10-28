# Forecast a deployed Autopilot

model

After training your models using the AutoML API, you can deploy them for real-time or
batch-based forecasting.

The AutoML API trains several model candidates for your time-series data and selects an
optimal forecasting model based on your target objective metric. Once your model candidates
have been trained, you can find the best candidate in the response [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md")
at [BestCandidate](../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-CandidateName "../APIReference/API_AutoMLCandidate.md#sagemaker-Type-AutoMLCandidate-CandidateName").

To get predictions using this best performing model, you can either set up an endpoint to
obtain forecasts interactively or use batch forecasting to make predictions on a batch of
observations.

###### Considerations

- When providing input data for forecasting, the schema of your data should remain the
  same as the one used to train your model, including the number of columns, column headers,
  and data types. You can forecast for existing or new item IDs within the same or different
  timestamp range to predict for a different time period.
- Forecasting models predict for the forecast horizon points in the future specified in
  the input request at training, which is from the _target end
  date_ to the _target end date + forecast
  horizon_. To use the model for predicting specific dates, you should provide
  the data in the same format as the original input data, extending up to a specified
  _target end date_. In this scenario, the model will
  start predicting from the new target end date.

For example, if your dataset had monthly data from January to June with a Forecast
horizon of 2, then the model would predict the target value for the next 2 months, which
would be July and August. If in August, you want to predict for the next 2 months, this
time your input data should be from January to August and the model will predict for the
next 2 months (September, October).

- When forecasting future data points, there is no set minimum for the amount of
  historical data to provide. Include enough data to capture seasonal and recurrent patterns
  in your time-series.

###### Topics

- [Real-time forecasting](timeseries-forecasting-realtime.md "timeseries-forecasting-realtime.md")
- [Batch forecasting](timeseries-forecasting-batch.md "timeseries-forecasting-batch.md")
