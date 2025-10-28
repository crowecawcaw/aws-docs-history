# Prerequisites for connecting Amazon Q Business to AEM (Server)

Before you begin, make sure that you have completed the following
prerequisites.

**In AEM, make sure you have:**

- Access to an account with administrative permissions, or an admin user.
- Copied your AEM host URL.
- Noted your basic authentication credentials of admin username and
  password.
- (Optional) Added the following OAuth scopes if you're using OAuth 2.0
  authentication:
  - **Profile** – Needed to get user
    and groups related data, like email ID and username.
  - **Replicate** – Needed to get data
    and metadata from Assets and Pages (not including user data).

- **Optional**: Generated OAuth 2.0 credentials in
  AEM On-Premise. If you use AEM On-Premise, the
  credentials include client ID, client secret, and private key. Adobe
  Granite OAuth 2.0 server implementation
  (com.adobe.granite.oauth.server) provides the support for
  OAuth 2.0 server functionalities in AEM.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your AEM (Server) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
