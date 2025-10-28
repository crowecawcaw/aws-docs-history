# Manage data storage in AWS IoT SiteWise

You can configure AWS IoT SiteWise to save your data in the following storage tiers:

**Hot tier**

The hot storage tier is an AWS IoT SiteWise managed time series storage. Hot tier is most effective for frequently
accessed data, with low write-to-read latency. Data stored in the hot tier is used by industrial applications
that need quick access to the latest values of measurements in your equipment. This includes applications that
visualize real-time metrics with an interactive dashboard, or applications that monitor operations and launch
alarms to identify performance issues.

By default, data ingested into AWS IoT SiteWise is stored in the hot tier. You can define a
retention period for the hot tier, after which AWS IoT SiteWise moves data in the hot tier to either
warm or cold tier storage, based on your configuration. For best performance and cost
efficiency, set your hot tier retention period to be longer than the time taken to
retrieve data often. This is used for real time metrics, alarms, and monitoring scenarios.
If a retention period is not set, your data is stored indefinitely in the hot tier.

**Warm tier**

The warm storage tier is an AWS IoT SiteWise managed tier that's effective for cost-efficient storage of historical
data. It's best used to retrieve large volumes of data with medium write-to-read latency characteristics. Use
the warm tier to store historical data that's needed for large workloads. For example, it's used for
data retrieval for analytics, business intelligence applications (BI), reporting tools, and
training of machine learning (ML) models. If you enable the cold storage tier, you can define a warm tier
retention period. After the retention period ends, AWS IoT SiteWise deletes data from the warm tier.

**Cold tier**

The cold storage tier uses an Amazon S3 bucket to store data that's rarely used. With cold tier enabled, AWS IoT SiteWise
replicates the time series, including measurements, metrics, transforms and aggregates, and asset model
definitions every 6 hours. Cold tier is used to store data that tolerates high read latency for historical
reports and backups.

###### Topics

- [Configure storage settings in AWS IoT SiteWise](configure-storage.md "configure-storage.md")
- [Troubleshoot storage settings for AWS IoT SiteWise](troubleshoot-storage-configuration.md "troubleshoot-storage-configuration.md")
- [File paths and schemas of data saved in the cold
  tier](file-path-and-schema.md "file-path-and-schema.md")
