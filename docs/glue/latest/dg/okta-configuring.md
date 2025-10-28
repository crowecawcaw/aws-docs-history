# Configuring Okta

Before you can use AWS Glue to transfer data to or from Okta, you must meet these requirements:

## Minimum requirements

- You have a Okta account. For more information on creating an account, see
  [Okta New Account and Developer App creation steps](okta-create-account.md "okta-create-account.md").
- Your Okta account is enabled for API access.
- You have created a OAuth2 API integration in your Okta account. This integration provides the client
  credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account.
  For more information, refer Steps to Create a Client app and OAuth2.0 credentials: Okta New Account and Developer
  App Creation Steps
- You have a Okta account with a OktaApiToken. Refer to
  [Okta documentation](https://developer.okta.com/docs/guides/create-an-api-token/main/#create-the-token "https://developer.okta.com/docs/guides/create-an-api-token/main/#create-the-token") .

If you meet these requirements, you’re ready to connect AWS Glue to your Okta account. For typical connections, you don't
need do anything else in Okta.
