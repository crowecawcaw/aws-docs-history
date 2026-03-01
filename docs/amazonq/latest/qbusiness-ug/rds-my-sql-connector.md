# Connecting Amazon RDS (MySQL) to Amazon Q Business

###### Note

Amazon RDS (MySQL) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Amazon RDS (MySQL) (Amazon Relational Database Service) is a web service that makes it
easier to set up, operate, and scale a relational database in the AWS Cloud. You can
connect your Amazon RDS (MySQL) instance to Amazon Q Business – using either
the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API – and create an Amazon Q web experience.

The Amazon Q
Aurora (MySQL) data source connector supports Amazon RDS MySql 5.6, 5.7, and
8.0.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the Amazon RDS (MySQL) connector](rds-my-sql-limitations.md "rds-my-sql-limitations.md")
- [Amazon RDS (MySQL) connector overview](rds-my-sql-overview.md "rds-my-sql-overview.md")
- [Prerequisites for connecting Amazon Q Business to Amazon RDS (MySQL)](rds-my-sql-prereqs.md "rds-my-sql-prereqs.md")
- [Connecting Amazon Q Business to Amazon RDS (MySQL) using the console](rds-my-sql-console.md "rds-my-sql-console.md")
- [Connecting Amazon Q Business to Amazon RDS (MySQL) using APIs](rds-my-sql-api.md "rds-my-sql-api.md")
- [How Amazon Q Business connector crawls Amazon RDS (MySQL) ACLs](rds-my-sql-user-management.md "rds-my-sql-user-management.md")
- [Amazon RDS (MySQL) data source connector field mappings](rds-my-sql-field-mappings.md "rds-my-sql-field-mappings.md")
- [IAM role for Amazon RDS (MySQL) connector](rds-my-sql-iam-role.md "rds-my-sql-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
