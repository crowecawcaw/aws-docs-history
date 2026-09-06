

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Gmail to Amazon Q Business
<a name="gmail-connector"></a>

With Amazon Q Business, you can connect your Gmail enterprise email system to unlock valuable organizational knowledge stored in email communications. When you connect Gmail to Amazon Q Business, your users can search and get answers from email content and conversations directly through the Amazon Q web experience.

You can connect your Gmail instance to Amazon Q Business using either the AWS Management Console or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API. This connection enables your organization to leverage email-based knowledge for improved decision-making and faster information discovery.

**Topics**
+ [Gmail connector versions](gmail-versions.md)
+ [Gmail connector overview](gmail-overview.md)
+ [Prerequisites for connecting Amazon Q Business to Gmail](gmail-prereqs.md)
+ [Connecting Amazon Q Business to Gmail using the latest connector (Console)](gmail-console-new.md)
+ [Connecting Amazon Q Business to Gmail using the legacy connector (Console)](gmail-console-original.md)
+ [Connecting Amazon Q Business to Gmail using the new connector (API)](gmail-new-api.md)
+ [Connecting Amazon Q Business to Gmail using the original connector (API)](gmail-original-api.md)
+ [How Amazon Q Business connector crawls Gmail ACLs](gmail-user-management.md)
+ [Gmail data source connector field mappings](gmail-field-mappings.md)
+ [IAM role for Amazon Q Business Gmail connector](gmail-iam-role.md)
+ [Understand error codes in the Amazon Q Business Gmail connector](gmail-error-codes.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).

**Note**  
**ACL behavior by connector version:**  
**New connector:** ACL and identity crawling is automatically enabled and cannot be disabled. No manual configuration is required.
**Original connector:** ACL and identity crawling can be manually configured during setup.

**Note**  
**Original connector only:** Field mappings are only available when using the original Gmail connector. The new connector uses optimized default field mappings that cannot be customized.