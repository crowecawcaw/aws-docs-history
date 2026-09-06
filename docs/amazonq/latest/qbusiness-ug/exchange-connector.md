

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Microsoft Exchange to Amazon Q Business
<a name="exchange-connector"></a>

You can connect your Microsoft Exchange enterprise messaging system to Amazon Q Business to unlock valuable organizational knowledge. This connection allows your users to search emails, calendar events, and shared content directly through the Amazon Q web experience.

You can connect your Microsoft Exchange instance to Amazon Q Business using the AWS Management Console or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API. This enables faster information discovery and improved decision-making across your organization.

**Topics**
+ [Microsoft Exchange connector versions](exchange-versions.md)
+ [Known limitations for the Microsoft Exchange connector](exchange-limitations.md)
+ [Microsoft Exchange connector overview](exchange-overview.md)
+ [Prerequisites for connecting Amazon Q Business to Microsoft Exchange](exchange-prereqs.md)
+ [Connecting using the Latest Microsoft Exchange Connector (Console)](exchange-console-new.md)
+ [Connecting using the Legacy Microsoft Exchange Connector (Console)](exchange-console-original.md)
+ [Connecting Amazon Q Business to Microsoft Exchange using APIs](exchange-api.md)
+ [Connecting Amazon Q Business to Microsoft Exchange (New connector) using APIs](exchange-new-api.md)
+ [How Amazon Q Business connector crawls Exchange ACLs](exchange-user-management.md)
+ [Microsoft Exchange data source connector field mappings](exchange-field-mappings.md)
+ [IAM role for Microsoft Exchange connector](exchange-iam-role.md)
+ [Understand error codes in the Microsoft Exchange connector](exchange-error-codes.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).

**Note**  
ACL crawling is available for both new and original Microsoft Exchange connector versions.

**Note**  
Field mappings are available for the original Microsoft Exchange connector only. The new connector uses automatic field mapping.