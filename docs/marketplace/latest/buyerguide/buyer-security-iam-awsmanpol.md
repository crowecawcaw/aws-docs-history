# AWS managed policies for AWS Marketplace

buyers

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

This section lists each of the policies used to manage buyer access to AWS Marketplace. For
information about seller policies, see [AWS managed policies
for AWS Marketplace sellers](../userguide/security-iam-awsmanpol.md "../userguide/security-iam-awsmanpol.md") in the _AWS Marketplace Seller Guide_.

###### Topics

- [AWS managed policy:
  AWSMarketplaceDeploymentServiceRolePolicy](#deployment-service-manpol "#deployment-service-manpol")
- [AWS managed policy:
  AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess "#security-iam-awsmanpol-awsmarketplacefullaccess")
- [AWS
  managed policy: AWSMarketplaceImageBuildFullAccess
  (Deprecated)](#security-iam-awsmanpol-awsmarketplaceimagebuildfullaccess "#security-iam-awsmanpol-awsmarketplaceimagebuildfullaccess")
- [AWS managed policy: AWSMarketplaceLicenseManagementServiceRolePolicy](#security-iam-awsmanpol-awsmarketplacelicensemanagementservicerolepolicy "#security-iam-awsmanpol-awsmarketplacelicensemanagementservicerolepolicy")
- [AWS managed
  policy: AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions "#security-iam-awsmanpol-awsmarketplacemanagesubscriptions")
- [AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess](#security-iam-awsmanpol-awsmarketplaceprocurementsystemadminfullaccess "#security-iam-awsmanpol-awsmarketplaceprocurementsystemadminfullaccess")
- [AWS managed policy:
  AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only "#security-iam-awsmanpol-awsmarketplaceread-only")
- [AWS
  managed policy: AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess")
- [AWS managed
  policy: AWSPrivateMarketplaceRequests](#security-iam-awsmanpol-awsprivatemarketplacerequests "#security-iam-awsmanpol-awsprivatemarketplacerequests")
- [AWS managed policy:
  AWSServiceRoleForPrivateMarketplaceAdminPolicy](#private-marketplace-slr-manpol "#private-marketplace-slr-manpol")
- [AWS managed policy:
  AWSVendorInsightsAssessorFullAccess](#aws-vi-assessor-full-access "#aws-vi-assessor-full-access")
- [AWS managed policy:
  AWSVendorInsightsAssessorReadOnly](#aws-vi-assessor-read-only "#aws-vi-assessor-read-only")
- [AWS managed policy: AWSServiceRoleForProcurementInsightsPolicy](#aws-procurement-insights "#aws-procurement-insights")
- [AWS Marketplace updates to AWS
  managed policies](#buyer-security-iam-awsmanpol-updates "#buyer-security-iam-awsmanpol-updates")

## AWS managed policy:

AWSMarketplaceDeploymentServiceRolePolicy

You can't attach the `AWSMarketplaceDeploymentServiceRolePolicy` to your
IAM entities. This policy is attached to a service-linked role that allows AWS Marketplace
to perform actions on your behalf. For more information, see [Using service-linked roles for
AWS Marketplace](buyer-using-service-linked-roles.md "buyer-using-service-linked-roles.md").

This policy grants contributor permissions that allow AWS Marketplace to manage
deployment-related parameters, which are stored as secrets in [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"), on your behalf.

To view the permissions for this policy, see [AWSMarketplaceDeploymentServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSMarketplaceDeploymentServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceDeploymentServiceRolePolicy.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy:

AWSMarketplaceFullAccess

You can attach the `AWSMarketplaceFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow full access to AWS Marketplace and
related services, both as a buyer and a seller. These permissions include the ability to
subscribe and unsubscribe to AWS Marketplace software, manage AWS Marketplace software instances from the
AWS Marketplace, creating and managing private marketplace in your account, as well as access to
Amazon EC2, AWS CloudFormation, and Amazon EC2 Systems Manager.

To view the permissions for this policy, see [AWSMarketplaceFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md") in the _AWS Managed
Policy Reference_.

## AWS

managed policy: AWSMarketplaceImageBuildFullAccess
(Deprecated)

This policy granted contributor permissions that allow full access to the AWS Marketplace private
image build feature. In addition to creating private images, it also provided
permissions to add tags to images, and to launch and terminate Amazon EC2 instances.

For more information, see [Deprecated AWS managed policies](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md#deprecated-managed-policies "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md#deprecated-managed-policies") in the _AWS Managed Policy Reference Guide_.

## AWS managed policy: AWSMarketplaceLicenseManagementServiceRolePolicy

You can't attach the `AWSMarketplaceLicenseManagementServiceRolePolicy` to your IAM
entities. This policy is attached to a service-linked role that allows AWS Marketplace to
perform actions on your behalf. For more information, see [Using service-linked roles for
AWS Marketplace](buyer-using-service-linked-roles.md "buyer-using-service-linked-roles.md").

This policy grants contributor permissions that allow AWS Marketplace to manage licenses on your
behalf.

To view the permissions for this policy, see [AWSMarketplaceLicenseManagementServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSMarketplaceLicenseManagementServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceLicenseManagementServiceRolePolicy.md") in the _AWS
Managed Policy Reference_.

## AWS managed

policy: AWSMarketplaceManageSubscriptions

You can attach the `AWSMarketplaceManageSubscriptions` policy to your IAM
identities.

This policy grants contributor permissions that allow subscribing and unsubscribing to
AWS Marketplace products.

To view the permissions for this policy, see [AWSMarketplaceManageSubscriptions](../../../aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md") in the _AWS Managed Policy
Reference_.

## AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess

You can attach the `AWSMarketplaceProcurementSystemAdminFullAccess` policy
to your IAM identities.

This policy grants admin permissions that allow managing all aspects of an AWS Marketplace
eProcurement integration, including listing the accounts in your organization. For more
information about eProcurement integrations, see [Integrating AWS Marketplace with procurement
systems](procurement-system-integration.md "procurement-system-integration.md") .

To view the permissions for this policy, see [AWSMarketplaceProcurementSystemAdminFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceProcurementSystemAdminFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceProcurementSystemAdminFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS managed policy:

AWSMarketplaceRead-only

You can attach the `AWSMarketplaceRead-only` policy to your IAM
identities.

This policy grants read-only permissions that allows viewing products, private offers,
and subscriptions for your account on AWS Marketplace, as well as viewing the Amazon EC2, AWS Identity and Access Management,
and Amazon SNS resources in the account.

To view the permissions for this policy, see [AWSMarketplaceRead-only](../../../aws-managed-policy/latest/reference/AWSMarketplaceRead-only.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceRead-only.md") in the _AWS Managed
Policy Reference_.

## AWS

managed policy: AWSPrivateMarketplaceAdminFullAccess

You can attach the `AWSPrivateMarketplaceAdminFullAccess` policy to your
IAM identities.

This identity-based policy enables administrators to manage AWS Private Marketplace configurations and associated organizational controls. This policy includes IAM and Organizations permissions. It grants permissions to do the following actions:

1. Manage Private Marketplace service-linked roles (SLR).
   1. Get role information for `AWSServiceRoleForPrivateMarketplaceAdmin`.
   2. Create service-linked roles for Private Marketplace administration.

2. Handle organizational delegated administration.
   1. Register and deregister delegated administrators for Private Marketplace.
   2. Enable AWS service access for Private Marketplace within Organizations.

3. Manage Private Marketplace products and requests.
   1. Associate and disassociate products with Private Marketplace.
   2. List and describe Private Marketplace requests.
   3. Perform catalog operations (list entities, describe entities, manage change sets).
   4. Handle resource tagging for AWS Marketplace resources.

4. Access Organizations information.
   1. View organization details, organizational units, and accounts.
   2. List organizational hierarchy information.
   3. Monitor AWS service access and delegated administrators.

This policy is designed for administrators who need to set up and manage Private Marketplace across an Organizations structure, granting both console and programmatic access to these functions.

The policy includes specific conditions to ensure Private Marketplace service principal validation and appropriate resource-level permissions for IAM roles and organizational management. For more information about using multiple administrators, see [Example policies for private marketplace administrators](it-administrator.md#creating-custom-policies-for-private-marketplace-admin "it-administrator.md#creating-custom-policies-for-private-marketplace-admin").

To view the permissions for this policy, see [AWSPrivateMarketplaceAdminFullAccess](../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceAdminFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceAdminFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS managed

policy: AWSPrivateMarketplaceRequests

You can attach the `AWSPrivateMarketplaceRequests` policy to your IAM
identities.

This policy grants contributor permissions that allow access to request products be
added to your private marketplace, and to view those requests. These requests must be
approved or denied by a private marketplace administrator.

To view the permissions for this policy, see [AWSPrivateMarketplaceRequests](../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceRequests.md "../../../aws-managed-policy/latest/reference/AWSPrivateMarketplaceRequests.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy:

AWSServiceRoleForPrivateMarketplaceAdminPolicy

You can't attach the `AWSServiceRoleForPrivateMarketplaceAdminPolicy` to
your IAM entities. This policy is attached to a service-linked role that allows
AWS Marketplace to perform actions on your behalf. For more information, see [Using service-linked roles for
AWS Marketplace](buyer-using-service-linked-roles.md "buyer-using-service-linked-roles.md").

This policy grants contributor permissions that allow AWS Marketplace to describe and update
Private Marketplace resources and describe AWS Organizations.

To view the permissions for this policy, see [AWSServiceRoleForPrivateMarketplaceAdminPolicy](../../../aws-managed-policy/latest/reference/AWSServiceRoleForPrivateMarketplaceAdminPolicy.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForPrivateMarketplaceAdminPolicy.md") in the
_AWS Managed Policy Reference_.

## AWS managed policy:

AWSVendorInsightsAssessorFullAccess

You can attach the `AWSVendorInsightsAssessorFullAccess` policy to your
IAM identities.

This policy grants full access for viewing entitled AWS Marketplace Vendor Insights resources and managing
AWS Marketplace Vendor Insights subscriptions. These requests must be approved or denied by an administrator. It
allows read-only access to AWS Artifact third-party reports.

AWS Marketplace Vendor Insights identifies assessor is equal to buyer and vendor is equal to seller.

To view the permissions for this policy, see [AWSVendorInsightsAssessorFullAccess](../../../aws-managed-policy/latest/reference/AWSVendorInsightsAssessorFullAccess.md "../../../aws-managed-policy/latest/reference/AWSVendorInsightsAssessorFullAccess.md") in the
_AWS Managed Policy Reference_.

## AWS managed policy:

AWSVendorInsightsAssessorReadOnly

You can attach the `AWSVendorInsightsAssessorReadOnly` policy to your IAM
identities.

This policy grants read-only access for viewing entitled AWS Marketplace Vendor Insights resources. These
requests must be approved or denied by an administrator. It allows read-only access to
reports in AWS Artifact.

requests must be approved or denied by an administrator. It allows read-only access
to AWS Artifact third-party reports.

AWS Marketplace Vendor Insights identifies assessor as the buyer and vendor is equal to the seller for the
purposes of this guide.

To view the permissions for this policy, see [AWSVendorInsightsAssessorReadOnly](../../../aws-managed-policy/latest/reference/AWSVendorInsightsAssessorReadOnly.md "../../../aws-managed-policy/latest/reference/AWSVendorInsightsAssessorReadOnly.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy: AWSServiceRoleForProcurementInsightsPolicy

You can attach the `AWSServiceRoleForProcurementInsightsPolicy` policy to your IAM
identities.

This policy grants the `AWSServiceRoleForProcurementInsightsPolicy` access
to the resource data in your AWS organization.. AWS Marketplace uses the data to populate the [Procurement insights dashboard](procurement-insights.md "procurement-insights.md"). The dashboard enables buyers with
management accounts to view all the agreements across all the accounts in
an organization.

To view the permissions for this policy, see [AWSServiceRoleForProcurementInsightsPolicy](../../../aws-managed-policy/latest/reference/AWSServiceRoleForProcurementInsightsPolicy.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForProcurementInsightsPolicy.md") in the
_AWS Managed Policy Reference_.

## AWS Marketplace updates to AWS

managed policies

View details about updates to AWS managed policies for AWS Marketplace since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS Marketplace [Document history for AWS Marketplace Buyer Guide](document-history.md "document-history.md")

###### Note

In AWS Marketplace Vendor Insights, an assessor is equal to a buyer, and a vendor is
equal to a seller for the purposes of this guide.

| Change                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                      | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess") — updates to existing policy                                                                                                                           | AWS Marketplace added service-linked role and Organizations integration permissions for Private Marketplace administrators.                                                                                                      | June 5, 2025      |
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only "#security-iam-awsmanpol-awsmarketplaceread-only") and [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions "#security-iam-awsmanpol-awsmarketplacemanagesubscriptions") — updates to existing policies          | AWS Marketplace updated existing policies to remove policies related to the discontinued Private Image Build delivery method.                                                                                                    | May 7, 2025       |
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only "#security-iam-awsmanpol-awsmarketplaceread-only") and [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions "#security-iam-awsmanpol-awsmarketplacemanagesubscriptions") — updates to existing policies | AWS Marketplace updated existing policies to support listing agreement charges and updating purchase orders in the AWS Marketplace console.                                                                                      | November 21, 2024 |
| Added the [AWSServiceRoleForProcurementInsightsPolicy](buyer-security-iam-awsmanpol.md#aws-procurement-insights "buyer-security-iam-awsmanpol.md#aws-procurement-insights").                                                                                                                                               | AWS Marketplace added a new policy for accessing and describing the data in an Organizations. AWS Marketplace uses the data to populate the [Procurement insights dashboard](procurement-insights.md "procurement-insights.md"). | October 3, 2024   |
| Deprecated the legacy `AWSMarketplaceImageBuildFullAccess` AWS Marketplace policy                                                                                                                                                                                                                                          | AWS Marketplace discontinued the Private Image Build delivery method, so the `AWSMarketplaceImageBuildFullAcces` policy was also discontinued.                                                                                   | May 30, 2024      |
| [AWSServiceRoleForPrivateMarketplaceAdminPolicy](buyer-security-iam-awsmanpol.md#private-marketplace-slr-manpol "buyer-security-iam-awsmanpol.md#private-marketplace-slr-manpol") — Added policy for new feature in AWS Marketplace                                                                                        | AWS Marketplace added a new policy to support managing Private Marketplace resources and describing AWS Organizations.                                                                                                           | February 16, 2024 |
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess") — Update to existing policy                                                                                                                            | AWS Marketplace updated the policy to support reading AWS Organizations data.                                                                                                                                                    | February 16, 2024 |
| [AWSMarketplaceDeploymentServiceRolePolicy](buyer-security-iam-awsmanpol.md#deployment-service-manpol "buyer-security-iam-awsmanpol.md#deployment-service-manpol") — Added policy for new feature in AWS Marketplace                                                                                                       | AWS Marketplace added a new policy to support managing deployment-related parameters.                                                                                                                                            | November 29, 2023 |
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only "#security-iam-awsmanpol-awsmarketplaceread-only") and [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions "#security-iam-awsmanpol-awsmarketplacemanagesubscriptions") — updates to existing policies | AWS Marketplace updated existing policies to allow access to the **Private offers** page.                                                                                                                                        | January 19, 2023  |
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess") — Update to existing policy                                                                                                                            | AWS Marketplace updated the policy for the new tag-based authorization feature.                                                                                                                                                  | December 9, 2022  |
| [AWSVendorInsightsAssessorReadOnly](#aws-vi-assessor-read-only "#aws-vi-assessor-read-only") AWS Marketplace updated `AWSVendorInsightsAssessorReadOnly`                                                                                                                                                                   | AWS Marketplace updated `AWSVendorInsightsAssessorReadOnly` to add read-only access to reports in AWS Artifact third-party report (preview).                                                                                     | November 30, 2022 |
| [AWSVendorInsightsAssessorFullAccess](#aws-vi-assessor-full-access "#aws-vi-assessor-full-access") AWS Marketplace updated `AWSVendorInsightsAssessorFullAccess`                                                                                                                                                           | AWS Marketplace updated `AWSVendorInsightsAssessorFullAccess` to add agreement search and read-only access to AWS Artifact third-party report (preview).                                                                         | November 30, 2022 |
| [AWSVendorInsightsAssessorFullAccess](#aws-vi-assessor-full-access "#aws-vi-assessor-full-access") and [AWSVendorInsightsAssessorReadOnly](#aws-vi-assessor-read-only "#aws-vi-assessor-read-only") — Added policies for new feature in AWS Marketplace                                                                    | AWS Marketplace added policies for the new feature AWS Marketplace Vendor Insights: `AWSVendorInsightsAssessorFullAccess` and `AWSVendorInsightsAssessorReadOnly`                                                                | July 26, 2022     |
| [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess "#security-iam-awsmanpol-awsmarketplacefullaccess") and AWSMarketplaceImageBuildFullAccess — Updates to an existing policies                                                                                                                   | AWS Marketplace removed unneeded permissions to improve security.                                                                                                                                                                | March 4, 2022     |
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess "#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess") — Update to an existing policy                                                                                                                         | AWS Marketplace removed unused permissions from the `AWSPrivateMarketplaceAdminFullAccess` policy.                                                                                                                               | August 27, 2021   |
| [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess "#security-iam-awsmanpol-awsmarketplacefullaccess") — Update to an existing policy                                                                                                                                                             | AWS Marketplace removed a duplicate `ec2:DescribeAccountAttributes` permission from the `AWSMarketplaceFullAccess` policy.                                                                                                       | July 20, 2021     |
| AWS Marketplace started tracking changes                                                                                                                                                                                                                                                                                   | AWS Marketplace started tracking changes for its AWS managed policies.                                                                                                                                                           | April 20, 2021    |
