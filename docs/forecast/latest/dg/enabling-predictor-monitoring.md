Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Enabling Predictor

Monitoring

You can enable predictor monitoring when you create the predictor, or you can
enable it for an existing predictor.

###### Note

Predictor monitoring is only available for AutoPredictors.
You can upgrade existing legacy predictors to AutoPredictor. See [Upgrading to AutoPredictor](howitworks-predictor.md#upgrading-autopredictor "howitworks-predictor.md#upgrading-autopredictor").

###### Topics

- [Enabling Predictor
  Monitoring for a New Predictor](#enabling-predictor-monitoring-new "#enabling-predictor-monitoring-new")
- [Enabling Predictor
  Monitoring for an Existing Predictor](#enabling-predictor-monitoring-existing "#enabling-predictor-monitoring-existing")

## Enabling Predictor

Monitoring for a New Predictor

You can enable predictor monitoring for a new predictor with the console, AWS CLI, AWS SDKs, and the [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md") operation.

Console
**To enable Predictor
monitoring**

1. Sign in to the AWS Management Console and open the Amazon Forecast console at [https://console.aws.amazon.com/forecast/](https://console.aws.amazon.com/forecast/ "https://console.aws.amazon.com/forecast/").
2. From **Dataset groups**, choose your dataset
   group.
3. In the navigation pane, choose
   **Predictors**.
4. Choose **Train new predictor**.
5. In the **Predictor configuration** section,
   choose **Enable monitoring**.
6. Provide values for the following mandatory fields:
   - **Name** - a unique
     predictor name.
   - **Forecast frequency** -
     the granularity of your forecasts.
   - **Forecast horizon** -
     The number of time steps to forecast.

7. Choose **Start** to create an auto predictor with monitoring enabled. You’ll see monitoring results as you use the predictor to generate forecasts and then import more data.

Python
To enable predictor monitoring for a new predictor with the SDK for Python (Boto3), use the `create_auto_predictor`
method and provide a monitor name in the `MonitoringConfig`.

The following
code creates an auto predictor that makes predictions for 24 (`ForecastHorizon`) days (`ForecastFrequency`) in the future, and specifies
`MyPredictorMonitor` as the `MonitorName`. After you generate a forecast and then import more data, you can view the results of predictor monitoring. For
more information about retrieving results, see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md").

For information on
required and optional parameters for creating a predictor see [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md").

```
import boto3

forecast = boto3.client('forecast')

create_predictor_response = forecast.create_auto_predictor(
    PredictorName = '`predictor_name`',
    ForecastHorizon = 24,
    ForecastFrequency = 'D',
    DataConfig = {
        "DatasetGroupArn": "arn:aws:forecast:`region`:`account`:dataset-group/`datasetGroupName`"
    },
    MonitorConifg = {
        "MonitorName": "`MyMonitorName`"
    }
)
```

## Enabling Predictor

Monitoring for an Existing Predictor

You can enable predictor monitoring for an existing predictor with the console, AWS CLI, and AWS SDKs.

Console

###### To enable predictor monitoring

1. Sign in to the AWS Management Console and open the Amazon Forecast console at [https://console.aws.amazon.com/forecast/](https://console.aws.amazon.com/forecast/ "https://console.aws.amazon.com/forecast/").
2. From **Dataset groups**, choose your dataset
   group.
3. In the navigation pane, choose
   **Predictors**.
4. Choose your predictor.
5. Navigate to the **Monitoring** tab.
6. In the **Monitoring details** section,
   choose **Start monitoring**

When the **Monitoring status** is
Active, predictor monitoring is enabled. After you generate a forecast and then import more data, you can view the results of predictor monitoring. For
more information see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md")

Python
To enable predictor monitoring for an existing predictor with the SDK for Python (Boto3),
use the `create_monitor` method. Specify a name for the monitoring,
and for `ResourceArn` specify the Amazon Resource Name (ARN) for the predictor to monitor. Use the `describe_monitor` method and provide the monitor ARN to get the status
of the monitor.
After you generate a forecast and then import more data, you can view the results of predictor monitoring. For
more information see [Viewing Monitoring Results](predictor-monitoring-results.md "predictor-monitoring-results.md").

For information on
required and optional parameters, see the [CreateMonitor](API_CreateMonitor.md "API_CreateMonitor.md") and [DescribeMonitor](API_DescribeMonitor.md "API_DescribeMonitor.md").

```
import boto3

forecast = boto3.client('forecast')

create_monitor_response = forecast.create_monitor(
    MonitorName = '`monitor_name`',
    ResourceArn = 'arn:aws:forecast:`region`:`accountNumber`:predictor/`predictorName`'
)

monitor_arn = create_monitor_response['MonitorArn']

describe_monitor_response = forecast.describe_monitor(
    MonitorArn = monitor_arn
)
print("Monitor status: " + describe_monitor_response['Status'])
```
