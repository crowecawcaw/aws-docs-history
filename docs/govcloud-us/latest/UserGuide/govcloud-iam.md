# AWS Identity and Access Management in AWS GovCloud (US)

AWS Identity and Access Management (IAM) is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.

## How IAM differs for AWS GovCloud (US)

- You must have an existing standard AWS account to create an AWS GovCloud (US) account. See [AWS GovCloud (US) Sign Up](getting-started-sign-up.md "getting-started-sign-up.md") to learn more. If you have AWS GovCloud (US) sign up issues, contact [AWS Customer Support](https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service&serviceCode=customer-account&categoryCode=aws-govcloud-us-onboarding/ "https://console.aws.amazon.com/support/home#/case/create?issueType=customer-service&serviceCode=customer-account&categoryCode=aws-govcloud-us-onboarding/").
- When your AWS GovCloud (US) account is created, you are provided initial access to the [AWS Management Console for AWS GovCloud (US)](https://signin.amazonaws-us-gov.com "https://signin.amazonaws-us-gov.com") by an `Administrator`
  IAM user or an `OrganizationAccountAccessRole`
  IAM role, depending on the method used.

You cannot access the AWS Management Console for AWS GovCloud (US) using the [associated standard AWS accountroot user credentials](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md").

- The AWS GovCloud (US) account root user is created at the same time the AWS GovCloud (US) account is created, but access to this user is not provided by default to AWS GovCloud (US) customers.
  - Sign in to the AWS Management Console for AWS GovCloud (US) as the AWS GovCloud (US) account root user is not supported.
  - AWS GovCloud (US) account root user access keys can be provided at the request of [associated standard AWS account](getting-started-standard-account-linking.md "getting-started-standard-account-linking.md") root user by contacting AWS Customer Support. See [Requesting root access keys for an AWS GovCloud (US) account](govcloud-account-root-user.md#requesting-root-user-keys "govcloud-account-root-user.md#requesting-root-user-keys") to get started.
  - Tasks that require the root user in AWS GovCloud (US) are limited. See [Tasks in AWS GovCloud (US) Regions that require root user access keys](govcloud-account-root-user.md#govcloud-tasks-require-root-user "govcloud-account-root-user.md#govcloud-tasks-require-root-user").
  - Since there is no access to the root user, there is no ability to centrally manage such credentials in AWS Organizations. However, you can perform privileged tasks for member accounts in your organization. To learn more about performing some root user tasks using short-term credentials, see [Perform a privileged task on an AWS Organizations member account](../../../IAM/latest/UserGuide/id_root-user-privileged-task.md "../../../IAM/latest/UserGuide/id_root-user-privileged-task.md").
  - Solution Providers reselling in AWS GovCloud (US) may receive AWS GovCloud (US) account root user access keys to be used for initial access to their account from an AWS business representative.
  - For more information, see [AWS GovCloud (US) account root user](govcloud-account-root-user.md "govcloud-account-root-user.md").

- Access issues for IAM users that are administrators in your AWS GovCloud (US) can be resolved by another administrator in the account.

If all administrators have forgotten or lost access to the AWS GovCloud (US) account, request AWS GovCloud (US) account root user access keys to [Restore IAM Administrator access to the AWS Management Console for AWS GovCloud (US)](govcloud-account-root-user.md#restore-root-user-keys "govcloud-account-root-user.md#restore-root-user-keys"). See [Requesting root access keys for an AWS GovCloud (US) account](govcloud-account-root-user.md#requesting-root-user-keys "govcloud-account-root-user.md#requesting-root-user-keys") to get started.

- There is one IAM control plane for all AWS GovCloud (US) Regions, which is located in the AWS GovCloud (US-West) Region. Each AWS Region has a completely independent instance of the IAM data plane. For more information, see [Resilience in AWS Identity and Access Management](../../../IAM/latest/UserGuide/disaster-recovery-resiliency.md "../../../IAM/latest/UserGuide/disaster-recovery-resiliency.md").
- In the AWS GovCloud (US) Regions, the IAM dual-stack public endpoint is `https://iam.us-gov.api.aws`.
  This endpoint supports clients using either IPv4 or IPv6 addresses.
  For more information, see [Dual-stack endpoint support](../../../IAM/latest/UserGuide/reference_dual-stack_endpoint_support.md "../../../IAM/latest/UserGuide/reference_dual-stack_endpoint_support.md") in the _IAM User Guide_.
- In the AWS GovCloud (US) Regions, there is no AWS STS global endpoint. AWS provides Regional AWS STS endpoints.
- When using the IAM or AWS STS service in AWS GovCloud (US), you must use [AWS GovCloud (US)IAM/AWS STS endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
  Use SSL (HTTPS) when you make calls to the IAM or AWS STS service in AWS GovCloud (US) Regions.
- IAM users that you create in AWS GovCloud (US) are specific to AWS GovCloud (US) and do not exist in other standard AWS Regions.
- AWS GovCloud (US) supports MFA devices listed in the [Multi-Factor Authentication (MFA) in AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/mfa/ "https://aws.amazon.com/govcloud-us/mfa/") page.
  - You can use these MFA devices with your AWS GovCloud (US) administrator user or any IAM user in your account.
  - You cannot use these MFA devices with your AWS GovCloud (US) account root user.

- You cannot create a role to delegate access between an AWS GovCloud (US) account and a standard AWS account.
- Customers with export-controlled data (e.g. export-controlled technical data) in their environment may consider using IAM roles as part of their export control compliance program. It is the customer’s responsibility to properly architect its AWS GovCloud (US) account if there will be export controlled data in its environment in order to comply with export control laws.
- When you create policies, use the AWS GovCloud (US) resource ARN prefix. For more information, see [Amazon Resource Names (ARNs) in GovCloud (US) Regions](using-govcloud-arns.md "using-govcloud-arns.md").
- When you use a SAML provider in AWS GovCloud (US) Regions, use the following URL for the XML document that contains relying party information and certificates: `https://signin.amazonaws-us-gov.com/static/saml-metadata.xml`.
  For more information, see [Configuring a Relying Party and Adding Claims](../../../IAM/latest/UserGuide/identity-providers-saml-configure-relying-party.md "../../../IAM/latest/UserGuide/identity-providers-saml-configure-relying-party.md") in _IAM User Guide_.
- In the AWS GovCloud (US) Regions, there is no AWS STS global endpoint. AWS provides Regional AWS STS endpoints.
- In the AWS GovCloud (US-West) Region, the AWS STS endpoint only supports request Signature Version 4 (SigV4) by default and can be updated to support both SigV4 and Signature Version 4A (SigV4A). Session tokens supporting the SigV4A algorithm are larger than those supporting SigV4 and match the size of tokens issued by the AWS STS endpoint in the AWS GovCloud (US-East) Region, which already supports SigV4A. Changing this setting might affect existing systems where you temporarily store tokens. For more information, see [Managing AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md").
  - Documentation that mentions **Valid only in AWS Regions enabled by default** refers to **Support only SigV4-based signatures on AWS requests** for the AWS STS endpoint in the AWS GovCloud (US-West) Region.
  - Documentation that mentions **All AWS Regions** refers to **Both the SigV4 and SigV4A algorithms** for the AWS STS endpoint in the AWS GovCloud (US-West) Region.

- IAM Access Analyzer policy generation is not supported in AWS GovCloud (US). To learn more, see [Using AWS Identity and Access Management Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") in the _IAM User Guide_.
- IAM Roles Anywhere is now supported in AWS GovCloud (US). To learn more, see [Providing access for non AWS workloads](../../../IAM/latest/UserGuide/id_roles_common-scenarios_non-aws.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_non-aws.md") in the _IAM User Guide_.
- When configuring SAML Applications for single sign on in AWS GovCloud (US), the SAML Audience and ACS links will be different than those used in the standard Regions.
  - Application ACS URL: https://signin.amazonaws-us-gov.com/saml
  - Application SAML audience: `urn:amazon:webservices:govcloud`

## Documentation for AWS Identity and Access Management

[AWSIAM documentation](https://aws.amazon.com/documentation/iam/ "https://aws.amazon.com/documentation/iam/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- IAM metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your IAM entities.
- Do not enter export-controlled data in the following fields:
  - Authentication codes, which are clear-text memcached
  - User names
  - Group names
  - Password policies
  - Policy names
  - Roles and role names
  - Policy documents
