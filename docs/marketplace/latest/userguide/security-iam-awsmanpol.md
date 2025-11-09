# AWS managed policies for AWS Marketplace sellers

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

This section lists each of the policies used to manage seller access to AWS Marketplace. For
information about buyer policies, see [AWS managed
policies for AWS Marketplace buyers](../buyerguide/buyer-security-iam-awsmanpol.md "../buyerguide/buyer-security-iam-awsmanpol.md") in the _AWS Marketplace Buyer Guide_.

###### Topics

- [AWS managed
  policy: AWSMarketplaceAmiIngestion](#security-iam-awsmanpol-awsmarketplaceamiingestion "#security-iam-awsmanpol-awsmarketplaceamiingestion")
- [AWS managed policy:
  AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess "#security-iam-awsmanpol-awsmarketplacefullaccess")
- [AWS managed
  policy: AWSMarketplaceGetEntitlements](#security-iam-awsmanpol-awsmarketplacegetentitlements "#security-iam-awsmanpol-awsmarketplacegetentitlements")
- [AWS managed
  policy: AWSMarketplaceMeteringFullAccess](#security-iam-awsmanpol-awsmarketplacemeteringfullaccess "#security-iam-awsmanpol-awsmarketplacemeteringfullaccess")
- [AWS
  managed policy: AWSMarketplaceMeteringRegisterUsage](#security-iam-awsmanpol-awsmarketplacemeteringregisterusage "#security-iam-awsmanpol-awsmarketplacemeteringregisterusage")
- [AWS managed
  policy: AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")
- [AWS
  managed policy: AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess "#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess")
- [AWS
  managed policy: AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly "#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly")
- [AWS
  managed policy: AWSMarketplaceSellerOfferManagement](#security-iam-awsmanpol-awsmarketplaceselleroffermanagement "#security-iam-awsmanpol-awsmarketplaceselleroffermanagement")
- [AWS managed
  policy: AWSMarketplaceResaleAuthorizationServiceRolePolicy](#security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy "#security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy")
- [AWS managed
  policy: AWSVendorInsightsVendorFullAccess](#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess "#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess")
- [AWS managed
  policy: AWSVendorInsightsVendorReadOnly](#security-iam-awsmanpol-awsvendorinsightsvendorreadonly "#security-iam-awsmanpol-awsvendorinsightsvendorreadonly")
- [AWS Marketplace updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed

policy: AWSMarketplaceAmiIngestion

You can create a service role with this policy that can then be used by AWS Marketplace to
perform actions on your behalf. For more information about using
`AWSMarketplaceAmiIngestion`, see [Giving AWS Marketplace access to your
AMI](single-ami-marketplace-ami-access.md "single-ami-marketplace-ami-access.md").

This policy grants contributor permissions that allow AWS Marketplace to copy your Amazon
Machine Images (AMIs) in order to list them on AWS Marketplace.

To view the permissions for this policy, see [AWSMarketplaceAmiIngestion](../../../aws-managed-policy/latest/reference/AWSMarketplaceAmiIngestion.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceAmiIngestion.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSMarketplaceFullAccess

You can attach the `AWSMarketplaceFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow full access to AWS Marketplace and
related services, both as a seller and a buyer. These permissions include the following
abilities:

- Subscribe and unsubscribe to AWS Marketplace software.
- Manage AWS Marketplace software instances from AWS Marketplace.
- Create and manage a private marketplace in your account.
- Provide access to Amazon EC2, AWS CloudFormation, and Amazon EC2 Systems Manager.

To view the permissions for this policy, see
[AWSMarketplaceFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md")
in the _AWS Managed Policy Reference_.

## AWS managed

policy: AWSMarketplaceGetEntitlements

You can attach the `AWSMarketplaceGetEntitlements` policy to your IAM
identities.

This policy grants read-only permissions that allow software as a service (SaaS)
product sellers to check whether a customer has subscribed to their AWS Marketplace SaaS
product.

To view the permissions for this policy, see [AWSMarketplaceGetEntitlements](../../../aws-managed-policy/latest/reference/AWSMarketplaceGetEntitlements.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceGetEntitlements.md") in the
_AWS Managed Policy Reference_.

## AWS managed

policy: AWSMarketplaceMeteringFullAccess

You can attach the `AWSMarketplaceMeteringFullAccess` policy to your IAM
identities.

This policy grants contributor permissions that allow reporting metered usage that
corresponds to AMI and container products with flexible consumption pricing on
AWS Marketplace.

To view the permissions for this policy, see [AWSMarketplaceMeteringFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS

managed policy: AWSMarketplaceMeteringRegisterUsage

You can attach the `AWSMarketplaceMeteringRegisterUsage` policy to your
IAM identities.

This policy grants contributor permissions that allow reporting metered usage that
corresponds to container products with hourly pricing on AWS Marketplace.

To view the permissions for this policy, see [AWSMarketplaceMeteringRegisterUsage](../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringRegisterUsage.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceMeteringRegisterUsage.md") in the
_AWS Managed Policy Reference_.

## AWS managed

policy: AWSMarketplaceSellerFullAccess

You can attach the `AWSMarketplaceSellerFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow full access to all seller
operations on AWS Marketplace, including AWS Marketplace Management Portal, and managing the Amazon EC2 AMI used in AMI-based
products.

To view the permissions for this policy, see [AWSMarketplaceSellerFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS

managed policy: AWSMarketplaceSellerProductsFullAccess

You can attach the `AWSMarketplaceSellerProductsFullAccess` policy to your
IAM identities.

This policy grants contributor permissions that allow full access to manage products
and to the AWS Marketplace Management Portal, and managing the Amazon EC2 AMI used in AMI-based products.

To view the permissions for this policy, see [AWSMarketplaceSellerProductsFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerProductsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerProductsFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS

managed policy: AWSMarketplaceSellerProductsReadOnly

You can attach the `AWSMarketplaceSellerProductsReadOnly` policy to your
IAM identities.

This policy grants read-only permissions that allow access to view products on the
AWS Marketplace Management Portal, and view the Amazon EC2 AMI used in AMI-based products.

To view the permissions for this policy, see [AWSMarketplaceSellerProductsReadOnly](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerProductsReadOnly.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerProductsReadOnly.md") in the
_AWS Managed Policy Reference_.

## AWS

managed policy: AWSMarketplaceSellerOfferManagement

You can attach the `AWSMarketplaceSellerOfferManagement` policy to your
IAM identities.

This policy grants sellers access to Offers and Agreements management
activities.

To view the permissions for this policy, see [AWSMarketplaceSellerOfferManagement](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement.md") in the
_AWS Managed Policy Reference_.

## AWS managed

policy: AWSMarketplaceResaleAuthorizationServiceRolePolicy

This policy is attached to a service-linked role that allows AWS Marketplace to perform actions on your behalf for Resale Authorization. For more information about using this service-linked role, see [Using service-linked roles for Resale Authorization
with AWS Marketplace](using-roles-for-resale-authorization.md "using-roles-for-resale-authorization.md").

This policy grants permissions that allow AWS Marketplace to share ResaleAuthorization resources between manufacturers (ISVs) and channel partners using AWS Resource Access Manager (AWS RAM).

This policy includes permissions for AWS Marketplace operations and AWS Resource Access Manager (RAM) actions to facilitate the sharing and management of ResaleAuthorization resources across different AWS accounts and catalogs.

To view the permissions for this policy, see [AWSMarketplaceResaleAuthorizationServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSMarketplaceResaleAuthorizationServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceResaleAuthorizationServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

## AWS managed

policy: AWSVendorInsightsVendorFullAccess

You can attach the `AWSVendorInsightsVendorFullAccess` policy to your IAM
identities.

This policy grants full access to create and manage all resources on AWS Marketplace Vendor Insights. In
AWS Marketplace Vendor Insights, an assessor is equal to a buyer, and a vendor is equal to a seller for the
purposes of this guide.

To view the permissions for this policy, see [AWSVendorInsightsVendorFullAccess](../../../aws-managed-policy/latest/reference/AWSVendorInsightsVendorFullAccess.md "../../../aws-managed-policy/latest/reference/AWSVendorInsightsVendorFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS managed

policy: AWSVendorInsightsVendorReadOnly

You can attach the `AWSVendorInsightsVendorReadOnly` policy to your IAM
identities.

This policy grants read-only access for viewing AWS Marketplace Vendor Insights profiles and related
resources. In AWS Marketplace Vendor Insights, an assessor is equal to a buyer, and a vendor is equal to a
seller for the purposes of this guide.

To view the permissions for this policy, see [AWSVendorInsightsVendorReadOnly](../../../aws-managed-policy/latest/reference/AWSVendorInsightsVendorReadOnly.md "../../../aws-managed-policy/latest/reference/AWSVendorInsightsVendorReadOnly.md") in the
_AWS Managed Policy Reference_.

## AWS Marketplace updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Marketplace since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS Marketplace [Document history](document-history.md "document-history.md") page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                        | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSMarketplaceResaleAuthorizationServiceRolePolicy](#security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy "#security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | AWS Marketplace updated the policy to support multi-catalog features and enable proper lifecycle management of ResaleAuthorization entities. The updates include:<br>• Updated resource ARN pattern from `arn:aws:aws-marketplace:*:*:AWSMarketplace/ResaleAuthorization/*` to `arn:aws:aws-marketplace:*:*:*/ResaleAuthorization/*`.<br>• Added permissions `ram:DeleteResourceShare` and `aws-marketplace:DeleteResourcePolicy`. | July 24, 2025     |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | AWS Marketplace added four new `SellerSettings`permissions for the supplemental tax<br>profile feature: `ListSupplementalTaxRegistrations`, `PutSupplementalTaxRegistration`, `DeleteSupplementalTaxRegistration`, `GetTaxRegistration`.                                                                                                                                                                                           | December 20, 2024 |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policies<br>[AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess "#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess")<br>– Updated policies<br>[AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policies<br>[AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly "#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly")<br>– Updated policies | AWS Marketplace removed the `ListTasks`,<br>`DescribeTask`, `UpdateTasks`, and<br>`CompleteTasks` permissions.                                                                                                                                                                                                                                                                                                                     | December 10, 2024 |
| [AWSMarketplaceSellerOfferManagement](#security-iam-awsmanpol-awsmarketplaceselleroffermanagement "#security-iam-awsmanpol-awsmarketplaceselleroffermanagement")<br>– Added new policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | AWS Marketplace added new policy:<br>`AWSMarketplaceSellerOfferManagement`                                                                                                                                                                                                                                                                                                                                                         | November 18, 2024 |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess") –<br>Updated policies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | AWS Marketplace added the `UploadFiles` permission. The change enables sellers to use a deprecated page in the AWS Marketplace Management Portal.                                                                                                                                                                                                                                                                                  | November 6, 2024  |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess") –<br>Updated policies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | AWS Marketplace added the `ListAssessments` and<br>`DescribeAssessments` permissions. The changes enable<br>SSLv2 users to access assessment data.                                                                                                                                                                                                                                                                                 | October 22, 2024  |
| [AWSMarketplaceSellerProductsFullAccess<br>– Updated policies](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess "#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | AWS Marketplace added the `ListAssessments` and<br>`DescribeAssessments` permissions. The changes enable<br>SSLv2 users to access assessment data.                                                                                                                                                                                                                                                                                 | October 22, 2024  |
| [AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly "#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly")<br>– Updated policies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | AWS Marketplace added the `ListAssessments` and<br>`DescribeAssessments` permissions. The changes enable<br>SSLv2 users to access assessment data.                                                                                                                                                                                                                                                                                 | October 22, 2024  |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Updated the `AWSMarketplaceSellerFullAccess`<br>documentation to reflect the removal of the following actions:<br>`aws-marketplace-management:viewMarketing`,<br>`aws-marketplace-management:viewSettings`, and<br>`aws-marketplace-management:uploadFiles`. This update<br>also includes removing the \*Using fine-grained<br>permissions<br>• section.                                                                           | June 4, 2024      |
| [AWSMarketplaceGetEntitlements](#security-iam-awsmanpol-awsmarketplacegetentitlements "#security-iam-awsmanpol-awsmarketplacegetentitlements")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | AWS Marketplace updated `AWSMarketplaceGetEntitlements` to add<br>`sid` for the policy statement.                                                                                                                                                                                                                                                                                                                                  | March 22, 2024    |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | AWS Marketplace updated `AWSMarketplaceSellerFullAccess` to add<br>permissions for creating service-linked roles.                                                                                                                                                                                                                                                                                                                  | March 15, 2024    |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | AWS Marketplace updated `AWSMarketplaceSellerFullAccess` to add a<br>permission for accessing tax information.                                                                                                                                                                                                                                                                                                                     | February 8, 2024  |
| [AWSVendorInsightsVendorFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess")<br>• Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | AWS Marketplace updated `AWSVendorInsightsVendorFullAccess` to add<br>permissions to update data sources.                                                                                                                                                                                                                                                                                                                          | October 18, 2023  |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | AWS Marketplace updated `AWSMarketplaceSellerFullAccess` to add<br>permissions for sharing entities.                                                                                                                                                                                                                                                                                                                               | June 1, 2023      |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | AWS Marketplace updated `AWSMarketplaceSellerFullAccess` to add<br>permissions related to account verifications, bank account<br>verifications, case management, and seller notification details.                                                                                                                                                                                                                                  | June 1, 2023      |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")<br>– Updated policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | AWS Marketplace updated `AWSMarketplaceSellerFullAccess` to add<br>permissions to access seller dashboards.                                                                                                                                                                                                                                                                                                                        | December 23, 2022 |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess"), [AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess "#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess"),<br>[AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly "#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly")<br>– Update to existing policy                                                                                                                                                                                                                | AWS Marketplace updated policies for the new tag-based authorization<br>feature.                                                                                                                                                                                                                                                                                                                                                   | December 9, 2022  |
| AWS Marketplace updated [AWSVendorInsightsVendorFullAccess](#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess "#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | AWS Marketplace updated `AWSMarketplaceSellerProductsFullAccess` to<br>add agreement search, updating profile snapshots, vendor tagging, and<br>allows read-only access to AWS Artifact third-party reports (preview).                                                                                                                                                                                                             | November 30, 2022 |
| AWS Marketplace updated [AWSVendorInsightsVendorReadOnly](#security-iam-awsmanpol-awsvendorinsightsvendorreadonly "#security-iam-awsmanpol-awsvendorinsightsvendorreadonly")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | AWS Marketplace updated `AWSVendorInsightsVendorReadOnly` to add<br>permissions to list tags and allows read-only accesss to AWS Artifact<br>third-party reports (preview).                                                                                                                                                                                                                                                        | November 30, 2022 |
| [AWSVendorInsightsVendorFullAccess](#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess "#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess") and<br>[AWSVendorInsightsVendorReadOnly](#security-iam-awsmanpol-awsvendorinsightsvendorreadonly "#security-iam-awsmanpol-awsvendorinsightsvendorreadonly")<br>– Added new policies                                                                                                                                                                                                                                                                                                                                                                                                     | AWS Marketplace added policies for the new feature AWS Marketplace Vendor Insights:<br>`AWSMarketplaceSellerProductsFullAccess` and<br>`AWSVendorInsightsVendorReadOnly`.                                                                                                                                                                                                                                                          | July 26, 2022     |
| [AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess "#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess")and [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess")– Updated policies                                                                                                                                                                                                                                                                                                                                                                                                   | AWS Marketplace updated policies for the new feature AWS Marketplace Vendor Insights:<br>`AWSMarketplaceSellerProductsFullAccess` and<br>`AWSMarketplaceSellerFullAccess`.                                                                                                                                                                                                                                                         | July 26, 2022     |
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess "#security-iam-awsmanpol-awsmarketplacesellerfullaccess") and<br>[AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess "#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess")<br>– Update to existing policies                                                                                                                                                                                                                                                                                                                                                                                | AWS Marketplace updated the policies so that the<br>`iam:PassedToService` condition is only applied to<br>`iam:PassRole`.                                                                                                                                                                                                                                                                                                          | November 22, 2021 |
| [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess "#security-iam-awsmanpol-awsmarketplacefullaccess") – Update<br>to an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | AWS Marketplace removed a duplicate<br>`ec2:DescribeAccountAttributes` permission from<br>`AWSMarketplaceFullAccess` policy.                                                                                                                                                                                                                                                                                                       | July 20, 2021     |
| AWS Marketplace started tracking changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | AWS Marketplace started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                          | April 20, 2021    |
