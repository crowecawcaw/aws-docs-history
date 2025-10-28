# Deleting a resource data sync

for Compliance

If you no longer want to use AWS Systems Manager Compliance to view compliance data, then we
also recommend deleting resource data syncs used for Compliance data collection.

###### To delete a Compliance resource data sync

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose **Account management**, **Resource data
   syncs**.
4. Choose a sync in the list.

###### Important

Make sure you choose the sync used for Compliance. Systems Manager supports resource
data sync for multiple tools. If you choose the wrong sync, you could
disrupt data aggregation for Systems Manager Explorer or Systems Manager Inventory. 5. Choose **Delete**. 6. Delete the Amazon Simple Storage Service (Amazon S3) bucket where the data was stored. For information
about deleting an S3 bucket, see [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md").
