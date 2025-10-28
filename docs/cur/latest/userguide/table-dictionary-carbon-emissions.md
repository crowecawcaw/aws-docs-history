# Carbon emissions

The carbon emissions table contains your estimated carbon emissions. It provides detailed
account-level and regional granularity of your carbon emissions data. You can configure
automated monthly deliveries to Amazon S3 in either CSV or Parquet format, making it
simple to integrate with your existing business intelligence tools and reporting
systems. For more detailed information, see [Viewing your carbon footprint](../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md "../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md") in the _AWS Billing User
Guide_.

The SQL table name for carbon emissions is `CARBON_EMISSIONS`.

## Historical data

You will receive data going back up to January 2022 within 24 hours of setup, enabling you
to perform baseline analysis and trend reporting without manual data
gathering.

## Table configurations

There are no table configurations for the Carbon emissions table.

## Permissions

To access data in the Customer Carbon Footprint Tool or the Carbon emissions table, you
need the IAM permission
`sustainability:GetCarbonFootprintSummary`.

## Model versions

The methodology for calculating your carbon emissions will evolve over time to better
reflect your usage and align with carbon accounting best practices. Exports are
partitioned in hierarchical order by “model_version=Y/” and “usage_period=YYYY-MM/”.
The “model_version” partition that an export is stored under will correspond to the
model version used to generate that export, while the “usage_period” partition
corresponds to the dates the carbon emissions were generated. This structure enables
you to differentiate between data with the old and new models by viewing the
partition names.

## AWS Organizations

support

The Carbon emissions table inherits the settings you made in the consolidated
billing feature in AWS Organizations. When consolidated billing is enabled, there
are different behaviors for management and member accounts. If you’re using a
management account, your Carbon emissions table includes estimated carbon emissions
data for the management account and all member accounts in your organization. If
you’re using a member account, your Carbon emissions table only includes estimated
carbon emissions data for that member account.

After a member account joins a new organization, or a management account converts
to a member account and joins a new organization, the account's carbon emissions
data is recorded in the new organization's exports. Each management account contains
member accounts' data for the time period it was linked to said management account.
For example, a member account leaves organization A and joins organization B on the
15th of the month. Then, the member account creates an export. Because the member
account created an export after joining organization B, the member account’s export
of the Carbon emissions table for the month includes estimated carbon emissions data
for the time that the account has been a member of organization B. As with all
carbon emissions data exports, each monthly publish contains data for three months
prior (for example, an April update contains data for January).

When a member account leaves an organization or converts to a standalone account, the
member account can still access previous exports if it has permissions to the Amazon
S3 bucket where those exports are stored. Carbon emissions associated with
terminated or suspended accounts will appear in the management account data exports
for the periods when these accounts were active.

For more information, see [Consolidated billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md") in the
_AWS Billing User Guide_.
