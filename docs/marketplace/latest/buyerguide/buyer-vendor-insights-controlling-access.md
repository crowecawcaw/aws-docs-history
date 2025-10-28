# Controlling access in

AWS Marketplace Vendor Insights

AWS Identity and Access Management (IAM) is an AWS service that helps you control access to AWS resources.
IAM is an AWS service that you can use with no additional charge. If you're an
administrator, you control who can be _authenticated_
(signed in) and _authorized_ (have permissions) to use
AWS Marketplace resources. AWS Marketplace Vendor Insights uses IAM to control access to seller data, assessments,
seller self-attestation, and industry standard audit reports.

The recommended way to control who can do what in AWS Marketplace Management Portal is to use IAM to create
users and groups. Then you add the users to the groups, and manage the groups. You can
assign a policy or permissions to the group that provide read-only permissions. If you have
other users that need read-only access, you can add them to the group you created rather
than adding permissions to their AWS account.

A _policy_ is a document that defines the permissions that apply to a
user, group, or role. The permissions determine what users can do in AWS. A policy
typically allows access to specific actions, and can optionally grant that the actions are
allowed for specific resources, like Amazon EC2 instances, Amazon S3 buckets, and so on. Policies can
also explicitly deny access. A _permission_ is a statement within a
policy that allows or denies access to a particular resource.

###### Important

All of the users that you create authenticate by using their credentials. However,
they use the same AWS account. Any change that a user makes can impact the whole
account.

AWS Marketplace has permissions defined to control the actions that someone with those permissions
can take in AWS Marketplace Management Portal. There are also policies that AWS Marketplace creates and manages that combine
several permissions. The `AWSMarketplaceSellerProductsFullAccess` policy gives
the user full access to products in the AWS Marketplace Management Portal.

For more information about the actions, resources, and condition keys that are available,
see [Actions, resources, and condition keys for AWS Marketplace Vendor Insights](../../../service-authorization/latest/reference/list_awsmarketplacevendorinsights.md "../../../service-authorization/latest/reference/list_awsmarketplacevendorinsights.md") in the _Service Authorization Reference_.

## Permissions for AWS Marketplace Vendor Insights buyers

You can use the following permissions in IAM policies for AWS Marketplace Vendor Insights. You can combine
permissions into a single IAM policy to grant the permissions you want.

## `GetProfileAccessTerms`

`GetProfileAccessTerms` allows users to retrieve necessary terms to review,
accept, and get access to a AWS Marketplace Vendor Insights profile.

Action groups: Read-only and read-write.

Required resources: `SecurityProfile`.

## `ListEntitledSecurityProfiles`

`ListEntitledSecurityProfiles` allows users to list all security profiles
they have an active entitlement to read.

Action groups: Read-only, list-only, and read-write.

Required resources: None

## `ListEntitledSecurityProfileSnapshots`

`ListEntitledSecurityProfileSnapshots` allows users to list the security
profile snapshots for a security profile that they have an active entitlement to
read.`SecurityProfile`.

Action groups: Read-only, list-only, and read-write.

Required resources: `SecurityProfile`

## `GetEntitledSecurityProfileSnapshot`

`GetEntitledSecurityProfileSnapshot` allows users to get the details of a
security profile snapshot for a security profile that they have an active entitlement to
read.

Action groups: Read-only and read-write.

Required resources: `SecurityProfile`
