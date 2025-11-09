# Amazon ECS container instance IAM role

Amazon ECS container instances, including both Amazon EC2 and external instances, run the Amazon ECS
container agent and require an IAM role for the service to know that the agent belongs to
you. Before you launch container instances and register them to a cluster, you must create
an IAM role for your container instances to use. The role is created in the account that
you use to log into the console or run the AWS CLI commands.

###### Important

If you are registering external instances to your cluster, the IAM role you use
requires Systems Manager permissions as well. For more information, see [Amazon ECS Anywhere IAM role](iam-role-ecsanywhere.md "iam-role-ecsanywhere.md").

Amazon ECS provides the `AmazonEC2ContainerServiceforEC2Role` managed IAM policy
which contains the permissions needed to use the full Amazon ECS feature set. This managed policy
can be attached to an IAM role and associated with your container instances.
Alternatively, you can use the managed policy as a guide when creating a custom policy to
use. The container instance role provides permissions needed for the Amazon ECS container agent
and Docker daemon to call AWS APIs on your behalf. For more information on the managed
policy, see [AmazonEC2ContainerServiceforEC2Role](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonEC2ContainerServiceforEC2Role").

## Create the container instance role

###### Important

If you are registering external instances to your cluster, see [Amazon ECS Anywhere IAM role](iam-role-ecsanywhere.md "iam-role-ecsanywhere.md").

You can manually create the role and attach the managed IAM policy for container
instances to allow Amazon ECS to add permissions for future features and enhancements as they
are introduced. Use the following procedure to attach the managed IAM policy if
needed.

AWS Management Console

###### To create the service role for Elastic Container Service (IAM console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, and
   then choose **Create role**.
3. For **Trusted entity type**, choose **AWS service**.
4. For **Service or use case**, choose **Elastic Container Service**, and then choose the **EC2 Role for Elastic Container Service** use case.
5. Choose **Next**.
6. In the **Permissions policies** section, verify that the
   **AmazonEC2ContainerServiceforEC2Role** policy is selected.

###### Important

The **AmazonEC2ContainerServiceforEC2Role** managed policy
should be attached to the container instance IAM role, otherwise you will
receive an error using the AWS Management Console to create clusters. 7. Choose **Next**. 8. For **Role name**, enter **ecsInstanceRole** 9. Review the role, and then choose **Create role**.

AWS CLI
Replace all `user input` with your own
values.

1. Create a file called `instance-role-trust-policy.json`
   with the following contents.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": { "Service": "ec2.amazonaws.com"},
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Use the following command to create the instance IAM role using
   the trust policy document.

```
`aws iam create-role \
 --role-name ecsInstanceRole \
 --assume-role-policy-document file://instance-role-trust-policy.json`
```

3. Create an instance profile named
   `ecsInstanceRole-profile` using the [create-instance-profile](../../../cli/latest/reference/iam/create-instance-profile.md "../../../cli/latest/reference/iam/create-instance-profile.md") command.

```
`aws iam create-instance-profile --instance-profile-name `ecsInstanceRole-profile``
```

Example response

```
{
    "InstanceProfile": {
        "InstanceProfileId": "AIPAJTLBPJLEGREXAMPLE",
        "Roles": [],
        "CreateDate": "2022-04-12T23:53:34.093Z",
        "InstanceProfileName": "ecsInstanceRole-profile",
        "Path": "/",
        "Arn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceRole-profile"
    }
}
```

4. Add the `ecsInstanceRole`
   role to the
   `ecsInstanceRole-profile`
   instance profile.

```
`aws iam add-role-to-instance-profile \
 --instance-profile-name ecsInstanceRole-profile \
 --role-name ecsInstanceRole`
```

5. Attach the `AmazonEC2ContainerServiceForEC2Role`
   managed policy to the role using the following command.

```
`aws iam attach-role-policy \
 --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role \
 --role-name ecsInstanceRole`
```

After you create the role, add additional permissions to the role for the following
features.

| Feature                                          | Additional permissions                                                                  |
| ------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Amazon ECR has the container image               | [Amazon ECR permissions](#container-instance-role-ecr "#container-instance-role-ecr")   |
| Have CloudWatch Logs monitor container instances | [Monitoring container instances permissions](#cwl_iam_policy "#cwl_iam_policy")         |
| Host configuration files in an Amazon S3 bucket  | [Amazon S3 read-only access](#container-instance-role-s3 "#container-instance-role-s3") |

## Amazon ECR permissions

The Amazon ECS container instance role that you
use with your container instances must have the following IAM policy
permissions for Amazon ECR.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

If you use the `AmazonEC2ContainerServiceforEC2Role` managed
policy for your container instances, then your role has the proper
permissions.

## Permissions required for setting the awsvpcTrunking account setting

Amazon ECS supports launching container instances with increased ENI density using supported
Amazon EC2 instance types. When you use this feature, we recommend that you create 2 container
instance roles. Enable the `awsvpcTrunking` account setting for one role and use
that role for tasks that require ENI trunking. For information about the
`awsvpcTrunking` account setting, see [Access Amazon ECS features with account settings](ecs-account-settings.md "ecs-account-settings.md").

The container instance role that you use with your container instances must have the following IAM policy permissions for setting the account setting

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecs:ListAccountSettings",
 "ecs:ListAttributes",
 "ecs:PutAccountSetting"
 ],
 "Resource": "*"
 }
 ]
}`

```

In order to use the container instance role, add the following to instance user data:

```
#!/bin/bash
aws ecs put-account-setting --name awsvpcTrunking --value enabled --region `region`
ECS_CLUSTER=`MyCluster`>> /etc/ecs/ecs.config
EOF
```

For more information about adding user data to your EC2 instances, see [Run commands on your Linux instance at launch](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md") in the _Amazon EC2 User Guide_.

## Amazon S3 read-only access

Storing configuration information in a private bucket in Amazon S3 and granting read-only
access to your container instance IAM role is a secure and convenient way to allow
container instance configuration at launch time. You can store a copy of your
`ecs.config` file in a private bucket, use Amazon EC2 user data to
install the AWS CLI and then copy your configuration information to
`/etc/ecs/ecs.config` when the instance launches.

For more information about creating an `ecs.config` file, storing
it in Amazon S3, and launching instances with this configuration, see [Storing Amazon ECS container instance configuration in Amazon S3](ecs-config-s3.md "ecs-config-s3.md").

You can use the following AWS CLI command to allow Amazon S3 read-only access for your
container instance role. Replace `ecsInstanceRole` with the
name of the role that you created.

```
`aws iam attach-role-policy \
 --role-name `ecsInstanceRole` \
 --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`
```

You can also use the IAM console to add Amazon S3 read-only access
(`AmazonS3ReadOnlyAccess`) to your role. For more information, see [Updating permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management User Guide_.

## Monitoring container instances permissions

Before your container instances can send log data to CloudWatch Logs, you must create an IAM
policy to allow the Amazon ECS agent to write the customer's application logs to CloudWatch
(normally handled through the `awslogs` driver). After you create the policy,
attach that policy to `ecsInstanceRole`.

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
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams"
            ],
            "Resource": ["arn:aws:logs:*:*:*"]
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

After you create the policy, attach the policy to the container instance
role. For information about how to attach the policy to the role, see [Updating permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management User Guide_.

AWS CLI

1. Create a file called `instance-cw-logs.json` with the
   following content.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": ["arn:aws:logs:*:*:*"]
 }
 ]
}`

```

2. Use the following command to create the IAM policy using the
   JSON policy document file.

```
`aws iam create-policy \
 --policy-name `cwlogspolicy` \
 --policy-document file://`instance-cw-logs.json``
```

3. Retrieve the ARN of the IAM policy you created using the
   following command. Replace `cwlogspolicy`
   with the name of the policy you created.

```
`aws iam list-policies --scope Local --query 'Policies[?PolicyName==``cwlogspolicy``].Arn'`
```

4. Use the following command to attach the policy to the container
   instance IAM role using the policy ARN.

```
`aws iam attach-role-policy \
 --role-name `ecsInstanceRole` \
 --policy-arn arn:aws:iam:111122223333:aws:policy/`cwlogspolicy``
```
