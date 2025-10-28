# Using Cost and Usage Reports for AWS Organizations

In AWS Organizations, both management accounts and member accounts can create Cost and Usage Reports. The
IAM policies that allow or restrict the ability to create a report are the same for both
types of accounts.

###### Note

The account that creates the Cost and Usage Report must also own the Amazon S3 bucket that AWS
sends the reports to. You cannot configure a Cost and Usage Report to deliver to an Amazon S3 bucket
owned by another account. For more information about Amazon S3 bucket setup requirements, see
[Setting up an Amazon S3 bucket for Cost and Usage Reports](cur-s3.md "cur-s3.md").

## Managing Cost and Usage Reports as a member account

If you have permissions to create a Cost and Usage Report for a member account within an
organization, you can create a report for only the member account’s cost and usage data. The
member account receives reports for its cost and usage during the time that the account has
been a member of its current organization.

For example, say a member account leaves organization A and joins organization B on the
15th of the month. Then, the member account creates a report. Because the member account
created a report after joining organization B, the member account’s report for the month
includes billing data for only the time that the account has been a member of organization
B.

After a member account joins a new organization, the member account's cost and usage are
recorded in the new organization’s reports. This is the same outcome for a management
account that converts to a member account and joins a new organization.

When a member account leaves an organization or converts into a standalone account, the
member account can still access the previous reports as long as they have permissions to the
Amazon S3 bucket where the previous reports are stored.

## Managing Cost and Usage Reports as a management

account

If you’re an administrator of an AWS Organizations management account and you don’t want member
accounts to create a report, you can apply a service control policy (SCP) that prevents
member accounts from creating reports. The SCP can prevent member accounts from creating new
reports, but it doesn’t delete reports created previously.

###### Note

SCPs apply only to member accounts. To prevent a management account from creating a
report, modify the IAM policies attached to the user roles in the management
account.

For more information on consolidated billing, see [Consolidated billing for
AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md") in the _AWS Billing User Guide_.
