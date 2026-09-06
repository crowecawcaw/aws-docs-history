

# Cross-account cross-Region metrics centralization
<a name="CloudWatchMetrics_Centralization"></a>

Amazon CloudWatch Metrics centralization automatically centralizes metrics from multiple source accounts and Regions into a single destination account within your AWS Organizations organization. You define rules to control what gets centralized, enabling unified monitoring, alarming, and analysis across your entire AWS infrastructure.

CloudWatch Metrics centralization supports the full range of CloudWatch metrics query capabilities in the destination account, including GetMetricData, PromQL, Metric Math, Anomaly Detection, and Alarms.

## Metrics centralization concepts
<a name="metrics-centralization-concepts"></a>

Before you begin using CloudWatch Metrics centralization, familiarize yourself with the following concepts:
+ **Source account** – The AWS account where metric data originates.
+ **Destination account** – The AWS account where centralized metric data is stored. This account serves as the centralized location for metric querying, alarming, and analysis.
+ **Source metadata** – Centralized metrics are automatically tagged with source metadata so you can identify the origin of each metric in the destination account. For Metrics Insights querying, the dimensions `:@aws.account` and `:@aws.region` are added. For PromQL querying, the attributes `@aws.account` and `@aws.region` are added.
+ **Backup region** – An optional secondary Region ([see pricing](https://aws.amazon.com/cloudwatch/pricing/)) within the destination account where metric data can be centralized for increased resiliency and disaster recovery purposes.

## Centralized metrics
<a name="metrics-centralization-centralized-metrics"></a>

When you enable metrics centralization, CloudWatch automatically centralizes metrics from your source accounts to the destination account. Once centralized, a copy of the metrics is now owned by your destination account. Metrics ingested through PutMetricData or EMF are queryable using GetMetricData. Metrics ingested through OpenTelemetry (OTLP) are queryable using PromQL.

### Supported metric types
<a name="metrics-centralization-supported-types"></a>

The following metric types are centralized:
+ Custom metrics (PutMetricData)
+ Embedded Metric Format (EMF) metrics
+ OpenTelemetry (OTLP) metrics

### Source metadata dimensions
<a name="metrics-centralization-source-metadata"></a>

Centralized metrics include additional source identification metadata. The format differs based on the query path:

**Metrics Insights querying (GetMetricData)**


| Dimension | Description | 
| --- | --- | 
| :@aws.account | The AWS account ID where the metric originated | 
| :@aws.region | The AWS Region where the metric originated | 

**PromQL querying**


| Attribute | Description | 
| --- | --- | 
| @aws.account | The AWS account ID where the metric originated | 
| @aws.region | The AWS Region where the metric originated | 

## Setting up metrics centralization
<a name="metrics-centralization-setup"></a>

To set up CloudWatch Metrics centralization, you need to configure centralization rules that define how metric data flows from source accounts to your destination account.

### Prerequisites
<a name="metrics-centralization-prerequisites"></a>
+ AWS Organizations must be set up and the source and destination accounts must both belong to the same organization.
+ Trusted access must be enabled for CloudWatch so the management account and the destination account can access the metric data.

**Note**  
It is recommended to enable trusted access through the console, which automatically creates the required service-linked role (SLR). If trusted access is enabled through other methods, the service-linked role will need to be created separately.

### Creating a centralization rule
<a name="metrics-centralization-create-rule"></a>

Use the following procedure to create a centralization rule that centralizes metric data from source accounts to your destination account.

**To create a centralization rule**

1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization.

1. Choose **Settings**.

1. Navigate to the **Organization** tab.

1. Choose **Configure rule**.

1. Specify source details by setting the following fields, then choose **Next**:

   1. **Centralization rule name**: Enter a unique name for the centralization rule.

   1. **Source accounts**: Define source selection criteria to pick accounts from which metric data will be centralized. The selection criteria can include:
      + A list of member accounts in the organization
      + A list of organization units in the organization
      + The entire organization

      You can provide the selection criteria in two modes:
      + **Builder**: A click-based experience to generate the source selection criteria
      + **Editor**: A free-form text box to provide the source selection criteria

      Supported syntax for source selection criteria:
      + **Supported Keys:**`OrganizationId` \| `OrganizationUnitId` \| `AccountId` \| `*`
      + **Supported Operators:**`=` \| `IN` \| `OR`

   1. **Source regions**: Select a list of Regions to look for the metric data to centralize.

1. Specify destination details by setting the following fields, then choose **Next**:

   1. **Metrics**: Make sure Metrics is selected (it is enabled by default). If you only want to centralize metrics, you can deselect Logs.

   1. **Destination region**: Select a primary Region that stores a copy of the centralized metric data.

1. Specify telemetry data by setting the following fields, then choose **Next**:

   1. **Metrics**: All metrics from the source accounts are centralized to the destination account. This includes custom metrics, Embedded Metric Format (EMF) metrics, and OpenTelemetry (OTLP) metrics.

   1. **Backup region**: Optionally select a Region that stores a second copy of the centralized metric data. Logs and metrics can have separate backup region settings.
**Note**  
Currently, all metrics from source accounts are centralized. Selective metric filtering is not supported at this time.

1. Review the centralization rule, optionally make any last-minute edits, and choose **Create centralization policy**.

### Modifying a centralization rule
<a name="metrics-centralization-modify-rule"></a>

**To modify a centralization rule**

1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization.

1. Choose **Settings**.

1. Navigate to the **Organization** tab.

1. Choose **Manage rules**.

1. Select the rule to update and choose **Edit**.

1. Update the rule configuration as needed, choosing **Next** to proceed through each step.

1. In Step 4, Review and configure, choose **Update centralization policy**.

### Viewing a centralization rule
<a name="metrics-centralization-view-rule"></a>

**To view a centralization rule**

1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization.

1. Choose **Settings**.

1. Navigate to the **Organization** tab.

1. Choose **Manage rules**.

1. View a list of all existing centralization rules and choose a specific rule name to view its details.

### Deleting a centralization rule
<a name="metrics-centralization-delete-rule"></a>

**To delete a centralization rule**

1. Navigate to the CloudWatch console in the Management or Delegated Administrator account of the organization.

1. Choose **Settings**.

1. Navigate to the **Organization** tab.

1. Choose **Manage rules**.

1. Select the rule to delete and choose **Delete**.

1. Confirm deletion and choose **Delete**.

## Features supported with centralized metrics
<a name="metrics-centralization-supported-features"></a>

The following CloudWatch features work with centralized metrics in the destination account:

**Note**  
Resource-based automatic dashboards (such as EC2 and S3) have partial support. These dashboards may show incomplete data for centralized metrics because they depend on resource metadata that is not centralized from source accounts.


| Feature | Description | 
| --- | --- | 
| GetMetricData API | Query metric data points programmatically | 
| GetMetricStatistics API | Query metric statistics | 
| ListMetrics API | Discover available centralized metrics | 
| Console Metric Browser | Browse and navigate centralized metrics | 
| Metrics Insights (SQL queries) | Query metrics using SQL-like syntax | 
| Query Studio | Unified query interface for PromQL and metrics | 
| Search Expressions | Dynamic metric discovery through SEARCH() | 
| Metric Math | Arithmetic, comparison, and logical operators on time series | 
| Anomaly Detection | ML-based anomaly detection models and alarms | 
| Metric Alarms | Standard threshold-based alarms | 
| Composite Alarms | Boolean logic combining multiple alarm states | 
| PromQL Alarms | Alarms using PromQL expressions | 
| Alarm Actions (SNS) | SNS notifications on alarm state changes | 
| CloudWatch Dashboards | Add centralized metrics to dashboards | 
| Metric Streams | Stream centralized metrics to Firehose, S3, or partners | 
| PromQL Querying | Prometheus-compatible metric queries | 

## Monitoring and troubleshooting centralization rules
<a name="metrics-centralization-monitoring"></a>

You can monitor the status and performance of your centralization rules using CloudWatch metrics, the CloudWatch console, and AWS CloudTrail logs.

### Monitoring centralization API calls with AWS CloudTrail
<a name="metrics-centralization-cloudtrail"></a>

AWS CloudTrail logs API calls made to the centralization service. Key CloudTrail events include:
+ `CreateCentralizationRuleForOrganization`: When a new centralization rule is created
+ `UpdateCentralizationRuleForOrganization`: When an existing rule is modified
+ `DeleteCentralizationRuleForOrganization`: When a rule is deleted
+ `GetCentralizationRuleForOrganization`: When rule details are retrieved
+ `ListCentralizationRulesForOrganization`: When rules are listed

### Troubleshooting common issues
<a name="metrics-centralization-troubleshooting"></a>

If metrics are not being centralized as expected, review the following common scenarios:
+ **Historical metric data** – The centralization feature only processes new metric data that arrives after rule creation. Historical data is not centralized.
+ **Trusted access not enabled** – Trusted access must be enabled for CloudWatch in AWS Organizations for the management account and the destination account.
+ **Source selection criteria** – Verify that your centralization rule's source selection criteria includes the correct accounts and Regions.
+ **Organization membership** – Both source and destination accounts must belong to the same AWS Organizations organization.
+ **Metric quota limits** – If the destination account has reached its metric quota limits, new metrics cannot be ingested. Request a quota increase if needed.
+ **Rule health status** – Check the centralization rule health status in the console or using the `GetCentralizationRuleForOrganization` API. Each centralization rule has a health status that indicates whether it is operating correctly. Rule health statuses include:
  + `HEALTHY`: The rule is operating normally and replicating metric data as configured.
  + `UNHEALTHY`: The rule has encountered issues and may not be replicating data correctly.
  + `PROVISIONING`: Centralization for the organization is in the process of being set up.

## Pricing
<a name="metrics-centralization-pricing"></a>

The first copy of centralized metrics is free. Please see the [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) page for more information.

## Related resources
<a name="metrics-centralization-related-resources"></a>
+ [Configure CloudWatch integration with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html)
+ [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md)
+ [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)