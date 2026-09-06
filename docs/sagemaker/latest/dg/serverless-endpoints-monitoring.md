

# Alarms and logs for tracking metrics from serverless endpoints
<a name="serverless-endpoints-monitoring"></a>

To monitor your serverless endpoint, you can use Amazon CloudWatch alarms. CloudWatch is a service that collects metrics in real time from your AWS applications and resources. An alarm watches metrics as they are collected and gives you the ability to pre-specify a threshold and the actions to take if that threshold is breached. For example, your CloudWatch alarm can send you a notification if your endpoint breaches an error threshold. By setting up CloudWatch alarms, you gain visibility into the performance and functionality of your endpoint. For more information about CloudWatch alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Monitoring with CloudWatch
<a name="serverless-endpoints-monitoring-metrics"></a>

The metrics below are an exhaustive list of metrics for serverless endpoints. Any metric not listed below is not published for serverless endpoints. For information about the following metrics, see [Monitor Amazon SageMaker AI with Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html).

### Common endpoint metrics
<a name="serverless-endpoints-monitoring-metrics-common"></a>

These CloudWatch metrics are the same as the metrics published for real-time endpoints.

The `OverheadLatency` metric tracks all additional latency that SageMaker AI added which includes the cold start time for launching new compute resources for your serverless endpoint. Compared to on-demand serverless endpoints, the `OverheadLatency` for serverless endpoints with provision concurrency is generally significantly less.

Serverless endpoints can also use the `Invocations4XXErrors`, `Invocations5XXErrors`, `Invocations`, `ModelLatency`, `ModelSetupTime` and `MemoryUtilization` metrics. To learn more about these metrics, see [SageMaker AI endpoint invocation metrics](monitoring-cloudwatch.md#cloudwatch-metrics-endpoint-invocation).

### Common serverless endpoint metrics
<a name="serverless-endpoints-monitoring-metrics-serverless"></a>

These CloudWatch metrics are published for both on-demand serverless endpoints and serverless endpoint with Provisioned Concurrency.


| Metric Name | Description | Unit/Stats | 
| --- | --- | --- | 
| ServerlessConcurrentExecutionsUtilization | The number of concurrent executions divided by the maximum concurrency. | Units: None<br />Valid statistics: Average, Max, Min | 

### Serverless endpoint with Provisioned Concurrency metrics
<a name="serverless-endpoints-monitoring-metrics-serverless-pc"></a>

These CloudWatch metrics are published for serverless endpoints with Provisioned Concurrency.


| Metric Name | Description | Unit/Stats | 
| --- | --- | --- | 
| ServerlessProvisionedConcurrencyExecutions | The number of concurrent executions handled by the endpoint. | Units: Count<br />Valid statistics: Average, Max, Min | 
| ServerlessProvisionedConcurrencyUtilization | The number of concurrent executions divided by the allocated Provisioned Concurrency. | Units: None<br />Valid statistics: Average, Max, Min | 
| ServerlessProvisionedConcurrencyInvocations | The number of InvokeEndpoint requests handled by Provisioned Concurrency. | Units: Count<br />Valid statistics: Average, Max, Min | 
| ServerlessProvisionedConcurrencySpilloverInvocations | The number of InvokeEndpoint requests not handled by Provisioned Concurrency, that is handled by on-demand Serverless Inference. | Units: Count<br />Valid statistics: Average, Max, Min | 

## Logs
<a name="serverless-endpoints-monitoring-logs"></a>

If you want to monitor the logs from your endpoint for debugging or progress analysis, you can use Amazon CloudWatch Logs. The SageMaker AI-provided log group that you can use for serverless endpoints is `/aws/sagemaker/Endpoints/[EndpointName]`. For more information about using CloudWatch Logs in SageMaker AI, see [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md). To learn more about CloudWatch Logs, see [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) in the *Amazon CloudWatch Logs User Guide*.