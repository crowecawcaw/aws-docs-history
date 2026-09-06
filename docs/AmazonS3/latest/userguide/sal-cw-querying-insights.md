

# Querying logs with CloudWatch Logs Insights
<a name="sal-cw-querying-insights"></a>

CloudWatch Logs Insights lets you interactively search and analyze your server access log data. Queries run against the log group where your logs are delivered and return results in seconds.

**Note**  
For querying logs delivered to an Amazon S3 general purpose bucket, see [Querying access logs for requests by using Amazon Athena](using-s3-access-logs-to-identify-requests.md#querying-s3-access-logs-for-requests). For querying the S3 Tables mirror with SQL, see [Querying access logs in S3 Tables](sal-cw-querying-s3tables.md).

## Getting started
<a name="sal-cw-insights-getting-started"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, then **Logs Insights**.

1. Select your server access log group from the log group selector.

1. Choose a time range for your query.

1. Enter a query and choose **Run query**.

## Traffic analysis
<a name="sal-cw-insights-traffic"></a>

The following queries help you understand request volume and traffic patterns.

**Example Request volume over time**  

```
stats count(*) as requests by bin(5m) as interval
| sort interval asc
```

**Example Request mix by operation type**  

```
stats count(*) as cnt by operation
| sort cnt desc
```

**Example Traffic by bucket**  

```
stats count(*) as requests, sum(bytes_sent_size) as bytes_out by bucket_arn
| sort requests desc
```

## Error troubleshooting
<a name="sal-cw-insights-errors"></a>

The following queries help you identify and diagnose errors.

**Example Error rate breakdown**  

```
filter http_status >= 400
| stats count(*) as error_count by http_status, error_code, operation
| sort error_count desc
```

**Example 403 Access Denied requests**  

```
filter http_status = 403
| stats count(*) as denied_count by key_name, remote_ip, requester
| sort denied_count desc
```

**Example 404 Not Found requests**  

```
filter http_status = 404
| stats count(*) as miss_count by key_name, error_code, remote_ip
| sort miss_count desc
```

**Example 503 SlowDown (throttling) events**  

```
filter http_status = 503
| stats count(*) as throttle_count by key_name, remote_ip
| sort throttle_count desc
```

## Access patterns
<a name="sal-cw-insights-access"></a>

The following queries help you understand who is accessing your data and how.

**Example Traffic by source IP**  

```
stats count(*) as total_requests,
  sum(http_status >= 400) as errors,
  sum(bytes_sent_size) as bytes_transferred
  by remote_ip
| sort total_requests desc
```

**Example Operations by requester**  

```
stats count(*) as requests by requester, operation
| sort requests desc
```

**Example Most accessed keys**  

```
filter operation like /REST\.(GET|PUT)\.OBJECT/
| stats count(*) as access_count, sum(bytes_sent_size) as bytes_out by key_name
| sort access_count desc
| limit 10
```

## Latency analysis
<a name="sal-cw-insights-latency"></a>

The following queries help you identify slow requests and latency trends.

**Example Latency by operation type**  

```
filter operation like /REST\.(GET|PUT)\.OBJECT/
| stats avg(total_duration) as avg_ms,
  pct(total_duration, 50) as p50_ms,
  pct(total_duration, 95) as p95_ms,
  max(total_duration) as max_ms,
  count(*) as requests
  by operation
```

**Example Slowest keys by p95 latency**  

```
filter operation like /REST\.GET\.OBJECT/
| stats avg(total_duration) as avg_ms,
  pct(total_duration, 95) as p95_ms,
  count(*) as requests
  by key_name
| sort p95_ms desc
| limit 10
```

**Example Latency over time**  

```
filter operation like /REST\.(GET|PUT)\.OBJECT/
| stats avg(total_duration) as avg_ms, pct(total_duration, 95) as p95_ms by bin(5m) as interval
| sort interval asc
```

## Cost attribution
<a name="sal-cw-insights-cost"></a>

The following queries help you understand data transfer and identify cost drivers.

**Example Data transfer by operation**  

```
filter operation like /REST\.(GET|PUT|DELETE)\.OBJECT/
| stats sum(bytes_sent_size) as total_bytes_out,
  sum(object_size) as total_object_bytes,
  count(*) as request_count
  by operation
| sort total_bytes_out desc
```

**Example Largest objects being served**  

```
filter operation like /REST\.GET\.OBJECT/ and bytes_sent_size > 0
| stats max(object_size) as max_size, avg(object_size) as avg_size, count(*) as reads by key_name
| sort max_size desc
| limit 10
```

## Security analysis
<a name="sal-cw-insights-security"></a>

The following queries help you detect suspicious access patterns.

**Example IPs with high error rates**  

```
stats count(*) as total,
  sum(http_status >= 400) as errors
  by remote_ip
| filter errors > 10
| sort errors desc
```

**Example Failed access attempts by key**  

```
filter http_status >= 400
| stats count(*) as attempts by remote_ip, key_name, operation, http_status
| sort attempts desc
| limit 20
```

**Example TLS version distribution**  

```
stats count(*) as cnt by tls_version
| sort cnt desc
```