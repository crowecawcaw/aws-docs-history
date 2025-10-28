# Troubleshooting CUR 2.0

###### Topics

- [Why are some columns that were available in CUR
  not appearing in CUR 2.0?](#dataexports-missing-columns "#dataexports-missing-columns")
- [What will happen to legacy Cost and Usage
  Reports; will it be deprecated?](#dataexports-legacy-cur-deprecation "#dataexports-legacy-cur-deprecation")
- [Does creating an export of CUR 2.0 affect my
  legacy CUR?](#dataexports-legacy-cur-affect "#dataexports-legacy-cur-affect")
- [Why can’t I create an export of CUR 2.0
  even though I have IAM permissions to use Data Exports and the CUR table?](#dataexports-missing-iam-permissions "#dataexports-missing-iam-permissions")
- [When attempting to create a data export
  with the same CSV format as the legacy CUR columns, I get an "Invalid QueryStatement" error.
  How can I resolve this?](#dataexports-invalid-query-statement "#dataexports-invalid-query-statement")
- [After migrating to Data Exports CUR 2.0, can I have a legacy CUR
  export and a CUR 2.0 export at the same time?](#dataexports-revert "#dataexports-revert")
- [When attempting to create an export of CUR 2.0, I get
  the error "This account is unable to create an export against this table". Why can't I create a
  CUR 2.0 export?](#dataexports-pro-forma "#dataexports-pro-forma")

## Why are some columns that were available in CUR

not appearing in CUR 2.0?

In CUR 2.0, four column types became nested into four individual columns. The resulting
nested columns are: `product`, `discount`, `resource_tag`, and
`cost_category`.

In legacy CUR, there could be hundreds of columns with names that started with these
strings. The variations depended on customer usage of AWS services or agreements with AWS.
This schema design resulted in hundreds of columns that were often sparsely filled. The
variability of the columns could also cause problems with SQL queries due to a charging
schema.

As a result, the columns that could vary across different AWS columns were nested
together into these four columns. Certain product columns that are commonly used were not
nested.

You can recreate the schema of the CUR in your CUR 2.0 export by using the dot operator in
SQL. To learn how to do this, see [Migrating from CUR to Data Exports CUR 2.0](data-exports-migrate.md "data-exports-migrate.md").

## What will happen to legacy Cost and Usage

Reports; will it be deprecated?

We currently have no plans to deprecate legacy CUR. However, as CUR 2.0 in Data Exports offers
several improvements such as a consistent schema, nested data, and additional columns
(`bill_payer_account_name` and `line_item_usage_account_name`), we
recommend migrating to CUR 2.0.

While there is no target date, we are planning to eventually deprecate **Cost and
Usage Reports** under **Legacy Pages** in the console. However, all
of the same functionality to create, update, and delete legacy CUR is available through the
**Data Exports** console page.

###### Note

Detailed Billing Reports (DBR), another legacy billing feature, may be deprecated at a
later date. The feature has been unavailable for new customers since July 8, 2019.

## Does creating an export of CUR 2.0 affect my

legacy CUR?

CUR and CUR 2.0 are two distinct reports. When creating CUR 2.0, there is no impact on your
existing CUR settings. You can choose between legacy CUR and CUR 2.0 based on your
preferences.

## Why can’t I create an export of CUR 2.0

even though I have IAM permissions to use Data Exports and the CUR table?

Make sure you also have IAM permissions for `cur:PutReportDefinition`.

## When attempting to create a data export

with the same CSV format as the legacy CUR columns, I get an "Invalid QueryStatement" error.
How can I resolve this?

Currently, you can't rename your columns to have special characters such as "/" to match
the legacy CUR column names in CSV format. For information about the supported character types,
see [SQL query](dataexports-data-query.md#dataexports-sql-query "dataexports-data-query.md#dataexports-sql-query").

## After migrating to Data Exports CUR 2.0, can I have a legacy CUR

export and a CUR 2.0 export at the same time?

Yes, you can have up to 10 legacy CUR exports and 5 CUR 2.0 exports at the same
time.

## When attempting to create an export of CUR 2.0, I get

the error "This account is unable to create an export against this table". Why can't I create a
CUR 2.0 export?

Unlike legacy CUR, CUR 2.0 does not currently support creating an export of CUR 2.0 with
pro forma billing data. If you are part of a billing group in AWS Billing Conductor, you are
only allowed to receive pro forma billing data. As a result, you receive this error message when
trying to create an export of CUR 2.0. You can still create a legacy CUR export.
