

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Configuring a delegated administrator for Explorer
<a name="Explorer-setup-delegated-administrator"></a>

If you aggregate AWS Systems Manager Explorer data from multiple AWS Regions and accounts by using resource data sync with AWS Organizations, then we recommend that you configure a delegated administrator for Explorer. A delegated administrator improves Explorer security in the following ways.
+ You limit the number of Explorer administrators who can create or delete multi-account and Region resource data syncs to an individual AWS account.
+ You no longer need to be logged into the AWS Organizations management account to administer resource data syncs in Explorer.

A delegated administrator can use the following Explorer resource data sync APIs using the console, SDK, AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell: 
+ [CreateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateResourceDataSync.html)
+ [DeleteResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourceDataSync.html)
+ [ListResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceDataSync.html)
+ [UpdateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateResourceDataSync.html)

A delegated administrator can search, filter, and aggregate Explorer data from the console or by using programmatic tools such as the SDK, the AWS CLI, or AWS Tools for Windows PowerShell. Search, filter, and data aggregation use the [GetOpsSummary](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsSummary.html) API operation.

A delegated administrator can create a maximum of five resource data syncs for either an entire organization or a subset of organizational units. Resource data syncs created by a delegated administrator are only available in the delegated administrator account. You can't view the syncs or the aggregated data in the AWS Organizations management account.

**Note**  
You can't use a delegated administrator account to create a resource data sync in [opt-in AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#regions-opt-in-status). You must use an AWS Organizations management account.

For more information about resource data sync, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](Explorer-resource-data-sync.md). For more information about AWS Organizations, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/) in the *AWS Organizations User Guide*.

**Topics**
+ [Before you begin](#Explorer-setup-delegated-administrator-before-you-begin)
+ [Configure an Explorer delegated administrator](Explorer-setup-delegated-administrator-configure.md)
+ [Deregister an Explorer delegated administrator](Explorer-setup-delegated-administrator-deregister.md)

## Before you begin
<a name="Explorer-setup-delegated-administrator-before-you-begin"></a>

The following list includes important information about Explorer delegated administration.
+ You can delegate only one account for Explorer administration.
+ The account ID that you specify as an Explorer delegated administrator must be listed as a member account in AWS Organizations. For more information, see [Creating an AWS account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) in the *AWS Organizations User Guide*.
+ A delegated administrator can use all Explorer resource data sync API operations in the console or by using programmatic tools such as the SDK, the AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell. Resource data sync API operations include the following: [CreateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateResourceDataSync.html), [DeleteResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourceDataSync.html), [ListResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceDataSync.html), and [UpdateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateResourceDataSync.html).
+ A delegated administrator can search, filter, and aggregate Explorer data in the console or by using programmatic tools such as the SDK, the AWS CLI, or AWS Tools for Windows PowerShell. Search, filter, and data aggregation use the [GetOpsSummary](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsSummary.html) API operation.
+ Resource data syncs created by a delegated administrator are only available in the delegated administrator account. You can't view the syncs or the aggregated data in the AWS Organizations management account.
+ A delegated administrator can create a maximum of five resource data syncs.
+ A delegated administrator can create a resource data sync for either an entire organization in AWS Organizations or a subset of organizational units.