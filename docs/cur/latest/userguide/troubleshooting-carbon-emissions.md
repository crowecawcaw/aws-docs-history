# Troubleshooting carbon emissions data

exports

###### Topics

- [Why can't I create an export of the Carbon
  emissions table even though I have IAM permissions to use Data Exports and the CUR 2.0 table?](#carbon-emissions-permissions "#carbon-emissions-permissions")
- [Why can't I see carbon emissions data for some member
  accounts in my organization?](#carbon-emissions-data "#carbon-emissions-data")
- [Why is one of the files in my S3 bucket
  empty?](#carbon-emissions-empty-file "#carbon-emissions-empty-file")
- [Why does my S3 export show zero carbon emissions
  for some Regions and services when there is usage data?](#carbon-emissions-show-zero "#carbon-emissions-show-zero")
- [Is historical data backfill
  available in Data Exports for carbon emissions?](#carbon-emissions-historical-data-backfill "#carbon-emissions-historical-data-backfill")
- [Why can't I see historical data in my S3
  bucket?](#carbon-emissions-historical-data "#carbon-emissions-historical-data")
- [I changed the settings of my report; can I
  backfill the data with the new settings?](#carbon-emissions-data-backfill "#carbon-emissions-data-backfill")
- [Why don't I see the newly released columns in my
  export?](#carbon-emissions-new-columns "#carbon-emissions-new-columns")

## Why can't I create an export of the Carbon

emissions table even though I have IAM permissions to use Data Exports and the CUR 2.0 table?

To access data in the Customer Carbon Footprint Tool or the Carbon emissions table, you
need the IAM permission `sustainability:GetCarbonFootprintSummary`.

## Why can't I see carbon emissions data for some member

accounts in my organization?

If you're using a management (payer) account, you should automatically see carbon emissions
data for your management account and all member (usage) accounts in the Carbon emissions table.
No extra configuration is required.

However, there is a 3-month data lag for carbon emissions data. For new member accounts,
data won't appear in the management account’s carbon emissions data export until the export
period that includes when the member account joined the organization. For example, if you linked
a new member account in January, its data first appears in the April export.

Similarly, when a member account leaves the organization, its data continues to appear
until the export period when it was removed.

## Why is one of the files in my S3 bucket

empty?

If your account doesn't have carbon emissions data for a given month, you'll receive a file
in your S3 bucket for the given carbon model version and usage period, but the file will be
empty.

## Why does my S3 export show zero carbon emissions

for some Regions and services when there is usage data?

If your total carbon emissions show as zero, it means they are lower than 0.0000005 MTCO2e,
which is our display threshold.

## Is historical data backfill

available in Data Exports for carbon emissions?

Yes, upon creating an export you will receive data going back up to January 2022 with the
first delivery and one month of data each month thereafter. If your account was created after
January 2022, you’ll receive carbon emissions estimates from your account creation date
onward.

## Why can't I see historical data in my S3

bucket?

Your S3 bucket might be missing historical data for any of the following reasons:

- **No historical data exists:** If you have an account
  without historical carbon emissions estimates due to being a new account or recently changing
  membership in AWS Organizations, no historical data can be populated in your S3 bucket. If
  your account has been created after January 2022, you'll receive the carbon emissions
  estimates for the entire duration of your account being active.
- **Historical backfill is still in progress:** Historical
  data backfill by Data Exports can take up to 24 hours to complete. You can use the SDK/CLI to check if
  any backfill executions failed with the `ListExecutions` API for this export, or if
  they are still in progress. Wait a little longer or use `ListExecutions` to ensure
  the backfill is not in progress.
- **Historical backfill failed:** Historical data backfill may
  have failed to complete due to an internal error. You can come to this conclusion if it's been
  more than 24 hours and the backfill is not complete, or you can use the
  `ListExecutions` API in the SDK/CLI and look for any failed executions for this
  export. If you believe the backfill has failed, try creating a new export. If it fails a
  second time, we recommend reaching out to AWS Support.

## I changed the settings of my report; can I

backfill the data with the new settings?

No, backfilling data is not currently supported.

## Why don't I see the newly released columns in my

export?

Existing exports continue with their original configuration and monthly updates until
updated. To add new columns to an existing export, you must update your export configuration for
future monthly exports (previously exported data remains unchanged). To backfill data with the
new columns, you need to create a new export. This provides up to 38 months of historical data
plus monthly updates.
