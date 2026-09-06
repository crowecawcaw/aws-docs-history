

# Setting up your AWS account
<a name="initial-account-setup"></a>

Before you can enable Amazon Security Lake, you must have an AWS account.

## Identify the account that you'll use to enable Security Lake
<a name="prerequisite-organizations"></a>

Security Lake integrates with AWS Organizations to manage log collection across multiple accounts in an organization. If you want to use Security Lake for an organization, you must use your Organizations management account to designate a delegated Security Lake administrator. Then, you must use the credentials of the delegated administrator to enable Security Lake, add member accounts, and enable Security Lake for them. For more information, see [Managing multiple accounts with AWS Organizations in Security Lake](multi-account-management.md).

Alternatively, you can use Security Lake without the Organizations integration for a standalone account that's not part of an organization.