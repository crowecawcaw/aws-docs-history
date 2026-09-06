

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Understanding resource data syncs for Explorer
<a name="Explorer-resource-data-sync-understanding"></a>

Resource data sync for Explorer offers two aggregation options:
+ **Single-account/Multiple-regions:** You can configure Explorer to aggregate OpsItems and OpsData data from multiple AWS Regions, but the data set is limited to the current AWS account.
+ **Multiple-accounts/Multiple-regions:** You can configure Explorer to aggregate data from multiple AWS Regions and accounts. This option requires that you set up and configure AWS Organizations. After you set up and configure AWS Organizations, you can aggregate data in Explorer by organizational unit (OU) or for an entire organization. Systems Manager aggregates the data into the AWS Organizations management account before displaying it in Explorer. For more information, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/) in the *AWS Organizations User Guide*.

**Warning**  
If you configure Explorer to aggregate data from an organization in AWS Organizations, the system enables OpsData in all member accounts in the organization. Enabling OpsData sources in all member accounts increases the number of calls to OpsCenter APIs like [CreateOpsItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateOpsItem.html) and [GetOpsSummary](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsSummary.html). You are charged for calls to these API actions.

The following diagram shows a resource data sync configured to work with AWS Organizations. In this scenario, the user has two accounts defined in AWS Organizations. Resource data sync aggregates data from both accounts and multiple AWS Regions into the AWS Organizations management account where it's then displayed in Explorer.

![Resource data sync for Systems Manager Explorer](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/ExplorerSyncFromSource.png)
