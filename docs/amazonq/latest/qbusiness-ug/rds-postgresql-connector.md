# Connecting Amazon RDS (PostgreSQL) to Amazon Q Business

###### Note

Amazon RDS (PostgreSQL) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Amazon RDS (PostgreSQL) is a web service that makes it easier to set up, operate, and scale a
relational database in the AWS Cloud. If you are a AWS user, you
can use Amazon Q Business to index your Amazon RDS (PostgreSQL) data source.

The Amazon Q Amazon RDS (PostgreSQL) data source connector supports PostgreSQL
9.6.

You can connect your Amazon RDS (PostgreSQL) instance to Amazon Q Business—using
either the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web
experience.

###### Important

As a best practice, provide Amazon Q with read-only database credentials. Also,
avoid adding tables with sensitive data or personal identifiable information (PII).

###### Topics

- [Known limitations for the Amazon RDS (PostgreSQL)
  connector](rds-postgresql-limitations.md "rds-postgresql-limitations.md")
- [Amazon RDS (PostgreSQL) connector overview](rds-postgresql-overview.md "rds-postgresql-overview.md")
- [Prerequisites for connecting Amazon Q Business to Amazon RDS (PostgreSQL)](rds-postgresql-prereqs.md "rds-postgresql-prereqs.md")
- [Connecting Amazon Q Business to
  Amazon RDS (PostgreSQL) using the console](rds-postgresql-console.md "rds-postgresql-console.md")
- [Connecting Amazon Q Business to
  Amazon RDS (PostgreSQL) using APIs](rds-postgresql-api.md "rds-postgresql-api.md")
- [How Amazon Q Business connector
  crawls Amazon RDS (PostgreSQL) ACLs](rds-postgresql-user-management.md "rds-postgresql-user-management.md")
- [Amazon RDS (PostgreSQL) data source connector
  field mappings](rds-postgresql-field-mappings.md "rds-postgresql-field-mappings.md")
- [IAM role for Amazon RDS (PostgreSQL)
  connector](rds-postgresql-iam-role.md "rds-postgresql-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
