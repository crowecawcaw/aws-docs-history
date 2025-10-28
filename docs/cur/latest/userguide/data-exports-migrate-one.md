# Method one: Create an export with an SQL query

using the CUR schema

You can create an export with an SQL query. The export schema matches what you receive
today in CUR. You do this using the AWS API or SDK.

1. Determine (a) the list of columns and (b) the CUR content settings (**Include
   resource IDs**, **Split cost allocation data**, and
   **Time granularity**) needed in order to match your CUR today.
   1. You can determine the list of columns either by viewing the schema of one of your
      CUR files or going to the manifest file and extracting the list of columns from
      there.
   2. You can determine the CUR content settings by going to Data Exports in the console and
      choosing your CUR export to view its details.

2. Write an SQL query that selects the columns you identified from the CUR 2.0 table
   named `COST_AND_USAGE_REPORT`.
   1. All column names in the CUR 2.0 table are in snake case (for example,
      `line_item_usage_amount`). For your SQL statement, you might need to
      convert the previous column names to snake case.
   2. For your SQL statement, you need to convert all `resource_tag` and
      `cost_category` columns, and certain `product` and
      `discount` columns, to have the dot operator in order to select the
      nested columns in CUR 2.0. For example, to select the
      `product_from_location` column in CUR 2.0, write an SQL statement
      selecting `product.from_location`.

   Example: `SELECT product.from_location FROM
 COST_AND_USAGE_REPORT`

   This selects the `from_location` column of the `product` map
   column. 3. By default, the column selected with a dot operator is named by the attribute (for
   example, `from_location`). To match your existing CUR, you’ll need to
   declare an alias for the column in order to have the same as before.

   Example: `SELECT product.from_location AS product_from_location FROM
 COST_AND_USAGE_REPORT`

   For more details on nested columns, see the [Data Exports table dictionary](dataexports-table-dictionary.md "dataexports-table-dictionary.md").

3. Write the CUR content settings, identified in step 1, into the table configuration
   format for the `CreateExport` API. You need to provide these table
   configurations with your data query in the next step.
4. In the AWS SDK/CLI for Data Exports, use the `CreateExport` API to input your SQL
   query and table configurations into the data-query field.
   1. Specify delivery preferences, such as the target Amazon S3 bucket and the
      overwrite preference. We recommend choosing the same delivery preferences you had
      before. For more information on the required fields, see [AWS Data Exports](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Data_Exports.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Data_Exports.md") in the _AWS Billing and Cost Management API
      Reference_.
   2. Update the permissions of the target Amazon S3 bucket to allow Data Exports to write to
      the bucket. For more information, see [Setting
      up an Amazon S3 bucket for data exports](dataexports-s3-bucket.md "dataexports-s3-bucket.md").

5. Direct your data ingestion pipeline to read data from the directory in the Amazon S3
   bucket where your CUR 2.0 is being delivered.
