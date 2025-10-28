# What are AWS Cost and Usage Reports?

AWS Cost and Usage Reports (AWS CUR) contains the most comprehensive set of cost and usage data available.
You can use Cost and Usage Reports to publish your AWS billing reports to an Amazon Simple Storage Service (Amazon S3) bucket that
you own. You can receive reports that break down your costs by the hour, day, or month, by
product or product resource, or by tags that you define yourself. AWS updates the report in
your bucket once a day in comma-separated value (CSV) format. You can view the reports using
spreadsheet software such as Microsoft Excel or Apache OpenOffice Calc, or access them from an
application using the Amazon S3 API.

AWS Cost and Usage Reports tracks your AWS usage and provides estimated charges associated with your account. Each report contains line items for each unique combination of AWS products, usage type, and operation that you use in your AWS account. You can customize the AWS Cost and Usage Reports to aggregate the information either by the hour, day, or month.

AWS Cost and Usage Reports can do the following:

- Deliver report files to your Amazon S3 bucket
- Update the report up to three times a day
- Create, retrieve, and delete your reports using the AWS CUR API Reference

## How Cost and Usage Reports work

After you create a Cost and Usage Report, AWS sends your report to the Amazon S3 bucket that you
specify. AWS updates your report at least once a day until your charges are
finalized.

Your report files consist of a .csv file or a collection of .csv files and a manifest
file. You can choose to configure your report data for integration with Amazon Athena, Amazon Redshift,
or Quick Suite.

## Report timeline

After you create your report, it can take up to 24 hours for AWS to deliver the first
report to your Amazon S3 bucket.

After delivery starts, AWS updates the report files at least once a day. Each report
update in a given month is cumulative, so each version of the report includes all of the
billing data for the month to date. The report updates that you receive throughout the month
are estimates. The charges are subject to change as you continue to use your AWS
services.

###### Note

Different AWS services provide your usage-based billing information at different
times, so you might notice updates to a certain hour or day come in at different
times.

AWS builds on previous reports until the end of the billing period. AWS finalizes your
report’s usage charges after issuing an invoice at the end of the month. After the end of the
report billing period, AWS generates a new report for the next month with none of the
information from the previous report.

After your report is finalized, AWS might update the report if AWS applies refunds,
credits, or AWS Support fees to your usage for the month. Because Developer, Business, and
Enterprise Support are calculated based on final usage charges, those are reflected on the
sixth or seventh of the month for the prior month’s Cost and Usage Report. AWS applies credits or
refunds based on the terms of your agreement or contract with AWS.

## Report files

Your report is a .csv file or a collection of .csv files stored in an Amazon S3 bucket. The
number of files that your report generates depends on your selection for report versioning and
the size of your report.

When you create a report, you can choose to create new report versions or overwrite the
existing report version with every update. If you choose to create new report versions, then
your report generates more files with every update.

The size of an individual report can grow to more than a gigabyte and might exceed the
capacity of desktop spreadsheet applications to display every line. If a report is larger than
most applications can handle (around 1 million rows), then AWS splits the report into
multiple files that are stored in the same folder in the Amazon S3 bucket.

AWS also generates refunds into separate files. AWS issues refunds after the closing
of a monthly bill.

For more information on report files, file-naming conventions, and versioning, see [Understanding your report versions](understanding-report-versions.md "understanding-report-versions.md").

## Report columns

Each report includes several columns with details about your AWS costs and usage. The
columns that AWS includes in your report depend on your usage during the month.

Every report includes columns with the **identity/**,
**bill/**, and **lineItem/** prefixes. All other columns
are included only if your monthly AWS usage generates data to populate those columns.

For example, your report includes **savingsPlan/** columns only if you
used Savings Plans during that month.

To learn more about the columns in your report, see the [Data dictionary](data-dictionary.md "data-dictionary.md").

## Using your report

You can download your report from the Amazon S3 console, query the report using Amazon Athena, or
upload the report into Amazon Redshift or Quick Suite.

- For more information about creating an Amazon S3 bucket and using Athena to query your data,
  see [Querying Cost and Usage Reports using Amazon Athena](cur-query-athena.md "cur-query-athena.md").
- For more information about uploading to Amazon Redshift, see [Loading report data to Amazon Redshift](cur-query-other.md#cur-query-other-rs "cur-query-other.md#cur-query-other-rs").
- For more information about uploading to Quick Suite, see [Loading report data to Amazon Quick Suite](cur-query-other.md#cur-query-other-qs "cur-query-other.md#cur-query-other-qs").
