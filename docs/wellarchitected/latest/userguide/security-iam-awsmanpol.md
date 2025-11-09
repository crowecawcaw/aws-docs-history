# AWS managed policies for AWS Well-Architected Tool

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

## AWS managed policy:

WellArchitectedConsoleFullAccess

You can attach the `WellArchitectedConsoleFullAccess` policy to your IAM
identities.

This policy grants full access to AWS Well-Architected Tool.

**Permissions details**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "wellarchitected:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

WellArchitectedConsoleReadOnlyAccess

You can attach the `WellArchitectedConsoleReadOnlyAccess` policy to your IAM
identities.

This policy grants read-only access to AWS Well-Architected Tool.

**Permissions details**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "wellarchitected:Get*",
 "wellarchitected:List*",
 "wellarchitected:ExportLens"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy:

AWSWellArchitectedOrganizationsServiceRolePolicy

You can attach the `AWSWellArchitectedOrganizationsServiceRolePolicy` policy to your IAM
identities.

This policy grants administrative permissions in AWS Organizations that are required to
support AWS Well-Architected Tool integration with Organizations. These permissions
allow the organization management account to enable resource sharing with AWS WA Tool.

**Permissions details**

This policy includes the following permissions.

- `organizations:ListAWSServiceAccessForOrganization` – Allows principals to check if the AWS service access is enabled for AWS WA Tool.
- `organizations:DescribeAccount` – Allows principals to retrieve information about an account in the organization.
- `organizations:DescribeOrganization` – Allows principals to retrieve information about the organization configuration.
- `organizations:ListAccounts` – Allows principals to retrieve the list of accounts that belong to an organization.
- `organizations:ListAccountsForParent` – Allows principals to retrieve the list of accounts that belong to an organization from a given root node in the organization.
- `organizations:ListChildren` – Allows principals to retrieve the list of accounts and organization units that belong to an organization from a given root node in the organization.
- `organizations:ListParents` – Allows principals to retrieve the list of immediate parents specified by the OU or account within an organization.
- `organizations:ListRoots` – Allows principals to retrieve the list of all root nodes within an organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListChildren",
 "organizations:ListParents",
 "organizations:ListRoots"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSWellArchitectedDiscoveryServiceRolePolicy

You can attach the `AWSWellArchitectedDiscoveryServiceRolePolicy` policy
to your IAM identities.

This policy allows AWS Well-Architected Tool to access AWS services and resources that relate to
AWS WA Tool resources.

**Permissions details**

This policy includes the following permissions.

- `trustedadvisor:DescribeChecks` – Lists Trusted Advisor checks
  available.
- `trustedadvisor:DescribeCheckItems` – Fetches Trusted Advisor check
  data, including status and resources flagged by Trusted Advisor.
- `servicecatalog:GetApplication` – Fetches details of an
  AppRegistry application.
- `servicecatalog:ListAssociatedResources` –Lists resources
  associated with an AppRegistry application.
- `cloudformation:DescribeStacks` –Gets details of AWS CloudFormation
  stacks.
- `cloudformation:ListStackResources` –Lists resources
  associated with the AWS CloudFormation stacks.
- `resource-groups:ListGroupResources` –Lists resources from a
  ResourceGroup.
- `tag:GetResources` – Required for ListGroupResources.
- `servicecatalog:CreateAttributeGroup` – Creates a
  service-managed attribute group when required.
- `servicecatalog:AssociateAttributeGroup` – Associates a
  service-managed attribute group with an AppRegistry application.
- `servicecatalog:UpdateAttributeGroup` – Updates a
  service-managed attribute group.
- `servicecatalog:DisassociateAttributeGroup` –Disassociates a
  service-managed attribute group from an AppRegistry application.
- `servicecatalog:DeleteAttributeGroup` – Deletes a
  service-managed attribute group when required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "trustedadvisor:DescribeChecks",
 "trustedadvisor:DescribeCheckItems"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:ListStackResources",
 "resource-groups:ListGroupResources",
 "tag:GetResources"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:ListAssociatedResources",
 "servicecatalog:GetApplication",
 "servicecatalog:CreateAttributeGroup"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:AssociateAttributeGroup",
 "servicecatalog:DisassociateAttributeGroup"
 ],
 "Resource": [
 "arn:*:servicecatalog:*:*:/applications/*",
 "arn:*:servicecatalog:*:*:/attribute-groups/AWS_WellArchitected-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:UpdateAttributeGroup",
 "servicecatalog:DeleteAttributeGroup"
 ],
 "Resource": [
 "arn:*:servicecatalog:*:*:/attribute-groups/AWS_WellArchitected-*"
 ]
 }
 ]
}`

```

## AWS WA Tool updates to AWS managed

policies

View details about updates to AWS managed policies for AWS WA Tool since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the AWS WA Tool [Document revisions](document-revisions.md "document-revisions.md") page.

| Change                                | Description                                                                                                                                                              | Date          |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| AWS WA Tool changed managed policy    | Added `"wellarchitected:Export*"` to `WellArchitectedConsoleReadOnlyAccess`.                                                                                             | June 22, 2023 |
| AWS WA Tool added service role policy | Added `AWSWellArchitectedDiscoveryServiceRolePolicy` to<br>allow AWS Well-Architected Tool to access AWS services and resources that relate to<br>AWS WA Tool resources. | May 3, 2023   |
| AWS WA Tool added permissions         | Added a new action to grant<br>`ListAWSServiceAccessForOrganization` to allow AWS WA Tool to<br>check if the AWS service access is enabled for AWS WA Tool.              | July 22, 2022 |
| AWS WA Tool started tracking changes  | AWS WA Tool started tracking changes for its AWS managed policies.                                                                                                       | July 22, 2022 |
