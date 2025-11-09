AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configuring a delegated

administrator for Explorer

If you aggregate AWS Systems Manager Explorer data from multiple AWS Regions and accounts by using
resource data sync with AWS Organizations, then we recommend that you configure a delegated
administrator for Explorer. A delegated administrator improves Explorer security in
the following ways.

- You limit the number of Explorer administrators who can create or delete
  multi-account and Region resource data syncs to an individual
  AWS account.
- You no longer need to be logged into the AWS Organizations management account to
  administer resource data syncs in Explorer.
  A delegated administrator can use the following Explorer resource data sync APIs
  using the console, SDK, AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell:

- [CreateResourceDataSync](../APIReference/API_CreateResourceDataSync.md "../APIReference/API_CreateResourceDataSync.md")
- [DeleteResourceDataSync](../APIReference/API_DeleteResourceDataSync.md "../APIReference/API_DeleteResourceDataSync.md")
- [ListResourceDataSync](../APIReference/API_ListResourceDataSync.md "../APIReference/API_ListResourceDataSync.md")
- [UpdateResourceDataSync](../APIReference/API_UpdateResourceDataSync.md "../APIReference/API_UpdateResourceDataSync.md")
  A delegated administrator can search, filter, and aggregate Explorer data from the
  console or by using programmatic tools such as the SDK, the AWS CLI, or AWS Tools for Windows PowerShell.
  Search, filter, and data aggregation use the [GetOpsSummary](../APIReference/API_GetOpsSummary.md "../APIReference/API_GetOpsSummary.md") API
  operation.

A delegated administrator can create a maximum of five resource data syncs for
either an entire organization or a subset of organizational units. Resource data
syncs created by a delegated administrator are only available in the delegated
administrator account. You can't view the syncs or the aggregated data in the
AWS Organizations management account.

###### Note

You can't use a delegated administrator account to create a resource data sync
in [opt-in AWS Regions](../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status "../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status"). You must use an AWS Organizations management
account.

For more information about resource data sync, see [Setting up Systems Manager Explorer to display data from
multiple accounts and Regions](Explorer-resource-data-sync.md "Explorer-resource-data-sync.md"). For more information about
AWS Organizations, see [What is AWS Organizations?](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md") in the
_AWS Organizations User Guide_.

###### Topics

- [Before
  you begin](#Explorer-setup-delegated-administrator-before-you-begin "#Explorer-setup-delegated-administrator-before-you-begin")
- [Configure
  an Explorer delegated administrator](Explorer-setup-delegated-administrator-configure.md "Explorer-setup-delegated-administrator-configure.md")
- [Deregister
  an Explorer delegated administrator](Explorer-setup-delegated-administrator-deregister.md "Explorer-setup-delegated-administrator-deregister.md")

## Before

you begin

The following list includes important information about Explorer delegated
administration.

- You can delegate only one account for Explorer administration.
- The account ID that you specify as an Explorer delegated administrator
  must be listed as a member account in AWS Organizations. For more information,
  see [Creating
  an AWS account in your organization](../../../organizations/latest/userguide/orgs_manage_accounts_create.md "../../../organizations/latest/userguide/orgs_manage_accounts_create.md") in the
  _AWS Organizations User Guide_.
- A delegated administrator can use all Explorer resource data sync API
  operations in the console or by using programmatic tools such as the
  SDK, the AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell. Resource data sync API
  operations include the following: [CreateResourceDataSync](../APIReference/API_CreateResourceDataSync.md "../APIReference/API_CreateResourceDataSync.md"), [DeleteResourceDataSync](../APIReference/API_DeleteResourceDataSync.md "../APIReference/API_DeleteResourceDataSync.md"), [ListResourceDataSync](../APIReference/API_ListResourceDataSync.md "../APIReference/API_ListResourceDataSync.md"), and [UpdateResourceDataSync](../APIReference/API_UpdateResourceDataSync.md "../APIReference/API_UpdateResourceDataSync.md").
- A delegated administrator can search, filter, and aggregate Explorer
  data in the console or by using programmatic tools such as the SDK, the
  AWS CLI, or AWS Tools for Windows PowerShell. Search, filter, and data aggregation use the [GetOpsSummary](../APIReference/API_GetOpsSummary.md "../APIReference/API_GetOpsSummary.md") API
  operation.
- Resource data syncs created by a delegated administrator are only
  available in the delegated administrator account. You can't view the
  syncs or the aggregated data in the AWS Organizations management account.
- A delegated administrator can create a maximum of five resource data
  syncs.
- A delegated administrator can create a resource data sync for either
  an entire organization in AWS Organizations or a subset of organizational
  units.
