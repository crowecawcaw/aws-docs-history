# Configuring Docusign Monitor

Before you can use AWS Glue to transfer data from Docusign Monitor to supported destinations, you must meet these requirements:

## Minimum requirements

The following are minimum requirements:

- You have an Docusign account where you use the Docusign Software product in Docusign Monitor.
- In the developer console for your Docusign account, you've created an OAuth 2.0 integration app for AWS Glue.

This app provides the client credentials that AWS Glue uses to access your data securely when it makes authenticated calls to your account. For more information, see [OAuth 2.0](https://developers.docusign.com/platform/webhooks/connect/validation-and-security/oauth-connect/ "https://developers.docusign.com/platform/webhooks/connect/validation-and-security/oauth-connect/") in the Docusign Monitor documentation.

If you meet these requirements, you’re ready to connect AWS Glue to your Docusign Monitor account.
