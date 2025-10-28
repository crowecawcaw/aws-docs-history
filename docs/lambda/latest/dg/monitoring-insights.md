# Monitor function performance with Amazon CloudWatch Lambda Insights

Amazon CloudWatch Lambda Insights collects and aggregates Lambda function runtime performance metrics and logs for your
serverless applications. This page describes how to enable and use Lambda Insights to diagnose issues with your
Lambda functions.

###### Sections

- [How Lambda Insights monitors serverless applications](#monitoring-insights-how "#monitoring-insights-how")
- [Pricing](#monitoring-insights-pricing "#monitoring-insights-pricing")
- [Supported runtimes](#monitoring-insights-runtimes "#monitoring-insights-runtimes")
- [Enabling Lambda Insights in the Lambda console](#monitoring-insights-enabling-console "#monitoring-insights-enabling-console")
- [Enabling Lambda Insights programmatically](#monitoring-insights-enabling-programmatically "#monitoring-insights-enabling-programmatically")
- [Using the Lambda Insights dashboard](#monitoring-insights-multifunction "#monitoring-insights-multifunction")
- [Example workflow to detect function anomalies](#monitoring-insights-anomalies "#monitoring-insights-anomalies")
- [Example workflow using queries to troubleshoot a function](#monitoring-insights-queries "#monitoring-insights-queries")
- [What's next?](#monitoring-console-next-up "#monitoring-console-next-up")

## How Lambda Insights monitors serverless applications

CloudWatch Lambda Insights is a monitoring and troubleshooting solution for serverless applications running on AWS Lambda. The solution collects, aggregates, and summarizes system-level metrics including CPU time, memory, disk and network usage. It also collects, aggregates, and summarizes diagnostic information such as cold starts and Lambda worker shutdowns to help you isolate issues with your Lambda functions and resolve them quickly.

Lambda Insights uses a new CloudWatch Lambda Insights [extension](lambda-extensions.md "lambda-extensions.md"), which is provided as a [Lambda layer](chapter-layers.md "chapter-layers.md"). When you enable this extension on a Lambda function for a supported runtime, it collects system-level metrics and emits a single performance log event for every invocation of that Lambda function. CloudWatch uses embedded metric formatting to extract metrics from the log events. For more information, see [Using AWS Lambda extensions](lambda-extensions.md "lambda-extensions.md").

The Lambda Insights layer extends the `CreateLogStream` and `PutLogEvents` for the `/aws/lambda-insights/` log group.

## Pricing

When you enable Lambda Insights for your Lambda function,
Lambda Insights reports 8 metrics per function and every function invocation sends about 1KB of log data to CloudWatch.
You only pay for the metrics and logs reported for your function by Lambda Insights.
There are no minimum fees or mandatory service usage policies.
You do not pay for Lambda Insights if the function is not invoked.
For a pricing example, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Supported runtimes

You can use Lambda Insights with any of the runtimes that support [Lambda extensions](runtimes-extensions-api.md "runtimes-extensions-api.md").

## Enabling Lambda Insights in the Lambda console

You can enable Lambda Insights enhanced monitoring on new and existing Lambda functions. When you enable Lambda Insights on a function in the Lambda console for a supported runtime, Lambda adds the Lambda Insights [extension](lambda-extensions.md "lambda-extensions.md") as a layer to your function, and verifies or attempts to attach the [`CloudWatchLambdaInsightsExecutionRolePolicy`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLambdaInsightsExecutionRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLambdaInsightsExecutionRolePolicy$jsonEditor") policy to your function’s [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md").

###### To enable Lambda Insights in the Lambda console

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose your function.
3. Choose the **Configuration** tab.
4. On the left menu, choose **Monitoring and operations tools**.
5. On the **Additional monitoring tools** pane, choose **Edit**.
6. Under **CloudWatch Lambda Insights**, turn on **Enhanced monitoring**.
7. Choose **Save**.

## Enabling Lambda Insights programmatically

You can also enable Lambda Insights using the AWS Command Line Interface (AWS CLI), AWS Serverless Application Model (SAM) CLI, AWS CloudFormation, or the AWS Cloud Development Kit (AWS CDK). When you enable Lambda Insights programmatically on a function for a supported runtime, CloudWatch attaches the [`CloudWatchLambdaInsightsExecutionRolePolicy`](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLambdaInsightsExecutionRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLambdaInsightsExecutionRolePolicy$jsonEditor") policy to your function’s [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md").

For more information, see [Getting started with Lambda Insights](../../../AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started.md "../../../AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started.md") in the _Amazon CloudWatch User Guide_.

## Using the Lambda Insights dashboard

The Lambda Insights dashboard has two views in the CloudWatch console: the multi-function overview and the single-function view. The multi-function overview aggregates the runtime metrics for the Lambda functions in the current AWS account and Region. The single-function view shows the available runtime metrics for a single Lambda function.

You can use the Lambda Insights dashboard multi-function overview in the CloudWatch console to identify over- and under-utilized Lambda functions. You can use the Lambda Insights dashboard single-function view in the CloudWatch console to troubleshoot individual requests.

###### To view the runtime metrics for all functions

1. Open the [Multi-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance "https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance") page in the CloudWatch console.
2. Choose from the predefined time ranges, or choose a custom time range.
3. (Optional) Choose **Add to dashboard** to add the
   widgets to your CloudWatch dashboard.

![The multi-function overview on the Lambda Insights dashboard.](images/lambdainsights-multifunction-view.png)

###### To view the runtime metrics of a single function

1. Open the [Single-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:functions "https://console.aws.amazon.com/cloudwatch/home#lambda-insights:functions") page in the CloudWatch console.
2. Choose from the predefined time ranges, or choose a custom time range.
3. (Optional) Choose **Add to dashboard** to add the widgets to your CloudWatch dashboard.

![The single-function view on the Lambda Insights dashboard.](images/lambainsights-singlefunction-view.png)

For more information, see [Creating and working with widgets on CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.md "../../../AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.md").

## Example workflow to detect function anomalies

You can use the multi-function overview on the Lambda Insights dashboard to identify and detect compute memory anomalies with your function. For example, if the multi-function overview indicates that a function is using a large amount of memory, you can view detailed memory utilization metrics in the **Memory Usage** pane. You can then go to the Metrics dashboard to enable anomaly detection or create an alarm.

###### To enable anomaly detection for a function

1. Open the [Multi-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance "https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance") page in the CloudWatch console.
2. Under **Function summary**, choose your function's name.

The single-function view opens with the function runtime metrics.

![The function summary pane on the Lambda Insights dashboard.](images/lambdainsights-function-summary.png) 3. On the **Memory Usage** pane, choose the three vertical dots, and then choose **View in metrics** to open the **Metrics** dashboard.

![The menu on the Memory Usage pane.](images/lambdainsights-memory-usage.png) 4. On the **Graphed metrics** tab, in the **Actions** column, choose the first icon to enable anomaly detection for the function.

![The Graphed metrics tab of the Memory Usage pane.](images/lambdainsights-graphed-metrics.png)

For more information, see [Using CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md").

## Example workflow using queries to troubleshoot a function

You can use the single-function view on the Lambda Insights dashboard to identify the root cause of a spike in function duration. For example, if the multi-function overview indicates a large increase in function duration, you can pause on or choose each function in the **Duration** pane to determine which function is causing the increase. You can then go to the single-function view and review the **Application logs** to determine the root cause.

###### To run queries on a function

1. Open the [Multi-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance "https://console.aws.amazon.com/cloudwatch/home#lambda-insights:performance") page in the CloudWatch console.
2. In the **Duration** pane, choose your function to filter the duration metrics.

![A function chosen in the Duration pane.](images/lambdainsights-choose-function.png) 3. Open the [Single-function](https://console.aws.amazon.com/cloudwatch/home#lambda-insights:functions "https://console.aws.amazon.com/cloudwatch/home#lambda-insights:functions") page. 4. Choose the **Filter metrics by function name** dropdown
list, and then choose your function. 5. To view the **Most recent 1000 application logs**, choose the **Application logs** tab. 6. Review the **Timestamp** and **Message** to identify the invocation request that you want to troubleshoot.

![The Most recent 1000 application logs.](images/lambdainsights-application-logs.png) 7. To show the **Most recent 1000 invocations**, choose the **Invocations**
tab. 8. Select the **Timestamp** or **Message** for the invocation request that you want to troubleshoot.

![Selecting a recent invocation request.](images/lambdainsights-invocations-function-select.png) 9. Choose the **View logs** dropdown list, and then choose **View performance
logs**.

An autogenerated query for your function opens in the **Logs Insights** dashboard. 10. Choose **Run query** to generate a **Logs** message for the invocation request.

![Querying the selected function in the Logs Insights dashboard.](images/lambdainsights-query.png)

## What's next?

- Learn how to create a CloudWatch Logs dashboard in [Create a Dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md") in the _Amazon CloudWatch User Guide_.
- Learn how to add queries to a CloudWatch Logs dashboard in [Add Query to Dashboard or Export Query Results](../../../AmazonCloudWatch/latest/logs/CWL_ExportQueryResults.md "../../../AmazonCloudWatch/latest/logs/CWL_ExportQueryResults.md") in the _Amazon CloudWatch User Guide_.
