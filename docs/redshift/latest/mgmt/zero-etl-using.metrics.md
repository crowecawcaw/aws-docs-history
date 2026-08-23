Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Metrics for zero-ETL integrations

You can use the metrics in the Amazon Redshift console and Amazon CloudWatch to learn about the health and
performance of your zero-ETL integrations. You can adjust the metrics to display data for shorter or
longer duration, or choose to view metrics in CloudWatch. To view the metrics for your integration
on the Amazon Redshift console, choose **Zero-ETL integrations** in the left navigation pane and
choose your integration ID.

Depending on the source data of zero-ETL integrations, Amazon Redshift provides metrics on the integration
details page for an integration. Possible metrics include the following types:

- From the **Integration metrics** tab, graphs of the following are
  available:

| Metric                                  | Metric name in Amazon Redshift console | Description                                                                                                                                                                                                       |
| --------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IntegrationLag`                        | `Lag`                                  | The lag from the time data is committed to your source to the time when the<br>data is available for queries in Amazon Redshift.<br>Units: Seconds<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds |
| `IntegrationNumTablesReplicated`        | `Tables replicated`                    | The number of tables that have been replicated from your source database to<br>Amazon Redshift.<br>Units: Count<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                                    |
| `IntegrationNumTablesFailedReplication` | `Tables failed`                        | The number of tables that failed replication.<br>Units: Count<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                                                                                      |
| `IntegrationDataTransferred`            | `Data transferred`                     | The amount of data transferred in logical bytes.<br>Units: Bytes<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                                                                                   |
| `IntegrationLatestDetectedChange`       | `Latest detected change`               | The time, in Unix epoch seconds, when the integration last staged a<br>source change in the replication queue.<br>Units: Seconds<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                   |
| `IntegrationLatestAppliedChange`        | `Latest applied change`                | The time, in Unix epoch seconds, when the integration last completed<br>ingestion on Amazon Redshift.<br>Units: Seconds<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                            |
| `IntegrationDuplicateRowsDetected`      | `Duplicate rows detected`              | The number of tables with duplicate rows identified during the reporting<br>interval.<br>Units: Count<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                                              |
| `IntegrationAutoRemediationTriggered`   | `Auto-remediation triggered`           | The number of tables that auto-remediation moved to resynchronization<br>during the reporting interval.<br>Units: Count<br>Dimensions: `IntegrationId`<br>Update Frequency: 60 seconds                            |

###### Note

For integrations that replicate multiple databases, the
`IntegrationLatestDetectedChange` and
`IntegrationLatestAppliedChange` metrics report the minimum value across
all databases. This represents the least recently updated database. Per-database
values are available in the `latest_detected_change_time` and
`latest_applied_change_time` columns of [SVV\_INTEGRATION](../dg/r_SVV_INTEGRATION.md "../dg/r_SVV_INTEGRATION.md").

- From the **Table statistics** tab, you can view the list of tables
  that are currently active or have errors. The statistics on this tab are as follows
  (depending on source type):

  - **Schema name** – The name of the schema that the table is
    in.
  - **Table name** – The name of the table in the source
    database.
  - **Status** – The status of the table. Possible values
    include `Synced`, `Failed`, `Deleted`, `Resync
   Required`, and `Resync Initiated`.
  - **Database** – The Amazon Redshift database the table is in.
  - **Last updated** – The date and time (UTC) when the last
    update was made to the table.
  - **Table row count** – The number of rows in the
    table.
  - **Table size** – The size of the table.
    You can also view a graph of the number of **Rows** inserted, deleted,
    and updated for the selected timeframe.
