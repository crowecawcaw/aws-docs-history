# View stack information from the

CloudFormation console

After you've created a CloudFormation stack, you can use the AWS Management Console to view its data and
resources.

###### To view information about your CloudFormation stack

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region where the
   stack is located.
3. On the **Stacks** page, choose the stack name. CloudFormation displays
   the stack details for the selected stack.

###### Note

If the stack has been deleted, you can find it by using the **Filter
status** option. For more information, see [View deleted stacks from the CloudFormation
console](cfn-console-view-deleted-stacks.md "cfn-console-view-deleted-stacks.md").
You can view the following stack information:

**Stack info**

Displays general information about the stack and its configuration,
including:

Overview

Displays stack name, stack ID, root stack, and [IAM role](using-iam-servicerole.md "using-iam-servicerole.md"), along with status
information such as stack status, drift status, and termination
protection.

Tags

Displays any tags that are associated with the stack.

Stack policy

Describes the stack resources that are protected against stack updates.
For you to be able to update these resources, they must be explicitly
allowed during a stack update. For more information, see [Prevent updates to stack resources](protect-stack-resources.md "protect-stack-resources.md").

Rollback configuration

Displays any CloudWatch alarms that you have specified that CloudFormation should
monitor during the stack operation or the specified monitoring period. If
any of the alarms goes to `ALARM` state during the stack
operation or the monitoring period, CloudFormation rolls back the entire stack
operation. For more information, see [Roll back your CloudFormation stack on alarm
breach with rollback triggers](using-cfn-rollback-triggers.md "using-cfn-rollback-triggers.md").

Notification options

Displays the Amazon Simple Notification Service topic where notifications about stack events are
sent, if specified.

**Events**

Displays the operations that are tracked when you create, update, or delete the
stack. For more information, see [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md").

All events that are triggered by a given stack operation are assigned the same
client request token, which you can use to track operations. Stack operations that
are initiated from the console use the token format
_Console-StackOperation-ID_, which helps you to easily identify
the stack operation. For example, if you create a stack using the console, each
resulting stack event would be assigned the same token in the following format:
`Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.

**Resources**

Displays the resources that are part of the stack.

**Outputs**

Displays outputs that were declared in the stack's template. For more information,
see [Get exported outputs from a deployed CloudFormation
stack](using-cfn-stack-exports.md "using-cfn-stack-exports.md").

**Parameters**

Displays the stack's parameters and their values.

For stacks that contain Systems Manager parameters, the **Resolved Value**
column displays the values that are used in the stack definition for the Systems Manager
parameters. For more information, see [Specify existing resources at
runtime with CloudFormation-supplied parameter types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").

**Template**

Displays the stack's template.

For stacks that contain macros, choose **View original template**
to view the user-submitted template, or **View processed template**
to view the template after CloudFormation processes the referenced macros. CloudFormation
uses the processed template to create or update your stack.

**Change sets**

Displays the stack's change sets.

For more information, see [View a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md "using-cfn-updating-stacks-changesets-view.md").

**Git sync**

Displays the stack's Git sync dashboard.

For more information, see [Git sync status dashboard](git-sync-status.md "git-sync-status.md").
