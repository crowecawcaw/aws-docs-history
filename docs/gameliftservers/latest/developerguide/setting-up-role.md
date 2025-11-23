# Set up an IAM service role for Amazon GameLift Servers

Some Amazon GameLift Servers features require you to extend limited access to other AWS resources that you
own. You can do this by creating an AWS Identity and Access Management (IAM) role.

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.

This topic covers how to create a role that you can use with your Amazon GameLift Servers managed fleets. If
you use Amazon GameLift Servers FleetIQ to optimize game hosting on your Amazon Elastic Compute Cloud (Amazon EC2) instances, see
[Set up your AWS account for Amazon GameLift Servers FleetIQ](../fleetiqguide/gsg-iam-permissions.md "../fleetiqguide/gsg-iam-permissions.md").

In the following procedure, create a role with a custom permissions policy and a trust
policy that allows Amazon GameLift Servers to assume the role.

## Create an IAM service role for an Amazon GameLift Servers managed EC2

fleet

**Step 1: Create a permissions policy.**

Use the instructions and examples on this page to create a custom permissions policy for the type of Amazon GameLift Servers fleet you're working with.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter or paste a JSON policy document. For details about the IAM policy language, see
[IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md"). 6. Resolve any security warnings, errors, or general warnings generated during [policy validation](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md"), and then choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON
or YAML policy template that you can use in CloudFormation templates.

To do this, in the **Policy editor** choose
**Actions**, and then choose **Generate CloudFormation
template**. To learn more about CloudFormation, see [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_. 8. When you are finished adding permissions to the policy, choose
**Next**. 9. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 10. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 11. Choose **Create policy** to save your new policy.

**Step 2: Create a role that Amazon GameLift Servers can assume.**

###### To create an IAM role

1. In the navigation pane of the IAM console, choose **Roles**, and then choose
   **Create role**.
2. On the **Select trusted entity** page, choose the **Custom trust
   policy** option. This selection opens the **Custom trust
   policy** editor.
3. Replace the default JSON syntax with the following, and then choose
   **Next** to continue.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "gamelift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

4. On the **Add permissions** page, locate and select the
   permissions policy that you created in Step 1. Choose **Next**
   to continue.
5. On the **Name, review and create** page, enter a
   **Role name** and a **Description**
   (optional) for the role that you are creating. Review the **Trust
   entities** and **Added permissions**.
6. Choose **Create role** to save your new role.

## Create an IAM role for Amazon GameLift Servers managed

containers

If you're using Amazon GameLift Servers managed containers, you need to create an IAM service role for
use with a container fleet. This role grants limited permissions that Amazon GameLift Servers needs to
manage your container fleet resources and take actions on your behalf.

###### To create an IAM role for a container fleet

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**,
   and then choose **Create role**.
3. On **Select trusted entity** page, choose **AWS
   service** and select the **Use case** "GameLift".
   Choose **Next**
4. On **Add permissions**, choose the managed policy
   `GameLiftContainerFleetPolicy`. Choose **Next**.
   See [AWS managed policies for Amazon GameLift Servers](security-iam-awsmanpol.md "security-iam-awsmanpol.md")for more information about this
   policy.
5. On **Name, review, and create**, enter a role name and choose
   **Create role** to save the new role.

## Permission policy syntax

- **Permissions for Amazon GameLift Servers to assume the service
  role**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "gamelift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

- **Permissions to access AWS Regions that aren't enabled by
  default**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "gamelift.amazonaws.com",
 "gamelift.ap-east-1.amazonaws.com",
 "gamelift.me-south-1.amazonaws.com",
 "gamelift.af-south-1.amazonaws.com",
 "gamelift.eu-south-1.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
