# Prerequisites and

considerations

Before you set up trusted identity propagation, review the following prerequisites
and considerations.

###### Topics

- [Prerequisites](#trustedidentitypropagation-prerequisites "#trustedidentitypropagation-prerequisites")
- [Considerations](#trustedidentitypropagation-considerations "#trustedidentitypropagation-considerations")
- [Considerations for
  customer managed applications](#trustedidentitypropagation-customer-apps "#trustedidentitypropagation-customer-apps")

## Prerequisites

To use trusted identity propagation, ensure your environment meets the
following prerequisites:

- Enable and provision IAM Identity Center
  - To use trusted identity propagation, you must enable IAM Identity Center in
    the same AWS Region where the AWS applications and services
    your users will access are enabled. For information, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").
    - IAM Identity Center Organization instance is recommended - We
      recommend you use an [organization instance](organization-instances-identity-center.md "organization-instances-identity-center.md") of IAM Identity Center that you
      enable in the management account of AWS Organizations. You can
      [delegate administration](organization-instances-identity-center.md "organization-instances-identity-center.md") of an organization
      instance of IAM Identity Center to a member account. If you choose an
      [account instance](account-instances-identity-center.md "account-instances-identity-center.md") of IAM Identity Center, all
      AWS services that you want users to access with
      trusted identity propagation must reside in the same
      AWS account where you enable IAM Identity Center. For more
      information, see [Account instances of IAM Identity Center](account-instances-identity-center.md "account-instances-identity-center.md").

  - Connect your existing identity provider to IAM Identity Center and provision
    your users and groups into IAM Identity Center. For more information, see
    [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md").

- Connect the AWS managed applications and services in your trusted
  identity propagation use case to IAM Identity Center. To use trusted identity
  propagation, AWS managed applications must be connected to
  IAM Identity Center.

## Considerations

Keep in mind the following considerations when configuring and using trusted
identity propagation:

- **Organization vs account instance of IAM Identity Center**
  - An [organization instance](organization-instances-identity-center.md "organization-instances-identity-center.md") of IAM Identity Center will give you the
    most control and flexibility to grow your use cases to multiple
    AWS accounts, users, and AWS services. If you are unable to
    use an organization instance, your use case may be supported
    with account instances of IAM Identity Center. To learn more about which
    AWS services in your use case support account instances of
    IAM Identity Center, see [AWS managed applications
    that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md").

- **Multi-account permissions (permission sets) not
  required**
  - Trusted identity propagation doesn't require you to set up
    [multi-account
    permissions](manage-your-accounts.md "manage-your-accounts.md") (permission sets). You can enable IAM Identity Center
    and use it for trusted identity propagation only.

## Considerations for

customer managed applications

Your workforce can benefit from trusted identity propagation even if your
users interact with client-facing applications that are not managed by AWS,
for example Tableau or your custom-developed applications. The users of these
applications may not be provisioned in IAM Identity Center. To enable the smooth recognition
and authorization of user access to AWS resources, IAM Identity Center enables you to
configure a trusted relationship between the identity provider authenticating
your users and IAM Identity Center. For more information, see [Using applications with a
trusted token issuer](using-apps-with-trusted-token-issuer.md "using-apps-with-trusted-token-issuer.md").

In addition, configuring trusted identity propagation for your application
will require:

- Your application must use OAuth 2.0 framework for authentication.
  Trusted identity propagation does not support SAML 2.0
  integrations.
- Your application must be recognized by IAM Identity Center. Follow the guidance
  specific to your [use case](trustedidentitypropagation-integrations.md "trustedidentitypropagation-integrations.md").
