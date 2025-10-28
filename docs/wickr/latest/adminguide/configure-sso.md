This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Configure SSO in AWS Wickr

To ensure secure access to your Wickr network, you can set up your current
single sign-on configuration. Detailed guides are available to assist you with this
process.

###### Important

- When you configure SSO, you specify a company ID for your Wickr
  network. Be sure to record this company ID. You must provide it to your
  end users when sending invitation emails. End users must specify the
  company ID when they register for your Wickr network.
- In September 2025, AWS Wickr introduced an improved, more secure SSO
  connection system. To take advantage of these security enhancements,
  organizations using SSO must migrate to a new redirect URI by March 09,

2026. For migration instructions, see the following AWS re:Post article:
      [Migrating to the New SSO Redirect URI for
      AWS Wickr](https://repost.aws/articles/ARwG2sEMHkShKNn77mc8pc8Q/migrating-to-the-new-sso-redirect-uri-for-aws-wickr "https://repost.aws/articles/ARwG2sEMHkShKNn77mc8pc8Q/migrating-to-the-new-sso-redirect-uri-for-aws-wickr").
      For more information about configuring SSO, see the following guides:

- [AWS Wickr Single
  Sign-on (SSO) setup with Microsoft Entra (Azure AD)](entra-ad-sso.md "entra-ad-sso.md")
- [AWS Wickr Single Sign-on (SSO) setup with Okta](https://repost.aws/articles/ARqcPJ8MctR02Om4APlBEANw/aws-wickr-single-sign-on-sso-setup-with-okta "https://repost.aws/articles/ARqcPJ8MctR02Om4APlBEANw/aws-wickr-single-sign-on-sso-setup-with-okta")
- [AWS Wickr Single Sign-on (SSO) setup with Amazon Cognito](https://repost.aws/articles/ARIOjROyJDTfutje_DJW9wWg/aws-wickr-single-sign-on-sso-setup-with-amazon-cognito "https://repost.aws/articles/ARIOjROyJDTfutje_DJW9wWg/aws-wickr-single-sign-on-sso-setup-with-amazon-cognito")
