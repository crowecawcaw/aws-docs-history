

# Monitoring Step Functions metrics using Amazon CloudWatch
<a name="procedure-cw-metrics"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Step Functions and your AWS solutions. You can collect data from the AWS services that you use to debug multi-point failures. 

Before you start monitoring Step Functions, you should create a monitoring plan that answers the following questions:
+ What are your monitoring goals?
+ What resources will you monitor?
+ How often will you monitor these resources?
+ What monitoring tools will you use?
+ Who will perform the monitoring tasks?
+ Who should be notified when something goes wrong?

The next step is to establish a baseline for normal performance in your environment. To do this, measure performance at various times and under different load conditions. As you monitor Step Functions, consider storing historical monitoring data. Such data can give you a baseline to compare against current performance data, to identify normal performance patterns and performance anomalies, and to devise ways to address issues.

We recommend monitoring Activity and Task failures to establish a baseline. When performance falls outside your baseline metric, set an alert so you can research the root cause.

To establish a baseline you should, at a minimum, monitor the following metrics:
+  `ExecutionsStarted` 
+  `ExecutionsTimedOut` 
+  *Optional* (if you use Activities) - `ActivitiesStarted` 
+  *Optional* (if you use Activities) - `ActivitiesTimedOut` 

## Types of Step Functions metrics for CloudWatch
<a name="sfn-cw-metrics"></a>

Step Functions provides the following types of metrics to Amazon CloudWatch. You can use these metrics to track your state machines and activities and to set alarms on threshold values. You can view metrics using the AWS Management Console.

Metrics are grouped by a *namespace*, a container for CloudWatch metrics, so that metrics from different applications are not mistakenly aggregated together. 

**Non-ASCII names and logging**  
Step Functions accepts names for state machines, executions, activities, and labels that contain non-ASCII characters. Because such characters will prevent Amazon CloudWatch from logging data, we recommend using only ASCII characters so you can track Step Functions metrics.

### CloudWatch metrics delivery
<a name="cloudwatch-best-effort"></a>

CloudWatch metrics are delivered on a best-effort basis.

The completeness and timeliness of metrics are not guaranteed. The data point for a particular request might be returned with a timestamp that is later than when the request was actually processed. The data point for a minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch request metrics give you an idea of the state machine executions in near-real time. It is not meant to be a complete accounting of all execution-related metrics.

It follows from the best-effort nature of this feature that the reports available at the [Billing & Cost Management Dashboard](https://console.aws.amazon.com/billing/home?#/) might include one or more access requests that do not appear in the execution metrics.

### Metrics that report a time interval
<a name="monitoring-using-cloudwatch-time-interval-metrics"></a>

Some of the Step Functions CloudWatch metrics are *time intervals*, always measured in milliseconds. These metrics generally correspond to stages of your execution for which you can set state machine, activity, and Lambda function timeouts, with descriptive names.

For example, the `ActivityRunTime` metric measures the time it takes for an activity to complete after it begins to execute. You can set a timeout value for the same time period.

In the CloudWatch console, you can get the best results if you choose **average** as the display statistic for time interval metrics.

### Metrics that report a count
<a name="monitoring-using-cloudwatch-count-metrics"></a>

Some of the Step Functions CloudWatch metrics report results as a *count*. For example, `ExecutionsFailed` records the number of failed state machine executions.

Of note, Step Functions emits **two** `ExecutionsStarted` metrics for every state machine execution. As a result, the [SampleCount](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) statistic for the `ExecutionsStarted` metric will show the value of **2** for every state machine execution. The SampleCount statistic shows `ExecutionStarted=1` and then `ExecutionStarted=0` after the execution completes.

Similarly, other execution status metrics can emit more than once due to at-least-once and best-effort delivery for CloudWatch metrics.

**Tip**  
We recommend using **Sum** as the display statistic for metrics that report a count in the CloudWatch console.

## Viewing Step Functions metrics in CloudWatch
<a name="monitoring-using-cloudwatch-console"></a>

You can use the CloudWatch console to view Step Functions metrics for executions, activities, functions, and service integrations.

1. Sign in to the AWS Management Console and open the CloudWatch console.

1. Choose **Metrics**, and on the **All Metrics** tab, choose **States**.

   If you ran any executions recently, you will see up to four types of metrics:
   +  **Execution Metrics** 
   +  **Activity Function Metrics** 
   +  **Lambda Function Metrics** 
   +  **Service Integration Metrics** 

1. Choose a metric type to see a list of metrics.
   + To view graphs for a metric, choose the box next to the metric on the list. You can change the graph parameters using the time range controls above the graph view.

     You can choose custom time ranges using relative or absolute values (specific days and times). You can also use the dropdown list to display values as lines, stacked areas, or numbers (values).
   + To view the details about a graph, hover over the metric color code that appears below the graph to display the metric details.

For more information about working with CloudWatch metrics, see [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/working_with_metrics.html) in the *Amazon CloudWatch User Guide*.

## Setting alarms for Step Functions metrics in CloudWatch
<a name="monitoring-using-cloudwatch-console-set-alarm"></a>

You can use Amazon CloudWatch alarms to perform actions. For example, if you want to know when an alarm threshold is reached, you can set an alarm to send a notification to an Amazon SNS topic or to send an email when the `StateMachinesFailed` metric rises above a certain threshold.

### To set an alarm on a metric
<a name="to-set-an-alarm-on-a-metric"></a>

1. Sign in to the AWS Management Console and open the CloudWatch console.

1. Choose one or more metrics to view, then choose **Graphed metrics**.

1. Choose the bell-shaped icon next to a metric on the list to display the **Create Alarm** page.

1. Enter the values for the **Alarm threshold** and **Actions**, and then choose **Create Alarm**.

For more information about setting and using CloudWatch alarms, see [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Account-level Usage Metrics
<a name="cloudwatch-step-functions-account-metrics"></a>

The `AWS/Usage` namespace includes the following Step Functions metrics. 

The following metrics are dimensionless and apply across your account in a region. 


| Metric | Description | 
| --- | --- | 
| StateMachineCount | Count of currently active State Machines in your account. You might need to add or delete a State Machine in your account and wait a few minutes to activate this metric for your account. | 
| ActivityCount | Count of currently active Activities in your account. You might need to add or delete an Activity in your account and wait a few minutes to activate this metric for your account. | 
| OpenExecutionCountPerStateMachine | Open executions per state machine in your account. | 

## Execution Metrics
<a name="cloudwatch-step-functions-execution-metrics"></a>

The `AWS/States` namespace includes the following metrics for all Step Functions executions. 

The following metrics are dimensionless and apply across your account in a region.


| Metric | Description | 
| --- | --- | 
| OpenExecutionCount | Approximate number of currently *open executions*—workflows that are currently in progress in your account.<br />The intent is to provide insight into when your workflows are approaching the **maximum** execution limit, to avoid **ExecutionLimitExceeded** errors when calling `StartExecution` or `RedriveExecution` for Standard Workflows.<br />`OpenExecutionCount` is an approximate number of open workflows. This metric will be lower than observed running workflow count. Running open workflow count lower than 10,000 may show zero open executions. For an alarm to notify when nearing your `OpenExecutionLimit`, we recommend using the [Maximum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) statistic with a threshold of 100K or higher since the default open workflow limit is 1,000,000 executions.  | 
| OpenExecutionLimit | Maximum number of open executions. For more information, see [Quotas related to accounts](service-quotas.md#service-limits-accounts). <br /> *This limit does not apply to Express Workflows.*  | 

### Execution metrics for all state machines
<a name="cloudwatch-step-functions-execution-metrics-version-alias"></a>

All state machines emit metrics. The `ExecutionThrottled` metric will only be emitted in the case of throttled execution. 

The following metrics can be filtered with a `StateMachineArn` to identify a specific state machine.

**Account level metrics**  
Without a state machine ARN, the following metrics report at the **account level**. Provide a state machine ARN to report at the state machine level.


| Metric | Description | 
| --- | --- | 
| ExecutionsAborted | Number of aborted or terminated executions. | 
| ExecutionsFailed | Number of failed executions. | 
| ExecutionsStarted | Number of started executions. | 
| ExecutionsSucceeded | Number of successfully completed executions. | 
| ExecutionsTimedOut | Number of executions that time out for any reason. | 
| ExecutionThrottled | Number of StateEntered events and retries that have been throttled. This is related to StateTransition throttling. For more information, see [Quotas related to state throttling](service-quotas.md#service-limits-api-state-throttling). | 
| ExecutionTime | Interval, in milliseconds, between the time the execution starts and the time it closes. | 

### Execution metrics for Express Workflows
<a name="cloudwatch-step-functions-execution-metrics-express-wf"></a>

The `AWS/States` namespace includes the following metrics for Step Functions Express Workflows' executions.

**Account level metrics**  
Without a state machine ARN, the `ExpressExecutionBilledDuration` and `ExpressExecutionBilledMemory` report at the **account level**. Provide a state machine ARN to report at the state machine level.


| Metric | Description | 
| --- | --- | 
| ExpressExecutionBilledDuration | The duration for which an Express Workflow is charged. | 
| ExpressExecutionBilledMemory | The amount of consumed memory for which an Express Workflow is charged. | 
|  ExpressExecutionMemory  | The total memory consumed by a specific Express Workflow. | 

### Redrive execution metrics for Standard Workflows
<a name="cloudwatch-redrive-execution-metrics"></a>

When you [redrive](redrive-executions.md) a state machine execution, Step Functions emits the following metrics.

For all redriven executions, the `Executions*` metric is emitted. For example, say a redriven execution aborts. This execution will emit non-zero datapoints for both `RedrivenExecutionsAborted` and `ExecutionsAborted`.


| Metric | Description | 
| --- | --- | 
| ExecutionsRedriven | Number of redriven executions. | 
| RedrivenExecutionsAborted | Number of redriven executions that are canceled or terminated. | 
| RedrivenExecutionsTimedOut | Number of redriven executions that time out for any reason. | 
| RedrivenExecutionsSucceeded | Number of redriven executions that completed successfully. | 
| RedrivenExecutionsFailed | Number of redriven executions that failed. | 

### Dimension for Step Functions execution metrics
<a name="cloudwatch-step-functions-execution-metrics-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
|  StateMachineArn  | The Amazon Resource Name (ARN) of the state machine for the execution in question. | 

### Dimensions for executions with version
<a name="cloudwatch-setp-functions-version-metrics-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
|  StateMachineArn  | The Amazon Resource Name (ARN) of the state machine whose execution was started by a [version](concepts-state-machine-version.md). | 
| Version | State machine version used to start the execution. | 

### Dimensions for executions with an alias
<a name="cloudwatch-setp-functions-alias-metrics-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
|  StateMachineArn  | The Amazon Resource Name (ARN) of the state machine whose execution was started by an [alias](concepts-state-machine-alias.md). | 
| Alias | State machine alias used to start the execution. | 

## Map Run Metrics
<a name="resource-count-metrics-map-run"></a>

The `AWS/States` namespace includes the following metrics for all Step Functions map runs. These are dimensionless metrics that apply across your account in a region.


| Metric | Description | 
| --- | --- | 
| ApproximateOpenMapRunCount | Approximate number of currently open Map Runs in progress in your account. <br />With this metric, you can take action when you are approaching the **OpenMapRunLimit**, to avoid backlogged Map Runs. <br />For an alarm to notify if you are nearing your **OpenMapRunLimit**, we recommend using the **Maximum **statistic with a threshold of 900 or higher, because the default **OpenManRunLimit** is 1,000 map runs. | 
| OpenMapRunLimit | Maximum number of open Map Runs. <br />For more information, see [Quotas related to accounts](service-quotas.md#service-limits-accounts). | 
| ApproximateMapRunBacklogSize | Approximate number of [Map Runs](concepts-examine-map-run.md) that are *backlogged*. Backlogged Map Runs wait at the [MapRunStarted](https://docs.aws.amazon.com/step-functions/latest/apireference/API_MapRunStartedEventDetails.html) event until the total number of open Map Runs is less than the quota.<br />The count of items will be zero while the Map Run is backlogged. The count will increase after the Map Run becomes open and starts to read its input. | 

## Version and Alias Metrics
<a name="resource-count-metrics-alias-versions"></a>

The `AWS/States` namespace includes the following metrics for the counts of versions and aliases of a state machine.


| Metric | Description | 
| --- | --- | 
| AliasCount | Number of [aliases](concepts-state-machine-alias.md) created for the state machine.<br />You can [create](concepts-state-machine-alias.md#procedure-create-aliases) up to 100 aliases for each state machine. | 
| VersionCount | Number of [versions](concepts-state-machine-version.md) published for the state machine.<br />You can [publish](concepts-state-machine-version.md#procedure-create-versions) up to 1000 versions of a state machine. | 

### Dimension for resource count metrics for versions and aliases
<a name="resource-count-metrics-alias-versions-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
|  ResourceArn  | The Amazon Resource Name (ARN) of the state machine with a version or an alias. | 

## Activity Metrics
<a name="cloudwatch-step-functions-activity-metrics"></a>

The `AWS/States` namespace includes the following metrics for Step Functions activities.

**Account level metrics**  
Without a state machine ARN, the following metrics report at the **account level**. Provide a state machine ARN to report at the state machine level.


| Metric | Description | 
| --- | --- | 
| ActivitiesFailed | Number of failed activities. | 
| ActivitiesHeartbeatTimedOut | Number of activities that time out due to a heartbeat timeout. | 
| ActivitiesScheduled | Number of scheduled activities. | 
| ActivitiesStarted | Number of started activities. | 
| ActivitiesSucceeded | Number of successfully completed activities. | 
| ActivitiesTimedOut | Number of activities that time out on close. | 
| ActivityRunTime  | Interval, in milliseconds, between the time the activity starts and the time it closes. | 
| ActivityScheduleTime | Interval, in milliseconds, for which the activity stays in the schedule state. | 
| ActivityTime | Interval, in milliseconds, between the time the activity is scheduled and the time it closes. | 

### Dimension for Step Functions Activity Metrics
<a name="cloudwatch-step-functions-activity-metrics-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
| ActivityArn | The ARN of the activity. | 

## Lambda Function Metrics
<a name="cloudwatch-step-functions-lambda-function-metrics"></a>

The `AWS/States` namespace includes the following metrics for Lambda functions which are referred to **directly** in the Resource field of a Task state definition. You might find these metrics in legacy state machines. In modern state machines, we recommend using the Optimized Lambda integration which emits Service Integration Metrics.


|  Metric  |  Description  | 
| --- | --- | 
| LambdaFunctionRunTime | Interval, in milliseconds, between the time the Lambda function starts and the time it closes. | 
| LambdaFunctionScheduleTime | Interval, in milliseconds, for which the Lambda function stays in the schedule state. | 
| LambdaFunctionTime | Interval, in milliseconds, between the time the Lambda function is scheduled and the time it closes. | 
| LambdaFunctionsFailed | Number of failed Lambda functions. | 
| LambdaFunctionsScheduled | Number of scheduled Lambda functions. | 
| LambdaFunctionsStarted | Number of started Lambda functions. | 
| LambdaFunctionsSucceeded | Number of successfully completed Lambda functions. | 
| LambdaFunctionsTimedOut | Number of Lambda functions that time out on close. | 

### Dimension for Step Functions Lambda Function Metrics
<a name="cloudwatch-step-functions-lambda-function-metrics-dimensions"></a>


|  Dimension  |  Description  | 
| --- | --- | 
| LambdaFunctionArn | The ARN of the Lambda function. | 

**Note**  
Lambda Function Metrics are emitted for Task states that specify the Lambda function ARN in the ` Resource` field. Task states that use `"Resource": "arn:aws:states:::lambda:invoke"` emit Service Integration Metrics instead. For more information, see [Invoke an AWS Lambda function with Step Functions](connect-lambda.md). 

## Service Integration Metrics
<a name="cloudwatch-step-functions-service-integration-metrics"></a>

The `AWS/States` namespace includes the following metrics for Step Functions service integrations. For more information, see [Integrating services with Step Functions](integrate-services.md). 


|  Metric  |  Description  | 
| --- | --- | 
| ServiceIntegrationRunTime | Interval, in milliseconds, between the time the Service Task starts and the time it closes. | 
| ServiceIntegrationScheduleTime | Interval, in milliseconds, for which the Service Task stays in the schedule state. | 
| ServiceIntegrationTime | Interval, in milliseconds, between the time the Service Task is scheduled and the time it closes. | 
| ServiceIntegrationsFailed | Number of failed Service Tasks. | 
| ServiceIntegrationsScheduled | Number of scheduled Service Tasks. | 
| ServiceIntegrationsStarted | Number of started Service Tasks. | 
| ServiceIntegrationsSucceeded | Number of successfully completed Service Tasks. | 
| ServiceIntegrationsTimedOut | Number of Service Tasks that time out on close. | 

### Dimension for Step Functions Service Integration Metrics
<a name="cloudwatch-step-functions-service-integration-metrics-dimensions"></a>


|  Dimension  |  Description  | 
| --- | --- | 
| ServiceIntegrationResourceArn | The resource ARN of the integrated service. | 

## Service Metrics
<a name="cloudwatch-step-functions-service-metrics"></a>

The `AWS/States` namespace includes the following metrics for the Step Functions service metrics.

**Account level metrics**  
Without a state machine ARN, the following metrics report at the **account level**. Provide a state machine ARN to report at the state machine level.


| Metric | Description | 
| --- | --- | 
| ConsumedCapacity | Count of requests per second. | 
| ProvisionedBucketSize | Count of available requests per second. | 
| ProvisionedRefillRate | Count of requests per second that are allowed into the bucket. | 
| ThrottledEvents  | Count of requests that have been throttled. | 

### Dimension for Step Functions Service Metrics
<a name="cloudwatch-step-functions-service-metrics-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
| ServiceMetric | Filters data to show StateTransition. | 
| StateMachineArn | Filters data to show transitions for a specific State Machine. | 

## API Usage Metrics
<a name="cloudwatch-step-functions-api-metrics"></a>

The `AWS/States` namespace includes the following metrics for the Step Functions API.


| Metric | Description | 
| --- | --- | 
| ThrottledEvents  | Count of requests that have been throttled. | 
| ProvisionedBucketSize | Count of available requests per second. | 
| ProvisionedRefillRate | Count of requests per second that are allowed into the bucket. | 
| ConsumedCapacity | Count of requests per second. | 

### Dimension for Step Functions API Metrics
<a name="cloudwatch-step-functions-api-metrics-dimensions"></a>


| Dimension | Description | 
| --- | --- | 
| APIName | Filters data to an API of the specified API name. | 