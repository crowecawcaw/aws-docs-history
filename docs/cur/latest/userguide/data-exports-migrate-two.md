# Method two: Create an export of CUR 2.0 with its

new schema

You can create an export of CUR 2.0 with its new schema of nested columns and additional
columns. However, you’ll need to adjust your current data pipeline to process these new
columns. You do this using the console, the AWS API, or SDK.

1. Determine the CUR content settings (**Include resource IDs**,
   **Split cost allocation data**, and **Time
   granularity**) needed in order to match your CUR today.
   - You can determine the CUR content settings by going to Data Exports in the console and
     choosing your CUR export to view its details.

2. Using either the Data Exports console page (**Option A**) or the
   AWS SDK/CLI (**Option B**), create an export of CUR 2.0
   that selects all columns from the “Cost and usage report” table.
3. **(Option A)** To create the export in the
   console:
   1. In the navigation pane, choose **Data Exports**.
   2. On the **Data Exports** page, choose **Create**.
   3. Choose **Standard data export**.

   For the **Cost and Usage Report (CUR 2.0)** table, all columns
   are selected by default. 4. Specify the CUR content settings that you identified in step 1. 5. Under **Data table delivery options**, choose your
   options. 6. Choose **Create**.

4. **(Option B)** To create the export using the AWS
   API/SDK, first write a query that selects all columns in the
   `COST_AND_USAGE_REPORT` table.
   1. Use the `GetTable` API to determine the complete list of columns and
      receive the full schema.
   2. Write the CUR content settings, identified in step 1, into the table configuration
      format for the `CreateExport` API.
   3. Use the `CreateExport` API to input your SQL query and table
      configurations into the `data-query` field.
   4. Specify delivery preferences, such as the target Amazon S3 bucket and the
      overwrite preference. We recommend choosing the same delivery preferences you had
      before. For more information on the required fields, see [AWS Data Exports](../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Data_Exports.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWS_Billing_and_Cost_Management_Data_Exports.md") in the _AWS Billing and Cost Management API
      Reference_.
   5. Update the permissions of the target Amazon S3 bucket to allow Data Exports to write to
      the bucket. For more information, see [Setting
      up an Amazon S3 bucket for data exports](dataexports-s3-bucket.md "dataexports-s3-bucket.md").

5. Direct your data ingestion pipeline to read data from the directory in the Amazon S3
   bucket where your CUR 2.0 is being delivered.

You also need to update your data ingestion pipeline and your business intelligence
tools to process the following new columns with nested key-values: `product`,
`resource_tags`, `cost_category`, and
`discounts`.
