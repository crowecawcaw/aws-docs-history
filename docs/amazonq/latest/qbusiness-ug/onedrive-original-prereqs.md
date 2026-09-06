

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites
<a name="onedrive-original-prereqs"></a>

Before you begin, make sure that you have completed the following prerequisites.

**In your Azure Active Directory (AD) application, make sure you have:**
+ Created an Azure Active Directory (AD) application.
+ Used the AD application ID to register a secret key for the application on the AD site. The secret key must contain the client ID and a client secret.
+ Copied the AD domain of the organization.
+ Added the following Application API permissions to your AD application on the Microsoft Graph option:
  + Read files in all site collections (`Files.Read.All`)
  + Read all users' full profiles (`User.Read.All`)
  + Read all groups (`Group.Read.All`)
**Note**  
Choose the Application permissions type instead of Delegated permissions while adding the API permissions.

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your Microsoft OneDrive authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).