# Execute a change set for a CloudFormation stack

To make the changes described in a change set to your stack, execute the change
 set.

###### Important

After you execute a change set, CloudFormation deletes any additional change sets that are
 associated with the stack because they're no longer valid for the updated stack. If an
 update fails, you need to create a new change set.


###### Stack Policies and Executing a
 Change Set


If you execute a change set on a stack that has a stack policy associated with it,
 CloudFormation enforces the policy when it updates the stack. You can't specify a temporary
 stack policy that overrides the existing policy when you execute a change set. To update a
 protected resource, you must update the stack policy or use the direct update method. For
 more information, see [Update stacks directly](using-cfn-updating-stacks-direct.md "using-cfn-updating-stacks-direct.md").



Execute a change set (console)
###### To execute a change set

1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, choose the name the stack that you want
 to update.
4. In the navigation pane, choose **Change sets** to view a list
 of the stack's change sets.
5. Choose the name of the change set that you want to execute.
6. On the change set's details page, choose **Execute change
 set**.


CloudFormation immediately starts updating the stack. The CloudFormation console directs
 you to the **Events** tab, where you can monitor the progress of
 the stack update. For more information, see [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md").


Execute a change set for nested stacks (console)
###### To execute a change set for nested stacks

1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, choose the name the stack that you want
 to update. You must choose the stack name associated with the root change
 set.
4. In the navigation pane, choose **Change sets** to view a list
 of the stack's change sets.
5. Choose the name of the root change set that you want to execute.
6. On the change set's details page, choose **Execute change
 set**.


###### Note

CloudFormation executes the changes described in your root change set and nested
 change sets, if **Enabled** for change sets for nested stacks was
 selected during the [Create a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-create.md "using-cfn-updating-stacks-changesets-create.md") process.


CloudFormation immediately starts updating the stack. The CloudFormation console directs
 you to the **Events** tab, where you can monitor the progress of
 the stack update. For more information, see [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md").


###### To execute a change set (AWS CLI)

* Run the [execute-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/execute-change-set.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/execute-change-set.html") command.


Specify the change set ID of the change set that you want to execute, as shown in the
 following example:



```
aws cloudformation execute-change-set \
    --change-set-name \
      `arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000`
```

The command in the example executes a change set with the ID
 `arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000`.


After you run the command, CloudFormation starts updating the stack. To view the stack's
 progress, use the [describe-stacks](service_code_examples.md#describe-stacks-sdk "service_code_examples.md#describe-stacks-sdk")
 command.
