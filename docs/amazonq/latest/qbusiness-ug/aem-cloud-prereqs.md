

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q Business to AEM (Cloud)
<a name="aem-cloud-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In AEM, make sure you have:**
+ Access to an account with administrative permissions, or are an admin user.
+ Copied your AEM (Cloud) host URL.
+ Noted your basic authentication credentials of admin username and password.
+ (Optional) Added the following OAuth scopes if you're using OAuth 2.0 authentication:
  + **Profile** – Needed to get user and groups related data, like email ID and username.
  + **Replicate** – Needed to get data and metadata from Assets and Pages (not including user data).
+ **Optional**: Generated OAuth 2.0 credentials in AEM (Cloud) as an admin user. The credentials include client ID, client secret, private key, organization ID, technical account ID, and Adobe Identity Management System (IMS) host. For more information about how to generate these credentials for AEM (Cloud), see [AEM (Cloud) documentation](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your AEM (Cloud) authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).