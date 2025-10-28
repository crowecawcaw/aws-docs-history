# Monitor collectors with vended logs

Amazon Managed Service for Prometheus collectors provide vended logs to help you monitor and troubleshoot the metrics
collection process. These logs are automatically sent to Amazon CloudWatch Logs and provide visibility
into service discovery, metric collection, and data export operations. The collector vends
logs for three main components of the metrics collection pipeline:

###### Topics

- [Service discovery
  logs](#amp-collector-service-discovery-vended-logs "#amp-collector-service-discovery-vended-logs")
- [Collector logs](#amp-collector-vended-logs "#amp-collector-vended-logs")
- [Exporter logs](#amp-exporter-vended-logs "#amp-exporter-vended-logs")
- [Understanding and using collector vended
  logs](#amp-collector-log-details "#amp-collector-log-details")

## Service discovery

logs

Service discovery logs provide information about the target discovery process,
including:

- Authentication or permission issues when accessing Kubernetes API
  resources.
- Configuration errors in service discovery settings.

The following examples demonstrate common authentication and permission errors you
might encounter during service discovery:

**Nonexistent Amazon EKS cluster**

When the specified Amazon EKS cluster does not exist, you receive the following
error:

```
{
  "component": "SERVICE_DISCOVERY",
  "timestamp": "2025-04-30T17:25:41.946Z",
  "message": {
    "log": "Failed to watch Service - Verify your scraper source exists."
  },
  "scrapeConfigId": "s-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

**Invalid permissions for services**

When the collector lacks proper Role-Based Access Control (RBAC)
permissions to watch Services, you receive this error:

```
{
  "component": "SERVICE_DISCOVERY",
  "timestamp": "2025-04-30T17:25:41.946Z",
  "message": {
    "log": "Failed to watch Service - Verify your scraper source permissions are valid."
  },
  "scrapeConfigId": "s-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

**Invalid permissions for endpoints**

When the collector lacks proper Role-Based Access Control (RBAC)
permissions to watch Endpoints, you receive this error:

```
{
  "component": "SERVICE_DISCOVERY",
  "timestamp": "2025-04-30T17:25:41.946Z",
  "message": {
    "log": "Failed to watch Endpoints - Verify your scraper source permissions are valid."
  },
  "scrapeConfigId": "s-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

## Collector logs

Collector logs provide information about the metric scraping process,
including:

- Scrape failures due to endpoints not being available.
- Connection issues when attempting to scrape targets.
- Timeouts during scrape operations.
- HTTP status errors returned by scrape targets.

The following examples demonstrate common collector errors you might encounter during
the metric scraping process:

**Missing metrics endpoint**

When the `/metrics` endpoint is not available on the target
instance, you receive this error:

```
{
    "component": "COLLECTOR",
    "message": {
        "log": "Failed to scrape Prometheus endpoint - verify /metrics endpoint is available",
        "job": "pod_exporter",
        "targetLabels": "{__name__=\"up\", instance=\10.24.34.0\", job=\"pod_exporter\"}"
    },
    "timestamp": "1752787969551",
    "scraperId": "s-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

**Connection refused**

When the collector cannot establish a connection to the target endpoint,
you receive this error:

```
{
  "scrapeConfigId": "s-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "timestamp": "2025-04-30T17:25:41.946Z",
  "message": {
    "message": "Scrape failed",
    "scrape_pool": "pod_exporter",
    "target": "http://10.24.34.0:80/metrics",
    "error": "Get \"http://10.24.34.0:80/metrics\": dial tcp 10.24.34.0:80: connect: connection refused"
  },
  "component": "COLLECTOR"
}
```

## Exporter logs

Exporter logs provide information about the process of sending collected metrics to
your Amazon Managed Service for Prometheus workspace, including:

- Number of metrics and data points processed.
- Export failures due to workspace issues.
- Permission errors when attempting to write metrics.
- Dependency failures in the export pipeline.

The following example demonstrates a common exporter error you might encounter during
the metric export process:

**Workspace not found**

When the target workspace for metric export cannot be found, you receive
this error:

```
{
    "component": "EXPORTER",
    "message": {
        "log": "Failed to export to the target workspace - Verify your scraper destination.",
        "samplesDropped": 5
    },
    "timestamp": "1752787969664",
    "scraperId": "s-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

## Understanding and using collector vended

logs

### Log structure

All collector vended logs follow a consistent structure with these fields:

**scrapeConfigId**

The unique identifier of the scrape configuration that generated the
log.

**timestamp**

The time when the log entry was generated.

**message**

The log message content, which may include additional structured
fields.

**component**

The component that generated the log (SERVICE_DISCOVERY, COLLECTOR, or
EXPORTER)

### Using vended logs for troubleshooting

The collector vended logs help you troubleshoot common issues with metrics
collection:

1. Service discovery issues
   - Check **SERVICE_DISCOVERY** logs for
     authentication or permission errors.
   - Verify that the collector has the necessary permissions to access
     Kubernetes resources.

2. Metric scraping issues
   - Check **COLLECTOR** logs for scrape
     failures.
   - Verify that target endpoints are accessible and returning
     metrics.
   - Ensure that firewall rules allow the collector to connect to
     target endpoints.

3. Metric export issues
   - Check **EXPORTER** logs for export
     failures.
   - Verify that the workspace exists and is correctly
     configured.
   - Ensure that the collector has the necessary permissions to write
     to the workspace.

### Accessing collector vended logs

Collector vended logs are automatically sent to Amazon CloudWatch Logs. To access these
logs:

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Log groups**.
3. Find and select the log group for your collector:
   `/aws/prometheus/workspace_id/collector/collector_id`.
4. Browse or search the log events to find relevant information.

You can also use CloudWatch Logs Insights to query and analyze your collector logs. For
example, to find all service discovery errors:

````
fields @timestamp, message.message
| filter component = "SERVICE_DISCOVERY" and message.message like /Failed/
| sort @timestamp desc ``` ### Best practices for monitoring collectors To effectively monitor your Amazon Managed Service for Prometheus collectors: 1. Set up CloudWatch alarms for critical collector issues, such as persistent scrape failures or export errors. For more information, see [Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the *Amazon CloudWatch User Guide*. 2. Create CloudWatch dashboards to visualize collector performance metrics alongside vended log data. For more information, see [Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the *Amazon CloudWatch User Guide*. 3. Regularly review service discovery logs to ensure targets are being discovered correctly. 4. Monitor the number of dropped targets to identify potential configuration issues. 5. Track export failures to ensure metrics are being successfully sent to your workspace.
````
