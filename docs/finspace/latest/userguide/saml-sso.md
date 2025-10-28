After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Setting up SAML based single sign-on (SSO) with

Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

When you use SAML based SSO, you can manage users with your enterprise identity
provider (IdP). You can use a third-party identity provider that supports through
Security Assertion Markup Language 2.0 (SAML 2.0) to provide a simple on-boarding flow
for your Amazon FinSpace users. Such identity providers include Microsoft Windows Active
Directory Federation Services and Okta among others.

With SSO, your users get one-click access to their FinSpace applications using their
existing identity credentials. You also have the security benefit of identity
authentication by your identity provider. You can control which users have access to
FinSpace using your existing identity provider.

######

Topics

- [Tutorial: Setup an Identity Provider with your
  Amazon FinSpace environment](setup-idp-finspace.md "setup-idp-finspace.md")
- [Tutorial: Creating an Amazon FinSpace environment
  with Okta SSO](tutorial-idp-okta-sso.md "tutorial-idp-okta-sso.md")
- [Tutorial: Creating an Amazon FinSpace environment
  with IAM Identity Center](tutorial-idp-aws-sso.md "tutorial-idp-aws-sso.md")
- [Tutorial: Creating an Amazon FinSpace environment
  with AD FS](tutorial-idp-ADFS-sso.md "tutorial-idp-ADFS-sso.md")
