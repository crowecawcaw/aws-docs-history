

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Metrics for zero-ETL integrations
<a name="zero-etl-using.metrics"></a>

You can use the metrics in the Amazon Redshift console and Amazon CloudWatch to learn about the health and performance of your zero-ETL integrations. You can adjust the metrics to display data for shorter or longer duration, or choose to view metrics in CloudWatch. To view the metrics for your integration on the Amazon Redshift console, choose **Zero-ETL integrations** in the left navigation pane and choose your integration ID.

Depending on the source data of zero-ETL integrations, Amazon Redshift provides metrics on the integration details page for an integration. Possible metrics include the following types:
+ From the **Integration metrics** tab, graphs of the following are available:


<table>
<thead>
  <tr><th>Metric</th><th>Metric name in Amazon Redshift console</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>IntegrationLag</code></td><td><code>Lag</code></td><td>The lag from the time data is committed to your source to the time when the data is available for queries in Amazon Redshift.<br />Units: Seconds<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationNumTablesReplicated</code></td><td><code>Tables replicated</code></td><td>The number of tables that have been replicated from your source database to Amazon Redshift.<br />Units: Count<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationNumTablesFailedReplication</code></td><td><code>Tables failed</code></td><td>The number of tables that failed replication.<br />Units: Count<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationDataTransferred</code></td><td><code>Data transferred</code></td><td>The amount of data transferred in logical bytes.<br />Units: Bytes<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationLatestDetectedChange</code></td><td><code>Latest detected change</code></td><td>The time, in Unix epoch seconds, when the integration last staged a source change in the replication queue.<br />Units: Seconds<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationLatestAppliedChange</code></td><td><code>Latest applied change</code></td><td>The time, in Unix epoch seconds, when the integration last completed ingestion on Amazon Redshift.<br />Units: Seconds<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationDuplicateRowsDetected</code></td><td><code>Duplicate rows detected</code></td><td>The number of tables with duplicate rows identified during the reporting interval.<br />Units: Count<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
  <tr><td><code>IntegrationAutoRemediationTriggered</code></td><td><code>Auto-remediation triggered</code></td><td>The number of tables that auto-remediation moved to resynchronization during the reporting interval.<br />Units: Count<br />Dimensions: <code>IntegrationId</code><br />Update Frequency: 60 seconds</td></tr>
</tbody>
</table>

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