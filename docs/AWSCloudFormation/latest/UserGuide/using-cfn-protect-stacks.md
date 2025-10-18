# Protect CloudFormation stacks from being
 deleted

You can prevent a stack from being accidentally deleted by enabling termination protection
 on the stack. If a user attempts to delete a stack with termination protection enabled, the
 deletion fails and the stack, including its status, remains unchanged. You can enable
 termination protection on a stack when you create it. Termination protection on stacks is
 disabled by default. You can set termination protection on a stack with any status except
 `DELETE_IN_PROGRESS` or `DELETE_COMPLETE`.

Enabling or disabling termination protection on a stack passes the same choice on to any
 nested stacks belonging to that stack as well. You can't enable or disable termination
 protection directly on a nested stack. If a user attempts to directly delete a nested stack
 belonging with a stack that has termination protection enabled, the operation fails and the
 nested stack remains unchanged.

However, if a user performs a stack update that would delete the nested stack, AWS CloudFormation
 deletes the nested stack accordingly.

Termination protection is different than disabling rollback. Termination protection
 applies only to attempts to delete stacks, while disabling rollback applies to auto rollback
 when stack creation fails.


###### To enable termination protection when creating a stack


On the **Specify stack options** page of the **Create
 stack** wizard, under **Advanced options**, expand the
 **Termination Protection** section and select
 **Enable**. For more information, see [Configure stack options](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options").


###### To enable or disable termination protection on an existing stack

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. Select the stack that you want.


###### Note

If **NESTED** is displayed next to the stack name, the stack
 is a nested stack. You can only change termination protection on the root stack
 to which the nested stack belongs.
4. In the stack details pane, select **Stack actions** and then
 **Edit termination protection**.


CloudFormation displays the **Edit termination protection** dialog
 box.
5. Choose **Enable** or **Disable**, and then
 select **Save**.
###### To enable or disable termination protection on a nested stack

If **NESTED** is displayed next to the stack name, the stack is a
 nested stack. You can only change termination protection on the root stack to which the
 nested stack belongs. To change termination protection on the root stack:

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. Select the nested stack that you want.
4. In the **Stack info** pane, in the **Overview**
 section, select the stack name listed as **Root stack**.


CloudFormation displays the stack details for the root stack.
5. Choose **Stack actions** and then choose **Edit
 Termination Protection**.


CloudFormation displays the **Edit termination protection** dialog
 box.
6. Choose **Enable** or **Disable**, and then
 select **Save**.

###### To enable or disable termination protection using the command line


Use the [update-termination-protection](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-termination-protection.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-termination-protection.html") command.


## Controlling who can change termination protection
 on stacks


To enable or disable termination protection on stacks, a user requires permission to
 the `cloudformation:UpdateTerminationProtection` action. For example, the
 policy below allows users to enable or disable termination protection on stacks.


For more information on specifying permissions in AWS CloudFormation, see [Control CloudFormation access with AWS Identity and Access Management](control-access-with-iam.md "control-access-with-iam.md").


###### Example A sample policy that grants permissions to change stack termination
 protection


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement":[{
 "Effect":"Allow",
 "Action":[
 "cloudformation:UpdateTerminationProtection"
 ],
 "Resource":"*"
 }]
}`

```
