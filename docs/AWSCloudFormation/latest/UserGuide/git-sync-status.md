# Git sync status dashboard

To view the status of a AWS CloudFormation Git sync deployment, select the stack in the CloudFormation
 console and choose the **Git sync** tab.

The Git sync tab is divided into two panels, **Git sync status** and
 **Latest sync
 events**.


## Git sync status


The top panel provides the following information about the Git sync configuration for
 the stack.




****Repository****

 A link to the repository that is connected to Git sync



****Repository provider****

The name of the repository provider



****Branch****

The name of the branch that Git sync is monitoring



****Deployment file path****

The full path to the stack deployment file for this stack



****Repository sync status****

The status of the most recent sync operation



****Repository sync status message****

The message of the most recent sync operation



****Git sync status****

The status of Git sync for this stack



****Provisioning status****

The status of the provisioning operation




In the upper-right of the panel, use the following buttons to modify or update
 Git sync:



* **Edit** - Edit the Git sync configuration.
* **Retry latest commit** - Update the stack according to the
 most recent commit to the repository.
* **Disconnect** - Disconnect Git sync from the stack.
* **Refresh** - Refresh the Git sync status panel.

## Latest sync events


The **Latest sync events** panel displays a table of commits that
 have been applied to the stack.


You can sort the table using the arrows in the header of each column. The table can be
 sorted in ascending or descending order according to the following:



* **Date**
* **Commit ID**
* **Event**
* **Date**
* **Event Type**

## Supported stack states


Git sync can only be configured for a stack if the stack is in one of the following
 supported states:



* `CREATE_COMPLETE`
* `UPDATE_COMPLETE`
* `UPDATE_ROLLBACK_COMPLETE`
* `IMPORT_COMPLETE`
* `IMPORT_ROLLBACK_COMPLETE`

The following table contains a complete list of stack status codes with
 descriptions:




| Stack status and optional detailed status | Description |
| --- | --- |
| `CREATE_COMPLETE` | Successful creation of one or more stacks. |
| `CREATE_IN_PROGRESS` | Ongoing creation of one or more stacks. |
| `CREATE_FAILED` | Unsuccessful creation of one or more stacks. View the stack events to see any associated error messages.
 Possible reasons for a failed creation include insufficient permissions to work with all resources in the stack,
 parameter values rejected by an AWS service, or a timeout during resource creation. |
| `DELETE_COMPLETE` | Successful deletion of one or more stacks. Deleted stacks are retained and viewable for 90 days. |
| `DELETE_FAILED` | Unsuccessful deletion of one or more stacks. Because the delete failed, you might have some resources that
 are still running; however, you can't work with or update the stack. Delete the stack again or view the stack
 events to see any associated error messages. |
| `DELETE_IN_PROGRESS` | Ongoing removal of one or more stacks. |
| `REVIEW_IN_PROGRESS` | Ongoing creation of one or more stacks with an expected `StackId` but without any templates or resources.ImportantA stack with this status code counts against the [maximum possible
 number of stacks](cloudformation-limits.md "cloudformation-limits.md"). |
| `ROLLBACK_COMPLETE` | Successful removal of one or more stacks after a failed stack creation or after an explicitly canceled stack
 creation. The stack returns to the previous working state. Any resources that were created during the create stack
 operation are deleted.
This status exists only after a failed stack creation. It signifies that all operations from the partially
 created stack have been appropriately cleaned up. When in this state, only a delete operation can be
 performed. |
| `ROLLBACK_FAILED` | Unsuccessful removal of one or more stacks after a failed stack creation or after an explicitly canceled
 stack creation. Delete the stack or view the stack events to see any associated error messages. |
| `ROLLBACK_IN_PROGRESS` | Ongoing removal of one or more stacks after a failed stack creation or after an explicitly canceled stack
 creation. |
| `UPDATE_COMPLETE` | Successful update of one or more stacks. |
| `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS` | Ongoing removal of old resources for one or more stacks after a successful stack update. For stack updates
 that require resources to be replaced, CloudFormation creates the new resources first and then deletes the old
 resources to help reduce any interruptions with your stack. In this state, the stack has been updated and is
 usable, but CloudFormation is still deleting the old resources. |
| `UPDATE_FAILED` | Unsuccessful update of one or more stacks. View the stack events to see any associated error
 messages. |
| `UPDATE_IN_PROGRESS` | Ongoing update of one or more stacks. |
| `UPDATE_ROLLBACK_COMPLETE` | Successful return of one or more stacks to a previous working state after a failed stack update. |
| `UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS` | Ongoing removal of new resources for one or more stacks after a failed stack update. In this state, the stack
 has been rolled back to its previous working state and is usable, but CloudFormation is still deleting any new
 resources it created during the stack update. |
| `UPDATE_ROLLBACK_FAILED` | Unsuccessful return of one or more stacks to a previous working state after a failed stack update. When in
 this state, you can delete the stack or [continue
 rollback](using-cfn-updating-stacks-continueupdaterollback.md "using-cfn-updating-stacks-continueupdaterollback.md"). You might need to fix errors before your stack can return to a working state. Or, you can
 contact Support to restore the stack to a usable state. |
| `UPDATE_ROLLBACK_IN_PROGRESS` | Ongoing return of one or more stacks to the previous working state after failed stack update. |
| `IMPORT_IN_PROGRESS` | The import operation is currently in progress. |
| `IMPORT_COMPLETE` | The import operation successfully completed for all resources in the stack that support `resource
 import`. |
| `IMPORT_ROLLBACK_IN_PROGRESS` | Import will roll back to the previous template configuration. |
| `IMPORT_ROLLBACK_FAILED` | The import rollback operation failed for at least one resource in the stack. Results will be available for
 the resources CloudFormation successfully imported. |
| `IMPORT_ROLLBACK_COMPLETE` | Import successfully rolled back to the previous template configuration. |
