# Objective metrics

Autopilot produces accuracy metrics to evaluate the model candidates and help you choose
which to use to generate forecasts. You can either let Autopilot optimize the predictor for you,
or you can manually choose an algorithm for your predictor. By default, Autopilot uses the
Average Weighted Quantile Loss.

The following list contains the names of the metrics that are currently available to
measure the performance of models for time-series forecasting.

**`RMSE`**

Root mean squared error (RMSE) – Measures the square root of the squared
difference between predicted and actual values, and is averaged over all values. It's an
important metric to indicate the presence of large model errors and outliers. Values
range from zero (0) to infinity, with smaller numbers indicating a better model fit to
the data. RMSE is dependent on scale, and should not be used to compare datasets of
different sizes.

**`wQL`**

Weighted Quantile Loss (wQL) – Assess the accuracy of the forecast by
measuring the weighted absolute differences between predicted and actual P10, P50, and
P90 quantiles with lower values indicating better performance.

**`Average wQL (default)`**

Average Weighted Quantile Loss (Average wQL) – Evaluates the forecast by
averaging the accuracy at the P10, P50, and P90 quantiles. A lower value indicates a
more accurate model.

**`MASE`**

Mean Absolute Scaled Error (MASE) – The mean absolute error of the forecast
normalized by the mean absolute error of a simple baseline forecasting method. A lower
value indicates a more accurate model, where MASE < 1 is estimated to be better than
the baseline and MASE > 1 is estimated to be worse than the baseline.

**`MAPE`**

Mean Absolute Percent Error (MAPE) – The percentage error (percent difference
of the mean forecasted value versus the actual value) averaged over all time points. A
lower value indicates a more accurate model, where MAPE = 0 is a model with no
errors.

**`WAPE`**

Weighted Absolute Percent Error (WAPE) – The sum of the absolute error
normalized by the sum of the absolute target, which measure the overall deviation of
forecasted values from observed values. A lower value indicates a more accurate
model.
