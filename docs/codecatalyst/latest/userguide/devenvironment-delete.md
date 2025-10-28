Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a Dev Environment

When you have finished working on the content that is stored in your Dev Environment, you can
delete the Dev Environment. Create a new Dev Environment to work on new content. If you delete your
Dev Environment, the persisted content will be permanently deleted. Before you delete your
Dev Environment, make sure you commit and push your code changes to the Dev Environment's original
source repository. After you have deleted your Dev Environment, compute and storage billing for
the Dev Environment will stop.

After you delete your Dev Environment, it may take a few minutes for the storage quota to be updated.
If you've reached the storage quota, you will be unable to create a new Dev Environment during this time.

###### Important

Deleting a Dev Environment cannot be undone. After you delete a Dev Environment,
you are no longer able to recover it.

###### To delete a Dev Environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to delete a Dev Environment.
3. In the navigation pane, choose **Code**.
4. Choose **Dev Environments**.
5. Choose the Dev Environment you want to delete.
6. Choose **Delete**.
7. Enter `delete` to confirm the Dev Environment deletion.
8. Choose **Delete**.

###### Note

Before deleting a VPC connection in your space, make sure to remove the Dev Environment associated to that VPC.

Even if you delete a Dev Environment, you might not delete the network interface in the VPC. Make sure to clean up your resources as needed. If an error occurs when you
delete a VPC-connected Dev Environment, you must [detach](../../../AWSEC2/latest/UserGuide/using-eni.md#detach_eni "../../../AWSEC2/latest/UserGuide/using-eni.md#detach_eni") your
stale connection, and [delete](../../../AWSEC2/latest/UserGuide/using-eni.md#delete_eni "../../../AWSEC2/latest/UserGuide/using-eni.md#delete_eni") it after
confirming that it's not being used.
