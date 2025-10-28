After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Identity and access management in Amazon FinSpace

This section explains the identity management and authentication for Amazon FinSpace Managed
kdb and Dataset browser.

## Identity management for Managed kdb

Amazon FinSpace Managed kdb uses AWS Identity and Access Management (IAM) policies to restrict access to
operations.

Whenever you use IAM policies, ensure that you follow IAM best practices. For
more information, see [Security best
practices](../../../IAM/latest/UserGuide/IAMBestPracticesAndUseCases.md "../../../IAM/latest/UserGuide/IAMBestPracticesAndUseCases.md") in the _IAM User Guide_.

## Identity management for Dataset

browser

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Amazon FinSpace Dataset browser supports two methods for identity management and
authentication. A FinSpace dataset browser environment can be created with either of the
following methods.

1. **Email and password** – FinSpace access is
   controlled via users that are created and managed within the FinSpace application.
   With email and password based authentication method, users sign in to FinSpace using
   their email address and password. An environment created with email and password
   based authentication method cannot be changed to SSO based authentication method
   in the future. Learn more about [Managing user access with email and
   password](managing-user-email-pwd.md "managing-user-email-pwd.md").
2. **Single Sign-On (SSO)** – FinSpace access is
   controlled through your organization's identity provider (IdP). With this
   authentication method, users will be redirected to the SSO login page of their
   Security Assertion Markup Language 2.0 (SAML 2.0) compliant identity provider
   (IdP) solution to authenticate their access to FinSpace. An environment created with
   SSO based authentication method cannot be changed to email and password based
   authentication method in the future. Learn more about [creating and managing users with SAML based
   SSO](managing-user-sso.md "managing-user-sso.md").

######

Topics

- [Setting up SAML based single sign-on (SSO) with
  Amazon FinSpace](saml-sso.md "saml-sso.md")
- [Managing user access in Amazon FinSpace](managing-user-access.md "managing-user-access.md")
- [AWS managed policies for Amazon FinSpace](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Using service-linked roles for
  FinSpace](using-service-linked-roles.md "using-service-linked-roles.md")
