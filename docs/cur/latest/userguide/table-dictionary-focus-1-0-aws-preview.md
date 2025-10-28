# FOCUS 1.0 with AWS columns

(preview)

###### Note

FOCUS 1.0 with AWS columns has now been released in General Availability (GA) in a new
Data Exports table. This page is for the _preview_ release of FOCUS 1.0
with AWS columns. Use the GA table in [FOCUS 1.0 with AWS columns](table-dictionary-focus-1-0-aws-columns.md "table-dictionary-focus-1-0-aws-columns.md").

The FOCUS 1.0 with AWS columns (preview) table contains your cost and usage data formatted
with FinOps Open Cost and Usage Specification (FOCUS) 1.0, along with five additional
columns from AWS that contain proprietary billing data. These columns are **x_CostCategories**, **x_Discounts**, **x_Operation**, **x_ServiceCode**, and **x_UsageType**. For more information about the FOCUS open-source
specification, refer to the [FOCUS](https://focus.finops.org/ "https://focus.finops.org/")
website.

The SQL table name for FOCUS 1.0 with AWS columns (preview) is
`FOCUS_1_0_AWS_PREVIEW`

## Preview notes

The FOCUS 1.0 with AWS columns (preview) table **will soon
be deprecated**.

We advise all customers to use the GA release of FOCUS 1.0 with AWS columns. If you're
currently using the FOCUS 1.0 with AWS columns (preview) table, you should switch
to the GA table as soon as possible. The GA table has a large reduction in the
number of specification conformance gaps that make it suitable for production FinOps
processes. For a list of the conformance gaps in the GA table, see [FOCUS 1.0 with AWS columns conformance
gaps](table-dictionary-focus-1-0-aws-conformance.md "table-dictionary-focus-1-0-aws-conformance.md").

We do not recommend FOCUS 1.0 with AWS columns (preview) for production workloads. For a
list of the conformance gaps in the _preview_ table, see [FOCUS 1.0 with AWS columns (preview) conformance
gaps](table-dictionary-focus-1-0-aws-preview-conformance.md "table-dictionary-focus-1-0-aws-preview-conformance.md").

## Table

configurations

There are no table configurations for the FOCUS 1.0 with AWS columns (preview)
table.

## AWS Organizations

support

The FOCUS 1.0 with AWS columns (preview) table inherits the settings you made in
the consolidated billing feature in AWS Organizations. When consolidated billing
is enabled, there are different behaviors for management and member accounts. If
you’re using a management account, your FOCUS 1.0 with AWS columns (preview) table
includes cost and usage data for the management account and all member accounts in
your organization. If you’re using a member account, your FOCUS 1.0 with AWS
columns (preview) table only includes cost and usage data for that member
account.

After joining an organization, a member account can only export data for the time
that the account has been a member of the organization. For example, let's say that
a member account leaves organization A and joins organization B on the 15th of the
month. Then, the member account creates an export. Because the member account
created an export after joining organization B, the member account’s export of FOCUS
1.0 with AWS columns (preview) for the month only includes cost and usage data for
the time that the account has been a member of organization B.
