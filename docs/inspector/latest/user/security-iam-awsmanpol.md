# AWS managed policies for Amazon Inspector

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AmazonInspector2FullAccess_v2

You can attach the `AmazonInspector2FullAccess_v2` policy to your IAM identities.

This policy grants full access to Amazon Inspector and access to other related services.

**Permissions details**

This policy includes the following permissions.

- `inspector2` – Allows complete access to Amazon Inspector APIs.
- `codeguru-security` – Allows administrators to retrieve security findings and configuration settings for an account.
- `iam` – Allows Amazon Inspector to create the service-linked roles `AWSServiceRoleForAmazonInspector2` and `AWSServiceRoleForAmazonInspector2Agentless`.
  `AWSServiceRoleForAmazonInspector2` is required for Amazon Inspector to perform operations like retrieving information about Amazon EC2 instances, Amazon ECR repositories, and Amazon ECR container images.
  It's also required to decrypt Amazon EBS snapshots encrypted with AWS KMS keys.
  For more information, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md "using-service-linked-roles.md").
- `organizations` – `AllowServicePrincipalBasedAccessToOrganizationApis` allows only service principals to create service-linked roles for AWS accounts, register an AWS account as a delegated administrator for an organization, and list delegated administrators in an organization.
  `AllowOrganizationalBasedAccessToOrganizationApis` allows the policy holder to retrieve information, specifically resource-level ARNs, about an organizational unit.
  `AllowAccountsBasedAccessToOrganizationApis` allows the policy holder to retrieve information, specifically resource-level ARNs, about an AWS account.
  `AllowAccessToOrganizationApis` allows the policy holder to view AWS services integrated with an organization and organization information.

###### Note

Amazon Inspector no longer uses CodeGuru to perform Lambda scans.
AWS will discontinue support for CodeGuru on November 20, 2025.
For more information, see [End of support for CodeGuru Security](../../../codeguru/latest/security-ug/end-of-support.md "../../../codeguru/latest/security-ug/end-of-support.md").
Amazon Inspector now uses Amazon Q to perform Lambda scans and does not require the permissions described in this section.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "AllowFullAccessToInspectorApis",
 "Effect" : "Allow",
 "Action" : "inspector2:*",
 "Resource" : "*"
 },
 {
 "Sid" : "AllowAccessToCodeGuruApis",
 "Effect" : "Allow",
 "Action" : [
 "codeguru-security:BatchGetFindings",
 "codeguru-security:GetAccountConfiguration"
 ],
 "Resource" : "*"
 },
 {
 "Sid" : "AllowAccessToCreateSlr",
 "Effect" : "Allow",
 "Action" : "iam:CreateServiceLinkedRole",
 "Resource" : "*",
 "Condition" : {
 "StringEquals" : {
 "iam:AWSServiceName" : [
 "agentless.inspector2.amazonaws.com",
 "inspector2.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid" : "AllowServicePrincipalBasedAccessToOrganizationApis",
 "Effect" : "Allow",
 "Action" : [
 "organizations:EnableAWSServiceAccess",
 "organizations:RegisterDelegatedAdministrator",
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource" : "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "inspector2.amazonaws.com",
 "agentless.inspector2.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid" : "AllowOrganizationalBasedAccessToOrganizationApis",
 "Effect" : "Allow",
 "Action" : [
 "organizations:DescribeOrganizationalUnit"
 ],
 "Resource" : "arn:*:organizations::*:ou/o-*/ou-*"
 },
 {
 "Sid" : "AllowAccountsBasedAccessToOrganizationApis",
 "Effect" : "Allow",
 "Action" : [
 "organizations:DescribeAccount"
 ],
 "Resource" : "arn:*:organizations::*:account/o-*/*"
 },
 {
 "Sid" : "AllowAccessToOrganizationApis",
 "Effect" : "Allow",
 "Action" : [
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DescribeOrganization"
 ],
 "Resource" : "*"
 }
 ]
}`

```

## AWS managed policy: AmazonInspector2FullAccess

You can attach the `AmazonInspector2FullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to Amazon Inspector.

**Permissions details**

This policy includes the following permissions.

- `inspector2` – Allows full access to Amazon Inspector functionality.
- `iam` – Allows Amazon Inspector to create the service-linked roles `AWSServiceRoleForAmazonInspector2` and `AWSServiceRoleForAmazonInspector2Agentless`.
  `AWSServiceRoleForAmazonInspector2` is required for Amazon Inspector to perform operations such as retrieve information about your Amazon EC2 instances, Amazon ECR repositories, and container images.
  It's also required for Amazon Inspector to analyze your VPC network and describe accounts that are associated with your organization.
  `AWSServiceRoleForAmazonInspector2Agentless` is required for Amazon Inspector to perform operations, such as retrieve information about your Amazon EC2 instances and Amazon EBS snapshots.
  It's also required to decrypt Amazon EBS snapshots that are encrypted with AWS KMS keys.
  For more information, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md "using-service-linked-roles.md").
- `organizations` – Allows administrators to use Amazon Inspector for an organization in AWS Organizations.
  When you [activate trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") for Amazon Inspector in AWS Organizations, members of the delegated administrator account can manage settings and view findings across their organization.
- `codeguru-security` – Allows administrators to use Amazon Inspector to retrieve information code snippets and change encryption settings for code that CodeGuru Security stores.
  For more information, see [Encryption at rest for code in your findings](encryption-rest.md#encryption-code-snippets "encryption-rest.md#encryption-code-snippets").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowFullAccessToInspectorApis",
 "Effect": "Allow",
 "Action": "inspector2:*",
 "Resource": "*"
 },
 {
 "Sid": "AllowAccessToCodeGuruApis",
 "Effect": "Allow",
 "Action": [
 "codeguru-security:BatchGetFindings",
 "codeguru-security:GetAccountConfiguration"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowAccessToCreateSlr",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "agentless.inspector2.amazonaws.com",
 "inspector2.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "AllowAccessToOrganizationApis",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:RegisterDelegatedAdministrator",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonInspector2ReadOnlyAccess

You can attach the `AmazonInspector2ReadOnlyAccess` policy to your IAM identities.

This policy grants permissions that allow read-only access to Amazon Inspector.

**Permissions details**

This policy includes the following permissions.

- `inspector2` – Allows read-only access to Amazon Inspector
  functionality.
- `organizations` – Allows details about Amazon Inspector coverage
  for an organization in AWS Organizations to be viewed.
- `codeguru-security` – Allows code snippets to be retrieved from CodeGuru Security. Also allows encryption settings for your code stored in CodeGuru Security to be viewed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "inspector2:BatchGet*",
 "inspector2:List*",
 "inspector2:Describe*",
 "inspector2:Get*",
 "inspector2:Search*",
 "codeguru-security:BatchGetFindings",
 "codeguru-security:GetAccountConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonInspector2ManagedCisPolicy

You can attach the `AmazonInspector2ManagedCisPolicy` policy to your IAM entities. This policy should be attached to a role that grants permissions to your Amazon EC2 instances to run CIS scans of the instance.

You can use an IAM role to manage temporary credentials for applications that are running on an EC2 instance and making AWS CLI or AWS API requests.
This is preferable to storing access keys within the EC2 instance. To assign an AWS role to an EC2 instance and make it
available to all of its applications, you create an instance profile that is attached to the
instance. An instance profile contains the role and enables programs that are running on the EC2 instance to
get temporary credentials. For more information, see [Use an IAM role to grant permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
_IAM User Guide_.

**Permissions details**

This policy includes the following permissions.

- `inspector2` – Allows access to actions used to run CIS scans.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "inspector2:StartCisSession",
 "inspector2:StopCisSession",
 "inspector2:SendCisSessionTelemetry",
 "inspector2:SendCisSessionHealth"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AmazonInspector2ServiceRolePolicy

You can't attach the `AmazonInspector2ServiceRolePolicy` policy to your
IAM entities. This policy is attached to a service-linked role that allows Amazon Inspector to
perform actions on your behalf. For more information, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md "using-service-linked-roles.md").

## AWS managed policy: AmazonInspector2AgentlessServiceRolePolicy

You can't attach the `AmazonInspector2AgentlessServiceRolePolicy` policy to your
IAM entities. This policy is attached to a service-linked role that allows Amazon Inspector to
perform actions on your behalf. For more information, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md "using-service-linked-roles.md").

## Amazon Inspector updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Inspector since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Amazon Inspector [Document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                         | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AmazonInspector2FullAccess_v2](#security-iam-awsmanpol-AmazonInspector2FullAccessV2 "#security-iam-awsmanpol-AmazonInspector2FullAccessV2") – New policy                                                                                    | Amazon Inspector has added a new managed policy that provides full access to Amazon Inspector and access to other related services.                                                                                                                                                                                                                                                 | July 03, 2025      |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added a new permission that allows Amazon Inspector to describe IP addresses and internet gateways.                                                                                                                                                                                                                                                            | April 29, 2025     |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow read-only access to Amazon ECS and Amazon EKS actions.                                                                                                                                                                                                                                                                        | March 25, 2025     |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to return function tags in AWS Lambda.                                                                                                                                                                                                                                                                       | July 31, 2024      |
| [AmazonInspector2FullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2FullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2FullAccess") – Updates to an existing policy                      | Amazon Inspector has added permissions that allow Amazon Inspector to create the service-linked role `AWSServiceRoleForAmazonInspector2Agentless` This allows users to perform [agent-based scanning](scanning-ec2.md#agent-based "scanning-ec2.md#agent-based") and [agentless scanning](scanning-ec2.md#agentless "scanning-ec2.md#agentless") when they enable Amazon Inspector. | April 24, 2024     |
| [AmazonInspector2ManagedCisPolicy](#security-iam-awsmanpol-AmazonInspector2ManagedCisPolicy "#security-iam-awsmanpol-AmazonInspector2ManagedCisPolicy") – New policy                                                                         | Amazon Inspector has added a new managed policy that you can use as part of an instance profile to allow CIS scans on an instance.                                                                                                                                                                                                                                                  | January 23, 2024   |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to start CIS scans on target instances.                                                                                                                                                                                                                                                                      | January 23, 2024   |
| [AmazonInspector2AgentlessServiceRolePolicy](using-service-linked-roles.md "using-service-linked-roles.md") – New policy                                                                                                                     | Amazon Inspector has added a new service-linked role policy to allow agentless scanning of EC2 instance.                                                                                                                                                                                                                                                                            | November 27, 2023  |
| [AmazonInspector2ReadOnlyAccess](#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess "#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess") – Updates to an existing policy                                                            | Amazon Inspector has added new permissions that allow read-only users to retrieve vulnerability intelligence details for package vulnerability findings.                                                                                                                                                                                                                            | September 22, 2023 |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to scan network configurations of Amazon EC2 instances that are part of Elastic Load Balancing target groups.                                                                                                                                                                                                | August 31, 2023    |
| [AmazonInspector2ReadOnlyAccess](#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess "#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess") – Updates to an existing policy                                                            | Amazon Inspector has added new permissions that allow read-only users to export Software Bill of Materials (SBOM) for their resources.                                                                                                                                                                                                                                              | June 29, 2023      |
| [AmazonInspector2ReadOnlyAccess](#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess "#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess") – Updates to an existing policy                                                            | Amazon Inspector has added new permissions that allow read-only users to retrieve details of encryption settings for Lambda code scanning findings for their account.                                                                                                                                                                                                               | June 13, 2023      |
| [AmazonInspector2FullAccess](#security-iam-awsmanpol-AmazonInspector2FullAccess "#security-iam-awsmanpol-AmazonInspector2FullAccess") – Updates to an existing policy                                                                        | Amazon Inspector has added new permissions that allow users configure a customer managed KMS key to encrypt code in findings from Lambda code scanning.                                                                                                                                                                                                                             | June 13, 2023      |
| [AmazonInspector2ReadOnlyAccess](#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess "#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess") – Updates to an existing policy                                                            | Amazon Inspector has added new permissions that allow read-only users to retrieve details of Lambda code scanning status and findings for their account.                                                                                                                                                                                                                            | May 02, 2023       |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to create AWS CloudTrail service-linked channels in your account when you activate Lambda scanning. This allows Amazon Inspector to monitor CloudTrail events in your account.                                                                                                                               | April 30, 2023     |
| [AmazonInspector2FullAccess](#security-iam-awsmanpol-AmazonInspector2FullAccess "#security-iam-awsmanpol-AmazonInspector2FullAccess") – Updates to an existing policy                                                                        | Amazon Inspector has added new permissions that allow users to retrieve details of code vulnerability findings from Lambda code scanning.                                                                                                                                                                                                                                           | April 21, 2023     |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to send information to Amazon EC2 Systems Manager about the custom paths a customer has defined for Amazon EC2 deep inspection.                                                                                                                                                                              | April 17, 2023     |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to create AWS CloudTrail service-linked channels in your account when you activate Lambda scanning. This allows Amazon Inspector to monitor CloudTrail events in your account.                                                                                                                               | April 30, 2023     |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added new permissions that allow Amazon Inspector to request scans of the developer code in AWS Lambda functions, and receive scan data from Amazon CodeGuru Security. Additionally, Amazon Inspector has added permissions to review IAM policies. Amazon Inspector uses this information to scan Lambda functions for code vulnerabilities.                  | February 28, 2023  |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added a new statement that allows Amazon Inspector to retrieve information from CloudWatch about when an AWS Lambda function was last invoked. Amazon Inspector uses this information to focus scans on the Lambda functions in your environment that have been active in the last 90 days.                                                                    | February 20, 2023  |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added a new statement that allows Amazon Inspector to retrieve information about AWS Lambda functions, including each layer version that is associated with each function. Amazon Inspector uses this information to scan Lambda functions for security vulnerabilities.                                                                                       | November 28, 2022  |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has added a new action to allow Amazon Inspector to describe SSM association executions. Additionally, Amazon Inspector has added additional resource scoping to allow Amazon Inspector to create, update, delete, and start SSM associations with `AmazonInspector2` owned SSM documents.                                                                         | August 31, 2022    |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") Updates to an existing policy   | Amazon Inspector has updated the resource scoping of the policy to allow Amazon Inspector to collect software inventory in other AWS partitions.                                                                                                                                                                                                                                    | August 12, 2022    |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – Updates to an existing policy | Amazon Inspector has restructured the resource scoping of the actions allowing Amazon Inspector to create, delete, and update SSM associations.                                                                                                                                                                                                                                     | August 10, 2022    |
| [AmazonInspector2ReadOnlyAccess](#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess "#security-iam-awsmanpol-AmazonInspector2ReadOnlyAccess") – New policy                                                                               | Amazon Inspector added a new policy to allow read-only access to Amazon Inspector functionality.                                                                                                                                                                                                                                                                                    | January 21, 2022   |
| [AmazonInspector2FullAccess](#security-iam-awsmanpol-AmazonInspector2FullAccess "#security-iam-awsmanpol-AmazonInspector2FullAccess") – New policy                                                                                           | Amazon Inspector added a new policy to allow full access to Amazon Inspector functionality.                                                                                                                                                                                                                                                                                         | November 29, 2021  |
| [AmazonInspector2ServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonInspector2ServiceRolePolicy") – New policy                    | Amazon Inspector added a new policy to allow Amazon Inspector to perform actions in other services on your behalf.                                                                                                                                                                                                                                                                  | November 29, 2021  |
| Amazon Inspector started tracking changes                                                                                                                                                                                                    | Amazon Inspector started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                             | November 29, 2021  |
