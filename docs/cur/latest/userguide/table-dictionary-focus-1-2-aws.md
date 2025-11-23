# FOCUS 1.2 with AWS columns

The FOCUS 1.2 with AWS columns table contains your cost and usage data formatted with
FinOps Open Cost and Usage Specification (FOCUS) 1.0, along with three additional
columns from AWS that contain proprietary billing data. These columns are **x_Discounts**, **x_Operation**, and **x_ServiceCode**. For more information about the FOCUS open-source
specification, refer to the [FOCUS](https://focus.finops.org/ "https://focus.finops.org/")
website.

The SQL table name for FOCUS 1.2 with AWS columns is
`FOCUS_1_2_AWS`

## Table configurations

Table configurations are user-controlled properties that a user can set to change the data or schema of a table before it's queried in Data Exports. The table configurations are saved as a JSON statement and are either specified through user input in the AWS SDK/CLI or user selections in the console.

FOCUS 1.2 has the following table configurations:

| Configuration name | Description                                                                                                                                                                                                               | Valid values                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| TIME_GRANULARITY   | This configuration changes the cost and usage line items in<br>the FOCUS 1.2 table to have different time granularities.<br>For example, selecting "HOURLY" will make all line items<br>represent a single hour of usage. | HOURLY,<br>DAILY,<br>MONTHLY |

## AWS Organizations support

The FOCUS 1.2 with AWS columns table inherits the settings you made in the consolidated
billing feature in AWS Organizations. When consolidated billing is enabled, there
are different behaviors for management and member accounts. If you’re using a
management account, your FOCUS 1.2 with AWS columns table includes cost and usage
data for the management account and all member accounts in your organization. If
you’re using a member account, your FOCUS 1.2 with AWS columns table only includes
cost and usage data for that member account.

After joining an organization, a member account can only export data for the time that the
account has been a member of the organization. For example, let's say that a member
account leaves organization A and joins organization B on the 15th of the month.
Then, the member account creates an export. Because the member account created an
export after joining organization B, the member account’s export of FOCUS 1.2 with
AWS columns for the month only includes cost and usage data for the time that the
account has been a member of organization B.
