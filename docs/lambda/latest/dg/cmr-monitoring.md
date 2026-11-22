

# Monitoring customer-managed runtimes

As a runtime publisher, you don't have access to the Lambda Event Functions that use your runtime, because the functions run in your consumers' accounts. To help you monitor your runtime, Lambda publishes runtime metrics to Amazon CloudWatch in your account. [AWS CloudTrail also delivers events](#cmr-monitoring-cloudtrail) to your account when other accounts configure functions to use your runtime, or try to. Use the metrics to check the health of each runtime version and runtime alias. You can also track the progress of a runtime update and see how much each runtime resource is used.

This topic describes the runtime metrics and how to use them. It then shows you how to view the metrics, create an alarm on the error rate of a runtime alias, and compare two runtime versions. It also describes the CloudTrail events that Lambda logs for customer-managed runtimes.

## Runtime metrics
<a name="cmr-monitoring-metrics"></a>

Lambda publishes the following metrics for each customer-managed runtime. The metrics count invocations of all functions that use the runtime.


**Runtime metrics**  

| Metric | Description | Useful statistic | 
| --- | --- | --- | 
| RuntimeInvocations | The number of invocations of functions that use the runtime. This count includes successful invocations and invocations that result in an error. | Sum | 
| RuntimeInvocationErrors | The number of invocations of functions that use the runtime that result in a function error. | Sum | 

Lambda publishes runtime metrics in the `AWS/Lambda` namespace.

To calculate an error rate, divide `RuntimeInvocationErrors` by `RuntimeInvocations` with CloudWatch metric math. For more information, see [Using math expressions with CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *Amazon CloudWatch User Guide*.

### Dimensions
<a name="cmr-monitoring-dimensions"></a>

You can view each runtime metric by the following dimensions.


**Runtime metric dimensions**  

| Dimension | Description | 
| --- | --- | 
| Runtime | The name of the runtime, for example, companyphp8. Use the runtime name, not the runtime ARN. When you use this dimension alone, the data includes all versions and aliases of the runtime. | 
| RuntimeVersion | The name of the runtime version, for example, v8.3.2. Data for this dimension includes invocations that use this version, no matter which alias resolved to it. | 
| RuntimeAlias | The name of the runtime alias, for example, prod. Data for this dimension includes invocations of functions that use this alias. Invocations of functions that are pinned to a runtime version aren't included. | 

Lambda publishes each runtime metric with the following dimension combinations:
+ `Runtime`
+ `Runtime` and `RuntimeAlias`
+ `Runtime` and `RuntimeVersion`
+ `Runtime`, `RuntimeAlias`, and `RuntimeVersion`

Lambda doesn't publish the `RuntimeAlias` or `RuntimeVersion` dimension alone. Every query must include the `Runtime` dimension.

Lambda doesn't count invocations of functions that are pinned to a runtime version in **Manual** mode in the `RuntimeAlias` dimension. These invocations appear only when you view a metric by `Runtime` alone, or by `Runtime` and `RuntimeVersion`.

### Granularity
<a name="cmr-monitoring-granularity"></a>

Lambda publishes runtime metrics at 1-minute granularity, the same as function metrics. You can use the metrics to act during a rollout, for example, to stop an alias update when the error rate rises.

### Scope and privacy
<a name="cmr-monitoring-scope"></a>

Runtime metrics appear in the runtime publisher's account, which is the account that owns the runtime. Lambda publishes the metrics in each AWS Region separately. For a runtime that you deploy to several Regions, check the metrics in each Region. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

In each Region, the metrics include invocations of all functions that use the runtime, across all accounts and organizations. The metrics don't reveal function names, account IDs, or other data about runtime consumers. You can see the impact of a runtime change across your whole consumer base, without access to your consumers' functions.

When a function uses a customer-managed runtime, Lambda includes its invocations in the aggregate metrics in the publisher's account. Runtime consumers continue to see the standard metrics for their own functions. Customer-managed runtimes don't change function metrics.

### Cost
<a name="cmr-monitoring-cost"></a>

Lambda doesn't charge extra for runtime metrics. Standard CloudWatch charges apply when you use the metrics, for example, for alarms, dashboards, and API requests. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## How to use runtime metrics
<a name="cmr-monitoring-uses"></a>

You can use runtime metrics for the following tasks.

### Check rollout health
<a name="cmr-monitoring-uses-health"></a>

When you update a runtime alias to a new runtime version, compare the error rates of the new and previous versions. If the new version has a higher error rate under similar traffic, the update might have caused a problem.

You can also compare the error rates of your aliases. For example, check whether errors are concentrated in the `prod` alias after you update it. We recommend that you create a CloudWatch alarm on the error rate of each alias. Stop your rollout or roll back when an alarm goes into the `ALARM` state. For more information about rollouts and rollbacks, see [Deploying runtime updates](cmr-deploy-updates.md).

### Track rollout progress
<a name="cmr-monitoring-uses-progress"></a>

Functions pick up an alias update at their next cold start, so a runtime update reaches functions gradually. To see how far a rollout has progressed, view the `RuntimeInvocations` metric by runtime version. As Lambda replaces execution environments, invocations shift from the previous version to the new version.

### Check usage before you delete or deprecate
<a name="cmr-monitoring-uses-usage"></a>

Lambda doesn't check whether functions use a runtime resource before you delete it. Before you delete a runtime version or alias, or deprecate a runtime, check its `RuntimeInvocations` metric. The metric shows which resources functions still use, and how many invocations a change might affect.

Choose a time range that's long enough to include functions that run infrequently, for example, 14–30 days.

**Note**  
If the `RuntimeInvocations` metric is zero, no functions invoked the resource during that time range. A zero value doesn't prove that no functions are configured to use the resource. An idle function might be invoked later. In addition, the metric for an alias doesn't include functions that are pinned to a runtime version. Their invocations appear only under the runtime version. Also check with your runtime consumers.

For more information, see [Deleting and restoring runtimes](cmr-delete.md) and [Runtime lifecycle](cmr-lifecycle.md).

## View runtime metrics
<a name="cmr-monitoring-view"></a>

You can view runtime metrics with the CloudWatch console or the AWS Command Line Interface (AWS CLI).

------
#### [ Console ]

**To view runtime metrics**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, under **Metrics**, choose **Classic metrics**.

1. Choose **Lambda**.

1. Choose **Runtime**.

1. On the **Browse** tab, choose the runtime. Then, for **RuntimeInvocations**, choose **Graph this metric only**.

1. On the **Graphed metrics** tab, for **Statistic**, select **Sum**. For **Period**, select **1 minute**.

The graph shows the total invocations of functions that use the runtime. This total includes both successful and failed invocations, across all runtime aliases and runtime versions.

To view invocations for an individual runtime alias or runtime version, at step 4, choose the **Runtime, RuntimeAlias** or **Runtime, RuntimeVersion** dimension group instead. To view invocations for each combination of alias and version, choose **Runtime, RuntimeAlias, RuntimeVersion**.

------
#### [ AWS CLI ]

To list the runtime metrics for the `companyphp8` runtime, run the following **list-metrics** command.

```bash
aws cloudwatch list-metrics \
  --region us-east-1 \
  --namespace AWS/Lambda \
  --dimensions Name=Runtime,Value={{companyphp8}}
```

The output lists each metric and dimension combination that has data. The following example shows part of the output.

```json
{
    "Metrics": [
        {
            "Namespace": "AWS/Lambda",
            "MetricName": "RuntimeInvocations",
            "Dimensions": [
                {
                    "Name": "Runtime",
                    "Value": "companyphp8"
                }
            ]
        },
        {
            "Namespace": "AWS/Lambda",
            "MetricName": "RuntimeInvocations",
            "Dimensions": [
                {
                    "Name": "Runtime",
                    "Value": "companyphp8"
                },
                {
                    "Name": "RuntimeAlias",
                    "Value": "prod"
                }
            ]
        },
        {
            "Namespace": "AWS/Lambda",
            "MetricName": "RuntimeInvocations",
            "Dimensions": [
                {
                    "Name": "Runtime",
                    "Value": "companyphp8"
                },
                {
                    "Name": "RuntimeVersion",
                    "Value": "v8.3.2"
                }
            ]
        }
    ]
}
```

**To get the error rate of a runtime alias**

1. Save the following metric queries to a file named `queries.json`. The `errorRate` expression calculates the percentage of invocations of the `prod` alias that result in an error.

   ```json
   [
       {
           "Id": "invokes",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocations",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeAlias", "Value": "prod" }
                   ]
               },
               "Period": 60,
               "Stat": "Sum"
           },
           "ReturnData": false
       },
       {
           "Id": "errors",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocationErrors",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeAlias", "Value": "prod" }
                   ]
               },
               "Period": 60,
               "Stat": "Sum"
           },
           "ReturnData": false
       },
       {
           "Id": "errorRate",
           "Expression": "100 * errors / invokes",
           "Label": "prod error rate (%)",
           "ReturnData": true
       }
   ]
   ```

1. Run the following **get-metric-data** command.

   ```bash
   aws cloudwatch get-metric-data \
     --region us-east-1 \
     --metric-data-queries file://queries.json \
     --start-time {{2026-10-05T00:00:00Z}} \
     --end-time {{2026-10-05T06:00:00Z}}
   ```

   The following example shows part of the output. Each value is the error rate, as a percentage, for one minute.

   ```json
   {
       "MetricDataResults": [
           {
               "Id": "errorRate",
               "Label": "prod error rate (%)",
               "Timestamps": [
                   "2026-10-05T05:59:00+00:00",
                   "2026-10-05T05:58:00+00:00",
                   "2026-10-05T05:57:00+00:00"
               ],
               "Values": [
                   0.12,
                   0.09,
                   0.15
               ],
               "StatusCode": "Complete"
           }
       ],
       "Messages": []
   }
   ```

To check usage over a longer time range, query only the `RuntimeInvocations` metric with a longer period, such as `86400` seconds (1 day). For an example, see [Checking usage before you delete](cmr-delete.md#cmr-delete-check-usage).

------

## Create an error rate alarm for a runtime alias
<a name="cmr-monitoring-alarm"></a>

To detect problems during a rollout, create a CloudWatch alarm on the error rate of each runtime alias. The following example creates an alarm for the `prod` alias. The alarm goes into the `ALARM` state when the error rate is greater than 1% for 3 of 5 minutes. It then sends a notification to an Amazon Simple Notification Service (Amazon SNS) topic. Your deployment pipeline can stop or roll back the rollout when the alarm goes into the `ALARM` state.

------
#### [ Console ]

First, graph the error rate of the runtime alias.

**To graph the error rate of a runtime alias**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, under **Metrics**, choose **Classic metrics**.

1. Choose **Lambda**, and then choose **Runtime, RuntimeAlias**.

1. On the **Browse** tab, for the `prod` alias of your runtime, select the **RuntimeInvocations** and **RuntimeInvocationErrors** metrics.

1. On the **Graphed metrics** tab, for each metric, select **Sum** for **Statistic** and **1 minute** for **Period**.

1. Choose **Add math**, and then choose **Start with empty expression**.

1. For the expression, enter **100 \* m2 / m1**. In this example, `m1` is the ID of `RuntimeInvocations` and `m2` is the ID of `RuntimeInvocationErrors`. If the IDs in the **Id** column are different, use those IDs instead.

Next, create the alarm on the error rate expression.

**To create the alarm**

1. On the **Graphed metrics** tab, clear the check boxes for `m1` and `m2` so that only the expression is selected.

1. In the row for the expression, choose the **Create alarm** icon.

1. Under **Conditions**, select **Static** and **Greater**, and then enter **1** for the threshold.

1. Under **Additional configuration**, for **Datapoints to alarm**, enter **3** out of **5**. For **Missing data treatment**, select **Treat missing data as good (not breaching threshold)**. Then choose **Next**.

1. Under **Notification**, for the **In alarm** state, select your Amazon SNS topic. Then choose **Next**.

1. For **Alarm name**, enter a name, such as **companyphp8-prod-error-rate**. Then choose **Next**.

1. Review the alarm settings, and then choose **Create alarm**.

Repeat these steps for each alias, such as `dev` and `test`. For more information, see [Create a CloudWatch alarm based on a metric math expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html) in the *Amazon CloudWatch User Guide*.

------
#### [ AWS CLI ]

**To create an error rate alarm for a runtime alias**

1. Save the following metric queries to a file named `alarm-metrics.json`.

   ```json
   [
       {
           "Id": "invokes",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocations",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeAlias", "Value": "prod" }
                   ]
               },
               "Period": 60,
               "Stat": "Sum"
           },
           "ReturnData": false
       },
       {
           "Id": "errors",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocationErrors",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeAlias", "Value": "prod" }
                   ]
               },
               "Period": 60,
               "Stat": "Sum"
           },
           "ReturnData": false
       },
       {
           "Id": "errorRate",
           "Expression": "100 * errors / invokes",
           "Label": "prod error rate (%)",
           "ReturnData": true
       }
   ]
   ```

1. Run the following **put-metric-alarm** command. Replace the example topic ARN with the Amazon Resource Name (ARN) of your Amazon SNS topic.

   ```bash
   aws cloudwatch put-metric-alarm \
     --region us-east-1 \
     --alarm-name {{companyphp8-prod-error-rate}} \
     --alarm-description "Error rate of the companyphp8 prod runtime alias" \
     --metrics file://alarm-metrics.json \
     --comparison-operator GreaterThanThreshold \
     --threshold 1 \
     --evaluation-periods 5 \
     --datapoints-to-alarm 3 \
     --treat-missing-data notBreaching \
     --alarm-actions {{arn:aws:sns:us-east-1:123456789012:runtime-alarms}}
   ```

   If the command succeeds, it produces no output.

1. To check the state of the alarm, run the following **describe-alarms** command.

   ```bash
   aws cloudwatch describe-alarms \
     --region us-east-1 \
     --alarm-names {{companyphp8-prod-error-rate}} \
     --query "MetricAlarms[].[AlarmName,StateValue]"
   ```

Repeat these steps for each alias, such as `dev` and `test`. For more information, see [Create a CloudWatch alarm based on a metric math expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html) in the *Amazon CloudWatch User Guide*.

------

## Compare two runtime versions
<a name="cmr-monitoring-compare"></a>

During a rollout, compare the new runtime version with the previous version. The following examples compare runtime versions `v8.3.1` and `v8.3.2`. They show the error rate and the number of invocations for each version.

------
#### [ Console ]

**To compare two runtime versions**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. In the navigation pane, under **Metrics**, choose **Classic metrics**.

1. Choose **Lambda**, and then choose **Runtime, RuntimeVersion**.

1. On the **Browse** tab, select the **RuntimeInvocations** and **RuntimeInvocationErrors** metrics for runtime versions `v8.3.1` and `v8.3.2`.

1. On the **Graphed metrics** tab, for each metric, select **Sum** for **Statistic** and **5 minutes** for **Period**.

1. To add an error rate for `v8.3.1`, choose **Add math**, and then choose **Start with empty expression**. Enter an expression such as **100 \* m2 / m1**. Use the IDs of the `v8.3.1` errors and invocations metrics from the **Id** column.

1. To add an error rate for `v8.3.2`, repeat the preceding step with the IDs of the `v8.3.2` metrics, for example, **100 \* m4 / m3**.

On the graph, compare the error rate expressions for the same time periods. To compare how invocations shift to the new version as the rollout progresses, compare the two `RuntimeInvocations` metrics. To make the graph easier to read, you can clear the check boxes for the `RuntimeInvocationErrors` metrics. The expressions still use these metrics when they're hidden.

------
#### [ AWS CLI ]

**To compare two runtime versions**

1. Save the following metric queries to a file named `compare-versions.json`.

   ```json
   [
       {
           "Id": "invokesOld",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocations",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeVersion", "Value": "v8.3.1" }
                   ]
               },
               "Period": 300,
               "Stat": "Sum"
           },
           "Label": "v8.3.1 invokes",
           "ReturnData": true
       },
       {
           "Id": "errorsOld",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocationErrors",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeVersion", "Value": "v8.3.1" }
                   ]
               },
               "Period": 300,
               "Stat": "Sum"
           },
           "ReturnData": false
       },
       {
           "Id": "invokesNew",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocations",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeVersion", "Value": "v8.3.2" }
                   ]
               },
               "Period": 300,
               "Stat": "Sum"
           },
           "Label": "v8.3.2 invokes",
           "ReturnData": true
       },
       {
           "Id": "errorsNew",
           "MetricStat": {
               "Metric": {
                   "Namespace": "AWS/Lambda",
                   "MetricName": "RuntimeInvocationErrors",
                   "Dimensions": [
                       { "Name": "Runtime", "Value": "companyphp8" },
                       { "Name": "RuntimeVersion", "Value": "v8.3.2" }
                   ]
               },
               "Period": 300,
               "Stat": "Sum"
           },
           "ReturnData": false
       },
       {
           "Id": "errorRateOld",
           "Expression": "100 * errorsOld / invokesOld",
           "Label": "v8.3.1 error rate (%)",
           "ReturnData": true
       },
       {
           "Id": "errorRateNew",
           "Expression": "100 * errorsNew / invokesNew",
           "Label": "v8.3.2 error rate (%)",
           "ReturnData": true
       }
   ]
   ```

1. Run the following **get-metric-data** command.

   ```bash
   aws cloudwatch get-metric-data \
     --region us-east-1 \
     --metric-data-queries file://compare-versions.json \
     --start-time {{2026-10-05T00:00:00Z}} \
     --end-time {{2026-10-05T06:00:00Z}}
   ```

In the output, compare the `v8.3.1 error rate (%)` and `v8.3.2 error rate (%)` values for the same time periods. The `v8.3.1 invokes` and `v8.3.2 invokes` values show how invocations shift to the new version as the rollout progresses.

To view the same comparison on a CloudWatch dashboard, you can use the **put-dashboard** command. The following dashboard body shows invocations and error rates for each version.

```json
{
    "widgets": [
        {
            "type": "metric",
            "x": 0,
            "y": 0,
            "width": 12,
            "height": 6,
            "properties": {
                "title": "companyphp8 invokes by runtime version",
                "region": "us-east-1",
                "view": "timeSeries",
                "stat": "Sum",
                "period": 60,
                "metrics": [
                    [ "AWS/Lambda", "RuntimeInvocations", "Runtime", "companyphp8", "RuntimeVersion", "v8.3.1" ],
                    [ "AWS/Lambda", "RuntimeInvocations", "Runtime", "companyphp8", "RuntimeVersion", "v8.3.2" ]
                ]
            }
        },
        {
            "type": "metric",
            "x": 12,
            "y": 0,
            "width": 12,
            "height": 6,
            "properties": {
                "title": "companyphp8 error rate by runtime version (%)",
                "region": "us-east-1",
                "view": "timeSeries",
                "stat": "Sum",
                "period": 60,
                "metrics": [
                    [ { "expression": "100 * e1 / i1", "label": "v8.3.1 error rate (%)", "id": "r1" } ],
                    [ { "expression": "100 * e2 / i2", "label": "v8.3.2 error rate (%)", "id": "r2" } ],
                    [ "AWS/Lambda", "RuntimeInvocations", "Runtime", "companyphp8", "RuntimeVersion", "v8.3.1", { "id": "i1", "visible": false } ],
                    [ "AWS/Lambda", "RuntimeInvocationErrors", "Runtime", "companyphp8", "RuntimeVersion", "v8.3.1", { "id": "e1", "visible": false } ],
                    [ "AWS/Lambda", "RuntimeInvocations", "Runtime", "companyphp8", "RuntimeVersion", "v8.3.2", { "id": "i2", "visible": false } ],
                    [ "AWS/Lambda", "RuntimeInvocationErrors", "Runtime", "companyphp8", "RuntimeVersion", "v8.3.2", { "id": "e2", "visible": false } ]
                ]
            }
        }
    ]
}
```

To create the dashboard, save the dashboard body to a file named `dashboard.json`, and then run the following command.

```bash
aws cloudwatch put-dashboard \
  --region us-east-1 \
  --dashboard-name {{companyphp8-rollout}} \
  --dashboard-body file://dashboard.json
```

For more information, see [Creating a CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) in the *Amazon CloudWatch User Guide*.

------

## Logging customer-managed runtime API calls with CloudTrail
<a name="cmr-monitoring-cloudtrail"></a>

AWS CloudTrail logs API calls for runtimes, runtime versions, runtime aliases, resource-based policies, and tags as management events. The event source is `lambda.amazonaws.com`. You can use these events to see who changed a runtime resource, and when. For more information about how Lambda works with CloudTrail, including Event history and trails, see [Logging AWS Lambda API calls using AWS CloudTrail](logging-using-cloudtrail.md).

The following table lists the CloudTrail event names for customer-managed runtime API calls.


**CloudTrail event names for customer-managed runtimes**  

| Resource | Event names | 
| --- | --- | 
| Runtime | CreateRuntime, GetRuntime, ListRuntimes, UpdateRuntime, DeleteRuntime, RestoreRuntime | 
| Runtime version | CreateRuntimeVersion, GetRuntimeVersion, ListRuntimeVersions, UpdateRuntimeVersion, DeleteRuntimeVersion | 
| Runtime alias | CreateRuntimeAlias, GetRuntimeAlias, ListRuntimeAliases, UpdateRuntimeAlias, DeleteRuntimeAlias | 
| Resource-based policy | PutResourcePolicy, GetResourcePolicy, DeleteResourcePolicy | 
| Tags | TagResource20170331v2, UntagResource20170331v2, ListTags20170331 | 

Function invocations are data events for the `AWS::Lambda::Function` resource type, the same as for other functions. CloudTrail doesn't have data events specific to customer-managed runtimes. For more information, see [Lambda data events in CloudTrail](logging-using-cloudtrail.md#cloudtrail-data-events).

### Events when a function uses a runtime
<a name="cmr-monitoring-cloudtrail-functions"></a>

The `lambda:AssociateRuntimeAlias` and `lambda:AssociateRuntimeVersion` actions are permission checks only. CloudTrail doesn't log them as separate events. Instead, CloudTrail logs the function operation that uses the runtime:
+ `CreateFunction20150331` – When you create a function that uses a runtime alias.
+ `UpdateFunctionConfiguration20150331v2` – When you set or change the runtime alias of a function.
+ `PutRuntimeManagementConfig` – When you pin a function to a runtime version in **Manual** mode.

These events include the runtime configuration of the function:
+ In `CreateFunction` and `UpdateFunctionConfiguration` events, `requestParameters` and `responseElements` include a `runtimeConfig` object with the `runtimeArn` and `runtimeAlias`. The `responseElements` also include `runtimeVersionConfig`, which shows the runtime version that the alias pointed to.
+ In `PutRuntimeManagementConfig` events, `requestParameters` and `responseElements` include the `runtimeVersionArn`.
+ The `resources` list includes the function and the runtime resource. The function has the type `AWS::Lambda::Function`, or `AWS::Lambda::Version` for a published version. The runtime resource has the type `AWS::Lambda::RuntimeAlias` or `AWS::Lambda::RuntimeVersion`.

When the function and the runtime are in different accounts, CloudTrail delivers these events to both accounts, whether Lambda allows or denies the request. As a runtime publisher, you can review these events in your own account to see which accounts use your runtime. For allowed requests, your copy also includes the function ARN in `requestParameters` and `resources`.

CloudTrail logs some function operations only in the consumer's account. These include operations that don't reference your runtime, such as an `UpdateFunctionConfiguration` request that changes only the timeout. They also include `PutRuntimeManagementConfig` requests that set **Auto** or **Function update** mode. Requests for a runtime that doesn't exist are also logged only in the consumer's account.

In the runtime publisher's copy, the `userIdentity` field identifies the caller only by account. The `type` is `AWSAccount`, and the `accountId` is the consumer's account ID. The publisher's copy doesn't include the IAM principal that made the request. Both copies have the same `requestID` and `sharedEventID`.

If Lambda denies the request, CloudTrail logs the event under the function operation event name with the `errorCode` `AccessDenied`. For example, this happens when the runtime's resource-based policy doesn't allow `lambda:AssociateRuntimeAlias`. The `errorMessage` names the action that was denied. The runtime publisher's copy of a denied event doesn't include `requestParameters`.

When you change the runtime alias of a function, the `UpdateFunctionConfiguration` event records the new alias. To find the alias that the function used before, review earlier events for the function.

The following example shows a `CreateFunction` event for a function that uses the `prod` alias of the `companyphp8` runtime. The example omits some fields.

```json
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAEXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/my-user",
        "accountId": "123456789012",
        "userName": "my-user"
    },
    "eventTime": "2026-11-06T18:09:29Z",
    "eventSource": "lambda.amazonaws.com",
    "eventName": "CreateFunction20150331",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "requestParameters": {
        "functionName": "my-function",
        "runtime": "custom",
        "role": "arn:aws:iam::123456789012:role/my-lambda-role",
        "handler": "index.handler",
        "architectures": [
            "x86_64"
        ],
        "runtimeConfig": {
            "runtimeArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
            "runtimeAlias": "prod"
        }
    },
    "responseElements": {
        "functionName": "my-function",
        "functionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
        "runtime": "custom",
        "version": "$LATEST",
        "runtimeConfig": {
            "runtimeArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
            "runtimeAlias": "prod"
        },
        "runtimeVersionConfig": {
            "runtimeVersionArn": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.2"
        }
    },
    "requestID": "EXAMPLE-1111-2222-3333-444444444444",
    "eventID": "EXAMPLE-5555-6666-7777-888888888888",
    "readOnly": false,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::Lambda::RuntimeAlias",
            "ARN": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod"
        },
        {
            "accountId": "123456789012",
            "type": "AWS::Lambda::Function",
            "ARN": "arn:aws:lambda:us-east-1:123456789012:function:my-function"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

### Track runtime alias changes
<a name="cmr-monitoring-cloudtrail-aliases"></a>

When you point a runtime alias to a different runtime version, CloudTrail logs an `UpdateRuntimeAlias` event in your account. The `requestParameters` include the name of the new runtime version in `runtimeVersion`. The `responseElements` include the ARN of the new version in `runtimeVersionArn`.

Functions that use the alias pick up the new version at their next cold start. CloudTrail doesn't log a separate event for each function. To see which version an alias pointed to at a given time, review the `CreateRuntimeAlias` and `UpdateRuntimeAlias` events for the alias. To see how invocations shift to the new version across all functions, use the runtime metrics. For more information, see [Track rollout progress](#cmr-monitoring-uses-progress). To confirm which runtime version a specific function uses, check the `INIT_START` line in the function's logs. Lambda writes this line each time it creates an execution environment, and the line includes the runtime version and runtime version ARN. Function owners can see these logs in their own accounts. For more information, see [Check which runtime version your function uses](cmr-using.md#cmr-using-check-version).

## Related topics
<a name="cmr-monitoring-related"></a>

For more information about tasks that use runtime metrics and CloudTrail events, see the following topics:
+ [Deploying runtime updates](cmr-deploy-updates.md)
+ [Deploying runtimes in multiple Regions](cmr-multi-region.md)
+ [Runtime lifecycle](cmr-lifecycle.md)
+ [Deleting and restoring runtimes](cmr-delete.md)
+ [Using a customer-managed runtime](cmr-using.md)
+ [Logging AWS Lambda API calls using AWS CloudTrail](logging-using-cloudtrail.md)