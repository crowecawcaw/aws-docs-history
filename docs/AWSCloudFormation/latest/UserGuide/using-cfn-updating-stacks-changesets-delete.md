# Delete a change set for a CloudFormation stack

Deleting a change set removes it from the list of change sets for the stack. Deleting a
 change set prevents you or another user from accidentally executing a change set that
 shouldn't be applied. Unless you delete them, CloudFormation retains all change sets until you
 update the stack.


Delete a change set
###### To delete a change set (console)

1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, select the name of the stack that
 contains the change set that you want to delete.
4. In the navigation pane, choose **Change sets** to view a list
 of the stack's change sets.
5. Select the name of the change set that you want to delete.
6. On the change set's details page, choose **Delete change
 set**.


CloudFormation immediately starts to delete the change set from the stack's list of
 change sets, and you're redirected to the **Stacks** page.


Delete a change set for nested stacks (console)
###### To delete a change set for nested stacks

1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, select the stack name associated with
 the root change set.
4. In the navigation pane, choose **Change sets** to view a list
 of the stack's change sets.
5. Select the name of the change set that you want to delete.
6. On the change set's details page, choose **Delete**. By
 choosing **Delete change set**, you will delete the whole hierarchy
 of nested change sets.


###### Note

The delete operation for change sets for nested stacks is asynchronous and
 will show a `DELETE_PENDING` status, followed by a
 `DELETE_IN_PROGRESS` status. Upon completion of the delete change set
 operation, the change sets will be removed from the list. Nested stacks in the
 `REVIEW_IN_PROGRESS` status will also be deleted if they were created
 during the change set creation.


CloudFormation immediately starts to delete the change set from the stack's list of
 change sets.


###### Note

If you have nested stacks that are stuck in an in-progress operation, see
 Troubleshooting Errors in [Nested
 stacks rollback failure](troubleshooting.md#troubleshooting-errors-nested-stacks-are-stuck "troubleshooting.md#troubleshooting-errors-nested-stacks-are-stuck").


###### To delete a change set (AWS CLI)

* Run the [delete-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/delete-change-set.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/delete-change-set.html") command, specifying the ID of the change set
 that you want to delete, as shown in the following example:



```
aws cloudformation delete-change-set \
    --change-set-name \
      `arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000`
```
