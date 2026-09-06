

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting MySQL to Amazon Q Business
<a name="my-sql-connector"></a>

**Note**  
MySQL connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-connector.html), designed to support a broader range of enterprise use cases with enhanced flexibility.

MySQL is an open source relational database management system. You can connect your MySQL instance to Amazon Q Business—using either the AWS Management Console, CLI, or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API—and create an Amazon Q web experience.

The Amazon Q MySQL data source connector supports MySQL 8.0. 21.

**Important**  
As a best practice, provide Amazon Q with read-only database credentials. Also, avoid adding tables with sensitive data or personal identifiable information (PII).

**Topics**
+ [Known limitations for the MySQL connector](my-sql-limitations.md)
+ [MySQL connector overview](my-sql-overview.md)
+ [Prerequisites for connecting Amazon Q Business to MySQL](my-sql-prereqs.md)
+ [Connecting Amazon Q Business to MySQL using the console](my-sql-console.md)
+ [Connecting Amazon Q Business to MySQL using APIs](my-sql-api.md)
+ [How Amazon Q Business connector crawls MySQL ACLs](my-sql-user-management.md)
+ [MySQL data source connector field mappings](my-sql-field-mappings.md)
+ [IAM role for MySQL connector](my-sql-iam-role.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).