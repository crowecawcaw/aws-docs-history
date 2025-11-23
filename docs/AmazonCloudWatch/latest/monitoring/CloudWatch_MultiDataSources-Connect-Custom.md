# Create a custom connector to a data source

This topic describes how to connect a custom data source to CloudWatch.
You can connect a custom data source to CloudWatch in two ways:

- Using a sample template that CloudWatch provides.
  You can use either JavaScript or Python with this template.
  These templates include sample Lambda code that will be useful to you when you create your Lambda function.
  You can then modify the Lambda function from the template to connect to your custom data source.
- Creating an AWS Lambda function from scratch that implements the data source connector, the data query, and the preparation of the time series for use by CloudWatch.
  This function must pre-aggregate or merge datapoints if needed, and also align the period and timestamps to be compatible with CloudWatch.

###### Contents

- [Use a template](CloudWatch_MultiDataSources-Connect-Custom.md#CloudWatch_MultiDataSources-Connect-Custom-template "CloudWatch_MultiDataSources-Connect-Custom.md#CloudWatch_MultiDataSources-Connect-Custom-template")
- [Create a custom data source from scratch](CloudWatch_MultiDataSources-Connect-Custom.md#CloudWatch_MultiDataSources-Connect-Custom-Lambda "CloudWatch_MultiDataSources-Connect-Custom.md#CloudWatch_MultiDataSources-Connect-Custom-Lambda")
  - [Step 1: Create the function](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Function "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Function")
    - [GetMetricData event](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-GetMetricData "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-GetMetricData")
    - [DescribeGetMetricData event](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-DescribeGetMetricData "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-DescribeGetMetricData")
    - [Important considerations for CloudWatch alarms](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Alarms "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Alarms")
    - [(Optional) Use AWS Secrets Manager to store credentials](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Secrets "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Secrets")
    - [(Optional) Connect to a data source in a VPC](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-VPC "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-VPC")

  - [Step 2: Create a Lambda permissions policy](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Permissions "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-Permissions")
  - [Step 3: Attach a resource tag to the Lambda function](CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-tags "CloudWatch_MultiDataSources-Connect-Custom.md#MultiDataSources-Connect-Custom-Lambda-tags")

##

Use a template

Using a template creates a sample Lambda function, and can help you get your custom connector
built faster. These sample functions provide sample code
for many common scenarios involved with building a custom connector. You can examine the Lambda code after you
create a connector with a template, then modify it to use to connect to your data source.

Additionally, if you use the template, CloudWatch takes care of creating the Lambda permissions policy and attaching
resource tags to the Lambda function.

###### To use the template to create a connector to a custom data source

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Metrics data sources** tab.
4. Choose **Create data source**.
5. Choose the radio button for **Custom - getting started template**
   and then choose **Next**.
6. Enter a name for the data source.
7. Select the one of the listed templates.
8. Select either Node.js or Python.
9. Choose **Create data source**.

The new custom source that you just
added doesn't appear until the CloudFormation stack finishes creating it. To check progress, you
can choose **View the status of my CloudFormation stack**. Or you can
choose the refresh icon to update this list.

When your new data source appears in this list, it is ready for you to test in the console
and modify. 10. (Optional) To query the test data from this source in the console, follow the instructions in
[Creating a graph of metrics from
another data source](graph_a_metric.md#create-metric-graph-multidatasource "graph_a_metric.md#create-metric-graph-multidatasource"). 11. Modify the Lambda function for your needs.

    1. In the navigation pane, choose **Settings**.
    2. Choose the **Metrics data sources** tab.
    3. Choose **View in Lambda console** for the source that you want to modify.You can now modify the function to access your data source. For more information, see

[Step 1: Create the function](#MultiDataSources-Connect-Custom-Lambda-Function "#MultiDataSources-Connect-Custom-Lambda-Function").

###### Note

By using the template, when you write your Lambda function you don't need to follow the instructions in
[Step 2: Create a Lambda permissions policy](#MultiDataSources-Connect-Custom-Lambda-Permissions "#MultiDataSources-Connect-Custom-Lambda-Permissions")
or [Step 3: Attach a resource tag to the Lambda function](#MultiDataSources-Connect-Custom-Lambda-tags "#MultiDataSources-Connect-Custom-Lambda-tags"). These steps were performed by
CloudWatch because you used the template.

##

Create a custom data source from scratch

Follow the steps in this section to create a Lambda function that connects CloudWatch to a data source.

###

Step 1: Create the function

A custom data source connector must support `GetMetricData` events from
CloudWatch. Optionally, you can also implement a `DescribeGetMetricData` event to
provide documentation to users in the CloudWatch console for how to use the connector. The
`DescribeGetMetricData` response can also be used to set defaults that are used
in the CloudWatch custom query builder.

CloudWatch provides code snippets as samples to help you get started. For more information,
see the samples repository at
[https://github.com/aws-samples/cloudwatch-data-source-samples](https://github.com/aws-samples/cloudwatch-data-source-samples "https://github.com/aws-samples/cloudwatch-data-source-samples").

**Constraints**

- The response from Lambda must be smaller than 6 Mb. If the response exceeds 6 Mb, the
  `GetMetricData` response marks the Lambda function as
  `InternalError` and no data is returned.
- The Lambda function must complete its execution within 10 seconds for visualization and
  dashboarding purposes, or within 4.5 seconds for alarms usage. If the execution time
  exceeds that time, the `GetMetricData` response marks the Lambda function as
  `InternalError` and no data is returned.
- The Lambda function must send its output using epoch timestamps in seconds.
- If the Lambda function doesn't resample the data and instead returns data that doesn't
  correspond to the start time and period length that was requested by the CloudWatch user,
  that data is ignored by CloudWatch. The extra data is discarded from any visualization or
  alarming. Any data that is not between the start time and end time is also discarded.

For example, if a user asks for data from 10:00 to 11:00 with a period of 5 min,
then "10:00:00 to 10:04:59" and "10:05:00 to 10:09:59" are the valid time ranges for
data to be returned. You must return a time series that includes `10:00
 value1`, `10:05 value2`, and so on. If the function returns
`10:03 valueX`, for example, it gets dropped because 10:03 does not
correspond to the requested start time and period.

- Multi-line queries are not supported by the CloudWatch data source connectors. Every line feed is
  replaced with a space when the query is executed, or when you create an alarm or a
  dashboard widget with the query. In some cases, this might make your query not
  valid.

####

GetMetricData event

**Request payload**

The following is an example of a `GetMetricData` request payload sent as
input to the Lambda function.

```
{
  "EventType": "GetMetricData",
  "GetMetricDataRequest": {
    "StartTime": 1697060700,
    "EndTime": 1697061600,
    "Period": 300,
    "Arguments": ["serviceregistry_external_http_requests{host_cluster!=\"prod\"}"]
  }
}
```

- **StartTime**– The timestamp specifying the earliest data
  to return. The **Type** is timestamp epoch seconds.
- **EndTime**– The timestamp specifying the latest data to
  return. The **Type** is timestamp epoch seconds.
- **Period**– The number of seconds that each aggregation of the metrics data
  represents. The minimum is 60 seconds. The **Type** is Seconds.
- **Arguments**– An array of arguments to pass to the Lambda metric
  math expression. For more information about passing arguments, see
  [How to pass arguments to your Lambda function](CloudWatch_MultiDataSources-Custom-Use.md#MultiDataSources-Connect-Custom-Lambda-arguments "CloudWatch_MultiDataSources-Custom-Use.md#MultiDataSources-Connect-Custom-Lambda-arguments").

**Response payload**

The following is an example of a `GetMetricData` response payload
returned by the Lambda function.

```
{
   "MetricDataResults": [
      {
         "StatusCode": "Complete",
         "Label": "CPUUtilization",
         "Timestamps": [ 1697060700, 1697061000, 1697061300 ],
         "Values": [ 15000, 14000, 16000 ]
      }
   ]
}
```

The response payload will contain either a `MetricDataResults` field or an `Error`
field, but not both.

A `MetricDataResults` field is a list of time-series fields of type `MetricDataResult`.
Each of those time-series fields can include the following fields.

- **StatusCode**– (Optional) `Complete` indicates
  that all data points in the requested time range were returned. `PartialData` means that an
  incomplete set of data points were returned. If this is omitted, the default is `Complete`.

Valid Values: `Complete` | `InternalError` | `PartialData` | `Forbidden`

- **Messages**– Optional list of messages with
  additional information about the data returned.

Type: Array of [MessageData](../APIReference/API_MessageData.md "../APIReference/API_MessageData.md")
objects with `Code` and `Value` strings.

- **Label**– The human-readable label associated with the data.

Type: String

- **Timestamps**– The timestamps for the data points,
  formatted in epoch time. The number of timestamps always matches the
  number of values and the value for `Timestamps[x]` is
  `Values[x`].

Type: Array of timestamps

- **Values**– The data point values for the metric,
  corresponding to `Timestamps`. The number of values always matches the
  number of timestamps and the value for `Timestamps[x]` is
  `Values[x`].

Type: Array of doubles

For more information about `Error` objects, see the following sections.

**Error response formats**

You can optionally use the error response to provide more information about errors.
We recommend that you return an error with Code Validation when a validation error occurs, such as
when a parameter is missing or is the wrong type.

The following is an example of the response when the Lambda function wants to raise a `GetMetricData`
validation exception.

```
{
   "Error": {
      "Code": "Validation",
      "Value": "Invalid Prometheus cluster"
   }
}
```

The following is an example of the response when the Lambda function indicates that
it's unable to return data because of an access issue. The response is translated into a
single time series with a status code of `Forbidden`.

```
{
   "Error": {
      "Code": "Forbidden",
      "Value": "Unable to access ..."
   }
}
```

The following is an example of when the Lambda function raises an overall
`InternalError` exception, which is translated into a single time series
with a status code of `InternalError` and a message. Whenever an error code
has a value other than `Validation` or `Forbidden`, CloudWatch assumes
that it's a generic internal error.

```
{
   "Error": {
      "Code": "PrometheusClusterUnreachable",
      "Value": "Unable to communicate with the cluster"
   }
}
```

####

DescribeGetMetricData event

**Request payload**

The following is an example of a `DescribeGetMetricData` request
payload.

```
{
  "EventType": "DescribeGetMetricData"
}
```

**Response payload**

The following is an example of a `DescribeGetMetricData` response
payload.

```
{
    "Description": "Data source connector",
    "ArgumentDefaults": [{
        Value: "default value"
     }]
}
```

- **Description**– A description of how to use
  the data source connector. This description will appear in the CloudWatch console. Markdown is supported.

Type: String

- **ArgumentDefaults**– Optional array of argument default
  values used pre-populate the custom data source builder.

If `[{ Value: "default value 1"}, { Value: 10}]`, is returned, the query builder in the
CloudWatch console displays two inputs, the first with “default value 1” and the second with 10.

If `ArgumentDefaults` is not provided, a single input is displayed with type default
set to `String`.

Type: Array of objects containing Value and Type.

- **Error**– (Optional) An error field can be
  included in any response. You can see examples in
  [GetMetricData event](#MultiDataSources-GetMetricData "#MultiDataSources-GetMetricData").

####

Important considerations for CloudWatch alarms

If you are going to use the data source to set CloudWatch alarms, you should set it up to
report data with timestamps every minute to CloudWatch. For more information and other
considerations for creating alarms on metrics from connected data sources, see [Create an alarm based on a connected data
source](Create_MultiSource_Alarm.md "Create_MultiSource_Alarm.md").

####

(Optional) Use AWS Secrets Manager to store credentials

If your Lambda function needs to use credentials to access the data source, we
recommend using AWS Secrets Manager to store these credentials instead of
hardcoding them into your Lambda function. For more information about using
AWS Secrets Manager with Lambda, see [Use
AWS Secrets Manager secrets in AWS Lambda functions](../../../secretsmanager/latest/userguide/retrieving-secrets_lambda.md "../../../secretsmanager/latest/userguide/retrieving-secrets_lambda.md").

####

(Optional) Connect to a data source in a VPC

If your data source is in a VPC managed by Amazon Virtual Private Cloud, you must configure your Lambda
function to access it. For more information, see [Connecting outbound networking to
resources in a VPC](../../../lambda/latest/dg/configuration-vpc.md "../../../lambda/latest/dg/configuration-vpc.md").

You might also need to configure VPC service endpoints to access services such
as AWS Secrets Manager. For more information, see
[Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint").

###

Step 2: Create a Lambda permissions policy

You must use create a policy statement that grants CloudWatch permission to use
the Lambda function that you created. You can use the AWS CLI or the Lambda console to create
the policy statement.

###### To use the AWS CLI to create the policy statement

- Enter the following command. Replace `123456789012` with your account ID,
  replace `my-data-source-function` with the name of your Lambda function, and replace
  `MyDataSource-DataSourcePermission1234` with an arbitrary unique value.

```
aws lambda add-permission --function-name `my-data-source-function` --statement-id `MyDataSource-DataSourcePermission1234` --action lambda:InvokeFunction --principal lambda.datasource.cloudwatch.amazonaws.com --source-account `123456789012`
```

###

Step 3: Attach a resource tag to the Lambda function

The CloudWatch console determines which of your Lambda functions are data source connectors by using
a tag. When you create a data source using one of the wizards, the tag is automatically
applied by the CloudFormation stack that configures it. When you create a data source yourself, you
can use the following tag for your Lambda function. This makes your
connector appear in the **Data source** dropdown in the CloudWatch console when
you query metrics.

- A tag with `cloudwatch:datasource` as the key and `custom` as the value.
