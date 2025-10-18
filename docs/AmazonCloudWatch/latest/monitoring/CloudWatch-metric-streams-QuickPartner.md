# Quick partner setup

CloudWatch provides a quick setup experience for the following third-party partners. To use this workflow, 
 you need to provide only a destination URL and API key for your destination. CloudWatch handles the rest of setup including
 creating the Firehose delivery stream and the necessary IAM roles.

###### Important

Before you use quick partner setup to create a metric stream, we strongly recommend that you 
 read that partner's documentation, linked in the following list.


* [Datadog](https://docs.datadoghq.com/integrations/guide/aws-cloudwatch-metric-streams-with-kinesis-data-firehose/ "https://docs.datadoghq.com/integrations/guide/aws-cloudwatch-metric-streams-with-kinesis-data-firehose/")
* [Dynatrace](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication "https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication")
* [Elastic](https://www.elastic.co/docs/current/integrations/awsfirehose "https://www.elastic.co/docs/current/integrations/awsfirehose")
* [New Relic](https://docs.newrelic.com/install/aws-cloudwatch/ "https://docs.newrelic.com/install/aws-cloudwatch/")
* [Splunk Observability Cloud](https://docs.splunk.com/observability/en/gdi/get-data-in/connect/aws/aws-console-ms.html "https://docs.splunk.com/observability/en/gdi/get-data-in/connect/aws/aws-console-ms.html")
* [SumoLogic](https://www.sumologic.com "https://www.sumologic.com")
When you set up a metric stream to one of these partners, the stream is created with some default settings, 
 as listed in the following sections.

###### Topics

* [Set up a metric stream using quick partner setup](#CloudWatch-metric-streams-QuickPartner-setup "#CloudWatch-metric-streams-QuickPartner-setup")
* [Datadog stream defaults](#CloudWatch-metric-streams-QuickPartner-Datadog "#CloudWatch-metric-streams-QuickPartner-Datadog")
* [Dynatrace stream defaults](#CloudWatch-metric-streams-QuickPartner-Dynatrace "#CloudWatch-metric-streams-QuickPartner-Dynatrace")
* [Elastic stream defaults](#CloudWatch-metric-streams-QuickPartner-Elastic "#CloudWatch-metric-streams-QuickPartner-Elastic")
* [New Relic stream defaults](#CloudWatch-metric-streams-QuickPartner-NewRelic "#CloudWatch-metric-streams-QuickPartner-NewRelic")
* [Splunk Observability Cloud stream defaults](#CloudWatch-metric-streams-QuickPartner-Splunk "#CloudWatch-metric-streams-QuickPartner-Splunk")
* [Sumo Logic stream defaults](#CloudWatch-metric-streams-QuickPartner-Sumologic "#CloudWatch-metric-streams-QuickPartner-Sumologic")

## Set up a metric stream using quick partner setup


CloudWatch provides a quick setup option for some third-party partners. Before you start the steps in this section, you must have certain information for the partner. This information might 
 include a destination URL and/or an API key for your 
 partner destination. You should also read the documentation at the partner's website linked in the previous 
 section, and the defaults for that partner listed in the following sections.


To stream to a third-party destination not supported by quick setup, you can follow the 
 instructions in Follow the instructions in [Custom setup with Firehose](CloudWatch-metric-streams-setup-datalake.md "CloudWatch-metric-streams-setup-datalake.md")
 to set up a stream using Firehose, and then send those metrics
 from Firehose to the final destination.


###### To use quick partner setup to create a metric stream to third-party provider

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, 
 **Streams**. Then choose **Create metric stream**.
3. (Optional) If you are signed in to an account that is set up as a monitoring account
 in CloudWatch cross-account observability, you can choose whether to include metrics from linked source
 accounts in this metric stream. To include metrics from source accounts, choose
 **Include source account metrics**.
4. Choose **Quick Amazon Web Services partner setup**
5. Select the name of the partner that you want to stream metrics to.
6. For **Endpoint URL**, enter the destination URL.
7. For **Access Key** or **API Key**, enter the access key for the partner.
 Not all partners require an access key.
8. For **Metrics to be streamed**, choose either 
 **All metrics** or **Select metrics**.


If you choose **All metrics**, all metrics from this account
 will be included in the stream.


Consider carefully whether to stream all metrics, because the more metrics that you stream the
 higher your metric stream charges will be.


If you choose **Select metrics**, do one of the following:


	* To stream most metric namespaces, choose **Exclude** 
	 and select the namespaces or metrics to 
	 exclude. When you specify a namespace in **Exclude**, 
	 you can optionally select some specific metrics from that namespace to exclude. If you choose
	 to exclude a namespace but don't then select metrics in that namespace, all metrics from that namespace
	 are excluded.
	* To include only a few metric namespaces or metrics in the metric stream, 
	 choose **Include** and 
	 then select the namespaces or metrics to include. If you choose
	 to include a namespace but don't then select metrics in that namespace, all metrics from that namespace
	 are included.
9. (Optional) To stream additional statistics for some of these metrics beyond Minimum, Maximum,
 SampleCount, and Sum, choose **Add additional statistics**. Either
 choose **Add recommended metrics** to add some commonly used statistics, or 
 manually select the 
 namespace and metric name to stream additional statistics for. Next, select
 the additional statistics to stream.


To then choose another group of metrics to stream a different set of additional statistics for, choose 
 **Add additional statistics**. Each metric can include as many 
 as 20 additional statistics, and as many as 100 metrics within a metric stream can include
 additional statistics.


Streaming additional statistics incurs more charges. For more information, 
 see [Statistics that can be streamed](CloudWatch-metric-streams-statistics.md "CloudWatch-metric-streams-statistics.md").


For definitions of the additional statistics, see 
 [CloudWatch statistics definitions](Statistics-definitions.md "Statistics-definitions.md").
10. (Optional) Customize the name of the new metric stream under
 **Metric stream name**.
11. Choose **Create metric stream**.

## Datadog stream defaults


Quick partner setup streams to Datadog use the following defaults:



* **Output format:** OpenTelemetry 0.7.0
* **Firehose stream content encoding** GZIP
* **Firehose stream buffering options** Interval of 60 seconds, size of 4 MBs
* **Firehose stream retry option** Duration of 60 seconds

When you use quick partner setup to create a metric stream to Datadog and you stream certain metrics,
 by default those metrics include some additional statistics. Streaming additional statistics can incur 
 additional charges. For more information about statistics and their charges, see [Statistics that can be streamed](CloudWatch-metric-streams-statistics.md "CloudWatch-metric-streams-statistics.md").


The following list shows the metrics that have additional statistics streamed by default, if you choose
 to stream those metrics. You can 
 choose to de-select these 
 additional statistics before you start the stream.



* **`Duration` in `AWS/Lambda`:** p50, p80, p95, p99, p99.9
* **`PostRuntimeExtensionDuration` in `AWS/Lambda`:** p50, p99
* **`FirstByteLatency` and `TotalRequestLatency`in `AWS/S3`:** p50, p90, p95, p99, p99.9
* **`ResponseLatency` in `AWS/Polly` and `TargetResponseTime` in AWS/ApplicationELB:** p50, p90, p95, p99
* **`Latency` and `IntegrationLatency` in `AWS/ApiGateway`:** p90, p95, p99
* **`Latency` and `TargetResponseTime` in `AWS/ELB`:** p95, p99
* **`RequestLatency` in `AWS/AppRunner`:** p50, p95, p99
* **`ActivityTime`, `ExecutionTime`, 
 `LambdaFunctionRunTime`, 
 `LambdaFunctionScheduleTime`, 
 `LambdaFunctionTime`, 
 `ActivityRunTime`, and 
 `ActivityScheduleTime` 
 in `AWS/States`:** p95, p99
* **`EncoderBitRate`, 
 `ConfiguredBitRate`, and 
 `ConfiguredBitRateAvailable` 
 in `AWS/MediaLive`:** p90
* **`Latency`
 in `AWS/AppSync`:** p90

## Dynatrace stream defaults


Quick partner setup streams to Dynatrace use the following defaults:



* **Output format:** OpenTelemetry 0.7.0
* **Firehose stream content encoding** GZIP
* **Firehose stream buffering options** Interval of 60 seconds, size of 5 MBs
* **Firehose stream retry option** Duration of 600 seconds

## Elastic stream defaults


Quick partner setup streams to Elastic use the following defaults:



* **Output format:** OpenTelemetry 1.0.0
* **Firehose stream content encoding** GZIP
* **Firehose stream buffering options** Interval of 60 seconds, size of 1 MB
* **Firehose stream retry option** Duration of 60 seconds

## New Relic stream defaults


Quick partner setup streams to New Relic use the following defaults:



* **Output format:** OpenTelemetry 0.7.0
* **Firehose stream content encoding** GZIP
* **Firehose stream buffering options** Interval of 60 seconds, size of 1 MB
* **Firehose stream retry option** Duration of 60 seconds

## Splunk Observability Cloud stream defaults


Quick partner setup streams to Splunk Observability Cloud use the following defaults:



* **Output format:** OpenTelemetry 1.0.0
* **Firehose stream content encoding** GZIP
* **Firehose stream buffering options** Interval of 60 seconds, size of 1 MB
* **Firehose stream retry option** Duration of 300 seconds

## Sumo Logic stream defaults


Quick partner setup streams to Sumo Logic use the following defaults:



* **Output format:** OpenTelemetry 0.7.0
* **Firehose stream content encoding** GZIP
* **Firehose stream buffering options** Interval of 60 seconds, size of 1 MB
* **Firehose stream retry option** Duration of 60 seconds
