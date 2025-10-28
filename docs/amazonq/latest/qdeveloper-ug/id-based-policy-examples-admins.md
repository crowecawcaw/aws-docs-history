# Administrator permissions

The following policies allow Amazon Q Developer administrators to perform administrative tasks in
the Amazon Q subscription management console and Amazon Q Developer console.

For policies that enable the use of Amazon Q Developer features, see [User permissions](id-based-policy-examples-users.md "id-based-policy-examples-users.md").

## Allow administrators to use the Amazon Q console

The following example policy grants permissions for a user to perform actions in the Amazon Q console. The
Amazon Q console is where you configure Amazon Q's integration with AWS IAM Identity Center and AWS Organizations. Most other
Amazon Q Developer-related tasks must be completed in the Amazon Q Developer console. For more information, see [Allow administrators to use the Amazon Q Developer console](#q-admin-setup-admin-users "#q-admin-setup-admin-users").

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DisableAWSServiceAccess",
 "organizations:EnableAWSServiceAccess",
 "organizations:DescribeOrganization"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "sso:ListApplications",
 "sso:ListInstances",
 "sso:DescribeRegisteredRegions",
 "sso:GetSharedSsoConfiguration",
 "sso:DescribeInstance",
 "sso:CreateInstance",
 "sso:CreateApplication",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationAssignmentConfiguration",
 "sso:PutApplicationGrant",
 "sso:PutApplicationAccessScope",
 "sso:DescribeApplication",
 "sso:DeleteApplication",
 "sso:GetSSOStatus",
 "sso:CreateApplicationAssignment",
 "sso:DeleteApplicationAssignment",
 "sso:UpdateApplication"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "sso-directory:DescribeUsers",
 "sso-directory:DescribeGroups",
 "sso-directory:SearchGroups",
 "sso-directory:SearchUsers",
 "sso-directory:DescribeGroup",
 "sso-directory:DescribeUser",
 "sso-directory:DescribeDirectory"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "signin:ListTrustedIdentityPropagationApplicationsForConsole",
 "signin:CreateTrustedIdentityPropagationApplicationForConsole"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "codewhisperer:ListProfiles",
 "codewhisperer:CreateProfile",
 "codewhisperer:DeleteProfile"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "user-subscriptions:ListClaims",
 "user-subscriptions:ListUserSubscriptions",
 "user-subscriptions:CreateClaim",
 "user-subscriptions:DeleteClaim",
 "user-subscriptions:UpdateClaim"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "q:CreateAssignment",
 "q:DeleteAssignment"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "iam:CreateServiceLinkedRole"
 ],
 "Resource":[
 "arn:aws:iam::*:role/aws-service-role/user-subscriptions.amazonaws.com/AWSServiceRoleForUserSubscriptions"
 ]
 }
 ]
}`

```

## Allow administrators to use the Amazon Q Developer console

The following example policy grants permissions for a user to access the Amazon Q Developer console. In the
Amazon Q Developer console, administrators perform most Amazon Q Developer-related configuration tasks, including
tasks related to subscriptions, code references, customizations, and chat plugins. This policy also includes permissions to
create and configure customer managed KMS keys.

There are a few Amazon Q Developer Pro tasks that administrators must complete through the Amazon Q console (instead of the
Amazon Q Developer console). For more information, see [Allow administrators to use the Amazon Q console](#q-admin-setup-admin-users-sub "#q-admin-setup-admin-users-sub").

###### Note

To create customizations or plugins, your Amazon Q Developer Pro administrator will require additional
permissions.

- For permissions needed for customizations, see [Prerequisites for customizations](customizations-prereq.md "customizations-prereq.md").
- For permissions needed for plugins, see [Allow administrators to configure
  plugins](#id-based-policy-examples-admin-plugins "#id-based-policy-examples-admin-plugins").

You will need one of two policies to use the Amazon Q Developer console. The policy you need depends on if
you're setting up Amazon Q Developer for the first time or if you're configuring a legacy Amazon CodeWhisperer profile.

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

For new administrators of Amazon Q Developer, use the following policy:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso:ListInstances",
 "sso:CreateInstance",
 "sso:CreateApplication",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant",
 "sso:PutApplicationAssignmentConfiguration",
 "sso:ListApplications",
 "sso:GetSharedSsoConfiguration",
 "sso:DescribeInstance",
 "sso:PutApplicationAccessScope",
 "sso:DescribeApplication",
 "sso:DeleteApplication",
 "sso:CreateApplicationAssignment",
 "sso:DeleteApplicationAssignment",
 "sso:UpdateApplication",
 "sso:DescribeRegisteredRegions",
 "sso:GetSSOStatus"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "identitystore:DescribeUser"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sso-directory:GetUserPoolInfo",
 "sso-directory:DescribeUsers",
 "sso-directory:DescribeGroups",
 "sso-directory:SearchGroups",
 "sso-directory:SearchUsers",
 "sso-directory:DescribeDirectory"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "signin:ListTrustedIdentityPropagationApplicationsForConsole",
 "signin:CreateTrustedIdentityPropagationApplicationForConsole"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "user-subscriptions:ListClaims",
 "user-subscriptions:ListApplicationClaims",
 "user-subscriptions:ListUserSubscriptions",
 "user-subscriptions:CreateClaim",
 "user-subscriptions:DeleteClaim",
 "user-subscriptions:UpdateClaim"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DisableAWSServiceAccess",
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases",
 "kms:CreateGrant",
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey*",
 "kms:RetireGrant",
 "kms:DescribeKey"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-security:UpdateAccountConfiguration"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/q.amazonaws.com/AWSServiceRoleForAmazonQDeveloper"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codewhisperer:UpdateProfile",
 "codewhisperer:ListProfiles",
 "codewhisperer:TagResource",
 "codewhisperer:UnTagResource",
 "codewhisperer:ListTagsForResource",
 "codewhisperer:CreateProfile"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "q:ListDashboardMetrics",
 "q:CreateAssignment",
 "q:DeleteAssignment"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

[Show moreShow less](# "#")
For legacy Amazon CodeWhisperer profiles, the following policy will enable an IAM principal to administer a
CodeWhisperer application.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso-directory:SearchUsers",
 "sso-directory:SearchGroups",
 "sso-directory:GetUserPoolInfo",
 "sso-directory:DescribeDirectory",
 "sso-directory:ListMembersInGroup"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "pricing:GetProducts"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sso:AssociateProfile",
 "sso:DisassociateProfile",
 "sso:GetProfile",
 "sso:ListProfiles",
 "sso:ListApplicationInstances",
 "sso:GetApplicationInstance",
 "sso:CreateManagedApplicationInstance",
 "sso:GetManagedApplicationInstance",
 "sso:ListProfileAssociations",
 "sso:GetSharedSsoConfiguration",
 "sso:ListDirectoryAssociations",
 "sso:DescribeRegisteredRegions",
 "sso:GetSsoConfiguration",
 "sso:GetSSOStatus"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "identitystore:ListUsers",
 "identitystore:ListGroups"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases",
 "kms:CreateGrant",
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey*",
 "kms:RetireGrant",
 "kms:DescribeKey"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-security:UpdateAccountConfiguration"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/q.amazonaws.com/AWSServiceRoleForAmazonQDeveloper"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codewhisperer:UpdateProfile",
 "codewhisperer:ListProfiles",
 "codewhisperer:TagResource",
 "codewhisperer:UnTagResource",
 "codewhisperer:ListTagsForResource",
 "codewhisperer:CreateProfile"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "q:ListDashboardMetrics",
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

[Show moreShow less](# "#")

## Allow administrators to

create customizations

The following policy grants administrators permission to create and manage customizations
in Amazon Q Developer.

To configure customizations in the Amazon Q Developer console, your Amazon Q Developer administrator will
require access to the Amazon Q Developer console. For more information, see [Allow administrators to use the Amazon Q Developer console](#q-admin-setup-admin-users "#q-admin-setup-admin-users").

###### Note

In the following policy, the IAM service will report errors on the
`codeconnections:ListOwners` and
`codeconnections:ListRepositories` permissions. Create the policy with
these permissions anyway. The permissions are required, and the policy will work despite
the errors.

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

In the following example, replace `account number` with your
AWS account number.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso-directory:DescribeUsers"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codewhisperer:CreateCustomization",
 "codewhisperer:DeleteCustomization",
 "codewhisperer:ListCustomizations",
 "codewhisperer:ListCustomizationVersions",
 "codewhisperer:UpdateCustomization",
 "codewhisperer:GetCustomization",
 "codewhisperer:ListCustomizationPermissions",
 "codewhisperer:AssociateCustomizationPermission",
 "codewhisperer:DisassociateCustomizationPermission"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codeconnections:ListOwners",
 "codeconnections:ListRepositories",
 "codeconnections:ListConnections",
 "codeconnections:GetConnection"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "codeconnections:UseConnection",
 "Resource": [
 "*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "codeconnections:ProviderAction": [
 "GitPull",
 "ListRepositories",
 "ListOwners"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject*",
 "s3:GetBucket*",
 "s3:ListBucket*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Allow administrators to configure

plugins

The following example policy grants administrators permissions to view and configure
third party plugins in the Amazon Q Developer console.

###### Note

In order to access the Amazon Q Developer console, administrators also need the permissions
defined in [Allow administrators to use the Amazon Q Developer console](#q-admin-setup-admin-users "#q-admin-setup-admin-users").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "q:CreatePlugin",
 "q:GetPlugin",
 "q:DeletePlugin",
 "q:ListPlugins",
 "q:ListPluginProviders",
 "q:UpdatePlugin",
 "q:CreateAuthGrant",
 "q:CreateOAuthAppConnection",
 "q:SendEvent",
 "q:UpdateAuthGrant",
 "q:UpdateOAuthAppConnection",
 "q:UpdatePlugin",
 "iam:CreateRole",
 "secretsmanager:CreateSecret"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "q.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Allow administrators

to configure plugins from one provider

The following example policy grants an administrator permission to configure plugins from
one provider, specified by the plugin ARN with the name of the plugin provider and a
wildcard character (`*`). To use this policy, replace the following in the ARN in
the Resource field:

- `AWS-region` – The AWS Region where the plugin
  will be created.
- `AWS-account-ID` – The AWS account ID of the
  account where your plugin is configured.
- `plugin-provider` – The name of the plugin provider
  that you want to allow configuration for, like `CloudZero`,
  `Datadog`, or `Wiz`. The plugin provider field is case
  sensitive.

###### Note

In order to access the Amazon Q Developer console, administrators also need the permissions
defined in [Allow administrators to use the Amazon Q Developer console](#q-admin-setup-admin-users "#q-admin-setup-admin-users").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateProviderPlugin",
 "Effect": "Allow",
 "Action": [
 "q:CreatePlugin",
 "q:GetPlugin",
 "q:DeletePlugin"
 ],
 "Resource": "arn:aws:qdeveloper:`us-east-1`:`111122223333`:plugin/`plugin-provider`/*"
 }
 ]
}`

```

## Allow migration of more than one network or

more than one subnet

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "MGNNetworkMigrationAnalyzerEC2ResourceSgTag",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:vpc/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/CreatedBy": "AWSApplicationMigrationService"
 }
 }
 },
 {
 "Sid": "MGNNetworkMigrationAnalyzerEC2RequestSgTag",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group-rule/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/CreatedBy": "AWSApplicationMigrationService"
 }
 }
 },

 {
 "Sid": "MGNNetworkMigrationAnalyzerEC2SecurityGroupTags",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group-rule/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-insights-path/*",
 "arn:aws:ec2:`us-east-1`:`111122223333`:network-insights-analysis/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/CreatedBy": "AWSApplicationMigrationService",
 "ec2:CreateAction": [
 "CreateSecurityGroup",
 "CreateNetworkInterface",
 "CreateNetworkInsightsPath",
 "StartNetworkInsightsAnalysis"
 ]
 }
 }
 },
 {
 "Sid": "MGNNetworkMigrationAnalyzerENIResourceTag",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:subnet/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/CreatedBy": "AWSApplicationMigrationService"
 }
 }
 },
 {
 "Sid": "MGNNetworkMigrationAnalyzerENISG",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:security-group/*"
 ]
 },
 {
 "Sid": "MGNNetworkMigrationAnalyzerEC2ResourceTag",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInsightsPath"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/CreatedBy": "AWSApplicationMigrationService"
 }
 }
 },
 {
 "Sid": "MGNNetworkMigAnalyzerEC2RequestTag",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInsightsPath",
 "ec2:StartNetworkInsightsAnalysis"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/CreatedBy": "AWSApplicationMigrationService"
 }
 }
 },
 {
 "Sid": "MGNNetworkMigrationAnalyzeNetwork",
 "Effect": "Allow",
 "Action": [
 "ec2:StartNetworkInsightsAnalysis"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
