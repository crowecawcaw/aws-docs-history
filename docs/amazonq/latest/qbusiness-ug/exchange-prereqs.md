

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for connecting Amazon Q Business to Microsoft Exchange
<a name="exchange-prereqs"></a>

**In Microsoft Exchange, make sure you have:**
+ Created a Microsoft Exchange account in Office 365.
+ Copied your Microsoft 365 tenant ID. You can find your tenant ID in the **Properties** of your Azure Active Directory Portal or in the Microsoft Entra Admin portal. For more information, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id) on the Microsoft website.
+ Configured an OAuth 2.0 credential token containing a client ID and client secret.
+ Added the following permissions for the connector application:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-prereqs.html)

**In your AWS account, make sure you have:**
+ Created a Amazon Q Business application.
+ Created a [Amazon Q Business retriever and added an index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html).
+ Created an [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/iam-roles.html#iam-roles-ds) for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
+ Stored your Microsoft Exchange authentication credentials in an AWS Secrets Manager secret and, if using the Amazon Q API, noted the ARN of the secret.
**Note**  
If you’re a console user, you can create the IAM role and Secrets Manager secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [ Data source connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).