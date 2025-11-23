# Using service-linked roles for AWS Compute Optimizer

AWS Compute Optimizer uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role").
A service-linked role is a unique type of IAM role
that's
linked directly to Compute Optimizer. Service-linked roles are predefined by Compute Optimizer and
include all of the permissions that the service requires to call other
on your behalf.

With a service-linked role,setting
up Compute Optimizer
doesn't
require manually
adding
the necessary permissions. Compute Optimizer defines the permissions of its service-linked roles,
and unless defined otherwise, only Compute Optimizer can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Role** column. Choose a
**Yes** with a link to view the service-linked role documentation
for that service.

###### Topics

- [Service-linked role permissions for Compute Optimizer](#slr-permissions "#slr-permissions")
- [Service-linked role permissions](#service-linked-role-permissions "#service-linked-role-permissions")
- [Creating a Service-Linked Role for Compute Optimizer](#create-slr "#create-slr")
- [Editing a Service-Linked Role for Compute Optimizer](#edit-slr "#edit-slr")
- [Deleting a Service-Linked Role for Compute Optimizer](#delete-slr "#delete-slr")
- [Supported Regions for Compute Optimizer service-linked Roles](#slr-regions "#slr-regions")
- [Additional resources](#slr-resources "#slr-resources")

## Service-linked role permissions for Compute Optimizer

Compute Optimizer uses the service-linked role that's named **AWSServiceRoleForComputeOptimizer** to
access Amazon CloudWatch metrics for AWS resources in the account.

The AWSServiceRoleForComputeOptimizer service-linked role trusts the following services to assume the
role:

- `compute-optimizer.amazonaws.com`

The role permissions policy allows Compute Optimizer to complete the following actions on the
specified resources:

- Action: `cloudwatch:GetMetricData` on all AWS resources.
- Action: `cloudwatch:DescribeAlarms` on all AWS resources.
- Action: `organizations:DescribeOrganization` on all AWS resources.
- Action: `organizations:ListAccounts` on all AWS resources.
- Action: `organizations:ListAWSServiceAccessForOrganization` on all AWS
  resources.
- Action: `organizations:ListDelegatedAdministrators` on all AWS
  resources.
- Action: `autoscaling:DescribeAutoScalingInstances` on all AWS
  resources.
- Action: `autoscaling:DescribeAutoScalingGroups` on all AWS
  resources.
- Action: `autoscaling:DescribePolicies` on all AWS
  resources.
- Action: `autoscaling:DescribeScheduledActions` on all AWS
  resources.
- Action: `ec2:DescribeInstances` on all AWS
  resources.
- Action: `ec2:DescribeSnapshots` on all AWS
  resources.
- Action: `ec2:DescribeVolumesModifications` on all AWS
  resources.
- Action: `ec2:CreateVolume` on all AWS
  resources.
- Action: `ec2:ModifyVolume` on all AWS
  resources.
- Action: `ec2:DeleteVolume` on all AWS
  resources.
- Action: `ec2:CreateSnapshot` on all AWS
  resources.
- Action: `ec2:createTags` on all AWS
  resources.

## Service-linked role permissions

To create a service-linked role for Compute Optimizer, configure permissions to allow an IAM
entity (such as a user, group, or role) to create the service-linked role. For more
information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

**To allow an IAM entity to create a specific service-linked role for
Compute Optimizer**

Add the following policy to the IAM entity that needs to create the service-linked
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
 "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
 },
 {
 "Effect": "Allow",
 "Action": "iam:PutRolePolicy",
 "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
 },
 {
 "Effect": "Allow",
 "Action": "compute-optimizer:UpdateEnrollmentStatus",
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
 "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
 },
 {
 "Effect": "Allow",
 "Action": "iam:PutRolePolicy",
 "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
 },
 {
 "Effect": "Allow",
 "Action": "compute-optimizer:UpdateEnrollmentStatus",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "organizations:DescribeOrganization",
 "Resource": "*"
 }
 ]
}`

```

**To allow an IAM entity to create any service-linked
role**

Add the following statement to the permissions policy for the IAM entity that needs to
create a service-linked role, or any service role that includes the needed policies. This
policy attaches a policy to the role.

```
{
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "arn:aws:iam::*:role/aws-service-role/*"
}
```

**To allow Compute Optimizer to perform recommended actions on behalf of customers**

Add a statement to the permissions policy for the IAM entity that needs to
create a service-linked role, or any service role that includes the needed policies. This
policy attaches a policy to the role. For more information, see [AWS managed policy: ComputeOptimizerAutomationServiceRolePolicy](managed-policies.md#security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy "managed-policies.md#security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy") on the managed policy page.

## Creating a Service-Linked Role for Compute Optimizer

You don't need to manually create a service-linked role. When you
opt in to the Compute Optimizer service in the AWS Management Console, the AWS CLI, or the AWS API, Compute Optimizer creates
the service-linked role for you.

###### Important

If you completed an action in another service that uses the features supported by the service-linked
role, the role can appear in your
account. For more information, see [A
New Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you
delete this service-linked role, and then need to create it again,
you can use the same process to recreate the role in your account. When you
opt in to the Compute Optimizer service, Compute Optimizer creates the service-linked role for you again.

## Editing a Service-Linked Role for Compute Optimizer

Compute Optimizer
doesn't
allow you to edit the AWSServiceRoleForComputeOptimizer service-linked role. After you create a service-linked role,
you
can't
change the name of the role because various entities might reference the role. However, you
can edit the description of the role using IAM. For more information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a Service-Linked Role for Compute Optimizer

We recommend that,
if
you no longer need to use Compute Optimizer, you delete the AWSServiceRoleForComputeOptimizer service-linked
role.
That
way
you don’t have an unused entity
that's
not actively monitored or maintained. However,
before you can manually
delete the service-linked role, you must opt out of
Compute Optimizer.

**To opt out of Compute Optimizer**

For information about opting out of Compute Optimizer, see [Opting out of Compute Optimizer](account-opt-out.md "account-opt-out.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForComputeOptimizer service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for Compute Optimizer service-linked Roles

Compute Optimizer supports using service-linked roles in all of the Regions where the service
is available. To view the currently supported
AWS Regions
and endpoints for Compute Optimizer, see [Compute Optimizer Endpoints and
Quotas](../../../general/latest/gr/compute-optimizer.md "../../../general/latest/gr/compute-optimizer.md") in the _AWS General Reference_.

## Additional resources

- Troubleshooting — [Troubleshooting in Compute Optimizer](troubleshooting-account-opt-in.md "troubleshooting-account-opt-in.md")
- [AWS managed policies for AWS Compute Optimizer](managed-policies.md "managed-policies.md")
- [Opting in to AWS Compute Optimizer](account-opt-in.md "account-opt-in.md")
- [Identity and Access Management for AWS Compute Optimizer](security-iam.md "security-iam.md")
