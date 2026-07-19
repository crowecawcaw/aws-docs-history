# Quotas and usage

Amazon Location Service places quotas on API key management operations to help manage service capacity
and prevent over-utilization. You can adjust these quotas through the AWS Service Quotas
console or by contacting support. This section covers the service quotas for authentication
APIs, usage monitoring with CloudWatch, and how to request increases.

## Service quotas

Amazon Location Service sets default quotas for API key management operations, which can be viewed
in the AWS Service Quotas management console. You can request an increase through
the self-service console (links are shown in the following table), for up to 2x the
default limit for each operation. For quota limits exceeding 2x the default limit,
request in the [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") and it will submit a support ticket. Alternatively,
you can connect with your premium support team. There are no direct charges for quota
increase requests.

API key management quotas| Operation | Default | Adjustable max limit | More than adjustable max limit |
| --- | --- | --- | --- |
| API keys per account per Region | 500 | Not adjustable | N/A |
| [CreateKey](../APIReference/API_geoapikeys_CreateKey.md "../APIReference/API_geoapikeys_CreateKey.md") | 10 TPS | 20 TPS | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [DescribeKey](../APIReference/API_geoapikeys_DescribeKey.md "../APIReference/API_geoapikeys_DescribeKey.md") | 10 TPS | 20 TPS | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [UpdateKey](../APIReference/API_geoapikeys_UpdateKey.md "../APIReference/API_geoapikeys_UpdateKey.md") | 10 TPS | 20 TPS | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [DeleteKey](../APIReference/API_geoapikeys_DeleteKey.md "../APIReference/API_geoapikeys_DeleteKey.md") | 10 TPS | 20 TPS | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [ListKeys](../APIReference/API_geoapikeys_ListKeys.md "../APIReference/API_geoapikeys_ListKeys.md") | 10 TPS | 20 TPS | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |

For quotas on the APIs that you call using an API key (Maps, Places, and Routes),
see the quota and usage page for each service:

- [Map quotas and usage](map-quota-and-usage.md "map-quota-and-usage.md")
- [Places quotas and usage](places-quota-usage.md "places-quota-usage.md")
- [Routes Quota and Usage](routes-quota-usage.md "routes-quota-usage.md")

## Monitor usage with CloudWatch

Use Amazon CloudWatch to monitor API key usage, detect anomalies, and set alarms when
usage patterns change unexpectedly. Amazon Location Service exports metrics to the
`AWS/Location` namespace with the `ApiKeyName` dimension,
allowing you to track usage per key.

### Available metrics

The following metrics are available with the `ApiKeyName`
dimension:

API key CloudWatch metrics| Metric | Description | Useful statistic |
| --- | --- | --- |
| `CallCount` | Number of API calls made using the key. | Sum |
| `ErrorCount` | Number of error responses for calls made using the<br>key. | Sum |
| `SuccessCount` | Number of successful calls made using the key. | Sum |
| `CallLatency` | Time to process and return a response for calls made using<br>the key. | Average |

You can filter metrics by the following dimension combinations:

- `ApiKeyName, OperationName` – Usage per key per
  API operation.
- `ApiKeyName, OperationName, ResourceName` – Usage
  per key per operation per resource.
- `ApiKeyName, OperationName, OperationVersion` –
  Usage per key per operation for standalone Maps, Places, and Routes
  APIs.

### Detect anomalies in usage patterns

Create CloudWatch alarms to detect unusual usage patterns that may indicate
unauthorized use of an API key or misconfigured applications:

- **Spike in call volume** – Set an
  alarm on `CallCount` with the `ApiKeyName`
  dimension to alert when a key's usage exceeds its normal baseline. Use
  CloudWatch anomaly detection to automatically adapt thresholds based on
  historical patterns.
- **Increase in errors** – Set an
  alarm on `ErrorCount` to detect when a key is receiving an
  abnormal number of rejected requests, which may indicate an
  unauthorized party attempting to use the key.
- **Unexpected off-hours usage** –
  Use CloudWatch anomaly detection on `CallCount` to automatically
  learn your application's normal daily and weekly traffic patterns.
  Alerts trigger when usage deviates from expected patterns, such as
  significant traffic during hours when your application is normally
  idle.

For more information about creating alarms, see [Using CloudWatch with
Amazon Location Service](cloudwatch.md "cloudwatch.md").

## Next steps

For additional information, see:

- [Visualizing your service quotas and setting alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md"): Monitor usage
  against quota limits in the CloudWatch User Guide.
- [Amazon Location Service
  pricing](https://aws.amazon.com/location/pricing/ "https://aws.amazon.com/location/pricing/"): Review pricing details for all Amazon Location Service APIs.
- [SLA](https://aws.amazon.com/location/sla/ "https://aws.amazon.com/location/sla/"): Review the
  Amazon Location Service Service Level Agreement to understand availability
  guarantees.
- [Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/"):
  Familiarize yourself with the legal terms governing the use of
  Amazon Location Service.
