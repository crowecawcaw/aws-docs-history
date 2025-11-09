# AWS managed policies for AWS Data Exchange

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

###### Topics

- [AWS managed policy:
  AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess")
- [AWS managed
  policy: AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess")
- [AWS managed policy:
  AWSDataExchangeReadOnly](#security-iam-awsmanpol-awsdataexchangereadonly "#security-iam-awsmanpol-awsdataexchangereadonly")
- [AWS managed policy:
  AWSDataExchangeServiceRolePolicyForLicenseManagement](#security-iam-awsmanpol-awsdataexchangeservicerolepolicyforlicensemanagement "#security-iam-awsmanpol-awsdataexchangeservicerolepolicyforlicensemanagement")
- [AWS managed policy:
  AWSDataExchangeServiceRolePolicyForOrganizationDiscovery](#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery "#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery")
- [AWS
  managed policy: AWSDataExchangeSubscriberFullAccess](#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess "#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess")
- [AWS
  managed policy: AWSDataExchangeDataGrantOwnerFullAccess](#security-iam-awsmanpol-awsdataexchangedatagrantownerfullaccess "#security-iam-awsmanpol-awsdataexchangedatagrantownerfullaccess")
- [AWS managed policy:
  AWSDataExchangeDataGrantReceiverFullAccess](#security-iam-awsmanpol-awsdataexchangedatagrantreceiverfullaccess "#security-iam-awsmanpol-awsdataexchangedatagrantreceiverfullaccess")
- [AWS Data Exchange updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy:

AWSDataExchangeFullAccess

You can attach the `AWSDataExchangeFullAccess` policy to your IAM
identities.

This policy grants administrative permissions that allow full access to AWS Data Exchange and
AWS Marketplace actions using the AWS Management Console and SDK. It also provides select access to Amazon S3 and
AWS Key Management Service as needed to take full advantage of AWS Data Exchange.

To view permissions for this policy, see
[AWSDataExchangeFullAccess](../../../aws-managed-policy/latest/reference/AWSDataExchangeFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeFullAccess.md")
in the _AWS Managed Policy Reference_.

## AWS managed

policy: AWSDataExchangeProviderFullAccess

You can attach the `AWSDataExchangeProviderFullAccess` policy to your IAM
identities.

This policy grants contributor permissions that provide data provider access to AWS Data Exchange
and AWS Marketplace actions using the AWS Management Console and SDK. It also provides select access to Amazon S3
and AWS Key Management Service as needed to take full advantage of AWS Data Exchange.

To view permissions for this policy, see
[AWSDataExchangeProviderFullAccess](../../../aws-managed-policy/latest/reference/AWSDataExchangeProviderFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeProviderFullAccess.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSDataExchangeReadOnly

You can attach the `AWSDataExchangeReadOnly` policy to your IAM
identities.

This policy grants read-only permissions that allow read-only access to AWS Data Exchange and
AWS Marketplace actions using the AWS Management Console and SDK.

To view permissions for this policy, see
[AWSDataExchangeReadOnly](../../../aws-managed-policy/latest/reference/AWSDataExchangeReadOnly.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeReadOnly.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSDataExchangeServiceRolePolicyForLicenseManagement

You can't attach the `AWSDataExchangeServiceRolePolicyForLicenseManagement`
to your IAM entities. This policy is attached to a service-linked role that allows
AWS Data Exchange to perform actions on your behalf. It grants role permissions that allow
AWS Data Exchange to retrieve information about your AWS organization and manage AWS Data Exchange
data grants licenses. For more information, see [Service-linked role for
AWS Data Exchange license management](using-service-linked-roles-license-management.md "using-service-linked-roles-license-management.md") later in this section.

To view permissions for this policy, see
[AWSDataExchangeServiceRolePolicyForLicenseManagement](../../../aws-managed-policy/latest/reference/AWSDataExchangeServiceRolePolicyForLicenseManagement.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeServiceRolePolicyForLicenseManagement.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSDataExchangeServiceRolePolicyForOrganizationDiscovery

You can't attach the
`AWSDataExchangeServiceRolePolicyForOrganizationDiscovery` to your IAM
entities. This policy is attached to a service-linked role that allows AWS Data Exchange to
perform actions on your behalf. It grants role permissions that allow AWS Data Exchange to
retrieve information about your AWS organization to determine eligibility for
AWS Data Exchange data grants license distribution. For more information, see [Service-linked roles for AWS
Organization discovery in AWS Data Exchange](using-service-linked-roles-aws-org-discovery.md "using-service-linked-roles-aws-org-discovery.md").

To view permissions for this policy, see
[AWSDataExchangeServiceRolePolicyForOrganizationDiscovery](../../../aws-managed-policy/latest/reference/AWSDataExchangeServiceRolePolicyForOrganizationDiscovery.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeServiceRolePolicyForOrganizationDiscovery.md")
in the _AWS Managed Policy Reference_.

## AWS

managed policy: AWSDataExchangeSubscriberFullAccess

You can attach the `AWSDataExchangeSubscriberFullAccess` policy to your
IAM identities.

This policy grants contributor permissions that allow data subscriber access to AWS Data Exchange
and AWS Marketplace actions using the AWS Management Console and SDK. It also provides select access to Amazon S3
and AWS Key Management Service as needed to take full advantage of AWS Data Exchange.

To view permissions for this policy, see
[AWSDataExchangeSubscriberFullAccess](../../../aws-managed-policy/latest/reference/AWSDataExchangeSubscriberFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeSubscriberFullAccess.md")
in the _AWS Managed Policy Reference_.

## AWS

managed policy: AWSDataExchangeDataGrantOwnerFullAccess

You can attach the `AWSDataExchangeDataGrantOwnerFullAccess` policy to your
IAM identities.

This policy gives a Data Grant owner access to AWS Data Exchange actions using the AWS Management Console and
SDKs.

To view permissions for this policy, see
[AWSDataExchangeDataGrantOwnerFullAccess](../../../aws-managed-policy/latest/reference/AWSDataExchangeDataGrantOwnerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeDataGrantOwnerFullAccess.md")
in the _AWS Managed Policy Reference_.

## AWS managed policy:

AWSDataExchangeDataGrantReceiverFullAccess

You can attach the `AWSDataExchangeDataGrantReceiverFullAccess` policy to
your IAM identities.

This policy gives a Data Grant receiver access to AWS Data Exchange actions using the AWS Management Console
and SDKs.

To view permissions for this policy, see
[AWSDataExchangeDataGrantReceiverFullAccess](../../../aws-managed-policy/latest/reference/AWSDataExchangeDataGrantReceiverFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDataExchangeDataGrantReceiverFullAccess.md")
in the _AWS Managed Policy Reference_.

## AWS Data Exchange updates to AWS managed

policies

The following table provides details about updates to AWS managed policies for
AWS Data Exchange since this service began tracking these changes. For automatic alerts about
changes to this page (and any other changes to this user guide), subscribe to the RSS
feed on the [Document history for AWS Data Exchange](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Date               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSDataExchangeDataGrantOwnerFullAccess](#security-iam-awsmanpol-awsdataexchangedatagrantownerfullaccess "#security-iam-awsmanpol-awsdataexchangedatagrantownerfullaccess") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                       | AWS Data Exchange added a new policy to grant Data Grant owners access to<br>AWS Data Exchange actions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | October 24, 2024   |
| [AWSDataExchangeDataGrantReceiverFullAccess](#security-iam-awsmanpol-awsdataexchangedatagrantreceiverfullaccess "#security-iam-awsmanpol-awsdataexchangedatagrantreceiverfullaccess") – New<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                              | AWS Data Exchange added a new policy to grant Data Grant receivers access<br>to AWS Data Exchange actions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | October 24, 2024   |
| [AWSDataExchangeReadOnly](#security-iam-awsmanpol-awsdataexchangereadonly "#security-iam-awsmanpol-awsdataexchangereadonly") – Update to an existing<br>policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Added necessary permissions to the<br>`AWSDataExchangeReadOnly` AWS managed policy for<br>the new data grants feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | October 24, 2024   |
| [AWSDataExchangeServiceRolePolicyForLicenseManagement](#security-iam-awsmanpol-awsdataexchangeservicerolepolicyforlicensemanagement "#security-iam-awsmanpol-awsdataexchangeservicerolepolicyforlicensemanagement")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                | Added a new policy to support service-linked roles to manage<br>license grants in customer accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | October 17, 2024   |
| [AWSDataExchangeServiceRolePolicyForOrganizationDiscovery](#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery "#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                    | Added a new policy to support service-linked roles to provide read<br>access to account information in your AWS Organization.                                                                                                                                                                                                                                                                                                                                                                                                                                              | October 17, 2024   |
| [AWSDataExchangeReadOnly](#security-iam-awsmanpol-awsdataexchangereadonly "#security-iam-awsmanpol-awsdataexchangereadonly")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Added statement IDs to make the policy easier to read, expanded the<br>wild carded permissions to the full list of read only ADX permissions,<br>and added new actions: `aws-marketplace:ListTagsForResource`<br>and `aws-marketplace:ListPrivateListings`.                                                                                                                                                                                                                                                                                                                | July 9, 2024       |
| [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Removed action:<br>`aws-marketplace:GetPrivateListing`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | May 22, 2024       |
| [AWSDataExchangeSubscriberFullAccess](#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess "#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Added statement IDs to make the policy easier to read and added new<br>action: `aws-marketplace:ListPrivateListings`.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | April 30, 2024     |
| [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Added statement IDs to make the policy easier to read and added new<br>actions: `aws-marketplace:TagResource`,<br>`aws-marketplace:UntagResource`,<br>`aws-marketplace:ListTagsForResource`,<br>`aws-marketplace:ListPrivateListings`,<br>`aws-marketplace:GetPrivateListing`, and<br>`aws-marketplace:DescribeAgreement`.                                                                                                                                                                                                                                                 | April 30, 2024     |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Added statement IDs to make the policy easier to read.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | August 9, 2024     |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess")                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Added `dataexchange:SendDataSetNotification`, a new<br>permission to send data set notifications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | March 5, 2024      |
| [AWSDataExchangeSubscriberFullAccess](#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess "#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess"), [AWSDataExchangeReadOnly](#security-iam-awsmanpol-awsdataexchangereadonly "#security-iam-awsmanpol-awsdataexchangereadonly"),[AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess"), and [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess") – Update to existing<br>policies | Added granular actions across all managed policies. New actions<br>added are `aws-marketplace:CreateAgreementRequest`,<br>`aws-marketplace:AcceptAgreementRequest`,<br>`aws-marketplace:ListEntitlementDetails`,<br>`aws-marketplace:ListPrivateListings`,<br>`aws-marketplace:GetPrivateListing`,<br>`license-manager:ListReceivedGrants`<br>`aws-marketplace:TagResource`,<br>`aws-marketplace:UntagResource`,<br>`aws-marketplace:ListTagsForResource`,<br>`aws-marketplace:DescribeAgreement`,<br>`aws-marketplace:GetAgreementTerms`<br>`aws-marketplace:GetLicense`. | July 31, 2023      |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess") – Update to<br>existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                          | Added `dataexchange:RevokeRevision`, a new permission<br>to revoke a revision.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | March 15, 2022     |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess") and [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess") – Update to existing<br>policies                                                                                                                                                                                                                                                                                                 | Added `apigateway:GET`, a new permission to retrieve an<br>API asset from Amazon API Gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | December 3, 2021   |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess") and [AWSDataExchangeSubscriberFullAccess](#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess "#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess") – Update to<br>existing policies                                                                                                                                                                                                                                                                   | Added `dataexchange:SendApiAsset`, a new permission to<br>send a request to an API asset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | November 29, 2021  |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess") and [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess") – Update to existing<br>policies                                                                                                                                                                                                                                                                                                 | Added `redshift:AuthorizeDataShare`,<br>`redshift:DescribeDataSharesForProducer`, and`redshift:DescribeDataShares`, new permissions to authorize<br>access to and create Amazon Redshift data sets.                                                                                                                                                                                                                                                                                                                                                                        | November 1, 2021   |
| [AWSDataExchangeSubscriberFullAccess](#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess "#security-iam-awsmanpol-awsdataexchangesubscriberfullaccess") – Update to<br>an existing policy                                                                                                                                                                                                                                                                                                                                                                                                                                 | Added `dataexchange:CreateEventAction`,<br>`dataexchange:UpdateEventAction`, and<br>`dataexchange:DeleteEventAction`, new permissions to<br>control access to automatically export new revisions of data<br>sets.                                                                                                                                                                                                                                                                                                                                                          | September 30, 2021 |
| [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess") and [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess") – Update to existing<br>policies                                                                                                                                                                                                                                                                                                 | Added `dataexchange:PublishDataSet`, a new permission<br>to control access to publishing new versions of data sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | May 25, 2021       |
| [AWSDataExchangeReadOnly](#security-iam-awsmanpol-awsdataexchangereadonly "#security-iam-awsmanpol-awsdataexchangereadonly"), [AWSDataExchangeProviderFullAccess](#security-iam-awsmanpol-awsdataexchangeproviderfullaccess "#security-iam-awsmanpol-awsdataexchangeproviderfullaccess"), and [AWSDataExchangeFullAccess](#security-iam-awsmanpol-awsdataexchangefullaccess "#security-iam-awsmanpol-awsdataexchangefullaccess") – Update to existing<br>policies                                                                                                                                                                  | Added `aws-marketplace:SearchAgreements` and<br>`aws-marketplace:GetAgreementTerms` to enable viewing<br>subscriptions for products and offers.                                                                                                                                                                                                                                                                                                                                                                                                                            | May 12, 2021       |
| AWS Data Exchange started tracking changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | AWS Data Exchange started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | April 20, 2021     |
