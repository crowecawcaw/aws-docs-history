# Setting up your AWS account

Before you can enable Amazon Security Lake, you must have an AWS account. If you do not have an AWS account, complete the following steps to create one.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Identify the account that you'll use to enable Security Lake

Security Lake integrates with AWS Organizations to manage log collection across multiple
accounts in an organization. If you want to use Security Lake for an organization, you
must use your Organizations management account to designate a delegated Security Lake
administrator. Then, you must use the credentials of the delegated administrator to
enable Security Lake, add member accounts, and enable Security Lake for them. For more
information, see [Managing multiple accounts with AWS Organizations in Security Lake](multi-account-management.md "multi-account-management.md").

Alternatively, you can use Security Lake without the Organizations integration for a standalone
account that's not part of an organization.
