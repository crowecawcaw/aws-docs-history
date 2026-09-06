

# Viewing and monitoring Aurora zero-ETL integrations
<a name="zero-etl.describingmonitoring"></a>

You can view the details of an Amazon Aurora zero-ETL integration to see its configuration information and current status. You can also monitor the status of your integration by querying specific system views in Amazon Redshift. In addition, Amazon Redshift publishes certain integration-related metrics to Amazon CloudWatch, which you can view within the Amazon Redshift console.

**Topics**
+ [Viewing integrations](#zero-etl.describing)
+ [Monitoring integrations using system tables for Amazon Redshift](#zero-etl.monitoring)
+ [Monitoring integrations with Amazon EventBridge for Amazon Redshift](#zero-etl.eventbridge)

## Viewing integrations
<a name="zero-etl.describing"></a>

You can view Aurora zero-ETL integrations using the AWS Management Console, the AWS CLI, or the RDS API.

### Console
<a name="zero-etl.describing-console"></a>

**To view the details of a zero-ETL integration**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. From the left navigation pane, choose **Zero-ETL integrations**. 

1. Select an integration to view more details about it, such as its source DB cluster and target data warehouse.  
![Details about a zero-ETL integration.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/zero-etl-integration-view.png)

An integration can have the following statuses:
+ `Creating` – The integration is being created.
+ `Active` – The integration is sending transactional data to the target data warehouse.
+ `Syncing` – The integration has encountered a recoverable error and is reseeding data. Affected tables aren't available for querying until they finish resyncing.
+ `Needs attention` – The integration encountered an event or error that requires manual intervention to resolve it. To fix the issue, follow the instructions in the error message on the integration details page.
+ `Failed` – The integration encountered an unrecoverable event or error that can't be fixed. You must delete and recreate the integration.
+ `Deleting` – The integration is being deleted.

### AWS CLI
<a name="zero-etl.describing-cli"></a>

To view all zero-ETL integrations in the current account using the AWS CLI, use the [describe-integrations](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-integrations.html) command and specify the `--integration-identifier` option.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds describe-integrations \
    --integration-identifier {{ee605691-6c47-48e8-8622-83f99b1af374}}
```
For Windows:  

```
aws rds describe-integrations ^
    --integration-identifier {{ee605691-6c47-48e8-8622-83f99b1af374}}
```

### RDS API
<a name="zero-etl.describing-api"></a>

To view zero-ETL integration using the Amazon RDS API, use the [`DescribeIntegrations`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeIntegrations.html) operation with the `IntegrationIdentifier` parameter.

## Monitoring integrations using system tables for Amazon Redshift
<a name="zero-etl.monitoring"></a>

Amazon Redshift has system tables and views that contain information about how the system is functioning. You can query these system tables and views the same way that you would query any other database table. For more information about system tables and views in Amazon Redshift, see [System tables and views reference](https://docs.aws.amazon.com/redshift/latest/dg/cm_chap_system-tables.html) in the *Amazon Redshift Database Developer Guide*.

You can query the following system views and tables to get information about your Aurora zero-ETL integrations:
+  [SVV\_INTEGRATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION.html) – Provides configuration details for your integrations.
+ [SVV\_INTEGRATION\_TABLE\_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION_TABLE_STATE.html) – Describes the state of each table within an integration.
+ [SYS\_INTEGRATION\_TABLE\_STATE\_CHANGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_TABLE_STATE_CHANGE.html) – Displays table state change logs for an integration.
+ [SYS\_INTEGRATION\_ACTIVITY](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_ACTIVITY.html) – Provides information about completed integration runs.

All integration-related Amazon CloudWatch metrics originate from Amazon Redshift. For more information, see [Metrics for zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.monitoring.html) in the *Amazon Redshift Management Guide*. Currently, Amazon Aurora doesn't publish any integration metrics to CloudWatch.

## Monitoring integrations with Amazon EventBridge for Amazon Redshift
<a name="zero-etl.eventbridge"></a>

Amazon Redshift send integration-related events to Amazon EventBridge. For a list of events and their corresponding event IDs, see [Zero-ETL integration event notifications with Amazon EventBridge](https://docs.aws.amazon.com/redshift/latest/mgmt/integration-event-notifications) in the *Amazon Redshift Management Guide*.