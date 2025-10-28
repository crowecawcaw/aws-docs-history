# Storage and structure of AWS Marketplace data feeds

AWS Marketplace provides data feeds as a mechanism to send structured, up-to-date product and
customer information from AWS Marketplace systems to seller Amazon S3 buckets for ETL (extract, transform, and
load) between seller-owned business intelligence tools. This topic provides more information about
the structure and storage of data feeds.

Data feeds collect and deliver comma-separated value (CSV) files to an encrypted Amazon S3
bucket that you provide. The CSV files have the following characteristics:

- They follow the [4180
  standards](https://tools.ietf.org/html/rfc4180 "https://tools.ietf.org/html/rfc4180").
- Character encoding is UTF-8 without BOM.
- Commas are used as separators between values.
- Fields are escaped by double quotation marks.
- `\n` is the line feed character.
- Dates are reported in the UTC time zone, are in ISO 8601 date and time format, and are
  accurate within 1 second.
- All `*_period_start_date` and `*_period_end_date` values are
  inclusive, which means that `23:59:59` is the last possible timestamp for any
  day.
- All monetary fields are preceded with a currency field.
- Monetary fields use a period (`.`) character as a decimal separator, and
  don't use a comma (,) as a thousands separator.
  Data feeds are generated and stored as follows:

- Data feeds are generated within a day, and contain 24 hours of data from the previous
  day.
- In the Amazon S3 bucket, data feeds are organized by month using the following
  format:

``bucket-name`/`data-feed-name_version`/year=`YYYY`/month=`MM`/data.csv`

- As each daily data feed is generated, it is appended to the existing CSV file for that
  month. When a new month starts, a new CSV file is generated for each data feed.
- Information in data feeds is backfilled from 2010/01/01 to 2020/04/30 (inclusive) and
  is available in the CSV file in the
  `year=2010/month=01` subfolder.

You may notice cases where the current month's file for a given data feed contains
only column headers, and no data. This means that there were no new entries for that month
for the feed. This can happen with data feeds that are updated less frequently, like the
product feed. In these cases, data is available in the backfilled folder.

- In Amazon S3, you can create an [Amazon S3
  lifecycle policy](../../../AmazonS3/latest/userguide/create-lifecycle.md "../../../AmazonS3/latest/userguide/create-lifecycle.md") to manage how long to keep files in the bucket.
- You can configure Amazon SNS to notify you when data is delivered to your encrypted Amazon S3
  bucket. For information on how to configure notifications, see [Getting started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the
  _Amazon Simple Notification Service Developer Guide_.

## Historization of the data

Each data feed includes columns that document the history of the data. Except for
`valid_to`, these columns are common to all data feeds. They're included as a
common history schema and are useful in querying the data.

| Column name          | Description                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| valid_from           | The first date that the value for the primary key is valid for in relation to values for other fields.                 |
| valid_to             | This column is only shown on the [Address](data-feed-address.md "data-feed-address.md") data feed and is always blank. |
| insert_date          | The date a record was inserted into the data feed.                                                                     |
| update_date          | The date the record was last updated.                                                                                  |
| delete_date          | This column is always blank.                                                                                           | The following shows an example of these columns. |
| valid_from           | valid_to                                                                                                               | insert_date                                      | update_date          | delete_date |
| ---                  | ---                                                                                                                    | ---                                              | ---                  | ---         |
| 2018-12-12T02:00:00Z |                                                                                                                        | 2018-12-12T02:00:00Z                             | 2018-12-12T02:00:00Z |             |
| 2019-03-29T03:00:00Z |                                                                                                                        | 2019-03-29T03:00:00Z                             | 2019-03-29T03:00:00Z |             |
| 2019-03-29T03:00:00Z |                                                                                                                        | 2019-03-29T03:00:00Z                             | 2019-04-28T03:00:00Z |             | The `valid_from` and `update_date` field together form a _bi-temporal data model_. The `valid_from` field, as it is named, tells you when the item is valid from. If the item was edited, it can have multiple records in the feed, each with a different `update_date`, but the same `valid_from` date. For example, to find the current value for an item, you would find the record with the most recent `update_date`, from the list of records with the most recent `valid_from` date. In the example above, the record was originally created 2018-12-12. It was then changed on 2019-03-29 (for example, if the address in the record changed). Later, on 2019-04-28, the address change was corrected (so the `valid_from` didn't change, but the `update_date` did). Correcting the address (a rare event) retroactively changes the record from the original `valid_from` date, so that field didn't change. A query to find the most recent `valid_from` would return two records, the one with the latest `update_date` gives you the actual current record. |
