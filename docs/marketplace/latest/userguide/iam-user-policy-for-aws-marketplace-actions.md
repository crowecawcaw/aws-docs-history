# AWS Marketplace metering and entitlement

API permissions

Software as a service (SaaS) products, Amazon Machine Image (AMI) products, and container
products can use the AWS Marketplace Metering Service and AWS Marketplace Entitlement Service APIs. Each type requires different AWS Identity and Access Management
(IAM) permissions. For your product or products, you meter for all usage, and customers are
billed by AWS based on the metering records that you provide. To enable the integration
required to provide AWS Marketplace your metering records, the service account that the integration is
using needs a constrained IAM policy to enable access. Attach the policy for the product type
that you're sending metering information for to the user or role that you're using for the
integration.

###### Topics

- [IAM policy for SaaS products](#iam-user-policy-for-saas-products "#iam-user-policy-for-saas-products")
- [IAM policy for AMI products](#iam-user-policy-for-ami-products "#iam-user-policy-for-ami-products")
- [IAM policy for container
  products](#iam-user-policy-for-container-products "#iam-user-policy-for-container-products")

## IAM policy for SaaS products

In the following policy, the ﬁrst permission,
`aws-marketplace:ResolveCustomer`, is required for all SaaS integrations. The
second permission, `aws-marketplace:BatchMeterUsage`, is needed for the AWS Marketplace Metering Service
API. The third permission, `aws-marketplace:GetEntitlements`, is needed for the
AWS Marketplace Entitlement Service API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:ResolveCustomer",
 "aws-marketplace:BatchMeterUsage",
 "aws-marketplace:GetEntitlements"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

For more information about SaaS products, see [SaaS-based products in AWS Marketplace](saas-products.md "saas-products.md").

## IAM policy for AMI products

Use the following IAM policy for AMI products.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:MeterUsage"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

For more information about AMI products, see [AMI-based products in AWS Marketplace](ami-products.md "ami-products.md").

## IAM policy for container

products

Use the following IAM policy for container products.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:RegisterUsage"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

For more information about container products, see [Container-based products on AWS Marketplace](container-based-products.md "container-based-products.md").

For more information about creating users, see [Creating a user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the
_IAM User Guide_. For more information about creating and
assigning policies, see [Changing
permissions for an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md").

This policy grants access to the APIs for the IAM role or user that you attach the policy
to. For more information about how to enable role assumption by another account for these API
calls, see [How to Best Architect Your AWS Marketplace SaaS Subscription Across Multiple AWS accounts](https://aws.amazon.com/blogs/apn/how-to-best-architect-your-aws-marketplace-saas-subscription-across-multiple-aws-accounts/ "https://aws.amazon.com/blogs/apn/how-to-best-architect-your-aws-marketplace-saas-subscription-across-multiple-aws-accounts/")
at the AWS Partner Network (APN) Blog.
