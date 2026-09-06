

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Deleting a resource data sync for Compliance
<a name="systems-manager-compliance-delete-RDS"></a>

If you no longer want to use AWS Systems Manager Compliance to view compliance data, we recommend deleting resource data syncs used for Compliance data collection.

**To delete a Compliance resource data sync**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Fleet Manager**.

1. Choose **Account management**, **Resource data syncs**.

1. Choose a sync in the list. 
**Important**  
Make sure you choose the sync used for Compliance. Systems Manager supports resource data sync for multiple tools. If you choose the wrong sync, you could disrupt data aggregation for Systems Manager Explorer or Systems Manager Inventory.

1. Choose **Delete**.

1. Delete the Amazon Simple Storage Service (Amazon S3) bucket where the data was stored. For information about deleting an S3 bucket, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html).