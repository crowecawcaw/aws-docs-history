

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q Business to Microsoft Teams
<a name="teams-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In Microsoft Teams, make sure you have:**
+ Created a Microsoft Teams account in Office 365.
+ Copied your Microsoft 365 Tenant ID. You can find your Tenant ID in the Properties of your Azure Active Directory Portal. You need this URL to allow Amazon Q to connect with your Microsoft Teams data source. For more information, see [Register a Microsoft Entra app and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#sign-in-to-the-application) on the Microsoft website.
+ Configured an OAuth 2.0 credential token containing a client ID and client secret. For more information, see [Azure documentation on managing access tokens for Teams](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/manage-teams-identity?pivots=programming-language-csharp) on the Microsoft website.
+ Added the necessary permissions. You can choose to add all permissions, or you can limit the scope by selecting fewer permissions based on which entities you want to crawl. *(Application level permissions required for new connector)* All permissions must be at *application* level, not delegated. The following table shows permissions by corresponding entity.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-prereqs.html)
+ Generated Microsoft Teams OAuth 2.0 credentials containing a client ID, client secret, username, and password. You need these credentials to authenticate Amazon Q to access Microsoft Teams.

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your Microsoft Teams authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).