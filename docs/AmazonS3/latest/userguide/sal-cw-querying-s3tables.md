

# Querying access logs in S3 Tables
<a name="sal-cw-querying-s3tables"></a>

When you enable the Amazon S3 Tables integration, Amazon CloudWatch Logs delivers your server access logs in Apache Iceberg format to the `aws-cloudwatch` managed table bucket. Because the data is in Iceberg format, you can query it with any tool that supports Apache Iceberg, including:
+ **Amazon Athena** – Run SQL queries directly from the Athena console using the S3 Tables catalog.
+ **Amazon SageMaker Unified Studio** – Use the built-in SQL editor to query your log data alongside other analytics workloads.
+ **Amazon Redshift** – Query Iceberg tables through Redshift Spectrum or direct integration.
+ **Apache Spark on Amazon EMR** – Use Spark SQL or the DataFrame API with the Iceberg connector.
+ **Open-source tools** – Any tool that supports the Apache Iceberg REST catalog, such as Trino, DuckDB, or PyIceberg.

**Note**  
For querying logs interactively in CloudWatch Logs Insights (without SQL), see [Querying logs with CloudWatch Logs Insights](sal-cw-querying-insights.md).

## Prerequisites
<a name="sal-cw-s3tables-prerequisites"></a>

Before you can query access logs in S3 Tables, you must complete the following:

1. **Enable the S3 Tables integration.** See [Enabling the S3 Tables integration (optional)](sal-cw-enabling.md#sal-cw-tables-integration).

1. **Enable S3 Tables integration with analytics services.** In the Amazon S3 console, navigate to **Table buckets** and choose **Enable integration**. This creates the `s3tablescatalog` federated catalog in Data Catalog and makes your tables visible to analytics services. By default, access is controlled through IAM permissions. You can optionally use AWS Lake Formation for fine-grained access control. For more information, see [Integrating S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html).

1. **Wait for data to populate.** Data typically appears within an hour of the first delivery to CloudWatch Logs.

## Connecting Amazon Athena
<a name="sal-cw-s3tables-athena-setup"></a>

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/).

1. In the query editor, select the **Amazon S3 Tables** catalog from the data source dropdown.

1. Your log tables appear in the database list under the `logs` namespace.

The table name for server access logs is `amazon_s3__server_access`. The fully qualified table reference is:

```
"s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
```

## Traffic analysis
<a name="sal-cw-s3tables-traffic"></a>

**Example Request volume over time**  

```
SELECT date_trunc('minute', request_time) AS interval,
  COUNT(*) AS requests
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY date_trunc('minute', request_time)
ORDER BY interval ASC;
```

**Example Request mix by operation type**  

```
SELECT operation, COUNT(*) AS cnt
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY operation
ORDER BY cnt DESC;
```

**Example Traffic by bucket**  

```
SELECT bucket_arn, COUNT(*) AS requests, SUM(bytes_sent_size) AS bytes_out
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY bucket_arn
ORDER BY requests DESC;
```

## Error troubleshooting
<a name="sal-cw-s3tables-errors"></a>

**Example Error rate breakdown**  

```
SELECT http_status, error_code, operation, COUNT(*) AS error_count
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE http_status >= 400
GROUP BY http_status, error_code, operation
ORDER BY error_count DESC;
```

**Example 403 Access Denied requests**  

```
SELECT key_name, remote_ip, requester, COUNT(*) AS denied_count
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE http_status = 403
GROUP BY key_name, remote_ip, requester
ORDER BY denied_count DESC;
```

**Example 404 Not Found requests**  

```
SELECT key_name, error_code, remote_ip, COUNT(*) AS miss_count
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE http_status = 404
GROUP BY key_name, error_code, remote_ip
ORDER BY miss_count DESC;
```

**Example 503 SlowDown (throttling) events**  

```
SELECT key_name, remote_ip, COUNT(*) AS throttle_count
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE http_status = 503
GROUP BY key_name, remote_ip
ORDER BY throttle_count DESC;
```

## Access patterns
<a name="sal-cw-s3tables-access"></a>

**Example Traffic by source IP**  

```
SELECT remote_ip,
  COUNT(*) AS total_requests,
  SUM(CASE WHEN http_status >= 400 THEN 1 ELSE 0 END) AS errors,
  SUM(bytes_sent_size) AS bytes_transferred
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY remote_ip
ORDER BY total_requests DESC;
```

**Example Operations by requester**  

```
SELECT requester, operation, COUNT(*) AS requests
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY requester, operation
ORDER BY requests DESC;
```

**Example Most accessed keys**  

```
SELECT key_name, COUNT(*) AS access_count, SUM(bytes_sent_size) AS bytes_out
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE operation IN ('REST.GET.OBJECT', 'REST.PUT.OBJECT')
GROUP BY key_name
ORDER BY access_count DESC
LIMIT 10;
```

## Latency analysis
<a name="sal-cw-s3tables-latency"></a>

**Example Latency by operation type**  

```
SELECT operation,
  AVG(total_duration) AS avg_ms,
  APPROX_PERCENTILE(total_duration, 0.5) AS p50_ms,
  APPROX_PERCENTILE(total_duration, 0.95) AS p95_ms,
  MAX(total_duration) AS max_ms,
  COUNT(*) AS requests
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE operation IN ('REST.GET.OBJECT', 'REST.PUT.OBJECT')
GROUP BY operation;
```

**Example Slowest keys by p95 latency**  

```
SELECT key_name,
  AVG(total_duration) AS avg_ms,
  APPROX_PERCENTILE(total_duration, 0.95) AS p95_ms,
  COUNT(*) AS requests
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE operation = 'REST.GET.OBJECT'
GROUP BY key_name
ORDER BY p95_ms DESC
LIMIT 10;
```

**Example Latency over time**  

```
SELECT date_trunc('minute', request_time) AS interval,
  AVG(total_duration) AS avg_ms,
  APPROX_PERCENTILE(total_duration, 0.95) AS p95_ms
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE operation IN ('REST.GET.OBJECT', 'REST.PUT.OBJECT')
GROUP BY date_trunc('minute', request_time)
ORDER BY interval ASC;
```

## Cost attribution
<a name="sal-cw-s3tables-cost"></a>

**Example Data transfer by operation**  

```
SELECT operation,
  SUM(bytes_sent_size) AS total_bytes_out,
  SUM(object_size) AS total_object_bytes,
  COUNT(*) AS request_count
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE operation IN ('REST.GET.OBJECT', 'REST.PUT.OBJECT', 'REST.DELETE.OBJECT')
GROUP BY operation
ORDER BY total_bytes_out DESC;
```

**Example Largest objects being served**  

```
SELECT key_name, MAX(object_size) AS max_size, AVG(object_size) AS avg_size, COUNT(*) AS reads
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE operation = 'REST.GET.OBJECT' AND bytes_sent_size > 0
GROUP BY key_name
ORDER BY max_size DESC
LIMIT 10;
```

## Security analysis
<a name="sal-cw-s3tables-security"></a>

**Example IPs with high error rates**  

```
SELECT remote_ip,
  COUNT(*) AS total,
  SUM(CASE WHEN http_status >= 400 THEN 1 ELSE 0 END) AS errors
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY remote_ip
HAVING SUM(CASE WHEN http_status >= 400 THEN 1 ELSE 0 END) > 10
ORDER BY errors DESC;
```

**Example Failed access attempts by key**  

```
SELECT remote_ip, key_name, operation, http_status, COUNT(*) AS attempts
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
WHERE http_status >= 400
GROUP BY remote_ip, key_name, operation, http_status
ORDER BY attempts DESC
LIMIT 20;
```

**Example TLS version distribution**  

```
SELECT tls_version, COUNT(*) AS cnt
FROM "s3tablescatalog/aws-cloudwatch"."logs"."amazon_s3__server_access"
GROUP BY tls_version
ORDER BY cnt DESC;
```

## Using AI agents to query Amazon S3 server access logs
<a name="sal-cw-s3tables-ai-agents"></a>

MCP-compatible AI agents can discover the S3 tables that contain your Amazon S3 server access logs, generate SQL queries, and analyze the results. Because your Amazon S3 server access logs are exported as Iceberg tables in the `aws-cloudwatch` table bucket, agents can query them through the same S3 Tables catalog that you use with Amazon Athena, Amazon EMR, Amazon Redshift, or any Iceberg-compatible tool.

The [Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) provides skills that give agents validated procedures for working with AWS data. The [Querying CloudWatch Logs system tables](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/system-table-skills/querying-aws-cloudwatch) skill runs SQL queries on CloudWatch Logs data exported to S3 Tables, including your Amazon S3 server access logs in the `aws-cloudwatch` table bucket. To use it, download the skill from the repository on GitHub and add it to your agent's skills directory.

For example, you can ask an agent to show the top 10 source IP addresses by request count in your S3 server access logs over the last 24 hours. The agent uses the skill to locate the access log table and run the query in Athena.