• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Control access

to maintenance windows using the console

The following procedures describe how to use the AWS Systems Manager console to create the
required permissions and roles for maintenance windows.

###### Topics

- [Task 1: Create a custom policy
  for your maintenance window service role using the console](#create-custom-policy-console "#create-custom-policy-console")
- [Task 2: Create a custom service
  role for maintenance windows using the console](#create-custom-role-console "#create-custom-role-console")
- [Task 3: Grant
  permissions to specified users to register maintenance window tasks using
  the console](#allow-maintenance-window-access-console "#allow-maintenance-window-access-console")
- [Task 4: Prevent
  specified users from registering maintenance window tasks using the
  console](#deny-maintenance-window-access-console "#deny-maintenance-window-access-console")

## Task 1: Create a custom policy

for your maintenance window service role using the console

Maintenance window tasks require an IAM role to provide the permissions
required to run on the target resources. The permissions are provided through an
IAM policy attached to the role. The types of tasks you run and your other
operational requirements determine the contents of this policy. We provide a
base policy you can adapt to your needs. Depending on the tasks and types of
tasks your maintenance windows run, you might not need all the permissions in
this policy, and you might need to include additional permissions. You attach
this policy to the role that you create later in [Task 2: Create a custom service
role for maintenance windows using the console](#create-custom-role-console "#create-custom-role-console").

###### To create a custom policy using the console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then
   choose **Create policy**.
3. In the **Policy editor** area, choose
   **JSON**.
4. Replace the default contents with the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand",
 "ssm:CancelCommand",
 "ssm:ListCommands",
 "ssm:ListCommandInvocations",
 "ssm:GetCommandInvocation",
 "ssm:GetAutomationExecution",
 "ssm:StartAutomationExecution",
 "ssm:ListTagsForResource",
 "ssm:DescribeInstanceInformation",
 "ssm:GetParameters"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "states:DescribeExecution",
 "states:StartExecution"
 ],
 "Resource": [
 "arn:aws:states:*:*:execution:*:*",
 "arn:aws:states:*:*:stateMachine:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:*:*:function:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:ListGroups",
 "resource-groups:ListGroupResources"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`maintenance-window-role-name`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

5. Modify the JSON content as needed for the maintenance tasks that you
   run in your account. The changes you make are specific to your planned
   operations.

For example:

    * You can provide Amazon Resource Names (ARNs) for specific
     functions and state machines instead of using wildcard (\*)
     qualifiers.
    * If you don’t plan to run AWS Step Functions tasks, you can remove the
     `states` permissions and (ARNs).
    * If you don’t plan to run AWS Lambda tasks, you can remove the
     `lambda` permissions and ARNs.
    * If you don't plan to run Automation tasks, you can remove the
     `ssm:GetAutomationExecution` and
     `ssm:StartAutomationExecution`
     permissions.
    * Add additional permissions that might be needed for the tasks
     to run. For example, some Automation actions work with AWS CloudFormation
     stacks. Therefore, the permissions
     `cloudformation:CreateStack`,
     `cloudformation:DescribeStacks`, and
     `cloudformation:DeleteStack` are required.


    For another example, the Automation runbook
     `AWS-CopySnapshot` requires permissions
     to create an Amazon Elastic Block Store (Amazon EBS) snapshot. Therefore, the service
     role needs the permission `ec2:CreateSnapshot`.


    For information about the role permissions needed by
     Automation runbooks, see the runbook descriptions in the [AWS Systems Manager Automation Runbook Reference](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md").

6. After completing the policy revisions, choose
   **Next**.
7. For **Policy name**, enter a name that identifies
   this as the policy attached to the service role you create. For example:
   `my-maintenance-window-role-policy`.
8. (Optional) In the **Add tags** area, add one or more
   tag-key value pairs to organize, track, or control access for this
   policy.
9. Choose **Create policy**.

Make a note of the name you specified for the policy. You refer to it
in the next procedure, [Task 2: Create a custom service
role for maintenance windows using the console](#create-custom-role-console "#create-custom-role-console").

## Task 2: Create a custom service

role for maintenance windows using the console

The policy you created in the previous task is attached to the maintenance
window service role you create in this task. When users register a maintenance
window task, they specify this IAM role as part of the task configuration. The
permissions in this role allow Systems Manager to run tasks in maintenance windows on your
behalf.

###### Important

Previously, the Systems Manager console provided you with the ability to choose the AWS managed
IAM service-linked role `AWSServiceRoleForAmazonSSM` to use as the maintenance
role for your tasks. Using this role and its associated policy,
`AmazonSSMServiceRolePolicy`, for maintenance window tasks is no longer
recommended. If you're using this role for maintenance window tasks now, we encourage
you to stop using it. Instead, create your own IAM role that enables communication between
Systems Manager and other AWS services when your maintenance window tasks run.

Use the following procedure to create a custom service role for Maintenance Windows, so
that Systems Manager can run Maintenance Windows tasks on your behalf. You attach the policy you
created in the previous task to the custom service role you create.

###### To create a custom service role for maintenance windows using the

console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then
   choose **Create role**.
3. For **Select trusted entity**, make the following
   choices:
   1. For **Trusted entity type**, choose
      **AWS service**.
   2. For **Use case**, choose
      **Systems Manager**
   3. Choose **Systems Manager**.

   The following image
   highlights the location of the Systems Manager option.

   ![Systems Manager is one of the options for Use case.](images/iam_use_cases_for_MWs.png)

4. Choose **Next**.
5. In the **Permissions policies** area, in the search
   box, enter the name of the policy you created in [Task 1: Create a custom policy
   for your maintenance window service role using the console](#create-custom-policy-console "#create-custom-policy-console"), select the box next
   to its name, and then choose **Next**.
6. For **Role name**, enter a name that identifies this
   role as a Maintenance Windows role. For example:
   `my-maintenance-window-role`.
7. (Optional) Change the default role description to reflect the purpose
   of this role. For example: `Performs maintenance window tasks
on your behalf`.
8. For **Step 1: Select trusted entities**, verify that
   the following policy is displayed in the **Trusted
   policy** box.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

9. For **Step 2: Add permissions**, verify that policy
   you created in [Task 1: Create a custom policy
   for your maintenance window service role using the console](#create-custom-policy-console "#create-custom-policy-console") is present.
10. (Optional) In **Step 3: Add tags**, add one or more
    tag-key value pairs to organize, track, or control access for this role.
11. Choose **Create role**. The system returns you to the
    **Roles** page.
12. Choose the name of the IAM role you just created.
13. Copy or make a note of the role name and the **ARN**
    value in the **Summary** area. Users in your account
    specify this information when they create maintenance windows.

## Task 3: Grant

permissions to specified users to register maintenance window tasks using
the console

Providing users with permissions to access the custom service role for
maintenance windows lets them use it with their maintenance windows tasks. This
is in addition to permissions that you’ve already given them to work with the
Systems Manager API commands for the Maintenance Windows tool. This IAM role conveys the
permissions need to run a maintenance window task. As a result, a user can't
register tasks with a maintenance window using your custom service role without
the ability to pass these IAM permissions.

When you register a task with a maintenance window, you specify a service role to run the
actual task operations. This is the role that the service assumes when it runs tasks on your
behalf. Before that, to register the task itself, assign the IAM `PassRole`
policy to an IAM entity (such as a user or group). This allows the IAM entity to
specify, as part of registering those tasks with the maintenance window, the role that
should be used when running tasks. For information, see [Grant a user permissions to pass a
role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the _IAM User Guide_.

###### To configure permissions to allow users to register maintenance window

tasks

If an IAM entity (user, role, or group) is set up with administrator
permissions, then the IAM user or role has access to Maintenance Windows.
For IAM entities without administrator permissions, an administrator must
grant the following permissions to the IAM entity. These are the minimum
permissions required to register tasks with a maintenance window:

- The `AmazonSSMFullAccess` managed policy, or a policy that
  provides comparable permissions.
- The following `iam:PassRole` and
  `iam:ListRoles`permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`my-maintenance-window-role`"
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws:iam::`111122223333`:role/"
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/ssm.amazonaws.com/"
 }
 ]
}`

```

`my-maintenance-window-role` represents the
name of the custom maintenance window service role you created
earlier.

`account-id` represents the ID of your
AWS account. Adding this permission for the resource
`arn:aws:iam::`account-id`:role/`
allows a user to view and choose from customer roles in the console when
they create a maintenance window task. Adding this permission for
`arn:aws:iam::`account-id`:role/aws-service-role/ssm.amazonaws.com/`
allows a user to choose the Systems Manager service-linked role in the console
when they create a maintenance window task.

To provide access, add permissions to your users, groups, or roles:

    + Users and groups in AWS IAM Identity Center:


    Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the *AWS IAM Identity Center User Guide*.
    + Users managed in IAM through an identity provider:


    Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
     in the *IAM User Guide*.
    + IAM users:




    	- Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
    	- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

###### To configure permissions for groups that are allowed to register

maintenance window tasks using the console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User
   groups**.
3. In the list of groups, select the name of the group you want to assign
   the `iam:PassRole` permission to, or first create a new group
   if necessary
4. On the **Permissions** tab, choose **Add
   permissions, Create inline policy**.
5. In the **Policy editor** area, choose
   **JSON**, and replace the default contents of the
   box with the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`my-maintenance-window-role`"
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws:iam::`111122223333`:role/"
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/ssm.amazonaws.com/"
 }
 ]
}`

```

`my-maintenance-window-role` represents the
name of the custom maintenance window role you created earlier.

`account-id` represents the ID of your
AWS account. Adding this permission for the resource
`arn:aws:iam::`account-id`:role/`
allows a user to view and choose from customer roles in the console when
they create a maintenance window task. Adding this permission for
`arn:aws:iam::`account-id`:role/aws-service-role/ssm.amazonaws.com/`
allows a user to choose the Systems Manager service-linked role in the console
when they create a maintenance window task. 6. Choose **Next**. 7. On the **Review and create** page, enter a name in
the **Policy name** box to identify this
`PassRole` policy, such as
`my-group-iam-passrole-policy`, and then choose
**Create policy**.

## Task 4: Prevent

specified users from registering maintenance window tasks using the
console

You can deny the `ssm:RegisterTaskWithMaintenanceWindow` permission
for the users in your AWS account who you don't want to register tasks with
maintenance windows. This provides an extra layer of prevention for users who
shouldn’t register maintenance window tasks.

###### To configure permissions for groups that aren't allowed to register

maintenance window tasks using the console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User
   groups**.
3. In the list of groups, select the name of the group you want to deny
   the `ssm:RegisterTaskWithMaintenanceWindow` permission from,
   or first create a new group if necessary.
4. On the **Permissions** tab, choose **Add
   permissions, Create inline policy**.
5. In the **Policy editor** area, choose
   **JSON**, and then replace the default contents of
   the box with the following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "ssm:RegisterTaskWithMaintenanceWindow",
 "Resource": "*"
 }
 ]
}`

```

6. Choose **Next**.
7. On the **Review and create** page, for
   **Policy name**, enter a name to identify this
   policy, such as `my-groups-deny-mw-tasks-policy`,
   and then choose **Create policy**.
