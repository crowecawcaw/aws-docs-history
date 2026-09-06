

# Configuring an integration
<a name="zero-etl-configuring-integration"></a>

When setting up a zero-ETL integration, you can configure various parameters to control how data is synchronized between your source and target systems. The following settings are currently available for SaaS sources only.

## Configuring Refresh Interval
<a name="zero-etl-config-refresh-interval"></a>

You can configure the Refresh interval for integration for SaaS sources at the time of integration creation. The default value is 1 hour. You can configure the frequency at which CDC (Change Data Capture) pulls or incremental loads should occur. This provides flexibility to align the refresh rate with your specific data update patterns, system load considerations, and performance optimization goals. Time increment can be set from 15 minutes to 8640 minutes (six days). The refresh interval cannot be modified after the integration is created when the target is Redshift. For other targets, the refresh interval can be modified after integration creation. For DynamoDB sources with refresh intervals of 24 hours or more, see [Sequential daily batches for DynamoDB sources](#zero-etl-config-refresh-interval-ddb-batches) for details about sequential daily batch processing.

This can be done through console, by updating the refresh interval within Replication Settings.

![The screenshot shows the refreshInterval parameter configuration in the zero-ETL integration settings.](http://docs.aws.amazon.com/glue/latest/dg/images/refreshinterval.png)


The time increment can be set from 15 minutes to 8640 minutes (six days), allowing you to balance between data freshness and system resource utilization. Currently, the refresh interval is customizable for both DynamoDB and SaaS sources:
+ **Minimum interval:** 15 minutes
+ **Maximum interval:** 8640 minutes (6 days)
+ **Default value:** 15 minutes for DynamoDB source and 60 minutes for SaaS source

Factors to consider when choosing a refresh interval:
+ **Data volatility:** How frequently your source data changes
+ **Business requirements:** How current your analytics data needs to be
+ **Cost considerations:** More frequent updates may result in higher processing and storage costs

**Note**  
RefreshInterval parameter defines frequency of trigger of CDC. The actual refresh frequency may be affected by the volume of changes in your source data and the processing capacity of the target system. Monitor your integration performance and adjust the refresh interval as needed to optimize for your specific use case.

Or through API by passing the `RefreshInterval` within [IntegrationConfig](https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationConfig.html) as part of CreateIntegration Request. To modify the refresh interval programmatically, you can use the [ModifyIntegration API](https://docs.aws.amazon.com/glue/latest/webapi/API_ModifyIntegration.html#API_ModifyIntegration_RequestSyntax) with the IntegrationConfig parameter.

### Sequential daily batches for DynamoDB sources
<a name="zero-etl-config-refresh-interval-ddb-batches"></a>

For zero-ETL integrations with an Amazon DynamoDB source, when you configure a refresh interval of 1440 minutes (24 hours) or greater, the integration uses sequential daily batch processing instead of a single export operation. This behavior is due to the [DynamoDB export window limitation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html), which has a maximum export period of 24 hours.

When the refresh interval exceeds 24 hours, the integration operates as follows:

1. The CDC process waits for the full refresh interval duration (for example, 6 days for a 8640-minute interval).

1. After the refresh interval elapses, the integration performs multiple sequential DynamoDB exports, each covering up to a 24-hour window.

1. The CDC jobs process each batch sequentially to capture all changes that occurred during the refresh interval period.

For example, if you set a refresh interval of 8640 minutes (6 days), the integration will wait 6 days and then execute 6 or 7 sequential exports (1 tail export covering extra time spent on export operations) and CDC jobs to synchronize all changes from that period.

## On-demand Snapshot
<a name="zero-etl-config-continuous-sync"></a>

Zero-ETL by default includes continuous data capture (CDC) but if you have use cases to replicate full data once you can do so by using the On-demand Snapshot feature. The feature currently supported for only SaaS sources can be used to replicate data once without continuous synchronization. This option provides one-time data replication with no ongoing updates, and requires manual cleanup. Once replication is complete, we recommend deleting the integration resource to avoid reaching the account integration limit.

![The screenshot shows the On-demand Snapshot setting configuration.](http://docs.aws.amazon.com/glue/latest/dg/images/ContinuousSync.png)


Or through API by setting the `ContinuousSync` parameter to `false` within [IntegrationConfig](https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationConfig.html) as part of CreateIntegration Request.

**Note**  
The On-demand Snapshot setting cannot be modified after the integration is created. Choose this option carefully based on your data synchronization requirements.

## Modifying Refresh interval
<a name="zero-etl-config-modify-refresh-interval"></a>

This feature is currently only available for AWS Glue targets and allows you to update the refresh interval for an existing integration.