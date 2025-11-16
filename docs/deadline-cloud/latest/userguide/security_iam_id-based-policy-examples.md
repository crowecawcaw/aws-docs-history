# Identity-based policy examples for

Deadline Cloud

By default, users and roles don't have permission to create or modify Deadline Cloud
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Deadline Cloud, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Deadline Cloud](../../../service-authorization/latest/reference/list_deadline.md "../../../service-authorization/latest/reference/list_deadline.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Deadline Cloud
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Policy to access the console](#security_iam_id-based-policy-console-access "#security_iam_id-based-policy-console-access")
- [Policy to submit
  jobs to a queue](#security_iam_id-based-policy-examples-submit-jobs "#security_iam_id-based-policy-examples-submit-jobs")
- [Policy to allow
  creating a license endpoint](#security_iam-id-based-policy-examples-create-endpoint "#security_iam-id-based-policy-examples-create-endpoint")
- [Policy to allow
  monitoring a specific farm queue](#security_iam-id-based-policy-examples-monitor-queue "#security_iam-id-based-policy-examples-monitor-queue")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Deadline Cloud resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the Deadline Cloud

console

To access the AWS Deadline Cloud console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Deadline Cloud resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Deadline Cloud console, also attach the
Deadline Cloud `ConsoleAccess`
or `ReadOnly` AWS managed
policy to the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Policy to access the console

To grant access to all functionality in the Deadline Cloud console, attach this identity policy
to a user or role you want to have full access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "EC2InstanceTypeSelection",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstanceTypeOfferings",
 "ec2:DescribeInstanceTypes",
 "ec2:GetInstanceTypesFromInstanceRequirements",
 "pricing:GetProducts"
 ],
 "Resource": ["*"]
 },
 {
 "Sid": "VPCResourceSelection",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": ["*"]
 },
 {
 "Sid": "ViewVpcLatticeResources",
 "Effect": "Allow",
 "Action": [
 "vpc-lattice:ListResourceConfigurations",
 "vpc-lattice:GetResourceConfiguration",
 "vpc-lattice:GetResourceGateway"
 ],
 "Resource": ["*"]
 },
 {
 "Sid": "ManageVpcEndpointsViaDeadline",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeVpcEndpoints",
 "ec2:DeleteVpcEndpoints",
 "ec2:CreateTags"
 ],
 "Resource": ["*"],
 "Condition": {
 "StringEquals": { "aws:CalledViaFirst": "deadline.amazonaws.com" }
 }
 },
 {
 "Sid": "ChooseJobAttachmentsBucket",
 "Effect": "Allow",
 "Action": ["s3:GetBucketLocation", "s3:ListAllMyBuckets"],
 "Resource": "*"
 },
 {
 "Sid": "CreateDeadlineCloudLogGroups",
 "Effect": "Allow",
 "Action": ["logs:CreateLogGroup"],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/deadline/*",
 "Condition": {
 "StringLike": { "aws:CalledViaFirst": "deadline.amazonaws.com" }
 }
 },
 {
 "Sid": "ValidateDependencies",
 "Effect": "Allow",
 "Action": ["s3:ListBucket"],
 "Resource": "*",
 "Condition": {
 "StringLike": { "aws:CalledViaFirst": "deadline.amazonaws.com" }
 }
 },
 {
 "Sid": "RoleSelection",
 "Effect": "Allow",
 "Action": ["iam:GetRole", "iam:ListRoles"],
 "Resource": "*"
 },
 {
 "Sid": "PassRoleToDeadlineCloud",
 "Effect": "Allow",
 "Action": ["iam:PassRole"],
 "Condition": {
 "StringLike": { "iam:PassedToService": "deadline.amazonaws.com" }
 },
 "Resource": "*"
 },
 {
 "Sid": "KMSKeySelection",
 "Effect": "Allow",
 "Action": ["kms:ListKeys", "kms:ListAliases"],
 "Resource": "*"
 },
 {
 "Sid": "IdentityStoreReadOnly",
 "Effect": "Allow",
 "Action": [
 "identitystore:DescribeUser",
 "identitystore:DescribeGroup",
 "identitystore:ListGroups",
 "identitystore:ListUsers",
 "identitystore:IsMemberInGroups",
 "identitystore:ListGroupMemberships",
 "identitystore:ListGroupMembershipsForMember",
 "identitystore:GetGroupMembershipId"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrganizationAndIdentityCenterIdentification",
 "Effect": "Allow",
 "Action": [
 "sso:ListDirectoryAssociations",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "sso:DescribeRegisteredRegions",
 "sso:GetManagedApplicationInstance",
 "sso:GetSharedSsoConfiguration",
 "sso:ListInstances",
 "sso:GetApplicationAssignmentConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ManagedDeadlineCloudIDCApplication",
 "Effect": "Allow",
 "Action": [
 "sso:CreateApplication",
 "sso:PutApplicationAssignmentConfiguration",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant",
 "sso:DeleteApplication",
 "sso:UpdateApplication"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": { "aws:CalledViaFirst": "deadline.amazonaws.com" }
 }
 },
 {
 "Sid": "ChooseSecret",
 "Effect": "Allow",
 "Action": ["secretsmanager:ListSecrets"],
 "Resource": "*"
 },
 {
 "Sid": "DeadlineMembershipActions",
 "Effect": "Allow",
 "Action": [
 "deadline:AssociateMemberToFarm",
 "deadline:AssociateMemberToFleet",
 "deadline:AssociateMemberToQueue",
 "deadline:AssociateMemberToJob",
 "deadline:DisassociateMemberFromFarm",
 "deadline:DisassociateMemberFromFleet",
 "deadline:DisassociateMemberFromQueue",
 "deadline:DisassociateMemberFromJob",
 "deadline:ListFarmMembers",
 "deadline:ListFleetMembers",
 "deadline:ListQueueMembers",
 "deadline:ListJobMembers"
 ],
 "Resource": ["*"]
 },
 {
 "Sid": "DeadlineControlPlaneActions",
 "Effect": "Allow",
 "Action": [
 "deadline:CreateMonitor",
 "deadline:GetMonitor",
 "deadline:UpdateMonitor",
 "deadline:DeleteMonitor",
 "deadline:ListMonitors",
 "deadline:CreateFarm",
 "deadline:GetFarm",
 "deadline:UpdateFarm",
 "deadline:DeleteFarm",
 "deadline:ListFarms",
 "deadline:CreateQueue",
 "deadline:GetQueue",
 "deadline:UpdateQueue",
 "deadline:DeleteQueue",
 "deadline:ListQueues",
 "deadline:CreateFleet",
 "deadline:GetFleet",
 "deadline:UpdateFleet",
 "deadline:DeleteFleet",
 "deadline:ListFleets",
 "deadline:ListWorkers",
 "deadline:CreateQueueFleetAssociation",
 "deadline:GetQueueFleetAssociation",
 "deadline:UpdateQueueFleetAssociation",
 "deadline:DeleteQueueFleetAssociation",
 "deadline:ListQueueFleetAssociations",
 "deadline:CreateQueueEnvironment",
 "deadline:GetQueueEnvironment",
 "deadline:UpdateQueueEnvironment",
 "deadline:DeleteQueueEnvironment",
 "deadline:ListQueueEnvironments",
 "deadline:CreateLimit",
 "deadline:GetLimit",
 "deadline:UpdateLimit",
 "deadline:DeleteLimit",
 "deadline:ListLimits",
 "deadline:CreateQueueLimitAssociation",
 "deadline:GetQueueLimitAssociation",
 "deadline:DeleteQueueLimitAssociation",
 "deadline:UpdateQueueLimitAssociation",
 "deadline:ListQueueLimitAssociations",
 "deadline:CreateStorageProfile",
 "deadline:GetStorageProfile",
 "deadline:UpdateStorageProfile",
 "deadline:DeleteStorageProfile",
 "deadline:ListStorageProfiles",
 "deadline:ListStorageProfilesForQueue",
 "deadline:ListBudgets",
 "deadline:TagResource",
 "deadline:UntagResource",
 "deadline:ListTagsForResource",
 "deadline:CreateLicenseEndpoint",
 "deadline:GetLicenseEndpoint",
 "deadline:DeleteLicenseEndpoint",
 "deadline:ListLicenseEndpoints",
 "deadline:ListAvailableMeteredProducts",
 "deadline:ListMeteredProducts",
 "deadline:PutMeteredProduct",
 "deadline:DeleteMeteredProduct"
 ],
 "Resource": ["*"]
 }]
}`

```

## Policy to submit

jobs to a queue

In this example, you create a scoped-down policy that grants permission to submit
jobs to a specific queue in a specific farm.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SubmitJobsFarmAndQueue",
 "Effect": "Allow",
 "Action": "deadline:CreateJob",
 "Resource": "arn:aws:deadline:`us-east-1`:`111122223333`:farm/`FARM_A`/queue/`QUEUE_B`/job/*"
 }
 ]
}`

```

## Policy to allow

creating a license endpoint

In this example, you create a scoped-down policy that grants the required permissions
to create and manage license endpoints. Use this policy to create the license
endpoint for the VPC associated with your farm.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "CreateLicenseEndpoint",
 "Effect": "Allow",
 "Action": [
 "deadline:CreateLicenseEndpoint",
 "deadline:DeleteLicenseEndpoint",
 "deadline:GetLicenseEndpoint",
 "deadline:ListLicenseEndpoints",
 "deadline:PutMeteredProduct",
 "deadline:DeleteMeteredProduct",
 "deadline:ListMeteredProducts",
 "deadline:ListAvailableMeteredProducts",
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeVpcEndpoints",
 "ec2:DeleteVpcEndpoints"
 ],
 "Resource": [
 "arn:aws:deadline:*:`111122223333`:*",
 "arn:aws:ec2:*:`111122223333`:vpc-endpoint/*"
 ]
 }]
}`

```

## Policy to allow

monitoring a specific farm queue

In this example, you create a scoped-down policy that grants permission to monitor
jobs in a specific queue for a specific farm.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "MonitorJobsFarmAndQueue",
 "Effect": "Allow",
 "Action": [
 "deadline:SearchJobs",
 "deadline:ListJobs",
 "deadline:GetJob",
 "deadline:SearchSteps",
 "deadline:ListSteps",
 "deadline:ListStepConsumers",
 "deadline:ListStepDependencies",
 "deadline:GetStep",
 "deadline:SearchTasks",
 "deadline:ListTasks",
 "deadline:GetTask",
 "deadline:ListSessions",
 "deadline:GetSession",
 "deadline:ListSessionActions",
 "deadline:GetSessionAction"
 ],
 "Resource": [
 "arn:aws:deadline:`us-east-1`:`123456789012`:farm/`FARM_A`/queue/`QUEUE_B`",
 "arn:aws:deadline:`us-east-1`:`123456789012`:farm/`FARM_A`/queue/`QUEUE_B`/*"
 ]
 }]
}`

```
