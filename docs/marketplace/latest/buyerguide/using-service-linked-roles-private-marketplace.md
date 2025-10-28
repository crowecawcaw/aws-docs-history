# Service-linked role to configure Private Marketplace in AWS Marketplace

AWS Marketplace uses the service-linked role named
`AWSServiceRoleForPrivateMarketplaceAdmin` to describe and
update Private Marketplace resources and describe AWS Organizations.

The `AWSServiceRoleForPrivateMarketplaceAdmin` service-linked
role trusts the following services to assume the role:

- `private-marketplace.marketplace.amazonaws.com`
  The `AWSServiceRoleForPrivateMarketplaceAdminPolicy` policy allows
  AWS Marketplace to perform the following actions on specified resources.

###### Note

For more information about AWS Marketplace managed policies, see [AWS managed policies for AWS Marketplace
buyers](buyer-security-iam-awsmanpol.md "buyer-security-iam-awsmanpol.md") in this guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PrivateMarketplaceCatalogDescribePermissions",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:DescribeEntity"
 ],
 "Resource": [
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/Experience/*",
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/Audience/*",
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/ProcurementPolicy/*",
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/BrandingSettings/*"
 ]
 },
 {
 "Sid": "PrivateMarketplaceCatalogDescribeChangeSetPermissions",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:DescribeChangeSet"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PrivateMarketplaceCatalogListPermissions",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:ListEntities",
 "aws-marketplace:ListChangeSets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PrivateMarketplaceStartChangeSetPermissions",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:StartChangeSet"
 ],
 "Condition": {
 "StringEquals": {
 "catalog:ChangeType": [
 "AssociateAudience",
 "DisassociateAudience"
 ]
 }
 },
 "Resource": [
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/Experience/*",
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/ChangeSet/*"
 ]
 },
 {
 "Sid": "PrivateMarketplaceOrganizationPermissions",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListChildren"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

You must configure permissions to allow your users, groups, or roles to create,
edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
