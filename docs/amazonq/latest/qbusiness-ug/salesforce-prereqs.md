# Prerequisites for connecting Amazon Q Business to Salesforce Online

Before you begin, make sure that you have completed the following
prerequisites.

**In Salesforce, make sure you have:**

- Copied the Salesforce security token associated with the account that's
  used to connect to Salesforce.
- Created a Salesforce Connected App account with OAuth activated and
  have copied the consumer key (client ID) and consumer secret (client secret) assigned to
  your Salesforce Connected App. For more information, see [Salesforce documentation on Connected Apps](https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm&type=5") on the
  Salesforce website.
- Copied the URL of the Salesforce instance that you want to index.
  Typically, this is `https://<company>.salesforce.com/`. The
  server must be running a Salesforce connected app.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Salesforce Online authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
