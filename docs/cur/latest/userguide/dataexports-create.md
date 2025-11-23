# Creating data exports

You can use the **Data Exports** page in the Billing and Cost Management console to create data exports of
three different types: standard exports, cost and usage dashboard exports, and legacy
exports.

There are the following limits on the number of exports you can create per table:

- **Cost and Usage Report 2.0 (CUR 2.0)**: 5 exports
- **Cost optimization recommendations**: 2 exports
- **FOCUS 1.0 with AWS columns**: 2 exports
- **Cost and usage dashboard**: 2 exports
- **Carbon emissions**: 2 exports
  For more information, see [Quotas and restrictions](dataexports-quotas.md "dataexports-quotas.md").

Set up an export in minutes by either creating an export in the console and selecting the
table you want to export, or creating an export in the AWS SDK/CLI and defining an SQL query
of column selections and row filters from the data table you want.

When creating an export in the console, you can create an Amazon S3 bucket for your data
export storage. When creating an export in the AWS SDK/CLI, you need to create an Amazon S3
bucket with the correct bucket policy in advance. For more information, see [Setting up an
Amazon S3 bucket for data exports](dataexports-s3-bucket.md "dataexports-s3-bucket.md").

Once you create a new data export, Data Exports starts to export the data to the Amazon S3
bucket.

###### Note

It can take up to 24 hours for AWS to start delivering exports to your Amazon S3 bucket.
Once delivery starts, AWS refreshes the billing and cost management export output at least
once a day and the carbon emissions export output at least once a month in your S3 bucket. The
actual refresh rate may be different due to various factors.

###### Topics

- [Setting up an Amazon S3 bucket for data
  exports](dataexports-s3-bucket.md "dataexports-s3-bucket.md")
- [Creating a standard export](dataexports-create-standard.md "dataexports-create-standard.md")
- [Creating a cost and usage dashboard](dataexports-create-dashboard.md "dataexports-create-dashboard.md")
- [Creating a Legacy CUR export](dataexports-create-legacy.md "dataexports-create-legacy.md")
- [Creating exports with billing views](dataexports-create-billing-view.md "dataexports-create-billing-view.md")
- [Data query–SQL query and table configurations](dataexports-data-query.md "dataexports-data-query.md")
- [Configuring Cost and Usage Reports 2.0 using AWS Billing Conductor](dataexports-create-abc.md "dataexports-create-abc.md")
