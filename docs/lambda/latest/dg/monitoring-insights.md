

# Monitor Event Function performance with Amazon CloudWatch Lambda Insights
<a name="monitoring-insights"></a>

Amazon CloudWatch Lambda Insights collects and aggregates Lambda Event Function runtime performance metrics and logs for your serverless applications. This page describes how to enable and use Lambda Insights to diagnose issues with your Lambda Event Functions.

**Topics**
+ [How Lambda Insights monitors serverless applications](#monitoring-insights-how)
+ [Pricing](#monitoring-insights-pricing)
+ [Supported runtimes](#monitoring-insights-runtimes)
+ [Enabling Lambda Insights in the Lambda console](#monitoring-insights-enabling-console)
+ [Enabling Lambda Insights programmatically](#monitoring-insights-enabling-programmatically)
+ [Using the Lambda Insights dashboard](#monitoring-insights-multifunction)
+ [Example workflow to detect Event Function anomalies](#monitoring-insights-anomalies)
+ [Example workflow using queries to troubleshoot an Event Function](#monitoring-insights-queries)
+ [What's next?](#monitoring-console-next-up)

## How Lambda Insights monitors serverless applications
<a name="monitoring-insights-how"></a>

CloudWatch Lambda Insights is a monitoring and troubleshooting solution for serverless applications running on AWS Lambda. The solution collects, aggregates, and summarizes system-level metrics including CPU time, memory, disk and network usage. It also collects, aggregates, and summarizes diagnostic information such as cold starts and Lambda worker shutdowns to help you isolate issues with your Lambda Event Functions and resolve them quickly.

Lambda Insights uses a new CloudWatch Lambda Insights [extension](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html), which is provided as a [Lambda layer](chapter-layers.md). When you enable this extension on a Lambda Event Function for a supported runtime, it collects system-level metrics and emits a single performance log event for every invocation of that Lambda Event Function. CloudWatch uses embedded metric formatting to extract metrics from the log events. For more information, see [Using AWS Lambda extensions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html).

The Lambda Insights layer extends the `CreateLogStream` and `PutLogEvents` for the `/aws/lambda-insights/` log group.

## Pricing
<a name="monitoring-insights-pricing"></a>

When you enable Lambda Insights for your Lambda Event Function, Lambda Insights reports 8 metrics per Event Function and every Event Function invocation sends about 1KB of log data to CloudWatch. You only pay for the metrics and logs reported for your Event Function by Lambda Insights. There are no minimum fees or mandatory service usage policies. You do not pay for Lambda Insights if the Event Function is not invoked. For a pricing example, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/). 

## Supported runtimes
<a name="monitoring-insights-runtimes"></a>

You can use Lambda Insights with any of the runtimes that support [Lambda extensions](runtimes-extensions-api.md).

## Enabling Lambda Insights in the Lambda console
<a name="monitoring-insights-enabling-console"></a>

You can enable Lambda Insights enhanced monitoring on new and existing Lambda Event Functions. When you enable Lambda Insights on an Event Function in the Lambda console for a supported runtime, Lambda adds the Lambda Insights [extension](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html) as a layer to your Event Function, and verifies or attempts to attach the [CloudWatchLambdaInsightsExecutionRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLambdaInsightsExecutionRolePolicy$jsonEditor) policy to your Event Function's [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html).

**To enable Lambda Insights in the Lambda console**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your Event Function.

1. Choose the **Configuration** tab.

1. On the left menu, choose **Monitoring and operations tools**.

1. On the **Additional monitoring tools** pane, choose **Edit**.

1. Under **CloudWatch Lambda Insights**, turn on **Enhanced monitoring**.

1. Choose **Save**.

## Enabling Lambda Insights programmatically
<a name="monitoring-insights-enabling-programmatically"></a>

You can also enable Lambda Insights using the AWS Command Line Interface (AWS CLI), AWS Serverless Application Model (SAM) CLI, CloudFormation, or the AWS Cloud Development Kit (AWS CDK). When you enable Lambda Insights programmatically on an Event Function for a supported runtime, CloudWatch attaches the [CloudWatchLambdaInsightsExecutionRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLambdaInsightsExecutionRolePolicy$jsonEditor) policy to your Event Function's [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html).

For more information, see [Getting started with Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started.html) in the *Amazon CloudWatch User Guide*.

## Using the Lambda Insights dashboard
<a name="monitoring-insights-multifunction"></a>

The Lambda Insights dashboard has two views in the CloudWatch console: the multi-function overview and the single-function view. The multi-function overview aggregates the runtime metrics for the Lambda Event Functions in the current AWS account and Region. The single-function view shows the available runtime metrics for a single Lambda Event Function.

You can use the Lambda Insights dashboard multi-function overview in the CloudWatch console to identify over- and under-utilized Lambda Event Functions. You can use the Lambda Insights dashboard single-function view in the CloudWatch console to troubleshoot individual requests.

**To view the runtime metrics for all Event Functions**

1. Open the [Multi-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance) page in the CloudWatch console.

1. Choose from the predefined time ranges, or choose a custom time range.

1. (Optional) Choose **Add to dashboard** to add the widgets to your CloudWatch dashboard.  
![The multi-function overview on the Lambda Insights dashboard.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-multifunction-view.png)

**To view the runtime metrics of a single Event Function**

1. Open the [Single-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:functions) page in the CloudWatch console.

1. Choose from the predefined time ranges, or choose a custom time range.

1. (Optional) Choose **Add to dashboard** to add the widgets to your CloudWatch dashboard.  
![The single-function view on the Lambda Insights dashboard.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambainsights-singlefunction-view.png)

For more information, see [Creating and working with widgets on CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html).

## Example workflow to detect Event Function anomalies
<a name="monitoring-insights-anomalies"></a>

You can use the multi-function overview on the Lambda Insights dashboard to identify and detect compute memory anomalies with your Event Function. For example, if the multi-function overview indicates that an Event Function is using a large amount of memory, you can view detailed memory utilization metrics in the **Memory Usage** pane. You can then go to the Metrics dashboard to enable anomaly detection or create an alarm.

**To enable anomaly detection for an Event Function**

1. Open the [Multi-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance) page in the CloudWatch console.

1. Under **Function summary**, choose your Event Function's name.

   The single-function view opens with the Event Function runtime metrics.  
![The function summary pane on the Lambda Insights dashboard.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-function-summary.png)

1. On the **Memory Usage** pane, choose the three vertical dots, and then choose **View in metrics** to open the **Metrics** dashboard.  
![The menu on the Memory Usage pane.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-memory-usage.png)

1. On the **Graphed metrics** tab, in the **Actions** column, choose the first icon to enable anomaly detection for the Event Function.  
![The Graphed metrics tab of the Memory Usage pane.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-graphed-metrics.png)

For more information, see [Using CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html).

## Example workflow using queries to troubleshoot an Event Function
<a name="monitoring-insights-queries"></a>

You can use the single-function view on the Lambda Insights dashboard to identify the root cause of a spike in Event Function duration. For example, if the multi-function overview indicates a large increase in Event Function duration, you can pause on or choose each Event Function in the **Duration** pane to determine which Event Function is causing the increase. You can then go to the single-function view and review the **Application logs** to determine the root cause.

**To run queries on an Event Function**

1. Open the [Multi-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance) page in the CloudWatch console.

1. In the **Duration** pane, choose your function to filter the duration metrics.  
![A function chosen in the Duration pane.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-choose-function.png)

1. Open the [Single-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:functions) page.

1. Choose the **Filter metrics by function name** dropdown list, and then choose your function.

1. To view the **Most recent 1000 application logs**, choose the **Application logs** tab.

1. Review the **Timestamp** and **Message** to identify the invocation request that you want to troubleshoot.  
![The Most recent 1000 application logs.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-application-logs.png)

1. To show the **Most recent 1000 invocations**, choose the **Invocations** tab.

1. Select the **Timestamp** or **Message** for the invocation request that you want to troubleshoot.  
![Selecting a recent invocation request.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-invocations-function-select.png)

1. Choose the **View logs** dropdown list, and then choose **View performance logs**.

   An autogenerated query for your Event Function opens in the **Logs Insights** dashboard.

1. Choose **Run query** to generate a **Logs** message for the invocation request.  
![Querying the selected function in the Logs Insights dashboard.](https://docs.aws.amazon.com/lambda/latest/dg/images/lambdainsights-query.png)

## What's next?
<a name="monitoring-console-next-up"></a>
+ Learn how to create a CloudWatch Logs dashboard in [Create a Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) in the *Amazon CloudWatch User Guide*.
+ Learn how to add queries to a CloudWatch Logs dashboard in [Add Query to Dashboard or Export Query Results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_ExportQueryResults.html) in the *Amazon CloudWatch User Guide*.