# Troubleshooting Quick Setup

results

Use the following information to help you troubleshoot problems with Quick Setup, a tool
in AWS Systems Manager. This topic includes specific tasks to resolve issues based on the type of
Quick Setup issue.

**Issue: Failed deployment**

A deployment fails if the CloudFormation stack set failed during creation.
Use the following steps to investigate a deployment failure.

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
2. Choose the stack created by your Quick Setup configuration. The
   **Stack name** includes `QuickSetup`
   followed by the type of configuration you chose, such as
   `SSMHostMgmt`.

###### Note

CloudFormation sometimes deletes failed stack deployments. If the
stack isn't available in the **Stacks** table,
choose **Deleted** from the filter list. 3. View the **Status** and **Status
reason**. For more information about stack statuses,
see [Stack status codes](../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md#cfn-console-view-stack-data-resources-status-codes "../../../AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.md#cfn-console-view-stack-data-resources-status-codes") in the _AWS CloudFormation User Guide_. 4. To understand the exact step that failed, view the
**Events** tab and review each event's
**Status**. 5. Review [Troubleshooting](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md") in the _AWS CloudFormation User Guide_. 6. If you are unable to resolve the deployment failure using the
CloudFormation troubleshooting steps, delete the configuration and
reconfigure it.

**Issue: Failed association**

The **Configuration details** table on the
**Configuration details** page of your
configuration shows a **Configuration status** of
**Failed** if any of the associations failed during
set up. Use the following steps to troubleshoot a failed
association.

1. In the **Configuration details** table, choose
   the failed configuration and then choose **View
   Details**.
2. Copy the **Association name**.
3. Navigate to **State Manager** and paste the
   association name into the search field.
4. Choose the association and choose the **Execution
   history** tab.
5. Under **Execution ID**, choose the association
   execution that failed.
6. The **Association execution targets** page lists
   all of the nodes where the association ran. Choose the
   **Output** button for an execution that failed
   to run.
7. In the **Output** page, choose **Step -
   Output** to view the error message for that step in the
   command execution. Each step can display a different error message.
   Review the error messages for all steps to help troubleshoot the
   issue.

If viewing the step output doesn't solve the problem, then you can try to
recreate the association. To recreate the association, first delete the
failing association in State Manager. After deleting the association, edit the
configuration and choose the option you deleted and choose
**Update**.

###### Note

To investigate **Failed** associations for an
**Organization** configuration, you must sign in to
the account with the failed association and use the following failed
association procedure, previously described. The **Association
ID** isn't a hyperlink to the target account when viewing
results from the management account.

**Issue: Drift status**

When viewing a configuration's details page, you can view the drift
status of each deployment. Configuration drift occurs whenever a user
makes any change to a service or feature that conflicts with the
selections made through Quick Setup. If an association has changed after
the initial configuration, the table displays a warning icon that
indicates the number of items that have drifted. You can determine what
caused the drift by hovering over the icon.

When an association is deleted in State Manager, the related deployments
display a drift warning. To fix this, edit the configuration and choose the
option that was removed when the association was deleted. Choose
**Update** and wait for the deployment to
complete.
