

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon RDS (PostgreSQL) to Amazon Q Business
<a name="rds-postgresql-connector"></a>

**Note**  
Amazon RDS (PostgreSQL) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-connector.html), designed to support a broader range of enterprise use cases with enhanced flexibility.

Amazon RDS (PostgreSQL) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. If you are a AWS user, you can use Amazon Q Business to index your Amazon RDS (PostgreSQL) data source.

The Amazon Q Amazon RDS (PostgreSQL) data source connector supports PostgreSQL 9.6.

 You can connect your Amazon RDS (PostgreSQL) instance to Amazon Q Business—using either the AWS Management Console, CLI, or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API—and create an Amazon Q web experience.

**Important**  
As a best practice, provide Amazon Q with read-only database credentials. Also, avoid adding tables with sensitive data or personal identifiable information (PII).

**Topics**
+ [Known limitations for the Amazon RDS (PostgreSQL) connector](rds-postgresql-limitations.md)
+ [Amazon RDS (PostgreSQL) connector overview](rds-postgresql-overview.md)
+ [Prerequisites for connecting Amazon Q Business to Amazon RDS (PostgreSQL)](rds-postgresql-prereqs.md)
+ [Connecting Amazon Q Business to Amazon RDS (PostgreSQL) using the console](rds-postgresql-console.md)
+ [Connecting Amazon Q Business to Amazon RDS (PostgreSQL) using APIs](rds-postgresql-api.md)
+ [How Amazon Q Business connector crawls Amazon RDS (PostgreSQL) ACLs](rds-postgresql-user-management.md)
+ [Amazon RDS (PostgreSQL) data source connector field mappings](rds-postgresql-field-mappings.md)
+ [IAM role for Amazon RDS (PostgreSQL) connector](rds-postgresql-iam-role.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).