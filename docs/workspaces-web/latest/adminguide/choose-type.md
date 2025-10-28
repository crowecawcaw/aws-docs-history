# Choosing the identity provider type for Amazon WorkSpaces Secure Browser

WorkSpaces Secure Browser offers two authentication types: **Standard** and
**AWS IAM Identity Center**. You choose the authentication type to use with your portal on
the **Configure identity provider page**.

- For **Standard** (default option), federate your 3rd party SAML 2.0
  identity provider (such as Okta or Ping) directly with your portal. For more information, see
  [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md "configure-standard.md"). The standard type supports both SP-initiated and
  IdP-initiated authentication flows.
- For **IAM Identity Center** (advanced option), federate the IAM Identity Center with your portal.
  To use this authentication type, your IAM Identity Center and WorkSpaces Secure Browser portal must both reside in the same
  AWS Region. For more information, see [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md "configure-iam.md").

###### Topics

- [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md "configure-standard.md")
- [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md "configure-iam.md")
