

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q to Confluence (Server/Data Center)
<a name="confluence-server-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In Confluence Server/Data Center, make sure you have:**
+ Copied your Confluence instance URL. For example: {{https://example.confluence.com}}. You need your Confluence instance URL to connect to Amazon Q.
+ Configured basic authentication credentials containing a username (username used to log into Confluence) and password (Confluence Server/Data Center password) to allow Amazon Q to connect to your Confluence Server/Data Center instance.
+ **Optional:** Configured OAuth 2.0 credentials containing a Confluence app key, Confluence app secret, Confluence access token, and Confluence refresh token to allow Amazon Q to connect to your Confluence instance. If your access token expires, you can either use the refresh token to regenerate your access token and refresh token pair, or you can repeat the authorization process. 
+ **Optional:** Configured a Personal Access Token (PAT) containing a Confluence token to allow Amazon Q to connect to your Confluence Server/Data Center instance. For information about how to create a PAT token, see [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) on the Atlassian website.

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ If you want to have Amazon Q automatically rotate your secret, ensure that your IAM role includes the `secretsmanager:PutSecretValue` and `secretsmanager:UpdateSecret` permissions. 
+ Stored your Confluence (Server/Data Center) authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).