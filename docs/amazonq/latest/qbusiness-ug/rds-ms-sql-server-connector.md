# Connecting Amazon RDS (Microsoft SQL Server) to Amazon Q Business

###### Note

Amazon RDS (Microsoft SQL Server) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Amazon RDS (Microsoft SQL Server) is a relational database management system (RDBMS) built for the cloud.
You can connect your Amazon RDS (Microsoft SQL Server) instance to Amazon Q Business – using
either the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API – and create an Amazon Q web experience.

The Amazon Q Microsoft SQL Server data source connector supports MS SQL Server 2019.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the
  Amazon RDS (Microsoft SQL Server) connector](rds-ms-sql-server-limitations.md "rds-ms-sql-server-limitations.md")
- [Amazon RDS (Microsoft SQL Server) connector
  overview](rds-ms-sql-server-overview.md "rds-ms-sql-server-overview.md")
- [Prerequisites for connecting Amazon Q Business to Amazon RDS (Microsoft SQL Server)](rds-ms-sql-server-prereqs.md "rds-ms-sql-server-prereqs.md")
- [Connecting Amazon Q Business to
  Amazon RDS (Microsoft SQL Server) using the console](rds-ms-sql-server-console.md "rds-ms-sql-server-console.md")
- [Connecting Amazon Q Business to
  Amazon RDS (Microsoft SQL Server) using APIs](rds-ms-sql-server-api.md "rds-ms-sql-server-api.md")
- [How Amazon Q Business connector
  crawls Amazon RDS (Microsoft SQL Server) ACLs](rds-ms-sql-server-user-management.md "rds-ms-sql-server-user-management.md")
- [Amazon RDS (Microsoft SQL Server) data source
  connector field mappings](rds-ms-sql-server-field-mappings.md "rds-ms-sql-server-field-mappings.md")
- [IAM role for
  Amazon RDS (Microsoft SQL Server) connector](rds-ms-sql-server-iam-role.md "rds-ms-sql-server-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
