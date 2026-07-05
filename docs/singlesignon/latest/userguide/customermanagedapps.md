# Customer managed applications

IAM Identity Center acts as a central identity service to your workforce users and groups. If you
already use an identity provider (IdP), IAM Identity Center can integrate with your IdP so that you
can provision your users and groups into IAM Identity Center and use your IdP for authentication. With
a single connection, IAM Identity Center represents your IdP in front of multiple AWS services and
enables your OAuth 2.0 applications to request access to data in these services on
behalf of your users. You can also use IAM Identity Center to assign your users access to [SAML 2.0](https://wiki.oasis-open.org/security "https://wiki.oasis-open.org/security")
applications. This includes AWS services such as Connect Customer and AWS Client VPN, which integrate with IAM Identity Center
exclusively using SAML and are therefore categorized as customer managed applications.

- If your application supports **JSON Web Tokens (JWTs)**, you
  can use the trusted identity propagation feature of IAM Identity Center to enable your
  application to request access to data in AWS services on behalf of your users.
  Trusted identity propagation is built on the OAuth 2.0 Authorization Framework
  and includes an option for applications to exchange identity tokens that come
  from an external OAuth 2.0 authorization server for tokens issued by IAM Identity Center and
  recognized by AWS services. For more information, see [Trusted identity propagation use cases](trustedidentitypropagation-integrations.md "trustedidentitypropagation-integrations.md").
- If your application supports **SAML 2.0**, you can connect it
  to an [organization instance of
  IAM Identity Center](identity-center-instances.md "identity-center-instances.md"). You can use IAM Identity Center to assign access to your SAML 2.0
  application.

###### Note

When integrating customer managed applications with an IAM Identity Center instance that uses a
[customer managed KMS key](encryption-at-rest.md "encryption-at-rest.md"), verify whether the application invokes IAM Identity Center service APIs.
If it does, see the [baseline KMS key policy](baseline-KMS-key-policy.md "baseline-KMS-key-policy.md") for the required permissions.

###### Topics

- [Single sign-on access to SAML 2.0 and OAuth 2.0 applications](customermanagedapps-saml2-oauth2.md "customermanagedapps-saml2-oauth2.md")
- [Setting up customer managed SAML 2.0 applications](customermanagedapps-saml2-setup.md "customermanagedapps-saml2-setup.md")
- [Enable AWS account access for customer managed applications](enable-account-access-customer-managed-apps.md "enable-account-access-customer-managed-apps.md")
