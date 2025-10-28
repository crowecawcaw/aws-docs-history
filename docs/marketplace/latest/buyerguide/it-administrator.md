# Creating a private marketplace administrator

You can create an administrators group to manage your company’s [private marketplace](private-marketplace.md "private-marketplace.md") settings. After private
marketplace is enabled for your organization, administrators for the private marketplace can
perform many tasks including the following:

- View and create experiences and audiences.
- Add products to private marketplace experiences.
- Remove products from private marketplace experiences.
- Configure the user interface of private marketplace experiences.
- Enable and disable private marketplace experiences.
- Call the AWS Marketplace Catalog API to manage private marketplace experiences
  programmatically.
  To create multiple private marketplace administrators where each administrator is limited
  to a subset of tasks, see [Example policies for private marketplace administrators](#creating-custom-policies-for-private-marketplace-admin "#creating-custom-policies-for-private-marketplace-admin").

###### Note

Enabling private marketplace is a one-time action that must happen from the management
account. For more information, see [Getting started with private marketplace](private-catalog-administration.md#private-marketplace-getting-started "private-catalog-administration.md#private-marketplace-getting-started").

You grant AWS Identity and Access Management (IAM) permissions to administer your private marketplace by
attaching the [AWS
managed policy: AWSPrivateMarketplaceAdminFullAccess](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess")
to a user, group, or role. We recommend using a group or role. For more information about
how to attach the policy, see [Attaching a policy to a user
group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md") in the _IAM User Guide_.

For more information about the permissions in the
`AWSPrivateMarketplaceAdminFullAccess` policy, see [AWS
managed policy: AWSPrivateMarketplaceAdminFullAccess](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess"). To learn about
other policies for use in AWS Marketplace, sign in to the AWS Management Console, and go to the [IAM policies page](https://console.aws.amazon.com/iam/home?#/policies "https://console.aws.amazon.com/iam/home?#/policies"). In the search box,
enter `Marketplace` to find all of the policies that are associated
with AWS Marketplace.

## Example policies for private marketplace administrators

Your organization can create multiple private marketplace administrators where each
administrator is limited to a subset of tasks. You can tune AWS Identity and Access Management (IAM) policies
to specify condition keys and resources on AWS Marketplace Catalog API actions listed in [Actions, resources, and condition keys for AWS Marketplace Catalog](../../../service-authorization/latest/reference/list_awsmarketplacecatalog.md#awsmarketplacecatalog-catalog_ChangeType "../../../service-authorization/latest/reference/list_awsmarketplacecatalog.md#awsmarketplacecatalog-catalog_ChangeType"). The general
mechanism to use AWS Marketplace Catalog API change types and resources to tune IAM policies is
described in the [AWS
Marketplace Catalog API guide](../../../marketplace-catalog/latest/api-reference/api-access-control.md "../../../marketplace-catalog/latest/api-reference/api-access-control.md"). For a list of all change types available in
the private AWS Marketplace, see [Working with
a private marketplace.](../../../marketplace-catalog/latest/api-reference/private-marketplace.md "../../../marketplace-catalog/latest/api-reference/private-marketplace.md")

To create customer managed policies, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md"). Following is an example policy JSON that you can use to create an
administrator who can only add or remove products from private marketplaces.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:AssociateProductsWithPrivateMarketplace",
 "aws-marketplace:DisassociateProductsFromPrivateMarketplace",
 "aws-marketplace:ListPrivateMarketplaceRequests",
 "aws-marketplace:DescribePrivateMarketplaceRequests"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:ListEntities",
 "aws-marketplace:ListChangeSets",
 "aws-marketplace:DescribeChangeSet",
 "aws-marketplace:CancelChangeSet"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:StartChangeSet"
 ],
 "Condition": {
 "StringEquals": {
 "catalog:ChangeType": [
 "AllowProductProcurement",
 "DenyProductProcurement"
 ]
 }
 },
 "Resource": "*"
 }
 ]
}`

```

A policy can also be limited to manage a subset of private marketplace resources.
Following is an example policy JSON you can use to create an administrator who can only
manage a specific private marketplace experience. This example uses a resource string
with `exp-1234example` as the `Experience` identifier.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:AssociateProductsWithPrivateMarketplace",
 "aws-marketplace:DisassociateProductsFromPrivateMarketplace",
 "aws-marketplace:ListPrivateMarketplaceRequests",
 "aws-marketplace:DescribePrivateMarketplaceRequests"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:ListEntities",
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:ListChangeSets",
 "aws-marketplace:DescribeChangeSet",
 "aws-marketplace:CancelChangeSet"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:StartChangeSet"
 ],
 "Resource": [
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/Experience/exp-1234example"
 ]
 }
 ]
}`

```

For details about how entity identifiers can be retrieved and to view the set of
private marketplace resources, see [Working with
a private marketplace](../../../marketplace-catalog/latest/api-reference/private-marketplace.md "../../../marketplace-catalog/latest/api-reference/private-marketplace.md").
