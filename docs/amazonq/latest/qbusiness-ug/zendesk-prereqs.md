# Prerequisites for connecting Amazon Q Business to Zendesk

Before you begin, make sure that you have completed the following
prerequisites.

**In Zendesk, make sure you have:**

- Created a Zendesk Suite (Professional/Enterprise) administrative
  account.
- Copied your Zendesk host URL. For example,
  `https://{sub-domain}.zendesk.com/`. You need this URL to allow
  Amazon Q to connect with your Zendesk data source.
- Generated Zendesk OAuth 2.0 with implicit grant credentials containing an implicit
  grant token.
- Generated Zendesk OAuth 2.0 credentials containing a client ID, client
  secret, username, and password. You need these credentials to authenticate Amazon Q to access Zendesk.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Zendesk authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
