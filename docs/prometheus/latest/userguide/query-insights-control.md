# Managing the query cost in Amazon Managed Service for Prometheus

Amazon Managed Service for Prometheus offers the ability to limit query cost by providing limits on how much Query
Samples Processed (QSP) can be used by a single query. You can configure two types of
thresholds for QSP, _warning_ and _error_ to help
manage and control query costs effectively.

When queries hit the _warning_ threshold, a warning message appears
in the API query response. For queries viewed through Amazon Managed Grafana, the warning will be visible
in the Amazon Managed Grafana UI, helping users identify expensive queries. Queries that hit the
_error_ threshold are not charged and will be rejected with an
error.

In addition to query throttling, Amazon Managed Service for Prometheus offers the ability to log query performance
data to CloudWatch Logs. This feature allows you to analyze queries in detail, helping you
optimize your Amazon Managed Service for Prometheus queries and manage costs more effectively. Query logging captures
information about queries that exceed specified Query Samples Processed (QSP)
thresholds. This data is then published to CloudWatch Logs, enabling you to investigate and
analyze query performance. Logged queries include both API queries and Rule queries. By
default, query logging is disabled to minimize unnecessary CloudWatch Logs usage. You can enable
this feature when needed for query analysis.

###### Topics

- [Configuring query logging](#query-logging "#query-logging")
- [Configuring query throttling
  thresholds](#query-throttling-thresholds "#query-throttling-thresholds")
- [Log content](#log-content "#log-content")
- [Limitations](#limitations "#limitations")

## Configuring query logging

You can configure query logging in Amazon Managed Service for Prometheus console or in the AWS CLI by calling
the `create-query-logging-configuration` API request. This API body
contains list of destinations, but for now, we only support CloudWatch Logs as a destination
and destinations should contain exactly one element with CloudWatch configurations.

### Prerequisites

Make sure the `logGroup` is already created. The ID or role used to
configure should have the following policy or equivalent permissions.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
"Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries",
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups",
 "aps:CreateQueryLoggingConfiguration",
 "aps:UpdateQueryLoggingConfiguration",
 "aps:DescribeQueryLoggingConfiguration",
 "aps:DeleteQueryLoggingConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Configure CloudWatch Logs

You can configure CloudWatch Logs by logging into Amazon Managed Service for Prometheus using either the AWS Management Console or
the AWS CLI.

###### To configure query logging using Amazon Managed Service for Prometheus console

1. Navigate to the **Logs** tab in your workspace
   details panel.
2. Under **Query Insights**, choose
   **Create**.
3. Select the **Log Group** drop down and choose the log
   group to publish your logs.

You can also create a new log group in the CloudWatch console. 4. Enter the **Threshold (QSP)**. 5. Choose **Save**.

**To configure query logging using the AWS CLI use the
command**

```
aws amp create-query-logging-configuration \
--workspace-id `my_workspace_ID` \
--destinations '[{"cloudWatchLogs":{"logGroupArn":"`$my-log-group-arn`"},"filters":{"qspThreshold":`$qspThreshold`}}]'
```

For information on how to update, delete, and describe operations, see [Amazon Managed Service for Prometheus
API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Configuring query throttling

thresholds

To configure QSP thresholds, you must provide the query parameters in the [QueryMetrics API](AMP-APIReference-QueryMetrics.md "AMP-APIReference-QueryMetrics.md").

- max_samples_processed_warning_threshold – Sets the warning
  threshold for query samples processed
- max_samples_processed_error_threshold – Sets the error threshold
  for query samples processed

For Amazon Managed Grafana users, you can use grafana data source configuration to apply limits to
all the queries from the datasource:

1. Browse to the Amazon Managed Service for Prometheus data source configuration in Amazon Managed Grafana.
2. Under **Custom query parameters**, add the threshold
   headers.
3. Choose **Save**.

## Log content

For queries that originate from rules, you will see the following information
about the query in the CloudWatch Logs:

```
{
    workspaceId: "workspace_id",
    message: {
        query: "avg(rate(go_goroutines[1m])) > 1",
        name: "alert_rule",
        kind: "alerting",
        group: "test-alert",
        namespace: "test",
        samples: "59321",
    },
    component: "ruler"
}
```

For queries that originate from API calls, you will see the following information
about the query in the CloudWatch Logs:

```
{
    workspaceId: "ws-5e7658c2-7ccf-4c30-9de9-2ab26fa30639",
    message: {
        query: "sum by (instance) (go_memstats_alloc_bytes{job=\"node\"})",
        queryType: "range",
        start: "1683308700000",
        end: "1683913500000",
        step: "300000",
        samples: "11496",
        userAgent: "AWSPrometheusDPJavaClient/2.0.436.0 ",
        dashboardUid: "11234",
        panelId: "12"
    },
    component: "query-frontend"
}
```

## Limitations

**Policy size limits** – CloudWatch Logs resource
policies are limited to 5120 characters. When CloudWatch Logs detects that the policy is
approaching the size limit, it automatically enables log groups that start with
`/aws/vendedlogs/`. When you enable query logging, Amazon Managed Service for Prometheus must update
your CloudWatch Logs resource policy with the log group you specify. To avoid reaching the
CloudWatch Logs resource policy size limit, prefix your CloudWatch Logs log group names with
`/aws/vendedlogs/`.
