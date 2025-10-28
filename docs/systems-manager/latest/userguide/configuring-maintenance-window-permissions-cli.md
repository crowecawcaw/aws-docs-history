# Control access to

maintenance windows using the AWS CLI

The following procedures describe how to use the AWS Command Line Interface (AWS CLI) to create the
required permissions and roles for Maintenance Windows, a tool in AWS Systems Manager.

###### Topics

- [Task 1: Create trust
  policy and customer managed policy files in JSON format](#create-custom-policy-json-files-cli "#create-custom-policy-json-files-cli")
- [Task 2: Create and verify a custom
  service role for maintenance windows using the AWS CLI](#create-custom-role-cli "#create-custom-role-cli")
- [Task 3: Grant permissions
  to specified users to register maintenance window tasks using the
  AWS CLI](#allow-maintenance-window-access-cli "#allow-maintenance-window-access-cli")
- [Task 4: Prevent specified
  users from registering maintenance window tasks using the AWS CLI](#deny-maintenance-window-access-cli "#deny-maintenance-window-access-cli")

## Task 1: Create trust

policy and customer managed policy files in JSON format

Maintenance window tasks require an IAM role to provide the permissions
required to run on the target resources. The permissions are provided through an
IAM policy attached to the role. The types of tasks you run and your other
operational requirements determine the contents of this policy. We provide a
base policy you can adapt to your needs. Depending on the tasks and types of
tasks your maintenance windows run, you might not need all the permissions in
this policy, and you might need to include additional permissions.

In this task, you specify the permissions needed for your custom maintenance
window role in a pair of JSON files. You attach this policy to the role that you
create later in [Task 2: Create and verify a custom
service role for maintenance windows using the AWS CLI](#create-custom-role-cli "#create-custom-role-cli").

###### To create trust policy and customer managed policy files

1. Copy and paste the following trust policy into a text file. Save this
   file with the following name and file extension:
   `mw-role-trust-policy.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Copy and paste the following JSON policy into a different text file.
   In the same directory where you created the first file, save this file
   with the following name and file extension:
   `mw-role-custom-policy.json`.

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

3. Modify the the content of
   `mw-role-custom-policy.json` as needed for the
   maintenance tasks that you run in your account. The changes you make are
   specific to your planned operations.

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

Save the file again after making any needed changes.

## Task 2: Create and verify a custom

service role for maintenance windows using the AWS CLI

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

In this task, you run CLI commands to create your maintenance windows service
role, adding the policy content from the JSON files you created.

###### Create a custom service role for maintenance windows using the

AWS CLI

1. Open the AWS CLI and run the following command in the directory where
   you placed `mw-role-custom-policy.json` and
   `mw-role-trust-policy.json`. The command creates
   a maintenance window service role called
   `my-maintenance-window-role` and attaches the
   _trust policy_ to it.

Linux & macOS

```
aws iam create-role \
    --role-name "my-maintenance-window-role" \
    --assume-role-policy-document file://mw-role-trust-policy.json
```

Windows

```
aws iam create-role ^
    --role-name "my-maintenance-window-role" ^
    --assume-role-policy-document file://mw-role-trust-policy.json
```

The system returns information similar to the following.

```
{
    "Role": {
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ssm.amazonaws.com"
                    }
                }
            ]
        },
        "RoleId": "AROAIIZKPBKS2LEXAMPLE",
        "CreateDate": "2024-08-19T03:40:17.373Z",
        "RoleName": "my-maintenance-window-role",
        "Path": "/",
        "Arn": "arn:aws:iam::123456789012:role/my-maintenance-window-role"
    }
}
```

###### Note

Make a note of the `RoleName` and the `Arn`
values. You include them in the next command. 2. Run the following command to attach the _customer managed policy_ to the role. Replace the
`account-id` placeholder with your own
AWS account ID

Linux & macOS

```
aws iam attach-role-policy \
    --role-name "my-maintenance-window-role" \
    --policy-arn "arn:aws:iam::`account-id`:policy/`mw-role-custom-policy.json`"
```

Windows

```
aws iam attach-role-policy ^
    --role-name "my-maintenance-window-role" ^
    --policy-arn "arn:aws:iam::`account-id`:policy/`mw-role-custom-policy.json`"
```

3. Run the following command to verify that your role has been created,
   and that the trust policy has been attached.

```
aws iam get-role --role-name my-maintenance-window-role
```

The command returns information similar to the following:

```
{
    "Role": {
        "Path": "/",
        "RoleName": "my-maintenance-window-role",
        "RoleId": "AROA123456789EXAMPLE",
        "Arn": "arn:aws:iam::123456789012:role/my-maintenance-window-role",
        "CreateDate": "2024-08-19T14:13:32+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ssm.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        },
        "MaxSessionDuration": 3600,
        "RoleLastUsed": {
            "LastUsedDate": "2024-08-19T14:30:44+00:00",
            "Region": "us-east-2"
        }
    }
}
```

4. Run the following command to verify that the customer managed policy
   has been attached to the role.

```
aws iam list-attached-role-policies --role-name my-maintenance-window-role
```

The command returns information similar to the following:

```
{
    "AttachedPolicies": [
        {
            "PolicyName": "mw-role-custom-policy",
            "PolicyArn": "arn:aws:iam::123456789012:policy/mw-role-custom-policy"
        }
    ]
}
```

## Task 3: Grant permissions

to specified users to register maintenance window tasks using the
AWS CLI

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

###### To configure permissions for users who are allowed to register

maintenance window tasks using the AWS CLI

1. Copy and paste the following AWS Identity and Access Management (IAM) policy into a text
   editor and save it with the following name and file extension:
   `mw-passrole-policy.json`.

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

Replace `my-maintenance-window-role` with the
name of the custom maintenance window role you created earlier.

Replace `account-id` with the ID of your
AWS account. Adding this permission for the resource
`arn:aws:iam::`account-id`:role/`
allows users in the group to view and choose from customer roles in the
console when they create a maintenance window task. Adding this
permission for
`arn:aws:iam::`account-id`:role/aws-service-role/ssm.amazonaws.com/`
allows users in the group to choose the Systems Manager service-linked role in the
console when they create a maintenance window task. 2. Open the AWS CLI. 3. Depending on whether you're assigning the permission to an IAM
entity (user or group), run one of the following commands.

    * **For an IAM entity:**



    Linux & macOS

    ```
    aws iam put-user-policy \
        --user-name "`user-name`" \
        --policy-name "`policy-name`" \
        --policy-document file://`path-to-document`
    ```


    Windows

    ```
    aws iam put-user-policy ^
        --user-name "`user-name`" ^
        --policy-name "`policy-name`" ^
        --policy-document file://`path-to-document`
    ```



    For `user-name`, specify the user who
     assigns tasks to maintenance windows. For
     `policy-name`, specify the name you
     want to use to identify the policy, such as
     `my-iam-passrole-policy`. For
     `path-to-document`, specify the
     path to the file you saved in step 1. For example:
     `file://C:\Temp\mw-passrole-policy.json`


    ###### Note

    To grant access for a user to register tasks for
     maintenance windows using the Systems Manager console, you must also
     assign the `AmazonSSMFullAccess` policy to your
     user (or an IAM policy that provides a smaller set of
     access permissions for Systems Manager that covers maintenance window
     tasks). Run the following command to assign the
     `AmazonSSMFullAccess` policy to your
     user.


    Linux & macOS

    ```
    aws iam attach-user-policy \
        --policy-arn "arn:aws:iam::aws:policy/AmazonSSMFullAccess" \
        --user-name "`user-name`"
    ```


    Windows

    ```
    aws iam attach-user-policy ^
        --policy-arn "arn:aws:iam::aws:policy/AmazonSSMFullAccess" ^
        --user-name "`user-name`"
    ```
    * **For an IAM group:**



    Linux & macOS

    ```
    aws iam put-group-policy \
        --group-name "`group-name`" \
        --policy-name "`policy-name`" \
        --policy-document file://`path-to-document`
    ```


    Windows

    ```
    aws iam put-group-policy ^
        --group-name "`group-name`" ^
        --policy-name "`policy-name`" ^
        --policy-document file://`path-to-document`
    ```



    For `group-name`, specify the group
     whose members assign tasks to maintenance windows. For
     `policy-name`, specify the name you
     want to use to identify the policy, such as
     `my-iam-passrole-policy`. For
     `path-to-document`, specify the
     path to the file you saved in step 1. For example:
     `file://C:\Temp\mw-passrole-policy.json`


    ###### Note

    To grant access for members of a group to register tasks
     for maintenance windows using the Systems Manager console, you must
     also assign the `AmazonSSMFullAccess` policy to
     your group. Run the following command to assign this policy
     to your group.


    Linux & macOS

    ```
    aws iam attach-group-policy \
        --policy-arn "arn:aws:iam::aws:policy/AmazonSSMFullAccess" \
        --group-name "`group-name`"
    ```


    Windows

    ```
    aws iam attach-group-policy ^
        --policy-arn "arn:aws:iam::aws:policy/AmazonSSMFullAccess" ^
        --group-name "`group-name`"
    ```

4. Run the following command to verify that the policy has been assigned
   to the group.

Linux & macOS

```
aws iam list-group-policies \
    --group-name "`group-name`"
```

Windows

```
aws iam list-group-policies ^
    --group-name "`group-name`"
```

## Task 4: Prevent specified

users from registering maintenance window tasks using the AWS CLI

You can deny the `ssm:RegisterTaskWithMaintenanceWindow` permission
for the users in your AWS account who you don't want to register tasks with
maintenance windows. This provides an extra layer of prevention for users who
shouldn’t register maintenance window tasks.

Depending on whether you're denying the
`ssm:RegisterTaskWithMaintenanceWindow` permission for an
individual user or a group, use one of the following procedures to prevent users
from registering tasks with a maintenance window.

###### To configure permissions for users who aren't allowed to register

maintenance window tasks using the AWS CLI

1. Copy and paste the following IAM policy into a text editor and save
   it with the following name and file extension:
   `deny-mw-tasks-policy.json`.

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

2. Open the AWS CLI.
3. Depending on whether you're assigning the permission to an IAM
   entity (user or group), run one of the following commands.
   - **For a user:**

   Linux & macOS

   ```
   aws iam put-user-policy \
       --user-name "`user-name`" \
       --policy-name "`policy-name`" \
       --policy-document file://`path-to-document`
   ```

   Windows

   ```
   aws iam put-user-policy ^
       --user-name "`user-name`" ^
       --policy-name "`policy-name`" ^
       --policy-document file://`path-to-document`
   ```

   For `user-name`, specify the user to
   prevent from assigning tasks to maintenance windows. For
   `policy-name`, specify the name you
   want to use to identify the policy, such as
   `my-deny-mw-tasks-policy`. For
   `path-to-document`, specify the
   path to the file you saved in step 1. For example:
   `file://C:\Temp\deny-mw-tasks-policy.json`
   - **For a group:**

   Linux & macOS

   ```
   aws iam put-group-policy \
       --group-name "`group-name`" \
       --policy-name "`policy-name`" \
       --policy-document file://`path-to-document`
   ```

   Windows

   ```
   aws iam put-group-policy ^
       --group-name "`group-name`" ^
       --policy-name "`policy-name`" ^
       --policy-document file://`path-to-document`
   ```

   For `group-name`, specify the group
   whose to prevent from assigning tasks to maintenance windows.
   For `policy-name`, specify the name you
   want to use to identify the policy, such as
   `my-deny-mw-tasks-policy`. For
   `path-to-document`, specify the
   path to the file you saved in step 1. For example:
   `file://C:\Temp\deny-mw-tasks-policy.json`

4. Run the following command to verify that the policy has been assigned
   to the group.

Linux & macOS

```
aws iam list-group-policies \
    --group-name "`group-name`"
```

Windows

```
aws iam list-group-policies ^
    --group-name "`group-name`"
```
