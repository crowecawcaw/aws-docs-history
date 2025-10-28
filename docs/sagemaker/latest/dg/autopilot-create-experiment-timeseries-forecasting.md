# Create an AutoML job for

time-series forecasting using the API

Forecasting in machine learning refers to the process of predicting future outcomes or
trends based on historical data and patterns. By analyzing past time-series data and identifying
underlying patterns, machine learning algorithms can make predictions and provide valuable
insights into future behavior. In forecasting, the goal is to develop models that can accurately
capture the relationship between input variables and the target variable over time. This
involves examining various factors such as trends, seasonality, and other relevant patterns
within the data. The collected information is then used to train a machine learning model. The
trained model is capable of generating predictions by taking new input data and applying the
learned patterns and relationships. It can provide forecasts for a wide range of use cases, such
as sales projections, stock market trends, weather forecasts, demand forecasting, and many
more.

The following instructions show how to create an Amazon SageMaker Autopilot job as a pilot experiment for
time-series forecasting problem types using SageMaker [API Reference](autopilot-reference.md "autopilot-reference.md").

###### Note

Tasks such as text and image classification,
time-series forecasting, and fine-tuning of large language models are exclusively available
through the version 2 of the [AutoML REST API](autopilot-reference.md "autopilot-reference.md").
If your language of choice is Python, you can refer to [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_auto_ml_job_v2.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_auto_ml_job_v2.html") or the [AutoMLV2 object](https://sagemaker.readthedocs.io/en/stable/api/training/automlv2.html#sagemaker.automl.automlv2.AutoMLV2 "https://sagemaker.readthedocs.io/en/stable/api/training/automlv2.html#sagemaker.automl.automlv2.AutoMLV2") of the Amazon SageMaker Python SDK directly.

Users who prefer the convenience of a user interface can use [Amazon SageMaker Canvas](canvas-getting-started.md "canvas-getting-started.md") to access
pre-trained models and generative AI foundation models, or create custom models tailored for specific text, image classification,
forecasting needs, or generative AI.

You can create an Autopilot time-series forecasting experiment programmatically by calling the
[`CreateAutoMLJobV2`](../APIReference/API_CreateAutoMLJobV2.md "../APIReference/API_CreateAutoMLJobV2.md") API in any language supported by Amazon SageMaker Autopilot or the
AWS CLI.

For information on how this API action translates into a function in the language of your
choice, see the [See Also](../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_SeeAlso "../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_SeeAlso") section of `CreateAutoMLJobV2` and choose an SDK. As an example, for Python users, see the full request syntax of `create_auto_ml_job_v2` in AWS SDK for Python (Boto3).

Autopilot trains several model candidates with your target time-series, then selects an optimal
forecasting model for a given objective metric. When your model candidates have been trained,
you can find the best candidate metrics in the response to `DescribeAutoMLJobV2` at `BestCandidate`.

The following sections define the mandatory and optional input request parameters for the
`CreateAutoMLJobV2` API used in time-series forecasting.

###### Note

Refer to the notebook [Time-Series Forecasting with Amazon SageMaker Autopilot](https://github.com/aws/amazon-sagemaker-examples/blob/main/autopilot/autopilot_time_series.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/autopilot/autopilot_time_series.ipynb") for a practical, hands-on time-series
forecasting example. In this notebook, you use Amazon SageMaker Autopilot to train a time-series model
and produce predictions using the trained model. The notebook provides instructions for
retrieving a ready-made dataset of tabular historical data on Amazon S3.

## Prerequisites

Before using Autopilot to create a time-series forecasting experiment in SageMaker AI, make sure
to:

- Prepare your time-series dataset. Dataset preparation involves collecting relevant
  data from various sources, cleaning and filtering it to remove noise and inconsistencies,
  and organizing it into a structured format. See [Time-series datasets format and missing
  values filling methods](timeseries-forecasting-data-format.md "timeseries-forecasting-data-format.md") to learn more about time-series
  formats requirements in Autopilot. Optionally, you can supplement your dataset with the
  public holiday calendar of the country of your choice to capture associated patterns. For
  more information on holiday calendars, see [National holiday
  calendars](autopilot-timeseries-forecasting-holiday-calendars.md "autopilot-timeseries-forecasting-holiday-calendars.md").

###### Note

We recommend providing at least 3-5 historical data points for each 1 future data
point you want to predict. For example, to forecast 7 days ahead (horizon of 1 week)
based on daily data, train your model on a minimum of 21-35 days of historical data.
Make sure to provide enough data to capture seasonal and recurrent patterns.

- Place your time-series data in an Amazon S3 bucket.
- Grant full access to the Amazon S3 bucket containing your input data for the SageMaker AI execution
  role used to run your experiment. Once this is done, you can use the ARN of this execution
  role in Autopilot API requests.
  - For information on retrieving your SageMaker AI execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").
  - For information on granting your SageMaker AI execution role permissions to access one or
    more specific buckets in Amazon S3, see _Add Additional Amazon S3
    Permissions to a SageMaker AI Execution Role_ in [Create execution
    role](sagemaker-roles.md#sagemaker-roles-create-execution-role "sagemaker-roles.md#sagemaker-roles-create-execution-role").

## Required parameters

When calling `CreateAutoMLJobV2` to create an Autopilot experiment for time-series
forecasting, you must provide the following values:

- An `AutoMLJobName` to specify the name of your job. The name should be of
  type `string`, and should have a minimum length of 1 character and a maximum
  length of 32.
- At least one `AutoMLJobChannel` in `AutoMLJobInputDataConfig` in which you specify the name of the Amazon S3
  bucket that contains your data. Optionally, you can specify the content (CSV or Parquet
  files) and compression (GZip) types.
- An `AutoMLProblemTypeConfig` of type `TimeSeriesForecastingJobConfig` to configure the settings of your
  time-series forecasting job. In particular, you must specify:

      + The **frequency** of predictions, which refers to
       the desired granularity (hourly, daily, monthly, etc) of your forecast.


      Valid intervals are an integer followed by `Y` (Year), `M`
       (Month), `W` (Week), `D` (Day), `H` (Hour), and
       `min` (Minute). For example, `1D` indicates every day and
       `15min` indicates every 15 minutes. The value of a frequency must not
       overlap with the next larger frequency. For example, you must use a frequency of
       `1H` instead of `60min`.


      The valid values for each frequency are the following:




      	- Minute - 1-59
      	- Hour - 1-23
      	- Day - 1-6
      	- Week - 1-4
      	- Month - 1-11
      	- Year - 1
      + The **horizon** of predictions in your forecast,
       which refers to the number of time-steps that the model predicts. The forecast horizon
       is also called the prediction length. The maximum forecast horizon is the lesser of
       500 time-steps or 1/4 of the time-steps in the dataset.
      + A [TimeSeriesConfig](../APIReference/API_TimeSeriesConfig.md "../APIReference/API_TimeSeriesConfig.md") in which you define the schema of your dataset to map the
       column headers to your forecast by specifying:




      	- A `TargetAttributeName`: The column that contains historical data
      	 of the target field to forecast.
      	- A `TimestampAttributeName`: The column that contains a point in
      	 time at which the target value of a given item is recorded.
      	- A `ItemIdentifierAttributeName`: The column that contains the item
      	 identifiers for which you want to predict the target value.

  The following is an example of those request parameters. In this example, you are
  setting up a daily forecast for the expected quantity or level of demand of specific items
  over a period of 20 days.

```
"AutoMLProblemTypeConfig": {
        "ForecastFrequency": "D",
        "ForecastHorizon": 20,
        "TimeSeriesConfig": {
            "TargetAttributeName": "demand",
            "TimestampAttributeName": "timestamp",
            "ItemIdentifierAttributeName": "item_id"
        },
```

- An `OutputDataConfig` to specify the Amazon S3 output path to store the
  artifacts of your AutoML job.
- A `RoleArn` to specify the ARN of the role used to access your data. You
  can use the ARN of the execution role to which you have granted access to your
  data.

All other parameters are optional. For example, you can set specific forecast quantiles,
choose a filling method for missing values in the dataset, or define how to aggregate data
that does not align with forecast frequency. To learn how to set those additional parameters,
see [Optional parameters](#timeseries-forecasting-api-optional-params "#timeseries-forecasting-api-optional-params").

## Optional parameters

The following sections provide details of some optional parameters that you can pass to
your time-series forecasting AutoML job.

By default, your Autopilot job trains a pre-defined list of algorithms on your dataset.
However, you can provide a subset of the default selection of algorithms.

For time-series forecasting, you must choose `TimeSeriesForecastingJobConfig` as the type of `AutoMLProblemTypeConfig`.

Then, you can specify an array of selected `AutoMLAlgorithms` in the
`AlgorithmsConfig` attribute of [CandidateGenerationConfig](../APIReference/API_CandidateGenerationConfig.md "../APIReference/API_CandidateGenerationConfig.md").

The following is an example of an `AlgorithmsConfig` attribute listing
exactly three algorithms ("cnn-qr", "prophet", "arima") in its
`AutoMLAlgorithms` field.

```
{
   "AutoMLProblemTypeConfig": {
        "TimeSeriesForecastingJobConfig": {
          "CandidateGenerationConfig": {
            "AlgorithmsConfig":[
               {"AutoMLAlgorithms":["cnn-qr", "prophet", "arima"]}
            ]
         },
       },
     },
  }
```

For the list of available algorithms for time-series forecasting, see [`AutoMLAlgorithms`](../APIReference/API_AutoMLAlgorithmConfig.md#sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms "../APIReference/API_AutoMLAlgorithmConfig.md#sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms"). For details on each algorithm, see [Algorithms support for time-series
forecasting](timeseries-forecasting-algorithms.md "timeseries-forecasting-algorithms.md").

Autopilot trains 6 models candidates with your target time-series, then combines these
models using a stacking ensemble method to create an optimal forecasting model for a given
objective metric. Each Autopilot forecasting model generates a probabilistic forecast by
producing forecasts at quantiles between P1 and P99. These quantiles are used to account
for forecast uncertainty. By default, forecasts will be generated for the 0.1
(`p10`), 0.5 (`p50`), and 0.9 (`p90`). You can choose
to specify your own quantiles.

In Autopilot, you can specify up to five forecast quantiles from 0.01 (`p1`)
to 0.99 (`p99`), by increments of 0.01 or higher in the
`ForecastQuantiles` attribute of [TimeSeriesForecastingJobConfig](../APIReference/API_TimeSeriesForecastingJobConfig.md "../APIReference/API_TimeSeriesForecastingJobConfig.md").

In the following example, you are setting up a daily 10th, 25th, 50th, 75th, and 90th
percentile forecast for the expected quantity or level of demand of specific items over a
period of 20 days.

```
"AutoMLProblemTypeConfig": {
        "ForecastFrequency": "D",
        "ForecastHorizon": 20,
        "ForecastQuantiles": ["p10", "p25", "p50", "p75", "p90"],
        "TimeSeriesConfig": {
            "TargetAttributeName": "demand",
            "TimestampAttributeName": "timestamp",
            "ItemIdentifierAttributeName": "item_id"
        },
```

To create a forecast model (also referred to as the best model candidate from your
experiment), you must specify a forecast frequency. The forecast frequency determines the
frequency of predictions in your forecasts. For example, monthly sales forecasts. Autopilot
best model can generate forecasts for data frequencies that are higher than the frequency
at which your data is recorded.

During training, Autopilot aggregates any data that does not align with the forecast
frequency you specify. For example, you might have some daily data but specify a weekly
forecast frequency. Autopilot aligns the daily data based on the week that it belongs in.
Autopilot then combines it into single record for each week.

During aggregation, the default transformation method is to sum the data. You can
configure the aggregation when you create your AutoML job in the
`Transformations` attribute of [TimeSeriesForecastingJobConfig](../APIReference/API_TimeSeriesForecastingJobConfig.md "../APIReference/API_TimeSeriesForecastingJobConfig.md"). The supported aggregation methods are
`sum` (default), `avg`, `first`, `min`,
`max`. Aggregation is only supported for the target column.

In the following example, you configure the aggregation to calculate the average of
the individual promo forecasts to provide the final aggregated forecast values.

```
"Transformations": {
            "Aggregation": {
                "promo": "avg"
            }
        }
```

Autopilot provides a number of filling methods to handle missing values in the target and
other numeric columns of your time-series datasets. For information on the list of
supported filling methods and their available filling logic, see [Handle missing values](timeseries-forecasting-data-format.md#timeseries-missing-values "timeseries-forecasting-data-format.md#timeseries-missing-values").

You configure your filling strategy in the `Transformations` attribute of
[TimeSeriesForecastingJobConfig](../APIReference/API_TimeSeriesForecastingJobConfig.md "../APIReference/API_TimeSeriesForecastingJobConfig.md") when creating your AutoML job.

To set a filling method, you need to provide a key-value pair:

- The key is the name of the column for which you want to specify the filling
  method.
- The value associated with the key is an object that defines the filling strategy
  for that column.
  You can specify multiple filling methods for a single column.

To set a specific value for the filling method, you should set the fill parameter to
the desired filling method value (for example `"backfill" : "value"`), and
define the actual filling value in an additional parameter suffixed with "\_value". For
example, to set `backfill` to a value of `2`, you must include two
parameters: `"backfill": "value"` and `"backfill_value":"2"`.

In the following example, you specify the filling strategy for the incomplete data
column, "price" as follows: All missing values between the first data point of an item and
the last are set to `0` after which all missing values are filled with the
value `2` until the end date of the dataset.

```
"Transformations": {
            "Filling": {
                "price": {
                        "middlefill" : "zero",
                        "backfill" : "value",
                        "backfill_value": "2"
                }
            }
        }
```

Autopilot produces accuracy metrics to evaluate the model candidates and help you choose
which to use to generate forecasts. When you run a time-series forecasting experiment, you
can either choose AutoML to let Autopilot optimize the predictor for you, or you can manually
choose an algorithm for your predictor.

By default, Autopilot uses the Average Weighted Quantile Loss. However, you can configure
the objective metric when you create your AutoML job in the `MetricName`
attribute of [AutoMLJobObjective](../APIReference/API_AutoMLJobObjective.md "../APIReference/API_AutoMLJobObjective.md").

For the list of available algorithms, see [Algorithms support for time-series
forecasting](timeseries-forecasting-algorithms.md "timeseries-forecasting-algorithms.md").

In Autopilot, you can incorporate a feature-engineered dataset of national holiday
information to your time-series. Autopilot provide native support for the holiday calendars
of over 250 countries. After you choose a country, Autopilot applies that country’s holiday
calendar to every item in your dataset during training. This allows the model to identify
patterns associated with specific holidays.

You can enable the holiday featurization when you create your AutoML job by passing an
[HolidayConfigAttributes](../APIReference/API_HolidayConfigAttributes.md "../APIReference/API_HolidayConfigAttributes.md") object to the `HolidayConfig` attribute of
[TimeSeriesForecastingJobConfig](../APIReference/API_TimeSeriesForecastingJobConfig.md "../APIReference/API_TimeSeriesForecastingJobConfig.md"). The `HolidayConfigAttributes` object
contains the two letters `CountryCode` attribute that determines the country of
the public national holiday calendar used to augment your time-series dataset.

Refer to [Country Codes](autopilot-timeseries-forecasting-holiday-calendars.md#holiday-country-codes "autopilot-timeseries-forecasting-holiday-calendars.md#holiday-country-codes")
for the list of supported calendars and their corresponding country code.

Autopilot allows you to automatically deploy your forecast model to an endpoint. To
enable automatic deployment for the best model candidate of an AutoML job, include a
`ModelDeployConfig` in the AutoML job request. This allows the
deployment of the best model to a SageMaker AI endpoint. Below are the available configurations
for customization.

- To let Autopilotgenerate the endpoint name, set `AutoGenerateEndpointName` to `True`.
- To provide your own name for the endpoint, set `AutoGenerateEndpointName to `False` and provide a name of your
 choice in EndpointName`.
  You can configure your AutoML job V2 to automatically initiate a remote job on Amazon EMR
  Serverless when additional compute resources are needed to process large datasets. By
  seamlessly transitioning to EMR Serverless when required, the AutoML job can handle
  datasets that would otherwise exceed the initially provisioned resources, without any
  manual intervention from you. EMR Serverless is available for the tabular and time series
  problem types. We recommend setting up this option for time-series datasets larger than 30
  GB.

To allow your AutoML job V2 to automatically transition to EMR Serverless for large
dataset, you need to provide an `EmrServerlessComputeConfig` object, which
includes an `ExecutionRoleARN` field, to the `AutoMLComputeConfig`
of the AutoML job V2 input request.

The `ExecutionRoleARN` is the ARN of the IAM role granting the AutoML job
V2 the necessary permissions to run EMR Serverless jobs.

This role should have the following trust relationship:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "emr-serverless.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

And grant the permissions to:

- Create, list, and update EMR Serverless applications.
- Start, list, get, or cancel job runs on an EMR Serverless application.
- Tag EMR Serverless resources.
- Pass an IAM role to the EMR Serverless service for execution.

By granting the `iam:PassRole` permission, the AutoML job V2 can
temporarily assume the `EMRServerlessRuntimeRole-*` role and pass it to the
EMR Serverless service. These are the IAM roles used by the EMR Serverless job
execution environments to access other AWS services and resources needed during
runtime, such as Amazon S3 for data access, CloudWatch for logging, access to the AWS Glue Data
Catalog or other services based on your workload requirements.

See [Job runtime
roles for Amazon EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/security-iam-runtime-role.md "../../../emr/latest/EMR-Serverless-UserGuide/security-iam-runtime-role.md") for details on this role
permissions.
The IAM policy defined in the provided JSON document grants those
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "EMRServerlessCreateApplicationOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:CreateApplication",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessListApplicationOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:ListApplications",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessApplicationOperations",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:UpdateApplication",
 "emr-serverless:GetApplication"
 ],
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessStartJobRunOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:StartJobRun",
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessListJobRunOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:ListJobRuns",
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessJobRunOperations",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:GetJobRun",
 "emr-serverless:CancelJobRun"
 ],
 "Resource": "arn:aws:emr-serverless:*:*:/applications/*/jobruns/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EMRServerlessTagResourceOperation",
 "Effect": "Allow",
 "Action": "emr-serverless:TagResource",
 "Resource": "arn:aws:emr-serverless:*:*:/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/sagemaker:is-canvas-resource": "True",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "IAMPassOperationForEMRServerless",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/EMRServerlessRuntimeRole-*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "emr-serverless.amazonaws.com",
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```
