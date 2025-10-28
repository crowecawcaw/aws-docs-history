# IAM roles for AWS FIS experiments

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. To use AWS FIS, you must create an IAM role that grants AWS FIS the
permissions required so that AWS FIS can run experiments on your behalf. You specify this
experiment role when you create an experiment template. For a single-account experiment,
the IAM policy for the experiment role must grant permission to modify the resources that
you specify as targets in your experiment template. For a multi-account experiment, the experiment
role must grant the orchestrator role permission to assume the IAM role for each target account.
For more information, see [Permissions for multi-account experiments](multi-account-prerequisites.md#permissions "multi-account-prerequisites.md#permissions").

We recommend that you follow the standard security practice of granting least privilege.
You can do so by specifying specific resource ARNs or tags in your policies.

To help you get started with AWS FIS quickly, we provide AWS managed policies that you
can specify when you create an experiment role. Alternatively, you can also use these
policies as a model as you create your own inline policy documents.

###### Contents

- [Prerequisites](#create-fis-role-prereqs "#create-fis-role-prereqs")
- [Option 1: Create an experiment role and attach an AWS managed policy](#fis-role-managed-policy "#fis-role-managed-policy")
- [Option 2: Create an experiment role and add an inline policy document](#fis-role-inline-policy-document "#fis-role-inline-policy-document")

## Prerequisites

Before you begin, install the AWS CLI and create the required trust policy.

**Install the AWS CLI**

Before you begin, install and configure the AWS CLI. When you configure the AWS CLI,
you are prompted for AWS credentials. The examples in this procedure assume that
you also configured a default Region. Otherwise, add the `--region` option
to each command. For more information, see
[Installing or updating the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and
[Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

**Create a trust relationship policy**

An experiment role must have a trust relationship that allows the AWS FIS service to
assume the role. Create a text file named `fis-role-trust-policy.json`
and add the following trust relationship policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "fis.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

We recommend that you use the `aws:SourceAccount` and
`aws:SourceArn` condition keys to protect yourself against [the confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). The
source account is the owner of the experiment and the source ARN is the ARN of the
experiment. For example, you should add the following condition block to your trust
policy.

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "`account_id`"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:fis:`region`:`account_id`:experiment/*"
    }
}
```

**Add permissions to assume target account roles (multi-account experiments only)**

For multi-account experiments, you need permissions that allows orchestrator account to assume target account roles. You can modify the following example and add as an inline policy document to assume target account roles:

```
{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Resource":[
        "arn:aws:iam::`target_account_id`:role/`role_name`"
    ]
}
```

## Option 1: Create an experiment role and attach an AWS managed policy

Use one of the AWS managed policies from AWS FIS to get started quickly.

###### To create an experiment role and attach an AWS managed policy

1. Verify that there is a managed policy for the AWS FIS actions in your experiment.
   Otherwise, you'll need to create your own inline policy document instead.
   For more information, see [AWS managed policies for AWS Fault Injection Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
2. Use the following [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create a role and add the trust policy that
   you created in the prerequisites.

```
aws iam create-role --role-name `my-fis-role` --assume-role-policy-document file://`fis-role-trust-policy.json`
```

3. Use the following [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command to attach the AWS managed policy.

```
aws iam attach-role-policy --role-name `my-fis-role` --policy-arn `fis-policy-arn`
```

Where `fis-policy-arn` is one of the
following:

    * arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorEC2Access
    * arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorECSAccess
    * arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorEKSAccess
    * arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorNetworkAccess
    * arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorRDSAccess
    * arn:aws:iam::aws:policy/service-role/AWSFaultInjectionSimulatorSSMAccess

## Option 2: Create an experiment role and add an inline policy document

Use this option for actions that don't have a managed policy, or to include only the
permissions that are required for your specific experiment.

###### To create an experiment and add an inline policy document

1. Use the following [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create a role and add the trust policy that
   you created in the prerequisites.

```
aws iam create-role --role-name `my-fis-role` --assume-role-policy-document file://`fis-role-trust-policy.json`
```

2. Create a text file named `fis-role-permissions-policy.json`
   and add a permissions policy. For an example that you can use as a starting
   point, see the following.
   - Fault injection actions – Start
     from the following policy.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "AllowFISExperimentRoleFaultInjectionActions",
    "Effect": "Allow",
    "Action": [
    "fis:InjectApiInternalError",
    "fis:InjectApiThrottleError",
    "fis:InjectApiUnavailableError"
    ],
    "Resource": "arn:*:fis:*:*:experiment/*"
    }
    ]
   }`

   ```

   - Amazon EBS actions – Start from the
     following policy.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "ec2:DescribeVolumes"
    ],
    "Resource": "*"
    },
    {
    "Effect": "Allow",
    "Action": [
    "ec2:PauseVolumeIO"
    ],
    "Resource": "arn:aws:ec2:*:*:volume/*"
    }
    ]
   }`

   ```

   - Amazon EC2 actions – Start from the
     [AWSFaultInjectionSimulatorEC2Access](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.md") policy.
   - Amazon ECS actions – Start from the
     [AWSFaultInjectionSimulatorECSAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorECSAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorECSAccess.md") policy.
   - Amazon EKS actions – Start from the
     [AWSFaultInjectionSimulatorEKSAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.md") policy.
   - Network actions – Start from the
     [AWSFaultInjectionSimulatorNetworkAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.md") policy.
   - Amazon RDS actions – Start from the
     [AWSFaultInjectionSimulatorRDSAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorRDSAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorRDSAccess.md") policy.
   - Systems Manager actions – Start from the
     [AWSFaultInjectionSimulatorSSMAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorSSMAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorSSMAccess.md") policy.

3. Use the following [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md") command to add the permissions policy that you
   created in the previous step.

```
aws iam put-role-policy --role-name `my-fis-role` --policy-name `my-fis-policy` --policy-document file://`fis-role-permissions-policy.json`
```
