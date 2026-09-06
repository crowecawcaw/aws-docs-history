

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Metrics for zero-ETL integrations
<a name="zero-etl-using.metrics"></a>

You can use the metrics in the Amazon Redshift console and Amazon CloudWatch to learn about the health and performance of your zero-ETL integrations. You can adjust the metrics to display data for shorter or longer duration, or choose to view metrics in CloudWatch. To view the metrics for your integration on the Amazon Redshift console, choose **Zero-ETL integrations** in the left navigation pane and choose your integration ID.

Depending on the source data of zero-ETL integrations, Amazon Redshift provides metrics on the integration details page for an integration. Possible metrics include the following types:
+ From the **Integration metrics** tab, graphs of the following are available:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.metrics.html)
**Note**  
For integrations that replicate multiple databases, the `IntegrationLatestDetectedChange` and `IntegrationLatestAppliedChange` metrics report the minimum value across all databases. This represents the least recently updated database. Per-database values are available in the `latest_detected_change_time` and `latest_applied_change_time` columns of [SVV\_INTEGRATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION.html).
+ From the **Table statistics** tab, you can view the list of tables that are currently active or have errors. The statistics on this tab are as follows (depending on source type):
  + **Schema name** – The name of the schema that the table is in.
  + **Table name** – The name of the table in the source database.
  + **Status** – The status of the table. Possible values include `Synced`, `Failed`, `Deleted`, `Resync Required`, and `Resync Initiated`.
  + **Database** – The Amazon Redshift database the table is in.
  + **Last updated** – The date and time (UTC) when the last update was made to the table.
  + **Table row count** – The number of rows in the table.
  + **Table size ** – The size of the table.

You can also view a graph of the number of **Rows** inserted, deleted, and updated for the selected timeframe.