# Continually

managing your member accounts within GuardDuty

As a delegated GuardDuty administrator account, you are responsible for maintaining the configuration of GuardDuty and its
optional protection plans for all the accounts in your organization in each supported
AWS Region. The following sections provide the options about maintaining the
configuration status of GuardDuty or any of its optional protection plans:

###### To maintain the configuration status of your entire organization in each

Region

- **Set auto-enable preferences for the entire organization
  by using GuardDuty console** – You can enable GuardDuty
  automatically for either all (`ALL`) the members in the organization
  or new (`NEW`) members joining the organization, or choose not to
  (`NONE`) auto-enable it any of the members in the
  organization.

You can also configure the same or different settings for any of the
protection plans within GuardDuty.

It might take up to 24 hours to update the configuration for all member
accounts in the organization.

- **Update auto-enable preferences by using API**
  – Run [UpdateOrganizationConfiguration](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md") to automatically configure GuardDuty
  and its optional protection plans for the organization. When you run [CreateMembers](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md") to add new member accounts in your organization, the
  configured settings will apply automatically. When you run
  CreateMembers with an existing member account, the
  organization configuration will also apply to the existing members. This might
  change the current configuration of the existing member accounts.

To view all the accounts in your organization, run [ListAccounts](../../../organizations/latest/APIReference/API_ListAccounts.md "../../../organizations/latest/APIReference/API_ListAccounts.md") in the _AWS Organizations API Reference_.

###### To maintain the configuration status for member accounts individually in each

Region

- To view all the accounts in your organization, run [ListAccounts](../../../organizations/latest/APIReference/API_ListAccounts.md "../../../organizations/latest/APIReference/API_ListAccounts.md") in the _AWS Organizations API Reference_.
- When you want selective member accounts to have a different configuration
  status, run [UpdateMemberDetectors](../APIReference/API_UpdateMemberDetectors.md "../APIReference/API_UpdateMemberDetectors.md") for each member account individually.

You can use GuardDuty console to perform the same task by navigating to the
**Accounts** page in the GuardDuty console.

For information about enabling protection plans for individual accounts by
using either console or API, see the configuring page for the corresponding
protection plan.
