# Using custom policies to map users

The topics in this section explain how to map AWS Partner Central users to AWS IAM roles.
Mapping enables single sign-on access for users across AWS Partner Central and AWS. plus other
features such as product and offer linking.

###### Topics

- [Role mapping prerequisites](#role-mapping-prereqs "#role-mapping-prereqs")
- [Connecting ACE opportunities with AWS Marketplace private offers](#connect-ace-to-marketplace "#connect-ace-to-marketplace")

## Role mapping prerequisites

Before mapping, you must complete the following prerequistites:

- Create IAM roles in the AWS account. For more ionformation, refer to [Create a
  role using custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _AWS Identity and Access Management User
  Guide_.
- To allow AWS Partner Central to map AWS IAM roles, add the following custom trust policy to the
  roles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "partnercentral-account-management.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

- For AWS Partner Central users with the ACE user role, grant permissions to perform the
  `ListEntities` and `SearchAgreements` actions. For more
  information, refer to [Controlling access to AWS Marketplace Management Portal](../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md "../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md") in the _AWS Marketplace Seller Guide_.
- [Link your AWS Partner Central account to an AWS Marketplace account](linking-apc-aws-marketplace.md "linking-apc-aws-marketplace.md").

To map IAM roles to your AWS Partner Central users, you must create IAM roles with the
permissions you want to provide to your users. For cloud admin users, you can only map the cloud
admin IAM role created in your account during the account linking process.

You can create one or more IAM roles to associate with your AWS Partner Central users. The
role names must start with `PartnerCentralRoleFor`. You can't choose a
role unless the name begins with that text.

You can attach custom or managed policies to the IAM role. You can attach the AWS Marketplace managed policies such as
`AWSMarketplaceSellerFullAccess` to the IAM roles and provide access to your AWS Partner Central users.
For more information about creating roles, refer to
[Creating an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console") in the _IAM User Guide_.

## Connecting ACE opportunities with AWS Marketplace private offers

To enable ACE users to attach AWS Marketplace private offers to ACE opportunities, map them to an AWS IAM role in AWS Partner Central.

### Prerequisites

Complete the following before mapping users to AWS Marketplace IAM roles:

- When you link an AWS Marketplace account to AWS Partner Central, provide
  `AWSMarketplaceSellerFullAccess` or, minimally,
  `ListEntities`/`SearchAgreements` to the IAM role assigned to
  ACE users. This is required to enable ACE users to attach AWS Marketplace private offers to ACE
  opportunities.
- (Optional) To grant minimal permission, add a customer managed policy
  to your AWS account and to the IAM role you create for ACE managers and users.
  Refer to the following policy as an example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:SearchAgreements",
 "aws-marketplace:DescribeAgreement",
 "aws-marketplace:GetAgreementTerms",
 "aws-marketplace:ListEntities",
 "aws-marketplace:DescribeEntity",
 "aws-marketplace:StartChangeSet"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws-marketplace:PartyType": "Proposer"
 },
 "ForAllValues:StringEquals": {
 "aws-marketplace:AgreementType": [
 "PurchaseAgreement"
 ]
 }
 }
 }
 ]
}`

```

### Mapping users to AWS IAM

roles

Use the procedures in this section to map and unmap AWS Partner Central users to AWS IAM roles.

###### To map an AWS Partner Central user to an AWS IAM role

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. In the **Account linking** section of the AWS Partner Central homepage, choose **Manage linked account**.
3. In the **Non-cloud admin users** section of the **Account
   Linking** page, choose a user.
4. Choose **Map to IAM role**.
5. Choose an IAM role from the dropdown list.
6. Choose **Map role**.

###### To ummap an AWS Partner Central user from an AWS IAM role.

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. In the **Account linking** section of the AWS Partner Central
   homepage, choose **Manage linked account**.
3. In the **Non-cloud admin users** section of the **Account
   Linking** page, choose the user you want to unmap.
4. Choose **Unmap role**.
