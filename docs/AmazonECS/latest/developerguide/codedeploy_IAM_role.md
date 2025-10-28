# Amazon ECS CodeDeploy IAM Role

Before you can use the CodeDeploy blue/green deployment type with Amazon ECS, the CodeDeploy service
needs permissions to update your Amazon ECS service on your behalf. These permissions are
provided by the CodeDeploy IAM role (`ecsCodeDeployRole`).

###### Note

Users also require permissions to use CodeDeploy; these permissions are described in [Required IAM
permissions](deployment-type-bluegreen.md#deployment-type-bluegreen-IAM "deployment-type-bluegreen.md#deployment-type-bluegreen-IAM").

There are two managed policies provided. For more information, see one of the following
in the _AWS Managed Policy Reference Guide_:

- [AWSCodeDeployRoleForECS](../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECS.md "../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECS.md") - gives CodeDeploy permission to
  update any resource using the associated action.
- [AWSCodeDeployRoleForECSLimited](../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECSLimited.md "../../../aws-managed-policy/latest/reference/AWSCodeDeployRoleForECSLimited.md") - gives CodeDeploy more
  limited permissions.

## Creating the CodeDeploy role

You can use the following procedures to create a CodeDeploy role for Amazon ECS

AWS Management Console

###### To create the service role for CodeDeploy (IAM console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, and
   then choose **Create role**.
3. For **Trusted entity type**, choose **AWS service**.
4. For **Service or use case**, choose **CodeDeploy**, and then choose the **CodeDeploy - ECS** use case.
5. Choose **Next**.
6. In the **Attach permissions policy** section, ensure that the **AWSCodeDeployRoleForECS** policy is selected.
7. Choose **Next**.
8. For **Role name**, enter **ecsCodeDeployRole**.
9. Review the role, and then choose **Create role**.

AWS CLI
Replace all `user input` with your own
information.

1. Create a file named `codedeploy-trust-policy.json` that
   contains the trust policy to use for the CodeDeploy IAM role.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": ["codedeploy.amazonaws.com"]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Create an IAM role named `ecsCodedeployRole` using
   the trust policy created in the previous step.

```
`aws iam create-role \
 --role-name `ecsCodedeployRole` \
 --assume-role-policy-document file://`codedeploy-trust-policy.json``
```

3. Attach the `AWSCodeDeployRoleForECS` or
   `AWSCodeDeployRoleForECSLimited` managed policy to
   the `ecsTaskRole` role.

```
`aws iam attach-role-policy \
 --role-name `ecsCodedeployRole` \
 --policy-arn arn:aws:iam::aws:policy/AWSCodeDeployRoleForECS`
```

```
`aws iam attach-role-policy \
 --role-name `ecsCodedeployRole` \
 --policy-arn arn:aws:iam::aws:policy/AWSCodeDeployRoleForECSLimited`
```

When the tasks in your service need a task execution role, you must add the
`iam:PassRole` permission for each task execution role or task role
override to the CodeDeploy role as a policy.

### Task execution role

permissions

When the tasks in your service need a task execution role, you must add the
`iam:PassRole` permission for each task execution role or task role
override to the CodeDeploy role as a policy. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md") and
[Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md"). Then, you
attach that policy to the CodeDeploy role

Create the policy

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
            "Resource": ["arn:aws:iam::<aws_account_id>:role/<ecsCodeDeployRole>"]
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

After you create the policy, attach the policy to the CodeDeploy role. For
information about how to attach the policy to the role, see [Update permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the
_AWS Identity and Access Management User Guide_.

AWS CLI
Replace all `user input` with your own
information.

1. Create a file called `blue-green-iam-passrole.json`
   with the following content.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": ["arn:aws:iam::*:role/`code-deploy-role`"],
 "Condition": {
 "StringEquals": {"iam:PassedToService": "ecs.amazonaws.com"}
 }
 }
 ]
}`

```

2. Use the following command to create the IAM policy using the
   JSON policy document file.

```
`aws iam create-policy \
 --policy-name `cdTaskExecutionPolicy` \
 --policy-document file://blue-green-iam-passrole.json`
```

3. Retrieve the ARN of the IAM policy you created using the
   following command.

```
`aws iam list-policies --scope Local --query 'Policies[?PolicyName==``cdTaskExecutionPolicy``].Arn'`
```

4. Use the following command to attach the policy to the CodeDeploy
   IAM role.

```
`aws iam attach-role-policy \
 --role-name `ecsCodedeployRole` \
 --policy-arn arn:aws:iam:111122223333:aws:policy/`cdTaskExecutionPolicy``
```
