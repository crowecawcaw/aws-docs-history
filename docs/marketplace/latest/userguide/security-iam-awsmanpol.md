

# AWS managed policies for AWS Marketplace sellers
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

This section lists each of the policies used to manage seller access to AWS Marketplace. For information about buyer policies, see [AWS managed policies for AWS Marketplace buyers](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.html) in the *AWS Marketplace Buyer Guide*.

**Topics**
+ [AWS managed policy: AWSMarketplaceAmiIngestion](#security-iam-awsmanpol-awsmarketplaceamiingestion)
+ [AWS managed policy: AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess)
+ [AWS managed policy: AWSMarketplaceGetEntitlements](#security-iam-awsmanpol-awsmarketplacegetentitlements)
+ [AWS managed policy: AWSMarketplaceMeteringFullAccess](#security-iam-awsmanpol-awsmarketplacemeteringfullaccess)
+ [AWS managed policy: AWSMarketplaceMeteringRegisterUsage](#security-iam-awsmanpol-awsmarketplacemeteringregisterusage)
+ [AWS managed policy: AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess)
+ [AWS managed policy: AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess)
+ [AWS managed policy: AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly)
+ [AWS managed policy: AWSMarketplaceSellerOfferManagement](#security-iam-awsmanpol-awsmarketplaceselleroffermanagement)
+ [AWS managed policy: AWSMarketplaceResaleAuthorizationServiceRolePolicy](#security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy)
+ [AWS managed policy: AWSVendorInsightsVendorFullAccess](#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess)
+ [AWS managed policy: AWSVendorInsightsVendorReadOnly](#security-iam-awsmanpol-awsvendorinsightsvendorreadonly)
+ [AWS Marketplace updates to AWS managed policies](#security-iam-awsmanpol-updates)

## AWS managed policy: AWSMarketplaceAmiIngestion
<a name="security-iam-awsmanpol-awsmarketplaceamiingestion"></a>

You can create a service role with this policy that can then be used by AWS Marketplace to perform actions on your behalf. For more information about using `AWSMarketplaceAmiIngestion`, see [Giving AWS Marketplace access to your AMI](single-ami-marketplace-ami-access.md).

This policy grants contributor permissions that allow AWS Marketplace to copy your Amazon Machine Images (AMIs) to list them on AWS Marketplace.

To view the permissions for this policy, see [AWSMarketplaceAmiIngestion](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceAmiIngestion.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceFullAccess
<a name="security-iam-awsmanpol-awsmarketplacefullaccess"></a>

You can attach the `AWSMarketplaceFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to AWS Marketplace and related services, as a buyer. These permissions include the following abilities: 
+ Subscribe and unsubscribe to AWS Marketplace software.
+ Manage AWS Marketplace software instances from AWS Marketplace.
+ Create and manage a private marketplace in your account.
+ Provide access to Amazon EC2, CloudFormation, and Amazon EC2 Systems Manager.

To view the permissions for this policy, see [AWSMarketplaceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceGetEntitlements
<a name="security-iam-awsmanpol-awsmarketplacegetentitlements"></a>

You can attach the `AWSMarketplaceGetEntitlements` policy to your IAM identities.

This policy grants read-only permissions that allow software as a service (SaaS) product sellers to check whether a customer has subscribed to their AWS Marketplace SaaS product.

To view the permissions for this policy, see [AWSMarketplaceGetEntitlements](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceGetEntitlements.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceMeteringFullAccess
<a name="security-iam-awsmanpol-awsmarketplacemeteringfullaccess"></a>

You can attach the `AWSMarketplaceMeteringFullAccess` policy to your IAM identities.

This policy grants contributor permissions that allow reporting metered usage that corresponds to AMI and container products with flexible consumption pricing on AWS Marketplace.

To view the permissions for this policy, see [AWSMarketplaceMeteringFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceMeteringFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceMeteringRegisterUsage
<a name="security-iam-awsmanpol-awsmarketplacemeteringregisterusage"></a>

You can attach the `AWSMarketplaceMeteringRegisterUsage` policy to your IAM identities.

This policy grants contributor permissions that allow reporting metered usage that corresponds to container products with hourly pricing on AWS Marketplace.

To view the permissions for this policy, see [AWSMarketplaceMeteringRegisterUsage](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceMeteringRegisterUsage.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceSellerFullAccess
<a name="security-iam-awsmanpol-awsmarketplacesellerfullaccess"></a>

You can attach the `AWSMarketplaceSellerFullAccess` policy to your IAM identities.

This policy grants administrative permissions that allow full access to all seller operations on AWS Marketplace, including AWS Marketplace Management Portal, and managing the Amazon EC2 AMI used in AMI-based products.

**Permissions details**

This policy includes the following permissions:
+ `aws-marketplace` – Allows principals to manage change sets, entities, agreements, and seller dashboards.
+ `aws-marketplace` – Allows principals to search and view purchase agreements and their terms where the user is the seller.
+ `aws-marketplace` – Allows principals to send, retrieve, list, and cancel agreement payment requests for purchase agreements.
+ `aws-marketplace` – Allows principals to list invoice line items, manage billing adjustment requests, and handle agreement cancellation requests for purchase agreements.
+ `aws-marketplace` – Allows principals to start, retrieve, and list invoice submission tasks.
+ `aws-marketplace` – Allows principals to list payables.
+ `aws-marketplace` – Allows principals to list and retrieve customer tax invoices generated by AWS on behalf of sellers.
+ `invoicing` – Allows principals to list invoice summaries and retrieve invoice PDFs for listing fee invoices.
+ `aws-marketplace` – Allows principals to create, update, and retrieve verification evidence for seller verification.
+ `aws-marketplace` – Allows principals to list verification evidence, start verifications, retrieve verification details, and list verifications.
+ `aws-marketplace` – Allows principals to start tax compliance profile change tasks, list change tasks, retrieve tax compliance profiles, and list tax compliance profiles.
+ `aws-marketplace` – Allows principals to manage resource policies and tag resources.
+ `aws-marketplace-management` – Allows principals to upload files, view reports and support information.
+ `ec2` – Allows principals to describe and modify AMI images and snapshots.
+ `iam` – Allows principals to retrieve role information and pass roles to the assets marketplace service.
+ `iam` – Allows principals to create service-linked roles for resale authorization.
+ `vendor-insights` – Allows principals to retrieve and list data sources, security profiles, and snapshots.
+ `payments` – Allows principals to retrieve, create, and delete payment instruments.
+ `tax` – Allows principals to manage tax interviews, registrations, and retrieve tax documents.
+ `support` – Allows principals to create support cases.
+ `q` – Allows principals to use Amazon Q Partner Assistant for conversations and requests.
+ `partnercentral` – Allows principals to start and retrieve seller verification status.
+ `s3` – Allows principals to upload objects to the AWS Marketplace ephemeral file upload bucket scoped to the caller's account.

To view the permissions for this policy, see [AWSMarketplaceSellerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceSellerProductsFullAccess
<a name="security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess"></a>

You can attach the `AWSMarketplaceSellerProductsFullAccess` policy to your IAM identities.

This policy grants contributor permissions that allow full access to manage products and to the AWS Marketplace Management Portal, and managing the Amazon EC2 AMI used in AMI-based products.

**Permissions details**

To view the permissions for this policy, see [AWSMarketplaceSellerProductsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerProductsFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceSellerProductsReadOnly
<a name="security-iam-awsmanpol-awsmarketplacesellerproductsreadonly"></a>

You can attach the `AWSMarketplaceSellerProductsReadOnly` policy to your IAM identities.

This policy grants read-only permissions that allow access to view products on the AWS Marketplace Management Portal, and view the Amazon EC2 AMI used in AMI-based products.



**Permissions details**

To view the permissions for this policy, see [AWSMarketplaceSellerProductsReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerProductsReadOnly.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceSellerOfferManagement
<a name="security-iam-awsmanpol-awsmarketplaceselleroffermanagement"></a>

You can attach the `AWSMarketplaceSellerOfferManagement` policy to your IAM identities. 

This policy grants sellers access to manage offers and view purchase agreements. Sellers can create and modify offers, track change sets, and monitor agreement lifecycle events including invoice line items, billing adjustments, and cancellation requests.

**Permissions details**

This policy includes the following permissions:
+ `aws-marketplace` – Allows principals to view and track the status of change sets submitted to AWS Marketplace.
+ `aws-marketplace` – Allows principals to initiate changes to existing offers and change sets, or create new offers on products.
+ `aws-marketplace` – Allows principals to list and retrieve details about marketplace entities including offers, products, and resale authorizations.
+ `aws-marketplace` – Allows principals to search and view purchase agreements and their terms where the user is the seller (proposer).
+ `aws-marketplace` – Allows principals to track invoice line items, billing adjustments, and cancellation requests for purchase agreements.

To view the permissions for this policy, see [AWSMarketplaceSellerOfferManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSMarketplaceResaleAuthorizationServiceRolePolicy
<a name="security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy"></a>

This policy is attached to a service-linked role that allows AWS Marketplace to perform actions on your behalf for Resale Authorization. For more information about using this service-linked role, see [Using service-linked roles for Selling Authorization with AWS Marketplace](using-roles-for-resale-authorization.md).

This policy grants permissions that allow AWS Marketplace to share ResaleAuthorization resources between manufacturers (ISVs) and channel partners using AWS Resource Access Manager (AWS RAM).

This policy includes permissions for AWS Marketplace operations and AWS Resource Access Manager (RAM) actions to facilitate the sharing and management of ResaleAuthorization resources across different AWS accounts and catalogs.

To view the permissions for this policy, see [AWSMarketplaceResaleAuthorizationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceResaleAuthorizationServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSVendorInsightsVendorFullAccess
<a name="security-iam-awsmanpol-awsvendorinsightsvendorfullaccess"></a>

You can attach the `AWSVendorInsightsVendorFullAccess` policy to your IAM identities.

This policy grants full access to create and manage all resources on AWS Marketplace Vendor Insights. In AWS Marketplace Vendor Insights, an assessor is equal to a buyer, and a vendor is equal to a seller for the purposes of this guide.

To view the permissions for this policy, see [AWSVendorInsightsVendorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVendorInsightsVendorFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSVendorInsightsVendorReadOnly
<a name="security-iam-awsmanpol-awsvendorinsightsvendorreadonly"></a>

You can attach the `AWSVendorInsightsVendorReadOnly` policy to your IAM identities.

This policy grants read-only access for viewing AWS Marketplace Vendor Insights profiles and related resources. In AWS Marketplace Vendor Insights, an assessor is equal to a buyer, and a vendor is equal to a seller for the purposes of this guide. 

To view the permissions for this policy, see [AWSVendorInsightsVendorReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVendorInsightsVendorReadOnly.html) in the *AWS Managed Policy Reference*.

## AWS Marketplace updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Marketplace since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Marketplace [Document history](document-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added `payments:DeletePaymentInstrument` to the `SellerSettings` statement. | August 12, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added new `TaxComplianceProfileChangeTaskManagement`, `TaxComplianceProfileRead`, and `TaxComplianceProfileList` statements with `aws-marketplace:StartTaxComplianceProfileChangeTask`, `aws-marketplace:GetTaxComplianceProfile`, `aws-marketplace:ListTaxComplianceProfileChangeTasks`, and `aws-marketplace:ListTaxComplianceProfiles`. Updated the `TagManagement` statement resource ARN to include tax compliance profile and tax compliance profile change task resources. | July 21, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added `tax:PutTaxRegistration` and `tax:ListTaxRegistrations` to the `SellerSettings` statement. | June 30, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added new `MarketplaceSellerVerificationEvidenceManagement` and `MarketplaceSellerVerificationManagement` statements with `aws-marketplace:CreateVerificationEvidence`, `aws-marketplace:UpdateVerificationEvidence`, `aws-marketplace:GetVerificationEvidence`, `aws-marketplace:ListVerificationEvidence`, `aws-marketplace:StartVerification`, `aws-marketplace:GetVerification`, and `aws-marketplace:ListVerifications`. Updated the `TagManagement` statement resource ARN to include verification evidence resources. | June 1, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added `aws-marketplace:ListIssuedTaxInvoices` and `invoicing:ListInvoiceSummaries` to the `SellerSettings` statement. Added `invoicing:GetInvoicePDF` to the `SellerSettings` statement. Added a new `SellerSettingsGetIssuedTaxInvoice` statement with `aws-marketplace:GetIssuedTaxInvoice` scoped to issued tax invoice resources. | May 7, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added a new `MarketplaceEphemeralWriteS3Access` statement with `s3:PutObject` permission for write access to the AWS Marketplace ephemeral file upload bucket, scoped to the caller's account. Added `aws-marketplace:ListInvoiceSubmissionTasks` to the `SellerSettings` statement. | April 29, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added `aws-marketplace:ListPayables` to the `SellerSettings` statement. Added a new `InvoiceSubmissionManagement` statement with `aws-marketplace:StartInvoiceSubmissionTask`, `aws-marketplace:GetInvoiceSubmissionTask`, and `aws-marketplace:ListInvoiceSubmissionTasks` scoped to invoice submission task resources. Updated the resource ARN for the `TagManagement` and `ResourcePolicyManagement` statements. | April 21, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added 8 new actions for managing agreement cancellations and billing adjustments: `aws-marketplace:ListAgreementInvoiceLineItems`, `aws-marketplace:ListBillingAdjustmentRequests`, `aws-marketplace:GetBillingAdjustmentRequest`, `aws-marketplace:BatchCreateBillingAdjustmentRequest`, `aws-marketplace:ListAgreementCancellationRequests`, `aws-marketplace:GetAgreementCancellationRequest`, `aws-marketplace:SendAgreementCancellationRequest`, and `aws-marketplace:CancelAgreementCancellationRequest`. | March 31, 2026 | 
| [AWSMarketplaceSellerOfferManagement](#security-iam-awsmanpol-awsmarketplaceselleroffermanagement) – Update to an existing policy | AWS Marketplace added 5 new read-only actions to track invoice line items, billing adjustments, and cancellation requests for purchase agreements: `aws-marketplace:ListAgreementInvoiceLineItems`, `aws-marketplace:ListBillingAdjustmentRequests`, `aws-marketplace:GetBillingAdjustmentRequest`, `aws-marketplace:ListAgreementCancellationRequests`, and `aws-marketplace:GetAgreementCancellationRequest`. | March 31, 2026 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Update to an existing policy | AWS Marketplace added two new Partner Central permissions for seller identity verification: `partnercentral:StartVerification` and `partnercentral:GetVerification`. | February 27, 2026 | 
| [AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess) – Update to an existing policy | AWS Marketplace updated `AWSMarketplaceSellerProductsFullAccess` policy to support all AWSMarketplace catalogs, put files into S3, and access legacy Partner Central. | November 30, 2025 | 
| [AWSMarketplaceResaleAuthorizationServiceRolePolicy](#security-iam-awsmanpol-awsmarketplaceresaleauthorizationservicerolepolicy) – Updated policy | AWS Marketplace updated the policy to support multi-catalog features and enable proper lifecycle management of ResaleAuthorization entities. The updates include:+  Updated resource ARN pattern from `arn:aws:aws-marketplace:*:*:AWSMarketplace/ResaleAuthorization/*` to `arn:aws:aws-marketplace:*:*:*/ResaleAuthorization/*`. <br />+  Added permissions `ram:DeleteResourceShare` and `aws-marketplace:DeleteResourcePolicy`.  | July 24, 2025 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policies | AWS Marketplace added four new `SellerSettings`permissions for the supplemental tax profile feature: `ListSupplementalTaxRegistrations`, `PutSupplementalTaxRegistration`, `DeleteSupplementalTaxRegistration`, `GetTaxRegistration`. | December 20, 2024 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policies<br />[AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess) – Updated policies<br />[AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policies<br />[AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly) – Updated policies | AWS Marketplace removed the `ListTasks`, `DescribeTask`, `UpdateTasks`, and `CompleteTasks` permissions. | December 10, 2024 | 
| [AWSMarketplaceSellerOfferManagement](#security-iam-awsmanpol-awsmarketplaceselleroffermanagement) – Added new policy | AWS Marketplace added new policy: AWSMarketplaceSellerOfferManagement | November 18, 2024 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policies | AWS Marketplace added the `UploadFiles` permission. The change enables sellers to use a deprecated page in the AWS Marketplace Management Portal. | November 6, 2024 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policies | AWS Marketplace added the `ListAssessments` and `DescribeAssessments` permissions. The changes enable SSLv2 users to access assessment data. | October 22, 2024 | 
| [AWSMarketplaceSellerProductsFullAccess – Updated policies](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess) | AWS Marketplace added the `ListAssessments` and `DescribeAssessments` permissions. The changes enable SSLv2 users to access assessment data. | October 22, 2024 | 
| [AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly) – Updated policies | AWS Marketplace added the `ListAssessments` and `DescribeAssessments` permissions. The changes enable SSLv2 users to access assessment data. | October 22, 2024 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policy | Updated the `AWSMarketplaceSellerFullAccess` documentation to reflect the removal of the following actions: `aws-marketplace-management:viewMarketing`, `aws-marketplace-management:viewSettings`, and `aws-marketplace-management:uploadFiles`. This update also includes removing the *Using fine-grained permissions* section. | June 4, 2024 | 
| [AWSMarketplaceGetEntitlements](#security-iam-awsmanpol-awsmarketplacegetentitlements) – Updated policy | AWS Marketplace updated AWSMarketplaceGetEntitlements to add sid for the policy statement. | March 22, 2024 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policy | AWS Marketplace updated AWSMarketplaceSellerFullAccess to add permissions for creating service-linked roles. | March 15, 2024 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policy | AWS Marketplace updated AWSMarketplaceSellerFullAccess to add a permission for accessing tax information. | February 8, 2024 | 
| [AWSVendorInsightsVendorFullAccess](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess) - Updated policy | AWS Marketplace updated AWSVendorInsightsVendorFullAccess to add permissions to update data sources. | October 18, 2023 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policy | AWS Marketplace updated AWSMarketplaceSellerFullAccess to add permissions for sharing entities. | June 1, 2023 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policy | AWS Marketplace updated AWSMarketplaceSellerFullAccess to add permissions related to account verifications, bank account verifications, case management, and seller notification details. | June 1, 2023 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) – Updated policy | AWS Marketplace updated AWSMarketplaceSellerFullAccess to add permissions to access seller dashboards. | December 23, 2022 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess), [AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess), [AWSMarketplaceSellerProductsReadOnly](#security-iam-awsmanpol-awsmarketplacesellerproductsreadonly) – Update to existing policy | AWS Marketplace updated policies for the new tag-based authorization feature. | December 9, 2022 | 
| AWS Marketplace updated [AWSVendorInsightsVendorFullAccess](#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess)  | AWS Marketplace updated AWSMarketplaceSellerProductsFullAccess to add agreement search, updating profile snapshots, vendor tagging, and allows read-only access to AWS Artifact third-party reports (preview). | November 30, 2022 | 
| AWS Marketplace updated [AWSVendorInsightsVendorReadOnly](#security-iam-awsmanpol-awsvendorinsightsvendorreadonly) | AWS Marketplace updated AWSVendorInsightsVendorReadOnly to add permissions to list tags and allows read-only accesss to AWS Artifact third-party reports (preview). | November 30, 2022 | 
| [AWSVendorInsightsVendorFullAccess](#security-iam-awsmanpol-awsvendorinsightsvendorfullaccess) and [AWSVendorInsightsVendorReadOnly](#security-iam-awsmanpol-awsvendorinsightsvendorreadonly) – Added new policies | AWS Marketplace added policies for the new feature AWS Marketplace Vendor Insights: AWSMarketplaceSellerProductsFullAccess and AWSVendorInsightsVendorReadOnly. | July 26, 2022 | 
| [AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess)and [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess)– Updated policies | AWS Marketplace updated policies for the new feature AWS Marketplace Vendor Insights: AWSMarketplaceSellerProductsFullAccess and AWSMarketplaceSellerFullAccess. | July 26, 2022 | 
| [AWSMarketplaceSellerFullAccess](#security-iam-awsmanpol-awsmarketplacesellerfullaccess) and [AWSMarketplaceSellerProductsFullAccess](#security-iam-awsmanpol-awsmarketplacesellerproductsfullaccess) – Update to existing policies | AWS Marketplace updated the policies so that the iam:PassedToService condition is only applied to iam:PassRole. | November 22, 2021 | 
| [AWSMarketplaceFullAccess](#security-iam-awsmanpol-awsmarketplacefullaccess) – Update to an existing policy | AWS Marketplace removed a duplicate `ec2:DescribeAccountAttributes` permission from `AWSMarketplaceFullAccess` policy. | July 20, 2021 | 
| AWS Marketplace started tracking changes | AWS Marketplace started tracking changes for its AWS managed policies. | April 20, 2021 | 