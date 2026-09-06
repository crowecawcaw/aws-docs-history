

# Query metrics with PromQL
<a name="CloudWatch-PromQL"></a>

**Topics**
+ [What is Prometheus Query Language (PromQL)?](#CloudWatch-PromQL-WhatIs)
+ [PromQL limits and restrictions](#CloudWatch-PromQL-Limits)
+ [Supported AWS Regions](#CloudWatch-PromQL-Regions)
+ [IAM permissions for PromQL](#CloudWatch-PromQL-IAM)
+ [PromQL querying](CloudWatch-PromQL-Querying.md)
+ [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md)
+ [Using PromQL in alarms](CloudWatch-PromQL-Alarms.md)
+ [Prometheus-compatible APIs](CloudWatch-PromQL-APIs.md)

## What is Prometheus Query Language (PromQL)?
<a name="CloudWatch-PromQL-WhatIs"></a>

Prometheus Query Language (PromQL) is a functional query language that lets you select, aggregate, and transform time series data in real time. PromQL was originally designed for Prometheus and has become a popular query language for metrics.

Amazon CloudWatch supports PromQL for querying metrics including metrics ingested through OpenTelemetry Line Protocol (OTLP) and [AWS enriched vended metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html). When you ingest OTLP metrics, CloudWatch preserves the full semantic structure of your telemetry, including resource attributes, instrumentation scope, datapoint attributes, and AWS-specific metadata, and exposes them as queryable PromQL labels.

With PromQL you can do the following:
+ Select time series by metric name and label matchers.
+ Apply mathematical functions and operators across time series.
+ Aggregate metrics across dimensions such as service, region, or account.
+ Compute rates, histograms, quantiles, and moving averages.

You can use PromQL queries interactively in [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md) and also to create CloudWatch Alarms. For more information, see [PromQL querying](CloudWatch-PromQL-Querying.md) and [Using PromQL in alarms](CloudWatch-PromQL-Alarms.md).

**Note**  
CloudWatch uses PromQL based on the Prometheus 3.0 specification. This includes support for UTF-8 metric names and label names.

The following concepts are fundamental to working with PromQL in CloudWatch.


| Concept | Description | 
| --- | --- | 
| **Time series** | A stream of timestamped values identified by a metric name and a set of key-value pairs called *labels*. Each unique combination of metric name and labels forms a distinct time series. | 
| **Instant vector** | A set of time series containing a single sample for each series, all sharing the same timestamp. Returned by queries like `{"http.server.active_requests", "@resource.service.name"="myservice"}`. | 
| **Range vector** | A set of time series containing a range of data points over time for each series. Created by appending a time duration selector in brackets, for example, `avg_over_time({"http.server.active_requests", "@resource.service.name"="myservice"}[5m])`. | 
| **Label** | A key-value pair attached to a time series. In OTLP-ingested metrics, labels are derived from resource attributes, instrumentation scope, datapoint attributes, and AWS-specific metadata. | 
| **Label matcher** | An expression in curly braces that filters time series by label value. Supports exact match (`=`), not equal (`!=`), regex match (`=~`), and negative regex match (`!~`). | 
| **Aggregation operator** | A function that combines multiple time series into fewer series. Common operators include `sum`, `avg`, `min`, `max`, `count`, and `topk`. | 

## PromQL limits and restrictions
<a name="CloudWatch-PromQL-Limits"></a>

The following table lists the limits and restrictions for PromQL:


| Limit | Value | Additional information | Error code | 
| --- | --- | --- | --- | 
| Max TPS for query requests per account | 300 | Maximum number of query requests (/query, /query\_range) per second allowed per account. | 422 | 
| Max TPS for discovery requests per account | 10 | Maximum number of discovery requests (/series, /label, /label\_values) per second allowed per account. | 422 | 
| Max concurrent query requests per account | 30 | Maximum number of queries (/query, /query\_range) an account can have actively executing at the same time. | 429 | 
| Max concurrent discovery requests per account | 30 | Maximum number of discovery requests (/series, /labels, /label\_values) an account can have actively executing at the same time. | 429 | 
| Max series returned per query request | 500 | Maximum number of unique time series a query request (/query, /query\_range) can return. | 200 - truncated response | 
| Max labels returned per discovery request | 10,000 | Maximum number of unique labels a discovery request (/series, /labels, /label\_values) can return. | 200 - truncated response | 
| Max range per request | 7 days | Maximum time range a query can span, including range parameters and lookback periods. | 422 | 
| Max series scanned per 24h window | 100,000 | Maximum number of unique time series that can be scanned per 24-hour window of query execution. | 422 | 
| Max samples scanned per 24h window | 300,000,000 | Maximum number of samples that can be scanned per 24-hour window of query execution. | 422 | 
| Max samples processed per 24h window | 3,000,000,000 | Maximum number of samples that can be processed per 24-hour window of query execution. | 422 | 
| Execution timeout | 20 seconds | Maximum time the engine can spend evaluating a query, excluding time spent in queue and fetching data from storage. | 422 | 

## Supported AWS Regions
<a name="CloudWatch-PromQL-Regions"></a>

The following table lists the AWS Regions where OTLP metrics ingestion, PromQL querying, and Query Studio are available.


| Region name | Region code | OTLP metrics ingest | PromQL query | Query Studio | 
| --- | --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | ✓ | ✓ | ✓ | 
| US West (Oregon) | us-west-2 | ✓ | ✓ | ✓ | 
| Europe (Ireland) | eu-west-1 | ✓ | ✓ | ✓ | 
| Asia Pacific (Singapore) | ap-southeast-1 | ✓ | ✓ | ✓ | 
| Asia Pacific (Sydney) | ap-southeast-2 | ✓ | ✓ | ✓ | 
| US West (N. California) | us-west-1 | ✓ | ✓ | ✓ | 
| US East (Ohio) | us-east-2 | ✓ | ✓ | ✓ | 
| Europe (London) | eu-west-2 | ✓ | ✓ | ✓ | 
| Europe (Paris) | eu-west-3 | ✓ | ✓ | ✓ | 
| Europe (Frankfurt) | eu-central-1 | ✓ | ✓ | ✓ | 
| Europe (Stockholm) | eu-north-1 | ✓ | ✓ | ✓ | 
| Europe (Milan) | eu-south-1 | ✓ | ✓ | ✓ | 
| Europe (Spain) | eu-south-2 | ✓ | ✓ | ✓ | 
| Europe (Zurich) | eu-central-2 | ✓ | ✓ | ✓ | 
| Asia Pacific (Tokyo) | ap-northeast-1 | ✓ | ✓ | ✓ | 
| Asia Pacific (Seoul) | ap-northeast-2 | ✓ | ✓ | ✓ | 
| Asia Pacific (Osaka) | ap-northeast-3 | ✓ | ✓ | ✓ | 
| Asia Pacific (Mumbai) | ap-south-1 | ✓ | ✓ | ✓ | 
| Asia Pacific (Hyderabad) | ap-south-2 | ✓ | ✓ | ✓ | 
| Asia Pacific (Hong Kong) | ap-east-1 | ✓ | ✓ | ✓ | 
| Asia Pacific (Taipei) | ap-east-2 | ✓ | ✓ | ✓ | 
| Asia Pacific (Jakarta) | ap-southeast-3 | ✓ | ✓ | ✓ | 
| Asia Pacific (Melbourne) | ap-southeast-4 | ✓ | ✓ | ✓ | 
| Asia Pacific (Malaysia) | ap-southeast-5 | ✓ | ✓ | ✓ | 
| Asia Pacific (Auckland) | ap-southeast-6 | ✓ | ✓ | ✓ | 
| Asia Pacific (Thailand) | ap-southeast-7 | ✓ | ✓ | ✓ | 
| South America (São Paulo) | sa-east-1 | ✓ | ✓ | ✓ | 
| Canada (Central) | ca-central-1 | ✓ | ✓ | ✓ | 
| Canada West (Calgary) | ca-west-1 | ✓ | ✓ | ✓ | 
| Africa (Cape Town) | af-south-1 | ✓ | ✓ | ✓ | 
| Mexico (Central) | mx-central-1 | ✓ | ✓ | ✓ | 

## IAM permissions for PromQL
<a name="CloudWatch-PromQL-IAM"></a>

To execute PromQL queries, you need both `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions. The following table lists the Prometheus-compatible API endpoint paths and their required IAM actions:


| API endpoint path | HTTP methods | Required actions | 
| --- | --- | --- | 
| `/api/v1/query` | GET, POST | `cloudwatch:GetMetricData`, `cloudwatch:ListMetrics` | 
| `/api/v1/query_range` | GET, POST | `cloudwatch:GetMetricData`, `cloudwatch:ListMetrics` | 
| `/api/v1/series` | GET, POST | `cloudwatch:ListMetrics` | 
| `/api/v1/labels` | GET, POST | `cloudwatch:ListMetrics` | 
| `/api/v1/label/{{label_name}}/values` | GET | `cloudwatch:ListMetrics` | 