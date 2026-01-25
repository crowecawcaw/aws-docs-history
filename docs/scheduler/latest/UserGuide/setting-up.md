# Setting up Amazon EventBridge Scheduler

Before you can use EventBridge Scheduler, you must complete the following steps.

###### Topics

- [Sign up for AWS](#setting-up-aws-sign-up "#setting-up-aws-sign-up")
- [Create an IAM user](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [Use managed policies](#setting-up-managed-policies "#setting-up-managed-policies")
- [Set up the execution role](#setting-up-execution-role "#setting-up-execution-role")
- [Set up a target](#setting-up-target "#setting-up-target")
- [What's next?](#setting-up-whats-next "#setting-up-whats-next")

## Sign up for AWS

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create an IAM user

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                      | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM<br>users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |

## Use managed policies

In the previous step, you set up an IAM user with the credentials to access your AWS resources. In most cases, to use EventBridge Scheduler securely, we recommend that
you create separate users, groups, or roles with only the necessary permissions to use EventBridge Scheduler. EventBridge Scheduler supports the following managed policies for common use cases.

- AmazonEventBridgeSchedulerFullAccess – Grants full access to EventBridge Scheduler using the console and the API.
- AmazonEventBridgeSchedulerReadOnlyAccess – Grants read-only access to EventBridge Scheduler.

You can attach these managed policies to your IAM principals the same way you
attached the `AdministratorAccess` policy in the previous step. For more
information about managing access to EventBridge Scheduler using identity-based IAM policies, see
[Using identity-based policies in EventBridge Scheduler](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Set up the execution role

An _execution role_ is an IAM role that EventBridge Scheduler assumes in order to
interact with other AWS services on your behalf. You attach permission policies to
this role to grant EventBridge Scheduler access to invoke targets.

You can also create a new execution role when you use the console to [create a new schedule](getting-started.md#getting-started-console "getting-started.md#getting-started-console"). If you use the console,
EventBridge Scheduler creates a role on your behalf with permissions based on the target you choose. When EventBridge Scheduler creates a role for you,
the role's trust policy includes [condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") that limit which principals can assume the role on your behalf.
This guards against the potential [confused deputy security issue](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

The following steps describe how to create a new execution role and how to grant EventBridge Scheduler access to invoke a target. This topic describes permissions for popular templated targets.
For information on adding permissions for other targets, see [Using templated targets in EventBridge Scheduler](managing-targets-templated.md "managing-targets-templated.md").

###### To create an execution role using the AWS CLI

1. Copy the following assume role JSON policy and save it locally as
   `Scheduler-Execution-Role.json`. This trust policy allows EventBridge Scheduler
   to assume the role on your behalf.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "scheduler.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

###### Important

To set up an execution role in a production environment, we recommend implementing additional safeguards for preventing confused deputy issues. For more information and an example policy, see
[Confused deputy prevention in EventBridge Scheduler](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"). 2. From the AWS Command Line Interface (AWS CLI), enter the following command to create a new role.
Replace `SchedulerExecutionRole` with the
name you want to give this role.

```
`$` `aws iam create-role --role-name `SchedulerExecutionRole` --assume-role-policy-document file://Scheduler-Execution-Role.json`
```

If successful, you'll see the following output:

```
{
    "Role": {
        "Path": "/",
        "RoleName": "Scheduler-Execution-Role",
        "RoleId": "BR1L2DZK3K4CTL5ZF9EIL",
        "Arn": "arn:aws:iam::123456789012:role/SchedulerExecutionRole",
        "CreateDate": "2022-03-10T18:45:01+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "scheduler.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
}
```

3. To create a new policy that allows EventBridge Scheduler to invoke a target, choose one of the following common targets. Copy the JSON permission policy and save it locally as a `.json` file.

Amazon SQS – SendMessage

The following allows EventBridge Scheduler to call the `sqs:SendMessage` action on all Amazon SQS queues in your account.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sqs:SendMessage"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Amazon SNS – Publish

The following allows EventBridge Scheduler to call the `sns:Publish` action on all Amazon SNS topics in your account.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sns:Publish"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Lambda – Invoke

The following allows EventBridge Scheduler to call the `lambda:InvokeFunction` action on all Lambda functions in your account.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

4. Run the following command to create the new permission policy. Replace
   `PolicyName` with
   the name you want to give this policy.

```
`$` `aws iam create-policy --policy-name `PolicyName` --policy-document file://PermissionPolicy.json`
```

If successful, you'll see the following output. Note the policy ARN. You use this ARN
in the next step to attach the policy to our execution role.

```
{
    "Policy": {
        "PolicyName": "PolicyName",
        "CreateDate": "2022-03-015T19:31:18.620Z",
        "AttachmentCount": 0,
        "IsAttachable": true,
        "PolicyId": "ZXR6A36LTYANPAI7NJ5UV",
        "DefaultVersionId": "v1",
        "Path": "/",
        "Arn": "arn:aws:iam::123456789012:policy/PolicyName",
        "UpdateDate": "2022-03-015T19:31:18.620Z"
    }
}

```

5. Run the following command to attach the policy to your execution role. Replace
   `your-policy-arn` with the ARN of
   the policy you created in the previous step. Replace
   `SchedulerExecutionRole` with
   the name of your execution role.

```
`$` `aws iam attach-role-policy --policy-arn `your-policy-arn` --role-name `SchedulerExecutionRole``
```

The `attach-role-policy` operation doesn't return a response on the command
line.

## Set up a target

Before you create an EventBridge Scheduler schedule, you need at least one target for your schedule to
invoke. You can use an existing AWS resource, or create a new one. The following steps
show how to create a new standard Amazon SQS queue with CloudFormation.

###### To create a new Amazon SQS queue

1. Copy the following JSON CloudFormation template and save it locally as `Scheduler-Target-SQS.json`.

```
{
   "AWSTemplateFormatVersion": "2010-09-09",
   "Resources": {
      "MyQueue": {
         "Type": "AWS::SQS::Queue",
         "Properties": {
            "QueueName": "`MyQueue`"
             }
         }
      },
   "Outputs": {
      "QueueName": {
         "Description": "The name of the queue",
         "Value": {
            "Fn::GetAtt": [
               "MyQueue",
               "QueueName"
            ]
         }
      },
      "QueueURL": {
         "Description": "The URL of the queue",
         "Value": {
            "Ref": "MyQueue"
         }
      },
      "QueueARN": {
         "Description": "The ARN of the queue",
         "Value": {
            "Fn::GetAtt": [
               "MyQueue",
               "Arn"
            ]
         }
      }
   }
}
```

2. From the AWS CLI, run the following command to create an CloudFormation stack from the
   `Scheduler-Target-SQS.json` template.

```
`$` `aws cloudformation create-stack --stack-name `Scheduler-Target-SQS` --template-body file://Scheduler-Target-SQS.json`
```

If successful, you'll see the following output:

```
{
    "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/Scheduler-Target-SQS/1d2af345-a121-12eb-abc1-012e34567890"
}
```

3. Run the following command to view summary information for your CloudFormation stack. This
   information includes the status of the stack and the outputs specified in the
   template.

```
`$` `aws cloudformation describe-stacks --stack-name `Scheduler-Target-SQS``
```

If successful, the command creates the Amazon SQS queue and returns the following
output:

```
{
    "Stacks": [
        {
            "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/Scheduler-Target-SQS/1d2af345-a121-12eb-abc1-012e34567890",
            "StackName": "Scheduler-Target-SQS",
            "CreationTime": "2022-03-17T16:21:29.442000+00:00",
            "RollbackConfiguration": {},
            "StackStatus": "CREATE_COMPLETE",
            "DisableRollback": false,
            "NotificationARNs": [],
            "Outputs": [
                {
                    "OutputKey": "QueueName",
                    "OutputValue": "MyQueue",
                    "Description": "The name of the queue"
                },
                {
                    "OutputKey": "QueueARN",
                    "OutputValue": "arn:aws:sqs:us-west-2:123456789012:MyQueue",
                    "Description": "The ARN of the queue"
                },
                {
                    "OutputKey": "QueueURL",
                    "OutputValue": "https://sqs.us-west-2.amazonaws.com/123456789012/MyQueue",
                    "Description": "The URL of the queue"
                }
            ],
            "Tags": [],
            "EnableTerminationProtection": false,
            "DriftInformation": {
                "StackDriftStatus": "NOT_CHECKED"
            }
        }
    ]
}
```

Later in this guide, you'll use the value for `QueueARN` to set up the queue as a target for EventBridge Scheduler.

## What's next?

After you've completed the set up step, use the [Getting started](getting-started.md "getting-started.md") guide to create your first
EventBridge Scheduler scheduler and invoke a target.
