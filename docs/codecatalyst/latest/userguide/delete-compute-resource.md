Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a provisioned fleet

Use the following instructions to delete a provisioned fleet.

###### To delete a provisioned fleet

###### Warning

Before deleting a provisioned fleet, remove it from all actions by deleting
the `Fleet` property from the action's YAML code. Any action that
continues to reference a provisioned fleet after it is deleted will fail the
next time the action runs.

1. In the navigation pane, choose **CI/CD**, and then choose **Compute**.
2. In the **Provisioned fleet** list, choose the fleet you want
   to delete.
3. Choose **Delete**.
4. Enter `delete` to confirm the deletion.
5. Choose **Delete**.
