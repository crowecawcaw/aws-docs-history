

# AWS managed policies for AWS Marketplace buyers
<a name="buyer-security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

This section lists each of the policies used to manage buyer access to AWS Marketplace. For information about seller policies, see [AWS managed policies for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html) in the *AWS Marketplace Seller Guide*.

**Topics**
+ [AWS managed policy: AWSMarketplaceDeploymentServiceRolePolicy](#deployment-service-manpol)
+ [AWS managed policy: AWSMarketplaceDiscoveryFullAccess](#security-iam-awsmanpol-awsmarketplacediscoveryfullaccess)
+ [AWS managed policy: AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess)
+ [AWS managed policy: AWSMarketplaceImageBuildFullAccess (Deprecated)](#security-iam-awsmanpol-awsmarketplaceimagebuildfullaccess)
+ [AWS managed policy: AWSMarketplaceLicenseManagementServiceRolePolicy](#security-iam-awsmanpol-awsmarketplacelicensemanagementservicerolepolicy)
+ [AWS managed policy: AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions)
+ [AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess](#security-iam-awsmanpol-awsmarketplaceprocurementsystemadminfullaccess)
+ [AWS managed policy: AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only)
+ [AWS managed policy: AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess)
+ [AWS managed policy: AWSPrivateMarketplaceRequests](#security-iam-awsmanpol-awsprivatemarketplacerequests)
+ [AWS managed policy: AWSServiceRoleForPrivateMarketplaceAdminPolicy](#private-marketplace-slr-manpol)
+ [AWS managed policy: AWSVendorInsightsAssessorFullAccess](#aws-vi-assessor-full-access)
+ [AWS managed policy: AWSVendorInsightsAssessorReadOnly](#aws-vi-assessor-read-only)
+ [AWS managed policy: AWSServiceRoleForProcurementInsightsPolicy](#aws-procurement-insights)
+ [AWS Marketplace updates to AWS managed policies](#buyer-security-iam-awsmanpol-updates)

## AWS managed policy: AWSMarketplaceDeploymentServiceRolePolicy
<a name="deployment-service-manpol"></a>

You can't attach the `AWSMarketplaceDeploymentServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows AWS Marketplace to perform actions on your behalf. For more information, see [Using service-linked roles for AWS Marketplace](buyer-using-service-linked-roles.md).

This policy grants contributor permissions that allow AWS Marketplace to manage deployment-related parameters, which are stored as secrets in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), on your behalf.

To view the permissions for this policy, see [AWSMarketplaceDeploymentServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceDeploymentServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceDiscoveryFullAccess
<a name="security-iam-awsmanpol-awsmarketplacediscoveryfullaccess"></a>

You can attach the `AWSMarketplaceDiscoveryFullAccess` policy to your IAM identities.

Provides full access to the AWS Marketplace Discovery API for searching and retrieving product and pricing information.

To view the permissions for this policy, see [AWSMarketplaceDiscoveryFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceDiscoveryFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceFullAccess
<a name="security-iam-awsmanpol-awsmarketplacefullaccess"></a>

You can attach the `AWSMarketplaceFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to AWS Marketplace and related services, both as a buyer and a seller. These permissions include the ability to subscribe and unsubscribe to AWS Marketplace software, manage AWS Marketplace software instances from the AWS Marketplace, creating and managing private marketplace in your account, as well as access to Amazon EC2, CloudFormation, and Amazon EC2 Systems Manager.

To view the permissions for this policy, see [AWSMarketplaceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceImageBuildFullAccess (Deprecated)
<a name="security-iam-awsmanpol-awsmarketplaceimagebuildfullaccess"></a>

This policy granted contributor permissions that allow full access to the AWS Marketplace private image build feature. In addition to creating private images, it also provided permissions to add tags to images, and to launch and terminate Amazon EC2 instances.

For more information, see [Deprecated AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html#deprecated-managed-policies) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSMarketplaceLicenseManagementServiceRolePolicy
<a name="security-iam-awsmanpol-awsmarketplacelicensemanagementservicerolepolicy"></a>

You can't attach the `AWSMarketplaceLicenseManagementServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows AWS Marketplace to perform actions on your behalf. For more information, see [Using service-linked roles for AWS Marketplace](buyer-using-service-linked-roles.md).

This policy grants contributor permissions that allow AWS Marketplace to manage licenses on your behalf.

To view the permissions for this policy, see [AWSMarketplaceLicenseManagementServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceLicenseManagementServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceManageSubscriptions
<a name="security-iam-awsmanpol-awsmarketplacemanagesubscriptions"></a>

You can attach the `AWSMarketplaceManageSubscriptions` policy to your IAM identities.

This policy grants contributor permissions that allow subscribing and unsubscribing to AWS Marketplace products. It also allows buyers to access Express Private Offers and manage agreement cancellation requests.

The permissions are organized into the following groups:
+ `aws-marketplace` – Allows principals to view, subscribe to, and unsubscribe from AWS Marketplace products.
+ `aws-marketplace` – Allows principals to create and manage private marketplace requests and view private product listings.
+ `aws-marketplace` – Allows principals to manage purchase orders and handle payment requests for purchase agreements, including accepting or rejecting payment requests and viewing agreement charges. These permissions are restricted to agreements of type PurchaseAgreement.
+ `aws-marketplace` – Allows principals to view and describe changesets in the AWS Marketplace catalog.
+ `aws-marketplace` – Allows principals to create and manage agent token containers and express private offers through the changeset mechanism. These permissions are limited to specific change types: CreateAgentTokenContainer, RequestExpressPrivateOffer, and ExpireToken.
+ `aws-marketplace` – Allows principals to list and describe entities in the AWS Marketplace catalog, such as products, offers, and agreements.
+ `aws-marketplace` – Allows principals to manage agreement cancellation requests as the accepting party, including listing, retrieving, accepting, rejecting cancellation requests, and directly canceling agreements. These permissions are restricted to PurchaseAgreement type and Acceptor party type.
+ `aws-marketplace` – Allows principals to search listings, retrieve product and offer details, and list purchase and fulfillment options using the Discovery API.

To view the permissions for this policy, see [AWSMarketplaceManageSubscriptions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess
<a name="security-iam-awsmanpol-awsmarketplaceprocurementsystemadminfullaccess"></a>

You can attach the `AWSMarketplaceProcurementSystemAdminFullAccess` policy to your IAM identities.

This policy grants admin permissions that allow managing all aspects of an AWS Marketplace eProcurement integration, including listing the accounts in your organization and managing procurement portal preferences. For more information about eProcurement integrations, see [Integrating AWS Marketplace with procurement systems](procurement-system-integration.md) .

The permissions are organized into the following groups:
+ `aws-marketplace` – Allows managing AWS Marketplace procurement system configuration.
+ `organizations` – Allows listing and describing accounts and organizational structure in AWS Organizations.
+ `invoicing` – Allows creating, retrieving, and listing procurement portal preferences.

To view the permissions for this policy, see [AWSMarketplaceProcurementSystemAdminFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceProcurementSystemAdminFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceRead-only
<a name="security-iam-awsmanpol-awsmarketplaceread-only"></a>

You can attach the `AWSMarketplaceRead-only` policy to your IAM identities.

This policy grants read-only permissions that allows viewing products, private offers, and subscriptions for your account on AWS Marketplace, as well as viewing the Amazon EC2, AWS Identity and Access Management, and Amazon SNS resources in the account.

The permissions are organized into the following groups:
+ `aws-marketplace` – Allows principals to view subscriptions and list agreement charges.
+ `ec2` – Allows principals to describe account attributes, addresses, images, instances, key pairs, security groups, subnets, and VPCs.
+ `iam` – Allows principals to list roles and instance profiles.
+ `sns` – Allows principals to get topic attributes and list topics.
+ `aws-marketplace` – Allows principals to list and describe private marketplace requests, and view agreement payment requests.
+ `aws-marketplace` – Allows principals to list private product listings.
+ `aws-marketplace` – Allows principals to list and view agreement cancellation requests.
+ `aws-marketplace` – Allows principals to search listings, retrieve product and offer details, and list purchase and fulfillment options using the Discovery API.

To view the permissions for this policy, see [AWSMarketplaceRead-only](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceRead-only.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSPrivateMarketplaceAdminFullAccess
<a name="security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess"></a>

You can attach the `AWSPrivateMarketplaceAdminFullAccess` policy to your IAM identities.

This identity-based policy enables administrators to manage AWS Private Marketplace configurations and associated organizational controls. This policy includes IAM and Organizations permissions. It grants permissions to do the following actions: 

1. Manage Private Marketplace service-linked roles (SLR).

   1. Get role information for `AWSServiceRoleForPrivateMarketplaceAdmin`.

   1. Create service-linked roles for Private Marketplace administration.

1. Handle organizational delegated administration.

   1. Register and deregister delegated administrators for Private Marketplace.

   1. Enable AWS service access for Private Marketplace within Organizations.

1. Manage Private Marketplace products and requests.

   1. Associate and disassociate products with Private Marketplace.

   1. List and describe Private Marketplace requests.

   1. Perform catalog operations (list entities, describe entities, manage change sets).

   1. Handle resource tagging for AWS Marketplace resources.

1. Access Organizations information.

   1. View organization details, organizational units, and accounts.

   1. List organizational hierarchy information.

   1. Monitor AWS service access and delegated administrators.

This policy is designed for administrators who need to set up and manage Private Marketplace across an Organizations structure, granting both console and programmatic access to these functions.

The policy includes specific conditions to ensure Private Marketplace service principal validation and appropriate resource-level permissions for IAM roles and organizational management. For more information about using multiple administrators, see [Example policies for private marketplace administrators](it-administrator.md#creating-custom-policies-for-private-marketplace-admin).

To view the permissions for this policy, see [AWSPrivateMarketplaceAdminFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateMarketplaceAdminFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSPrivateMarketplaceRequests
<a name="security-iam-awsmanpol-awsprivatemarketplacerequests"></a>

You can attach the `AWSPrivateMarketplaceRequests` policy to your IAM identities.

This policy grants contributor permissions that allow access to request products to be added to their Private Marketplace experience, and to view those requests. These requests must be approved or declined by a Private Marketplace administrator.

The permissions are organized into multiple groups:

1. `LegacyPrivateMarketplaceRequestsPermissions`: These permissions are used by legacy Private Marketplace which will be deprecated. For details, see [Private Marketplace](private-marketplace-current.md).

1. `PrivateMarketplaceManageRequestsPermissions`: These permissions are required to create and cancel product approval requests.

1. `PrivateMarketplaceReadRequestsPermissions` and `PrivateMarketplaceListRequestsPermissions`: These permissions are required to list and get details of the product approval requests.

1. `PrivateMarketplaceReadChangeSetPermissions`: These permissions are required to list and get details of change sets to create and cancel requests. See [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets) in the *AWS Marketplace API Reference*.

1. `PrivateMarketplaceTaggingRequestsPermissions`: The tagging permissions are optional and allow users to tag the requests. See [Managing tags on resources](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/managing-tags.html) in the *AWS Marketplace API Reference*.

To view the permissions for this policy, see [AWSPrivateMarketplaceRequests](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPrivateMarketplaceRequests.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSServiceRoleForPrivateMarketplaceAdminPolicy
<a name="private-marketplace-slr-manpol"></a>

You can't attach the `AWSServiceRoleForPrivateMarketplaceAdminPolicy` to your IAM entities. This policy is attached to a service-linked role that allows AWS Marketplace to perform actions on your behalf. For more information, see [Using service-linked roles for AWS Marketplace](buyer-using-service-linked-roles.md).

This policy grants contributor permissions that allow AWS Marketplace to describe and update Private Marketplace resources and describe AWS Organizations.

To view the permissions for this policy, see [AWSServiceRoleForPrivateMarketplaceAdminPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSServiceRoleForPrivateMarketplaceAdminPolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSVendorInsightsAssessorFullAccess
<a name="aws-vi-assessor-full-access"></a>

You can attach the `AWSVendorInsightsAssessorFullAccess` policy to your IAM identities.

This policy grants full access for viewing entitled AWS Marketplace Vendor Insights resources and managing AWS Marketplace Vendor Insights subscriptions. These requests must be approved or denied by an administrator. It allows read-only access to AWS Artifact third-party reports. 

AWS Marketplace Vendor Insights identifies assessor is equal to buyer and vendor is equal to seller. 

To view the permissions for this policy, see [AWSVendorInsightsAssessorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVendorInsightsAssessorFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSVendorInsightsAssessorReadOnly
<a name="aws-vi-assessor-read-only"></a>

You can attach the `AWSVendorInsightsAssessorReadOnly` policy to your IAM identities.

This policy grants read-only access for viewing entitled AWS Marketplace Vendor Insights resources. These requests must be approved or denied by an administrator. It allows read-only access to reports in AWS Artifact. 

 requests must be approved or denied by an administrator. It allows read-only access to AWS Artifact third-party reports.

AWS Marketplace Vendor Insights identifies assessor as the buyer and vendor is equal to the seller for the purposes of this guide.

To view the permissions for this policy, see [AWSVendorInsightsAssessorReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVendorInsightsAssessorReadOnly.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSServiceRoleForProcurementInsightsPolicy
<a name="aws-procurement-insights"></a>

You can attach the `AWSServiceRoleForProcurementInsightsPolicy` policy to your IAM identities.

This policy grants the `AWSServiceRoleForProcurementInsightsPolicy` access to the resource data in your AWS organization.. AWS Marketplace uses the data to populate the [Procurement insights dashboard](https://docs.aws.amazon.com/marketplace/latest/buyerguide/procurement-insights.html). The dashboard enables buyers with management accounts to view all the agreements across all the accounts in an organization.

To view the permissions for this policy, see [AWSServiceRoleForProcurementInsightsPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSServiceRoleForProcurementInsightsPolicy.html) in the *AWS Managed Policy Reference*.

## AWS Marketplace updates to AWS managed policies
<a name="buyer-security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Marketplace since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Marketplace [Document history for AWS Marketplace Buyer Guide](document-history.md)

**Note**  
In AWS Marketplace Vendor Insights, an assessor is equal to a buyer, and a vendor is equal to a seller for the purposes of this guide.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions) — updates to existing policy | AWS Marketplace added Discovery API permissions for searching listings, retrieving product and offer details, and listing purchase and fulfillment options. | May 7, 2026 | 
| [AWSMarketplaceDiscoveryFullAccess](#security-iam-awsmanpol-awsmarketplacediscoveryfullaccess) — new policy | AWS Marketplace added a new policy that provides full access to the AWS Marketplace Discovery API for searching and retrieving product and pricing information. | May 7, 2026 | 
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only) — updates to existing policy | AWS Marketplace added read-only permissions for Discovery API operations including searching listings, retrieving product and offer details, and listing purchase and fulfillment options. | May 7, 2026 | 
| [AWSMarketplaceProcurementSystemAdminFullAccess](#security-iam-awsmanpol-awsmarketplaceprocurementsystemadminfullaccess) — updates to existing policy | AWS Marketplace added permissions for creating, retrieving, and listing procurement portal preferences. | April 7, 2026 | 
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only) — updates to existing policy | AWS Marketplace added permissions for listing and viewing agreement cancellation requests. | March 31, 2026 | 
| [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions) — updates to existing policy | AWS Marketplace added permissions for managing agreement cancellation requests, including listing, retrieving, accepting, rejecting cancellation requests, and directly canceling agreements. | March 31, 2026 | 
| [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions) — updates to existing policy | AWS Marketplace added permissions for buyers to access Express Private Offers. | November 30, 2025 | 
| [AWSPrivateMarketplaceRequests](#security-iam-awsmanpol-awsprivatemarketplacerequests) — updates to existing policy | AWS Marketplace added permissions to create and cancel product approval requests, list and get details of the product approval requests, and allow users to tag the requests. | November 17, 2025 | 
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess) — updates to existing policy | AWS Marketplace added service-linked role and Organizations integration permissions for Private Marketplace administrators. | June 5, 2025 | 
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only) and [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions) — updates to existing policies | AWS Marketplace updated existing policies to remove policies related to the discontinued Private Image Build delivery method. | May 7, 2025 | 
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only) and [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions) — updates to existing policies | AWS Marketplace updated existing policies to support listing agreement charges and updating purchase orders in the AWS Marketplace console. | November 21, 2024 | 
| Added the [AWSServiceRoleForProcurementInsightsPolicy](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.html#aws-procurement-insights). | AWS Marketplace added a new policy for accessing and describing the data in an Organizations. AWS Marketplace uses the data to populate the [Procurement insights dashboard](https://docs.aws.amazon.com/marketplace/latest/buyerguide/procurement-insights.html). | October 3, 2024 | 
| Deprecated the legacy AWSMarketplaceImageBuildFullAccess AWS Marketplace policy | AWS Marketplace discontinued the Private Image Build delivery method, so the AWSMarketplaceImageBuildFullAcces policy was also discontinued. | May 30, 2024 | 
| [AWSServiceRoleForPrivateMarketplaceAdminPolicy](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.html#private-marketplace-slr-manpol) — Added policy for new feature in AWS Marketplace | AWS Marketplace added a new policy to support managing Private Marketplace resources and describing AWS Organizations. | February 16, 2024 | 
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess) — Update to existing policy | AWS Marketplace updated the policy to support reading AWS Organizations data. | February 16, 2024 | 
| [AWSMarketplaceDeploymentServiceRolePolicy](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.html#deployment-service-manpol) — Added policy for new feature in AWS Marketplace | AWS Marketplace added a new policy to support managing deployment-related parameters. | November 29, 2023 | 
| [AWSMarketplaceRead-only](#security-iam-awsmanpol-awsmarketplaceread-only) and [AWSMarketplaceManageSubscriptions](#security-iam-awsmanpol-awsmarketplacemanagesubscriptions) — updates to existing policies  | AWS Marketplace updated existing policies to allow access to the Private offers page. | January 19, 2023 | 
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess) — Update to existing policy | AWS Marketplace updated the policy for the new tag-based authorization feature. | December 9, 2022 | 
| [AWSVendorInsightsAssessorReadOnly](#aws-vi-assessor-read-only) AWS Marketplace updated AWSVendorInsightsAssessorReadOnly | AWS Marketplace updated AWSVendorInsightsAssessorReadOnly to add read-only access to reports in AWS Artifact third-party report (preview). | November 30, 2022 | 
| [AWSVendorInsightsAssessorFullAccess](#aws-vi-assessor-full-access) AWS Marketplace updated AWSVendorInsightsAssessorFullAccess | AWS Marketplace updated `AWSVendorInsightsAssessorFullAccess` to add agreement search and read-only access to AWS Artifact third-party report (preview). | November 30, 2022 | 
|  [AWSVendorInsightsAssessorFullAccess](#aws-vi-assessor-full-access) and [AWSVendorInsightsAssessorReadOnly](#aws-vi-assessor-read-only) — Added policies for new feature in AWS Marketplace | AWS Marketplace added policies for the new feature AWS Marketplace Vendor Insights: `AWSVendorInsightsAssessorFullAccess` and `AWSVendorInsightsAssessorReadOnly` | July 26, 2022 | 
| [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess) and AWSMarketplaceImageBuildFullAccess — Updates to an existing policies | AWS Marketplace removed unneeded permissions to improve security. | March 4, 2022 | 
| [AWSPrivateMarketplaceAdminFullAccess](#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess) — Update to an existing policy | AWS Marketplace removed unused permissions from the `AWSPrivateMarketplaceAdminFullAccess` policy. | August 27, 2021 | 
| [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess) — Update to an existing policy | AWS Marketplace removed a duplicate `ec2:DescribeAccountAttributes` permission from the `AWSMarketplaceFullAccess` policy. | July 20, 2021 | 
| AWS Marketplace started tracking changes | AWS Marketplace started tracking changes for its AWS managed policies. | April 20, 2021 | 