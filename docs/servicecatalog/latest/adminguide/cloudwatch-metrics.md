# AWS Service Catalog CloudWatch Metrics

You can monitor your AWS Service Catalog resources using Amazon CloudWatch, which collects
and processes raw data from AWS Service Catalog into readable metrics. These statistics are recorded
for a period of two weeks, so that you can access historical information and gain a better
perspective on how your service is performing. AWS Service Catalog metric data is automatically sent to
CloudWatch in 1-minute periods. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Topics

- [Enabling CloudWatch Metrics](#enable_cloudwatch "#enable_cloudwatch")
- [Available Metrics and Dimensions](#available_cloudwatch_metrics "#available_cloudwatch_metrics")
- [Viewing AWS Service Catalog
  Metrics](viewing-cloudwatch-metrics.md "viewing-cloudwatch-metrics.md")

## Enabling CloudWatch Metrics

Amazon CloudWatch metrics are enabled by default.

## Available Metrics and Dimensions

The metrics and dimensions that AWS Service Catalog sends to Amazon CloudWatch are listed
below.

### AWS Service Catalog Metrics

The `AWS/ServiceCatalog` namespace includes the
following metrics.

| Metric                         | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ProvisionedProductLaunch`     | The number of provisioned products launched for a given<br>product and provisioning artifact in a specified time period.<br>The dimensions are published as separate records in CloudWatch logs.<br>Units: `Count`<br>Valid statistics: `Minimum`, `Maximum`,<br>`Sum`, `Average`<br>Dimensions: `State`, `PPState`,<br>`ProductId`,<br>`ProvisioningArtifactId` |
| `ProductProvisioningOperation` | The number of operations performed on product id,<br>`provisioningArtifactId`. The dimensions are published as one record in CloudWatch logs.<br>Units: `Count`<br>Valid statistics: `Minimum`, `Maximum`,<br>`Sum`, `Average`<br>Dimensions: `State`, `PPState`,<br>`ProductId`,<br>`ProvisioningArtifactId`                                                    |

### Dimensions for

AWS Service Catalog Metrics

AWS Service Catalog sends the following dimensions to Amazon CloudWatch.

| Dimension                | Description                                                                                                                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `PPState`                | This dimension filters the data you request for all<br>provisioned products launched with this specified state. This<br>helps you categorize your data by the state of launch.<br>Valid State: AVAILABLE, TAINTED, ERROR |
| `ProductId`              | This dimension filters the data you request for the identified<br>product id only. This helps you to pinpoint an exact product<br>from which to be launched.                                                             |
| `ProvisioningArtifactId` | This dimension filters the data you request for the identified<br>provisioning artifact id only. This helps you to pinpoint an<br>exact version of products from which to be launched.                                   |
| `State`                  | This dimension filters the data you request for all<br>provisioned products launched with this specified state. This<br>helps you categorize your data by the state of launch.<br>Valid State: SUCCEEDED, FAILED         |
