# Service-linked role permissions for GuardDuty

GuardDuty uses the service-linked role (SLR) named `AWSServiceRoleForAmazonGuardDuty`. The SLR
allows GuardDuty to perform the following tasks. It also allows GuardDuty to include the
retrieved metadata belonging to the EC2 instance in the findings that GuardDuty may generate
about the potential threat. The `AWSServiceRoleForAmazonGuardDuty` service-linked role trusts
the `guardduty.amazonaws.com` service to assume the role.

The permission policies help GuardDuty perform the following tasks:

- Use Amazon EC2 actions to manage and retrieve information about your EC2 instances,
  images, and networking components such as VPCs, subnets, and transit gateways.
- Use AWS Systems Manager actions to manage SSM associations on Amazon EC2 instances when you
  enable GuardDuty Runtime Monitoring with automated agent for Amazon EC2. When GuardDuty automated agent
  configuration is disabled, GuardDuty considers only those EC2 instances that have an
  inclusion tag (`GuardDutyManaged`:`true`).
- Use AWS Organizations actions to describe associated accounts and organization
  ID.
- Use Amazon S3 actions to retrieve information about S3 buckets and objects.
- Use AWS Lambda actions to retrieve information about your Lambda functions and
  tags.
- Use Amazon EKS actions to manage and retrieve information about the EKS clusters
  and manage [Amazon EKS add-ons](../../../eks/latest/userguide/eks-add-ons.md "../../../eks/latest/userguide/eks-add-ons.md") on EKS
  clusters. The EKS actions also retrieve the information about the tags
  associated to GuardDuty.
- Use IAM to create the [Service-linked role permissions for
  Malware Protection for EC2](slr-permissions-malware-protection.md "slr-permissions-malware-protection.md") after Malware Protection for EC2 has been
  enabled.
- Use Amazon ECS actions to manage and retrieve information about the Amazon ECS clusters,
  and manage the Amazon ECS account setting with `guarddutyActivate`. The
  actions pertaining to Amazon ECS also retrieve the information about the tags
  associated with GuardDuty.
  The role is configured with the following [AWS managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md"), named
  `AmazonGuardDutyServiceRolePolicy`.

To review the permissions for this policy, see [AmazonGuardDutyServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonGuardDutyServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonGuardDutyServiceRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

The following is the trust policy that is attached to the `AWSServiceRoleForAmazonGuardDuty`
service-linked role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "guardduty.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For details about updates to the `AmazonGuardDutyServiceRolePolicy` policy, see [GuardDuty updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates"). For automatic alerts about changes
to this policy, subscribe to the RSS feed on the [Document history](doc-history.md "doc-history.md") page.

## Creating a service-linked role for GuardDuty

The `AWSServiceRoleForAmazonGuardDuty` service-linked role is automatically created when
you enable GuardDuty for the first time or enable GuardDuty in a supported Region where you
previously didn't have it enabled. You can also create the service-linked
role manually using the IAM console, the AWS CLI, or the IAM API.

###### Important

The service-linked role that is created for the GuardDuty delegated administrator
account doesn't apply to the member GuardDuty accounts.

You must configure permissions to allow an IAM principal (such as a user, group,
or role) to create, edit, or delete a service-linked role. For the
`AWSServiceRoleForAmazonGuardDuty` service-linked role to be successfully created, the
IAM principal that you use GuardDuty with must have the required permissions. To grant
the required permissions, attach the following policy to this user, group, or role:

###### Note

Replace the sample `account ID` in the following
example with your actual AWS account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "guardduty:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "guardduty.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty"
 }
 ]
}`

```

For more information about creating the role manually, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_.

## Editing a service-linked role for GuardDuty

GuardDuty doesn't allow you to edit the `AWSServiceRoleForAmazonGuardDuty` service-linked
role. After you create a service-linked role, you can't change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for GuardDuty

If you no longer need to use a feature or service that requires a service-linked
role, we recommend that you delete that role. That way you don't have an unused
entity that isn't actively monitored or maintained.

###### Important

If you have enabled Malware Protection for EC2, deleting `AWSServiceRoleForAmazonGuardDuty` doesn't
automatically delete `AWSServiceRoleForAmazonGuardDutyMalwareProtection`. If you want to delete
`AWSServiceRoleForAmazonGuardDutyMalwareProtection`, see [Deleting a
service-linked role for Malware Protection for EC2](slr-permissions-malware-protection.md#delete-slr "slr-permissions-malware-protection.md#delete-slr").

You must first disable GuardDuty in all Regions where it is enabled in order to delete
the `AWSServiceRoleForAmazonGuardDuty`. If the GuardDuty service isn't disabled when you try to
delete the service-linked role, the deletion fails. For more information, see [Suspending or disabling GuardDuty](guardduty_suspend-disable.md "guardduty_suspend-disable.md").

When you disable GuardDuty, the `AWSServiceRoleForAmazonGuardDuty` doesn't get deleted
automatically. If you enable GuardDuty again, it'll start using the existing
`AWSServiceRoleForAmazonGuardDuty`.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the IAM API to delete the
`AWSServiceRoleForAmazonGuardDuty` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported AWS Regions

Amazon GuardDuty supports using the `AWSServiceRoleForAmazonGuardDuty` service-linked role in all
the AWS Regions where GuardDuty is available. For a list of Regions where GuardDuty is
currently available, see [Amazon GuardDuty endpoints and quotas](../../../general/latest/gr/guardduty.md "../../../general/latest/gr/guardduty.md") in
the _Amazon Web Services General Reference_.
