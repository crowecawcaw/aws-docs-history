# Connecting PostgreSQL to Amazon Q Business

###### Note

PostgreSQL connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

PostgreSQL is an open source database management system. You can connect your
PostgreSQL instance to Amazon Q Business—using either the AWS Management Console,
CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web experience.

The Amazon Q PostgreSQL data source connector supports PostgreSQL
9.6.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the PostgreSQL connector](postgresql-limitations.md "postgresql-limitations.md")
- [PostgreSQL connector overview](postgresql-overview.md "postgresql-overview.md")
- [Prerequisites for connecting Amazon Q Business to PostgreSQL](postgresql-prereqs.md "postgresql-prereqs.md")
- [Connecting Amazon Q Business to PostgreSQL using the console](postgresql-console.md "postgresql-console.md")
- [Connecting Amazon Q Business to PostgreSQL using APIs](postgresql-api.md "postgresql-api.md")
- [How Amazon Q Business connector crawls PostgreSQL ACLs](postgresql-user-management.md "postgresql-user-management.md")
- [PostgreSQL data source connector field mappings](postgresql-field-mappings.md "postgresql-field-mappings.md")
- [IAM role for PostgreSQL connector](postgresql-iam-role.md "postgresql-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
