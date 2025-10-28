# Prerequisites for connecting Amazon Q Business to Alfresco (Cloud)

Before you begin, make sure that you have completed the following
prerequisites.

## Troubleshooting prerequisites

- /group-members Endpoint Issues: If you experience problems with the /group-members API, upgrade to Alfresco version 7.0 or higher.
- Solr-Related Errors (On-Premises Only): Ensure Solr is properly configured and running. Misconfiguration may result in HTTP 500 errors or failed synchronizations.

**In Alfresco, make sure you
have:**

- Copied your Alfresco repository URL and web application URL. If
  you only want to index a specific Alfresco site, then also copy
  the site ID.
- Noted your Alfresco authentication credentials, which include a
  username and password with at least read permissions. If you want to use OAuth
  2.0 authentication, you should add the user to the Alfresco
  administrators group.
- **Optional**: Generated OAuth 2.0 credentials in
  Alfresco. The credentials include client ID, client secret,
  and token URL. For more information about how to configure clients for
  Alfresco On-Premises, see [Alfresco documentation](https://docs.alfresco.com/identity-service/latest/tutorial/sso/saml/ "https://docs.alfresco.com/identity-service/latest/tutorial/sso/saml/"). If you use Alfresco Cloud
  (PaaS), you must contact [Hyland
  support](https://community.hyland.com/ "https://community.hyland.com/") for Alfresco OAuth 2.0 authentication.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Alfresco (Cloud) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console. Only Alfresco version 7.0 or higher is supported.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
