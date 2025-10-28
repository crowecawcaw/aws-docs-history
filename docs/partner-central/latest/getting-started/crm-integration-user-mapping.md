# Mapping AWS Marketplace roles to a CRM integration user

This section explains how to map AWS Marketplace AWS Identity and Access Management (IAM) roles to your CRM integration service user on AWS Partner Central. Mapping enables the CRM Integration service user to perform actions on the AWS Marketplace account. Selecting an IAM role to access AWS Marketplace APIs through CRM integration enables features such as linking AWS Marketplace private offers to ACE opportunities.

Before mapping, you must first complete the following:

- [Create IAM roles in the AWS Marketplace account.](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md")
- While creating IAM roles, add the following custom trust policy to allow AWS Partner Central to map the IAM roles.

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

- Grant permissions to perform the `ListEntities` and `SearchAgreements` actions. For more information, refer to [Controlling access to AWS Marketplace Management Portal.](../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md "../../../marketplace/latest/userguide/marketplace-management-portal-user-access.md")
- [Link your AWS Partner Central account to an AWS Marketplace account.](linking-apc-aws-marketplace.md "linking-apc-aws-marketplace.md")

###### To map an AWS Marketplace IAM role to a CRM integration user

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. In the **AWS Marketplace** section of the AWS Partner Central homepage, choose **Manage Linked Account**.
3. On the **AWS Marketplace page**, in the **IAM role for CRM integration** section, choose **Map IAM role**.
4. Choose an IAM role from the dropdown list.
5. Choose **Map role**.

###### To unmap an AWS Marketplace IAM role from a CRM integration user.

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. In the **AWS Marketplace** section of the AWS Partner Central homepage, choose **Manage Linked Account**.
3. On the **AWS Marketplace page**, in the **IAM role for CRM
   integration** section, choose **Unmap IAM role**.
