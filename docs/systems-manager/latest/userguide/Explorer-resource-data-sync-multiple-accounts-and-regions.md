# Understanding multiple account and Region resource data syncs

This section describes important details about multiple account and multiple
Region resource data syncs that use AWS Organizations. Specifically, the information in
this section applies if you choose one of the following options in the
**Create resource data sync** page:

- Include all accounts from my AWS Organizations configuration
- Select organization units in AWS Organizations
  If you don't plan to use one of these options, you can skip this
  section.

When you create a resource data sync in the SSM console, if you choose one
of the AWS Organizations options, then Systems Manager automatically allows all OpsData sources in
the selected Regions for all AWS accounts in your organization (or in the
selected organizational units). For example, even if you haven't turned Explorer
on in a Region, if you select an AWS Organizations option for your resource data sync,
then Systems Manager automatically collects OpsData from that Region. To create a resource
data sync without allowing OpsData sources, specify
**EnableAllOpsDataSources** as false when creating the data
sync. For more information, see the `EnableAllOpsDataSources`
parameter details for the [ResourceDataSyncSource](../APIReference/API_ResourceDataSyncSource.md "../APIReference/API_ResourceDataSyncSource.md") data type in the
_Amazon EC2 Systems Manager API Reference_.

If you don't choose one of the AWS Organizations options for a resource data sync, then
you must complete Integrated Setup in each account and Region where you want
Explorer to access data. If you don't, Explorer won't display OpsData and OpsItems
for those accounts and Regions in which you didn't complete Integrated
Setup.

If you add a child account to your organization, Explorer automatically allows
all OpsData sources for the account. If, at a later time, you remove the child
account from your organization, Explorer continues to collect OpsData from the
account.

If you update an existing resource data sync that uses one of the AWS Organizations
options, the system prompts you to approve collection of all OpsData sources for
all accounts and Regions affected by the change.

If you add a new service to your AWS account, and if Explorer collects
OpsData for that service, Systems Manager automatically configures Explorer to collect
that OpsData. For example, if your organization didn't use AWS Trusted Advisor when
you previously created a resource data sync, but your organization signs up for
this service, Explorer automatically updates your resource data syncs to collect
this OpsData.

###### Important

Note the following important information about multiple account and Region
resource data syncs:

- Deleting a resource data sync doesn't turn off an OpsData source
  in Explorer.
- To view OpsData and OpsItems from multiple accounts, you must have
  the AWS Organizations **All features** mode turned on and
  you must be signed into the AWS Organizations management account.
- Most AWS Regions are active by default for your AWS account,
  but certain Regions are activated only when you manually select
  them. These Regions are known as [opt-in Regions](../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status "../../../global-infrastructure/latest/regions/aws-regions.md#regions-opt-in-status"). By default, Explorer
  cross-account/cross-Region resource data syncs don't support data
  aggregation in opt-in Regions. Support was added for the following
  opt-in Regions on June 30, 2025.

      + Europe (Milan)
      + Africa (Cape Town)
      + Middle East (Bahrain)
      + Asia Pacific (Hong Kong)

  Note that you can't use a delegated administrator account to
  create a resource data sync in opt-in Regions. You must use an
  AWS Organizations management account.
