# Connecting Microsoft SQL Server to Amazon Q Business

###### Note

Microsoft SQL Server connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Microsoft SQL Server is an relational database management system (RDBMS) developed by
Microsoft. You can connect your Microsoft SQL Server instance to Amazon Q Business—using either the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web experience.

The Amazon Q Microsoft SQL Server data source connector supports MS SQL Server 2019.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the Microsoft SQL Server connector](ms-sql-server-limitations.md "ms-sql-server-limitations.md")
- [Microsoft SQL Server connector overview](ms-sql-server-overview.md "ms-sql-server-overview.md")
- [Prerequisites for connecting Amazon Q Business to Microsoft SQL Server](ms-sql-server-prereqs.md "ms-sql-server-prereqs.md")
- [Connecting to Microsoft SQL Server using the console](ms-sql-server-console.md "ms-sql-server-console.md")
- [Connecting to Microsoft SQL Server using APIs](ms-sql-server-api.md "ms-sql-server-api.md")
- [How connector crawls Microsoft SQL Server ACLs](ms-sql-server-user-management.md "ms-sql-server-user-management.md")
- [Microsoft SQL Server data source connector field mappings](ms-sql-server-field-mappings.md "ms-sql-server-field-mappings.md")
- [IAM role for Microsoft SQL Server connector](ms-sql-server-iam-role.md "ms-sql-server-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
