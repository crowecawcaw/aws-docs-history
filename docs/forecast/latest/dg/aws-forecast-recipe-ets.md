Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Exponential Smoothing (ETS) Algorithm

Exponential Smoothing [(ETS)](https://en.wikipedia.org/wiki/Exponential_smoothing "https://en.wikipedia.org/wiki/Exponential_smoothing") is a commonly-used local statistical algorithm for time-series forecasting. The
Amazon Forecast ETS algorithm calls the [ets
function](https://cran.r-project.org/web/packages/forecast/forecast.pdf#Rfn.ets.1 "https://cran.r-project.org/web/packages/forecast/forecast.pdf#Rfn.ets.1") in the `Package 'forecast'` of the Comprehensive R Archive Network
(CRAN).

## How ETS Works

The ETS algorithm is especially useful for datasets with seasonality and other prior
assumptions about the data. ETS computes a weighted average over all observations in the input
time series dataset as its prediction. The weights are exponentially decreasing over time,
rather than the constant weights in simple moving average methods. The weights are dependent
on a constant parameter, which is known as the smoothing parameter.

## ETS Hyperparameters and Tuning

For information about ETS hyperparameters and tuning, see the `ets` function
documentation in the [Package
'forecast'](https://cran.r-project.org/web/packages/forecast/forecast.pdf "https://cran.r-project.org/web/packages/forecast/forecast.pdf") of [CRAN](https://cran.r-project.org "https://cran.r-project.org").

Amazon Forecast converts the `DataFrequency` parameter specified in the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation to the
`frequency` parameter of the R [ts](https://www.rdocumentation.org/packages/stats/versions/3.6.1/topics/ts "https://www.rdocumentation.org/packages/stats/versions/3.6.1/topics/ts")
function using the following table:

| DataFrequency (string) | R ts frequency (integer) |
| ---------------------- | ------------------------ |
| Y                      | 1                        |
| M                      | 12                       |
| W                      | 52                       |
| D                      | 7                        |
| H                      | 24                       |
| 30min                  | 2                        |
| 15min                  | 4                        |
| 10min                  | 6                        |
| 5min                   | 12                       |
| 1min                   | 60                       |

Supported data frequencies that aren't in the table default to a `ts` frequency
of 1.
