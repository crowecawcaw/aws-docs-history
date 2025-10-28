# Amazon ECS EventBridge IAM Role

Before you can use Amazon ECS scheduled tasks with EventBridge rules and targets, the EventBridge service
needs permissions to run Amazon ECS tasks on your behalf. These permissions are provided by the
EventBridge IAM role (`ecsEventsRole`).

The `AmazonEC2ContainerServiceEventsRole` policy is shown below.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["ecs:RunTask"],
 "Resource": ["*"]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": ["*"],
 "Condition": {
 "StringLike": {"iam:PassedToService": "ecs-tasks.amazonaws.com"}
 }
 },
 {
 "Effect": "Allow",
 "Action": "ecs:TagResource",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ecs:CreateAction": ["RunTask"]
 }
 }
 }
 ]
}`

```

If your scheduled tasks require the use of the task execution role, a task role, or a task
role override, then you must add `iam:PassRole` permissions for each task
execution role, task role, or task role override to the EventBridge IAM role. For more
information about the task execution role, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

###### Note

Specify the full ARN of your task execution role or task role override.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`ecsTaskExecutionRole_or_TaskRole_name`"
 ]
 }
 ]
}`

```

You can choose to let the AWS Management Console create the EventBridge role for you when you configure a
scheduled task. For more information, see [Using Amazon EventBridge Scheduler to schedule Amazon ECS tasks](tasks-scheduled-eventbridge-scheduler.md "tasks-scheduled-eventbridge-scheduler.md") .

## Creating the EventBridge role

Replace all `user input` with your own information.

1. Create a file named `eventbridge-trust-policy.json` that
   contains the trust policy to use for the IAM role. The file should contain the
   following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Use the following command to create an IAM role named
   `ecsEventsRole` by using the trust policy that you
   created in the previous step.

```
`aws iam create-role \
 --role-name `ecsEventsRole` \
 --assume-role-policy-document file://`eventbridge-trust-policy.json``
```

3. Attach the AWS managed
   `AmazonEC2ContainerServiceEventsRole` to the `ecsEventsRole` role using the following command.

```
`aws iam attach-role-policy \
 --role-name `ecsEventsRole` \
 --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceEventsRole`
```

You can also use the IAM console's **Custom trust policy** workflow
([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) to create the role. For more information, see [Creating a role using
custom trust policies (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _IAM User
Guide_.

## Attaching a policy to the `ecsEventsRole` role

You can use the following procedures to add permissions for the task execution role to the EventBridge IAM role.

AWS Management Console

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": ["arn:aws:iam::111122223333:role/<ecsTaskExecutionRole_or_TaskRole_name>"]
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.

After you create the policy, attach the policy to the EventBridge role. For information about
how to attach the policy to the role, see [Update permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management User Guide_.

AWS CLIReplace all `user input` with your own information.

1. Create a file called `ev-iam-passrole.json` with the
   following content.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`ecsTaskExecutionRole_or_TaskRole_name`"
 ]
 }
 ]
}`

```

2. Use the following AWS CLI command to create the IAM policy using the
   JSON policy document file.

```
`aws iam create-policy \
 --policy-name `eventsTaskExecutionPolicy` \
 --policy-document file://`ev-iam-passrole.json``
```

3. Retrieve the ARN of the IAM policy you created using the
   following command.

```
`aws iam list-policies --scope Local --query 'Policies[?PolicyName==``eventsTaskExecutionPolicy``].Arn'`
```

4. Use the following command to attach the policy to the EventBridge IAM role by using the policy ARN.

```
`aws iam attach-role-policy \
 --role-name `ecsEventsRole` \
 --policy-arn arn:aws:iam:111122223333:aws:policy/`eventsTaskExecutionPolicy``
```
