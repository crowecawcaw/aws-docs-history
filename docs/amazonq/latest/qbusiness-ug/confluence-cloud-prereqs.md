# Prerequisites for connecting Amazon Q Business to Confluence (Cloud)

Before you begin, make sure that you have completed the following
prerequisites.

**In Confluence Cloud, make sure you
have:**

- Copied your Confluence instance URL. For example:
  `https://example.atlassian.net`. You need your
  Confluence instance URL to connect to Amazon Q.
- Configured basic authentication credentials containing a username (email ID
  used to log into Confluence) and password
  (Confluence API token) to allow Amazon Q to
  connect to your Confluence instance. For information about how to
  create a Confluence API token, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token") on the
  Atlassian website.
- **Optional:** Configured OAuth 2.0 credentials
  containing a Confluence app key, Confluence app
  secret, Confluence access token, and Confluence
  refresh token to allow Amazon Q to connect to your
  Confluence instance. If your access token expires, you can
  either use the refresh token to regenerate your access token and refresh token
  pair, or you can repeat the authorization process. For more information about
  access tokens, see [Manage OAuth access tokens](https://support.atlassian.com/confluence-cloud/docs/manage-oauth-access-tokens/ "https://support.atlassian.com/confluence-cloud/docs/manage-oauth-access-tokens/") on the Atlassian
  website.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- If you want to have Amazon Q automatically rotate your secret,
  ensure that your IAM role includes the
  `secretsmanager:PutSecretValue` and
  `secretsmanager:UpdateSecret` permissions.
- Stored your Confluence (Cloud) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

###### Note

For more information on connecting Confluence (Cloud) to Amazon Q Business,
see [Index your Atlassian Confluence Cloud contents using the Amazon Q
Confluence Cloud connector for Amazon Q Business](https://aws.amazon.com/blogs/machine-learning/index-your-atlassian-confluence-cloud-contents-using-the-amazon-q-confluence-cloud-connector-for-amazon-q-business/ "https://aws.amazon.com/blogs/machine-learning/index-your-atlassian-confluence-cloud-contents-using-the-amazon-q-confluence-cloud-connector-for-amazon-q-business/") in the
_AWS Machine Learning Blog_.
