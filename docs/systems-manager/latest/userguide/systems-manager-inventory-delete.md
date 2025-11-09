AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Stopping data collection and deleting

inventory data

If you no longer want to use AWS Systems Manager Inventory to view metadata about your AWS
resources, you can stop data collection and delete data that has already been collected.
This section includes the following information.

###### Topics

- [Stopping data
  collection](#systems-manager-inventory-delete-association "#systems-manager-inventory-delete-association")
- [Deleting an Inventory
  resource data sync](#systems-manager-inventory-delete-RDS "#systems-manager-inventory-delete-RDS")

## Stopping data

collection

When you initially configure Systems Manager to collect inventory data, the system creates a
State Manager association that defines the schedule and the resources from which to
collect metadata. You can stop data collection by deleting any State Manager associations
that use the `AWS-GatherSoftwareInventory` document.

###### To delete an Inventory association

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **State Manager**.
3. Choose an association that uses the
   `AWS-GatherSoftwareInventory` document and then choose
   **Delete**.
4. Repeat step three for any remaining associations that use the
   `AWS-GatherSoftwareInventory` document.

## Deleting an Inventory

resource data sync

If you no longer want to use AWS Systems Manager Inventory to view metadata about your AWS
resources, then we also recommend deleting resource data syncs used for inventory
data collection.

###### To delete an Inventory resource data sync

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Inventory**.
3. Choose **Resource Data Syncs**.
4. Choose a sync in the list.

###### Important

Make sure you choose the sync used for Inventory. Systems Manager supports
resource data sync for multiple tools. If you choose the wrong sync, you
could disrupt data aggregation for Systems Manager Explorer or Systems Manager Compliance. 5. Choose **Delete** 6. Repeat these steps for any remaining resource data syncs you want to
delete. 7. Delete the Amazon Simple Storage Service (Amazon S3) bucket where the data was stored. For
information about deleting an Amazon S3 bucket, see [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md").
