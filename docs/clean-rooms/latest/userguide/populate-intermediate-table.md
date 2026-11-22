

# Populating an intermediate table

After you create an intermediate table, you must populate it to materialize data. You can also repopulate an intermediate table to refresh the data when base tables are updated.

Each populate operation creates a new version of the intermediate table. The previous version remains available during the refresh. If the refresh fails, the existing data is not affected.

**Considerations and limitations**

Before you populate an intermediate table, review the following:
+ **Access budgets** – Populating an intermediate table decrements access budgets on all referenced base tables, including transitive dependencies.
+ **Quotas** – SQL and PySpark analyses that populate an intermediate table count toward your quotas. For more information, see [AWS Clean Rooms quotas](clean-rooms-quotas.md).

If you populate an intermediate table with a PySpark analysis template, the following also apply:
+ You must use a PySpark 2.0 (`PYSPARK_2_0`) analysis template.
+ The script must return exactly one result DataFrame.
+ Results are written as Parquet only. CSV isn't supported.
+ The output can have at least 1 column and at most 100 columns.
+ The populate operation converts column names to lowercase. If two names become identical after conversion, the operation fails.
+ The populate operation runs as a protected job that can take from minutes to hours. During this time, the table moves from `POPULATE_STARTED` to `POPULATE_SUCCESS` or `POPULATE_FAILED`.

**To populate an intermediate table**

1. Open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration, and then choose the **Tables** tab.

1. Choose the intermediate table that you want to populate.

1. Choose **Populate**.

1. In the **Populate** dialog, review the stored analysis (SQL query or analysis template reference).

1. Configure the following settings:
   + **Query compute payer** – If your collaboration has multiple query compute payers, select the one that pays for query compute costs for the populate operation.
   + **Worker type** – The instance type for the populate job (default: CR.1X).
   + **Number of workers** – The number of instances to use (2–128, default: 16).
   + (Optional) **Spark properties** – Custom Spark runtime configuration.

1. Choose **Populate**.

**Tracking progress**

To view the status of a populate operation, choose the **Analysis** tab on the intermediate table details page. The information shown depends on how the table is populated:
+ When the table is populated by a SQL query, the tab shows the **Protected query ID** (linked to query details), **Status**, **Worker type**, **Number of workers**, and **Billed CRPU hours**.
+ When the table is populated by a PySpark analysis template, the tab shows the **Protected job ID** (linked to job details), **Status**, **Worker type**, and **Number of workers**.