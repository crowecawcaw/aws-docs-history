# Connecting Aurora (PostgreSQL) to Amazon Q Business

###### Note

Aurora (PostgreSQL) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Aurora (PostgreSQL) is a relational database management system (RDBMS) built for the cloud.
You can connect your Aurora (PostgreSQL) instance to Amazon Q Business—using
either the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web experience.

The Amazon Q
Aurora (PostgreSQL) data source connector supports Aurora PostgreSQL

1.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the Aurora (PostgreSQL) connector](aurora-postgresql-limitations.md "aurora-postgresql-limitations.md")
- [Aurora (PostgreSQL) connector overview](aurora-postgresql-overview.md "aurora-postgresql-overview.md")
- [Prerequisites for connecting Amazon Q Business to Aurora (PostgreSQL)](aurora-postgresql-prereqs.md "aurora-postgresql-prereqs.md")
- [Connecting Amazon Q Business to Aurora (PostgreSQL) using the console](aurora-postgresql-console.md "aurora-postgresql-console.md")
- [Connecting Amazon Q Business to Aurora (PostgreSQL) using APIs](aurora-postgresql-api.md "aurora-postgresql-api.md")
- [How Amazon Q Business connector crawls Aurora (PostgreSQL) ACLs](aurora-postgresql-user-management.md "aurora-postgresql-user-management.md")
- [Aurora (PostgreSQL) data source connector field mappings](aurora-postgresql-field-mappings.md "aurora-postgresql-field-mappings.md")
- [IAM role for Aurora (PostgreSQL) connector](aurora-postgresql-iam-role.md "aurora-postgresql-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
