

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deleting a Dev Environment
<a name="devenvironment-delete"></a>

When you have finished working on the content that is stored in your Dev Environment, you can delete the Dev Environment. Create a new Dev Environment to work on new content. If you delete your Dev Environment, the persisted content will be permanently deleted. Before you delete your Dev Environment, make sure you commit and push your code changes to the Dev Environment's original source repository. After you have deleted your Dev Environment, compute and storage billing for the Dev Environment will stop.

After you delete your Dev Environment, it may take a few minutes for the storage quota to be updated. If you've reached the storage quota, you will be unable to create a new Dev Environment during this time.

**Important**  
Deleting a Dev Environment cannot be undone. After you delete a Dev Environment, you are no longer able to recover it.<a name="devenvironment-delete-steps"></a>

**To delete a Dev Environment**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to the project where you want to delete a Dev Environment.

1. In the navigation pane, choose **Code**.

1. Choose **Dev Environments**.

1. Choose the Dev Environment you want to delete.

1. Choose **Delete**.

1. Enter **delete** to confirm the Dev Environment deletion.

1. Choose **Delete**.

**Note**  
Before deleting a VPC connection in your space, make sure to remove the Dev Environment associated to that VPC.  
Even if you delete a Dev Environment, you might not delete the network interface in the VPC. Make sure to clean up your resources as needed. If an error occurs when you delete a VPC-connected Dev Environment, you must [detach](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#detach_eni) your stale connection, and [delete](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#delete_eni) it after confirming that it's not being used.