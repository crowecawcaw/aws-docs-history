# Delete a stack from the CloudFormation console

If you no longer need the resources in a stack, you can delete the entire stack.

When deleting a stack, CloudFormation deletes all resources in that stack unless you used a
deletion policy to retain specific resources. For more information, see [DeletionPolicy attribute](../TemplateReference/aws-attribute-deletionpolicy.md "../TemplateReference/aws-attribute-deletionpolicy.md").

###### To delete a stack (console)

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region where the
   stack is located.
3. On the **Stacks** page, choose the stack that you want to delete.
   The stack must be currently running.
4. Choose **Delete**.
5. When prompted for confirmation, choose **Delete**.

###### Note

The stack deletion operation can't be stopped once the stack deletion has begun.
The stack proceeds to the `DELETE_IN_PROGRESS` state.

After the stack deletion is complete, the stack will be in the
`DELETE_COMPLETE` state. Stacks in the `DELETE_COMPLETE`
state aren't displayed in the CloudFormation console by default. To display deleted
stacks, you must change the stack view filter as described in [View deleted stacks from the CloudFormation
console](cfn-console-view-deleted-stacks.md "cfn-console-view-deleted-stacks.md").

###### To force delete a stack (console)

A stack deletion might fail because a resource in the stack fails to delete. For
example, CloudFormation will fail the deletion of a resource that another stack also depends
on. Any resources that haven't been deleted will remain until you can successfully delete
the stack. If the deletion fails and returns a `DELETE_FAILED` state, you can
choose to retry using one of two methods.

1. On the **Stacks** page in the CloudFormation console, choose the stack
   that you want to force delete.
2. In the stack details pane, choose **Retry delete**.
3. Choose between the following options:
   - **Delete this stack but retain resources**: This option allows
     you to select the specific resources that originally failed to delete, but you
     want to retain during the force stack deletion.
   - **Force delete this entire stack**: This option retains all resources that failed
     to delete, and retains dependencies of those resources.

4. Choose **Delete** to begin the force delete process with your
   selections.

###### To review retained resources (console)

After deleting the stack, you can view the resources that were retained in the
console.

1. In the stacks list, choose the **Filter status** and select
   **Deleted**.
2. Choose the deleted stack.
3. Choose the **Resources** tab.
4. All retained resources show the `DELETE_SKIPPED`
   **Status**.
5. Choose the retained resource you want to review.

###### To delete a stack using the command line

You can use one of the following commands:

- [delete-stack](../../../cli/latest/reference/cloudformation/delete-stack.md "../../../cli/latest/reference/cloudformation/delete-stack.md") (AWS CLI)
- [Remove-CFNStack](../../../powershell/latest/reference/items/Remove-CFNStack.md "../../../powershell/latest/reference/items/Remove-CFNStack.md") (AWS Tools for Windows PowerShell)
  For examples of using the command line to delete a stack, see [Examples of CloudFormation stack operation commands for
  the AWS CLI and PowerShell](service_code_examples.md "service_code_examples.md").

## Related resources

For help troubleshooting stack deletion errors, see the [Delete stack
fails](troubleshooting.md#troubleshooting-errors-delete-stack-fails "troubleshooting.md#troubleshooting-errors-delete-stack-fails") troubleshooting
topic.

For information on protecting stacks from being accidentally deleted, see [Protect CloudFormation stacks from being
deleted](using-cfn-protect-stacks.md "using-cfn-protect-stacks.md").
