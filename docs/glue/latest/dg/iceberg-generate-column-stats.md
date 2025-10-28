# Generating column statistics for Iceberg tables

Follow these steps to configure a schedule for generating statistics in the Data Catalog
using AWS Glue console or AWS CLI or the or run the
**StartColumnStatisticsTaskRun** operation.

###### To generate column statistics

1. Sign in to the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose **Tables** under Data Catalog
   .
3. Choose an Iceberg table from the list.
4. Choose **Column statistics**, **Generate on
   demand**,under **Actions** menu.

You can also choose **Generate statistics** button under
**Column statistics** tab in the lower section of the
**Tables** page. 5. On the **Generate statistics** page, provide the
statistics generation details. Follow steps 6-11 in the [Generating column statistics on a
schedule](generate-column-stats.md "generate-column-stats.md")
section to configure a schedule for statistics generation for Iceberg tables.

You can also choose to generate column statistics on-demand by followin the instructions in the [Generating column statistics on demand](column-stats-on-demand.md "column-stats-on-demand.md")

###### Note

Sampling option is not available for Iceberg tables.

AWS Glue calculates the number of distinct values for each column of the Iceberg table to a new Puffin file committed to the specified snapshot ID in your Amazon S3 location.
