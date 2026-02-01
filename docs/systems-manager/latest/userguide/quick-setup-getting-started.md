• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Getting started with Quick Setup

Use the information in this topic to help you prepare to use Quick Setup.

###### Topics

- [IAM roles and permissions for
  Quick Setup onboarding](#quick-setup-getting-started-iam "#quick-setup-getting-started-iam")
- [Manual onboarding for working
  with Quick Setup API programmatically](#quick-setup-api-manual-onboarding "#quick-setup-api-manual-onboarding")

## IAM roles and permissions for

Quick Setup onboarding

Quick Setup launched a new console experience and a new API. Now you can interact
with this API using the console, AWS CLI, CloudFormation, and SDKs. If you opt in to the new
experience, your existing configurations are recreated using the new API. Depending
on the number of existing configurations in your account, this process can take
several minutes.

To use the new Quick Setup console, you must have permissions for the following
actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm-quicksetup:*",
 "cloudformation:DescribeStackSetOperation",
 "cloudformation:ListStacks",
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackResources",
 "cloudformation:ListStackSetOperations",
 "cloudformation:ListStackInstances",
 "cloudformation:DescribeStackSet",
 "cloudformation:ListStackSets",
 "cloudformation:DescribeStackInstance",
 "cloudformation:DescribeOrganizationsAccess",
 "cloudformation:ActivateOrganizationsAccess",
 "cloudformation:GetTemplate",
 "cloudformation:ListStackSetOperationResults",
 "cloudformation:DescribeStackEvents",
 "cloudformation:UntagResource",
 "ec2:DescribeInstances",
 "ssm:DescribeAutomationExecutions",
 "ssm:GetAutomationExecution",
 "ssm:ListAssociations",
 "ssm:DescribeAssociation",
 "ssm:GetDocument",
 "ssm:ListDocuments",
 "ssm:DescribeDocument",
 "ssm:ListResourceDataSync",
 "ssm:DescribePatchBaselines",
 "ssm:GetPatchBaseline",
 "ssm:DescribeMaintenanceWindows",
 "ssm:DescribeMaintenanceWindowTasks",
 "ssm:GetOpsSummary",
 "organizations:DeregisterDelegatedAdministrator",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListRoots",
 "organizations:ListParents",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListAWSServiceAccessForOrganization",
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "resource-groups:ListGroups",
 "iam:ListRoles",
 "iam:ListRolePolicies",
 "iam:GetRole",
 "iam:CreatePolicy",
 "organizations:RegisterDelegatedAdministrator",
 "organizations:EnableAWSServiceAccess",
 "cloudformation:TagResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:RollbackStack",
 "cloudformation:CreateStack",
 "cloudformation:UpdateStack",
 "cloudformation:DeleteStack"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stack/StackSet-AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:stack/AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:type/resource/*",
 "arn:aws:cloudformation:*:*:stack/StackSet-SSMQuickSetup"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStackSet",
 "cloudformation:UpdateStackSet",
 "cloudformation:DeleteStackSet",
 "cloudformation:DeleteStackInstances",
 "cloudformation:CreateStackInstances",
 "cloudformation:StopStackSetOperation"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:*:stackset/AWS-QuickSetup-*",
 "arn:aws:cloudformation:*:*:stackset/SSMQuickSetup",
 "arn:aws:cloudformation:*:*:type/resource/*",
 "arn:aws:cloudformation:*:*:stackset-target/AWS-QuickSetup-*:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy",
 "iam:GetRolePolicy",
 "iam:PutRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AWS-QuickSetup-*",
 "arn:aws:iam::*:role/service-role/AWS-QuickSetup-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/AWS-QuickSetup-*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ssm-quicksetup.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:DeleteAssociation",
 "ssm:CreateAssociation",
 "ssm:StartAssociationsOnce"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ssm:StartAutomationExecution",
 "Resource": [
 "arn:aws:ssm:*:*:document/AWS-EnableExplorer",
 "arn:aws:ssm:*:*:automation-execution/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsSummary",
 "ssm:CreateResourceDataSync",
 "ssm:UpdateResourceDataSync"
 ],
 "Resource": "arn:aws:ssm:*:*:resource-data-sync/AWS-QuickSetup-*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "accountdiscovery.ssm.amazonaws.com",
 "ssm.amazonaws.com",
 "ssm-quicksetup.amazonaws.com",
 "stacksets.cloudformation.amazonaws.com"
 ]
 }
 },
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/stacksets.cloudformation.amazonaws.com/AWSServiceRoleForCloudFormationStackSetsOrgAdmin"
 }
 ]
}`

```

To restrict users to read-only permissions, only allow
`ssm-quicksetup:List*` and `ssm-quicksetup:Get*`
operations for the Quick Setup API.

During onboarding, Quick Setup creates the following AWS Identity and Access Management (IAM) roles on your
behalf:

- `AWS-QuickSetup-LocalExecutionRole` – Grants CloudFormation
  permissions to use any template, excluding the patch policy template, and
  create the necessary resources.
- `AWS-QuickSetup-LocalAdministrationRole` – Grants
  permissions to AWS CloudFormation to assume
  `AWS-QuickSetup-LocalExecutionRole`.
- `AWS-QuickSetup-PatchPolicy-LocalExecutionRole` – Grants
  permissions to AWS CloudFormation to use the patch policy template, and create the
  necessary resources.
- `AWS-QuickSetup-PatchPolicy-LocalAdministrationRole` –
  Grants permissions to AWS CloudFormation to assume
  `AWS-QuickSetup-PatchPolicy-LocalExecutionRole`.

If you're onboarding a management account—the account that you use to create
an organization in AWS Organizations—Quick Setup also creates the following roles on your
behalf:

- `AWS-QuickSetup-SSM-RoleForEnablingExplorer` – Grants
  permissions to the `AWS-EnableExplorer` automation runbook. The
  `AWS-EnableExplorer` runbook configures Explorer, a tool in
  Systems Manager, to display information for multiple AWS accounts and
  AWS Regions.
- `AWSServiceRoleForAmazonSSM` – A service-linked role
  that grants access to AWS resources managed and used by Systems Manager.
- `AWSServiceRoleForAmazonSSM_AccountDiscovery` – A
  service-linked role that grants permissions to Systems Manager to call AWS services
  to discover AWS account information when synchronizing data. For more
  information, see [Using roles to collect AWS account information for OpsCenter and Explorer](using-service-linked-roles-service-action-2.md "using-service-linked-roles-service-action-2.md").

When onboarding a management account, Quick Setup enables trusted access between
AWS Organizations and CloudFormation to deploy Quick Setup configurations across your organization.
To enable trusted access, your management account must have administrator
permissions. After onboarding, you no longer need administrator permissions. For
more information, see [Enable trusted access with Organizations](../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.md").

For information about AWS Organizations account types, see [AWS Organizations
terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the
_AWS Organizations User Guide_.

###### Note

Quick Setup uses CloudFormation StackSets to deploy your configurations across
AWS accounts and Regions. If the number of target accounts multiplied by the
number of Regions exceeds 10,000, the configuration fails to deploy. We
recommend reviewing your use case and creating configurations that use fewer
targets to accommodate the growth of your organization. Stack instances aren't
deployed to your organization's management account. For more information, see
[Considerations when creating a stack set with service-managed
permissions](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#stacksets-orgs-considerations "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md#stacksets-orgs-considerations").

## Manual onboarding for working

with Quick Setup API programmatically

If you use the console to work with Quick Setup, the service handles onboarding steps
for you. If you plan to use SDKs or the AWS CLI to work with the Quick Setup API, you can
still use the console to complete onboarding steps for you so you don't have to
perform them manually. However, some customers need to complete onboarding steps for
Quick Setup programmatically without interacting with the console. If this method fits
your use case, you must complete the following steps. All of these steps must be
completed from your AWS Organizations management account.

###### To complete manual onboarding for Quick Setup

1. Activate trusted access for CloudFormation with Organizations. This provides the
   management account with the permissions needed to create and manage StackSets
   for your organization. You can use CloudFormation's
   `ActivateOrganizationsAccess` API action to complete this
   step. For more information, see [ActivateOrganizationsAccess](../../../AWSCloudFormation/latest/APIReference/API_ActivateOrganizationsAccess.md "../../../AWSCloudFormation/latest/APIReference/API_ActivateOrganizationsAccess.md") in the
   _AWS CloudFormation API Reference_.
2. Enable the integration of Systems Manager with Organizations. This allows Systems Manager to create a
   service-linked role in all the accounts in your organization. This also
   allows Systems Manager to perform operations on your behalf in your organization and
   its accounts. You can use AWS Organizations's `EnableAWSServiceAccess` API
   action to complete this step. The service principal for Systems Manager is
   `ssm.amazonaws.com`.For more information, see [EnableAWSServiceAccess](../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md "../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md") in the
   _AWS Organizations API Reference_.
3. Create the required IAM role for Explorer. This allows Quick Setup to
   create dashboards for your configurations so you can view deployment and
   association statuses. Create an IAM role and attach the
   `AWSSystemsManagerEnableExplorerExecutionPolicy` managed
   policy. Modify the trust policy for the role to match the following. Replace
   each `account ID` with your information.

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
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:*:ssm:*:`111122223333`:automation-execution/*"
 }
 }
 }
 ]
}`

```

4. Update the Quick Setup service setting for Explorer. You can use Quick Setup's
   `UpdateServiceSettings` API action to complete this step.
   Specify the ARN for the IAM role you created in the previous step for the
   `ExplorerEnablingRoleArn` request parameter. For more
   information, see [UpdateServiceSettings](../../../quick-setup/latest/APIReference/API_UpdateServiceSettings.md "../../../quick-setup/latest/APIReference/API_UpdateServiceSettings.md") in the _Quick Setup API
   Reference_.
5. Create the required IAM roles for CloudFormation StackSets to use. You must
   create an _execution_ role and an
   _administration_ role.
   1. Create the execution role. The execution role should have at least
      one of the `AWSQuickSetupDeploymentRolePolicy` or
      `AWSQuickSetupPatchPolicyDeploymentRolePolicy`
      managed policies attached. If you're only creating patch policy
      configurations, you can use
      `AWSQuickSetupPatchPolicyDeploymentRolePolicy`
      managed policy. All other configurations use the
      `AWSQuickSetupDeploymentRolePolicy` policy. Modify
      the trust policy for the role to match the following. Replace each
      `account ID` and
      `administration role name` with your
      information.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "AWS": "arn:aws:iam::`111122223333`:role/`administration role name`"
    },
    "Action": "sts:AssumeRole"
    }
    ]
   }`

   ```

   2. Create the administration role. The permissions policy must match
      the following. Replace each `account ID`
      and `execution role name` with your
      information.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Action": [
    "sts:AssumeRole"
    ],
    "Resource": "arn:*:iam::`111122223333`:role/`execution role name`",
    "Effect": "Allow"
    }
    ]
   }`

   ```

   Modify the trust policy for the role to match the following.
   Replace each `account ID` with your
   information.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "cloudformation.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`111122223333`"
    },
    "ArnLike": {
    "aws:SourceArn": "arn:aws:cloudformation:*:`111122223333`:stackset/AWS-QuickSetup-*"
    }
    }
    }
    ]
   }`

   ```
