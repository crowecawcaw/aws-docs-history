

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Microsoft Teams to Amazon Q Business
<a name="teams-connector"></a>

You can connect Microsoft Teams to Amazon Q Business to index and search your team's messages, channel posts, and files. This connection enables your organization to find relevant information from Teams conversations and shared content through your Amazon Q web experience.

Use the AWS Management Console or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API to create the connection.

**Topics**
+ [Microsoft Teams connector versions](teams-versions.md)
+ [Known limitations for the Microsoft Teams connector](teams-limitations.md)
+ [Microsoft Teams connector overview](teams-overview.md)
+ [Prerequisites for connecting Amazon Q Business to Microsoft Teams](teams-prereqs.md)
+ [Connecting using the latest Microsoft Teams connector (Console)](teams-console-new.md)
+ [Connecting using the legacy Microsoft Teams connector (Console)](teams-console-original.md)
+ [Connecting Amazon Q Business to Microsoft Teams using APIs](teams-api.md)
+ [Connecting Amazon Q Business to Microsoft Teams using AWS CloudFormation](teams-cfn.md)
+ [How Amazon Q Business connector crawls Microsoft Teams ACLs](teams-user-management.md)
+ [Microsoft Teams data source connector field mappings](teams-field-mappings.md)
+ [IAM role for Microsoft Teams connector](teams-iam-role.md)
+ [Troubleshooting your Microsoft Teams connector](teams-troubleshooting.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).

**Note**  
ACL crawling is available for both new and original Microsoft Teams connector versions.

**Note**  
Field mappings are available for the original Microsoft Teams connector only. The new connector uses automatic field mapping.