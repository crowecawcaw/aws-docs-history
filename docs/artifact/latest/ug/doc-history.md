

# Document history for AWS Artifact
<a name="doc-history"></a>

The following table provides a history of AWS Artifact releases and related changes to the AWS Artifact User Guide.

| Change | Description | Date | 
| --- |--- |--- |
| [Updated AWSArtifactComplianceInquiriesFullAccess managed policy](#doc-history) | Updated the [AWSArtifactComplianceInquiriesFullAccess](security-iam-awsmanpol.html#security-iam-awsmanpol-AWSArtifactComplianceInquiriesFullAccess) managed policy to include the `artifact:PutComplianceInquiryFeedback` permission. With this permission, you can submit feedback on compliance inquiry responses. | July 23, 2026 | 
| [Assurance Assistant](#doc-history) | Added [Assurance Assistant](managing-compliance-inquiries.html) documentation for generating AI-powered responses to compliance and due diligence questions. Launched [AWSArtifactComplianceInquiriesReadOnlyAccess and AWSArtifactComplianceInquiriesFullAccess AWS managed policies](security-iam-awsmanpol.html#security-iam-awsmanpol-updates) and added [example IAM policies](example-iam-policies.html#example-policy-compliance-inquiries) for compliance inquiry access. | June 30, 2026 | 
| [Updated permissions for ListReportVersions API](#doc-history) | Updated [example IAM policies](example-iam-policies.html), [example GovCloud IAM policies](example-govcloud-iam-policies.html), [AWSArtifactReportsReadOnlyAccess](security-iam-awsmanpol.html) managed policy, and [downloading a report](downloading-documents.html) instructions to include the `artifact:ListReportVersions` permission and support for downloading report versions to accommodate the new ListReportVersions API. | December 15, 2025 | 
| [Updated AWSArtifactAgreementsFullAccess managed policy](#doc-history) | Updated [AWSArtifactReportsReadOnlyAccess](security-iam-awsmanpol.html) managed policy to scope `organizations:EnableAWSServiceAccess` permissions down to AWS Artifact's service principal. This does not impact the managed policy's functionality. | October 16, 2025 | 
| [IAM Action Deprecation Notice Update](#doc-history) | Updated the IAM action deprecation notice for `artifact:DownloadAgreement` and `artifact:Get` in the AWS GovCloud (US) partition. | July 1, 2025 | 
| [Fine-grained permissions for AWS Artifact in AWS GovCloud (US) Regions](#doc-history) | Updated and expanded policies for using AWS Artifact in AWS GovCloud (US) Regions, while removing notes about limitations as AWS Artifact functionality is now more broadly applicable across all regions. | March 31, 2025 | 
| [Updated AWSArtifactReportsReadOnlyAccess managed policy](#doc-history) | Updated [AWSArtifactReportsReadOnlyAccess](security-iam-awsmanpol.html) managed policy to remove the artifact:get permission. | March 21, 2025 | 
| [Example policies for AWS Artifact in AWS GovCloud (US) Regions](#doc-history) | Added example policies for using AWS Artifact in AWS GovCloud (US) Regions, and noted which pages do not apply to using AWS Artifact in AWS GovCloud (US) Regions. | December 6, 2024 | 
| [Fine-grained permissions for agreement execution, AWSArtifactAgreementsFullAccess and AWSArtifactAgreementsReadOnlyAccess managed policies](#doc-history) | Enabled fine-grained access for AWS Artifact agreement execution and launched [AWSArtifactAgreementsFullAccess and AWSArtifactAgreementsReadOnlyAccess AWS managed policies](security-iam-awsmanpol.html#security-iam-awsmanpol-updates). | November 21, 2024 | 
| [Fine-grained report access and AWSArtifactReportReadOnlyAccess managed policy](#doc-history) | Enabled fine-grained access to AWS Artifact reports, enabled report [condition keys](using-condition-keys.html), and launched [AWSArtifactReportsReadOnlyAccess managed policy](security-iam-awsmanpol.html). | December 15, 2023 | 
| [AWS Artifact service-linked role](#doc-history) | Added service-linked role documentation and updated example policies for AWS Artifact and AWS Organizations integration. | September 26, 2023 | 
| [Notifications](#doc-history) | Published the documentation for managing notifications, and made relevant updates to the AWS Artifact API Reference, CloudTrail logging documentation, and the **Identity and access management** page. | August 1, 2023 | 
| [Third-party reports - Generally available](#doc-history) | Added API reference documentation and CloudTrail logging documentation, and made third-party reports generally available. | January 27, 2023 | 
| [Third-party reports (Preview)](#doc-history) | Launched compliance reports of the independent software vendors (ISVs) who sell their products on AWS Marketplace. Added example policies to **Identity and access management** page for third-party reports. | November 30, 2022 | 
| [Security](#doc-history) | Added section to **Identity and access management** page for confused deputy prevention. | December 20, 2021 | 
| [Reports](#doc-history) | Removed nondisclosure agreement and introduced terms and conditions for report downloads. | December 17, 2020 | 
| [Home page and search](#doc-history) | Added service home page and search bar on the reports and agreements page. | May 15, 2020 | 
| [AWS GovCloud (US) launch](#doc-history) | Launched AWS Artifact in AWS GovCloud (US) Regions. | November 7, 2019 | 
| [AWS Organizations agreements](#doc-history) | Added support for managing agreements for an organization. | June 20, 2018 | 
| [Agreements](#doc-history) | Added support for managing AWS Artifact agreements. | June 17, 2017 | 
| [Initial release](#doc-history) | This release introduces AWS Artifact. | November 30, 2016 | 