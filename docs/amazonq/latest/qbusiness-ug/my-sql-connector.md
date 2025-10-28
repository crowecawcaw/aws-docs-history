# Connecting MySQL to Amazon Q Business

###### Note

MySQL connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

MySQL is an open source relational database management system. You can
connect your MySQL instance to Amazon Q Business—using either the
AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web experience.

The Amazon Q MySQL data source connector supports MySQL 8.0. 21.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the
  MySQL connector](my-sql-limitations.md "my-sql-limitations.md")
- [MySQL connector
  overview](my-sql-overview.md "my-sql-overview.md")
- [Prerequisites for connecting Amazon Q Business to MySQL](my-sql-prereqs.md "my-sql-prereqs.md")
- [Connecting Amazon Q Business to
  MySQL using the console](my-sql-console.md "my-sql-console.md")
- [Connecting Amazon Q Business to
  MySQL using APIs](my-sql-api.md "my-sql-api.md")
- [How Amazon Q Business connector
  crawls MySQL ACLs](my-sql-user-management.md "my-sql-user-management.md")
- [MySQL data source
  connector field mappings](my-sql-field-mappings.md "my-sql-field-mappings.md")
- [IAM role for
  MySQL connector](my-sql-iam-role.md "my-sql-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
