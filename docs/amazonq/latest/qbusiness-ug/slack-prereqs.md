# Prerequisites for connecting Amazon Q Business to Slack

Before you begin, make sure that you have completed the following
prerequisites.

**In Slack, make sure you have:**

- Created a Slack Bot User OAuth token or Slack User
  OAuth token. You can choose either token to connect Amazon Q to your
  Slack data source. See [Slack documentation
  on access tokens](https://api.slack.com/authentication/token-types "https://api.slack.com/authentication/token-types") for more information.

###### Note

If you use the bot token as part of your Slack credentials,
you cannot index direct messages and group messages. You must add the bot
token to the channel you want to index.

- Noted your Slack workspace team ID from your Slack
  workspace main page URL. For example,
  `https://app.slack.com/client/T0123456789/...`
  where `T0123456789` is the team ID.
- Added the required OAuth scopes/ read permissions. See [Setting up Slack](slack-credentials.md "slack-credentials.md") for more
  details.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Slack authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

###### Note

For more information on connecting Slack to Amazon Q Business,
see [Unlock the knowledge in your Slack workspace with Slack connector for Amazon Q
Business](https://aws.amazon.com/blogs/machine-learning/unlock-the-knowledge-in-your-slack-workspace-with-slack-connector-for-amazon-q-business/ "https://aws.amazon.com/blogs/machine-learning/unlock-the-knowledge-in-your-slack-workspace-with-slack-connector-for-amazon-q-business/") in the _AWS Machine Learning Blog_.
