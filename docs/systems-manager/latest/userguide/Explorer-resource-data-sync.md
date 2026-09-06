

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up Systems Manager Explorer to display data from multiple accounts and Regions
<a name="Explorer-resource-data-sync"></a>

AWS Systems Manager uses an integrated setup experience to help you get started with AWS Systems Manager Explorer *and* AWS Systems Manager OpsCenter. After completing Integrated Setup, Explorer and OpsCenter automatically synchronize data. More specifically, these tools synchronize OpsData and OpsItems for the AWS account and AWS Region you used when you completed Integrated Setup. If you want to aggregate OpsData and OpsItems from other accounts and Regions, you must create a resource data sync, as described in this topic.

**Note**  
For more information about Integrated Setup, see [Getting started with Systems Manager Explorer and OpsCenter](Explorer-setup.md).

**Topics**
+ [Understanding resource data syncs for Explorer](Explorer-resource-data-sync-understanding.md)
+ [Understanding multiple account and Region resource data syncs](Explorer-resource-data-sync-multiple-accounts-and-regions.md)
+ [Creating a resource data sync](Explorer-resource-data-sync-configuring-multi.md)