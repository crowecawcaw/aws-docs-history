Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

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

| Metric                                  | Metric name in Amazon Redshift console | Description                                                                                                                                                                       |
| --------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IntegrationLag`                        | `Lag`                                  | The lag from the time data is committed to your source to the time when the<br>data is available for queries in Amazon Redshift.<br>Units: Seconds<br>Dimensions: `IntegrationId` |
| `IntegrationNumTablesReplicated`        | `Tables replicated`                    | The number of tables that have been replicated from your source database to<br>Amazon Redshift.<br>Units: Count<br>Dimensions: `IntegrationId`                                    |
| `IntegrationNumTablesFailedReplication` | `Tables failed`                        | The number of tables that failed replication.<br>Units: Count<br>Dimensions: `IntegrationId`                                                                                      |
| `IntegrationDataTransferred`            | `Data transferred`                     | The amount of data transferred in logical bytes.<br>Units: Bytes<br>Dimensions: `IntegrationId`                                                                                   |

- From the **Table statistics** tab, you can view the list of tables
  that are currently active or have errors. The statistics on this tab are as follows
  (depending on source type):

      + **Schema name** – The name of the schema that the table is
       in.
      + **Table name** – The name of the table in the source
       database.
      + **Status** – The status of the table. Possible values
       include `Synced`, `Failed`, `Deleted`, `Resync
       Required`, and `Resync Initiated`.
      + **Database** – The Amazon Redshift database the table is in.
      + **Last updated** – The date and time (UTC) when the last
       update was made to the table.
      + **Table row count** – The number of rows in the
       table.
      + **Table size**  – The size of the table.

  You can also view a graph of the number of **Rows** inserted, deleted,
  and updated for the selected timeframe.
