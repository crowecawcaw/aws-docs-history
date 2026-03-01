# Connecting Aurora (MySQL) to Amazon Q Business

###### Note

Aurora (MySQL) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Aurora (MySQL) is a relational database management system (RDBMS) built for the cloud.
You can connect your Aurora (MySQL) instance to Amazon Q Business—using
either the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web experience.

The Amazon Q
Aurora (MySQL) data source connector supports Aurora MySQL 3 and
Aurora Serverless MySQL 8.0.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the Aurora (MySQL) connector](aurora-mysql-limitations.md "aurora-mysql-limitations.md")
- [Aurora (MySQL) connector overview](aurora-mysql-overview.md "aurora-mysql-overview.md")
- [Prerequisites for connecting Amazon Q Business to Aurora (MySQL)](aurora-mysql-prereqs.md "aurora-mysql-prereqs.md")
- [Connecting Amazon Q Business to Aurora (MySQL) using the console](aurora-mysql-console.md "aurora-mysql-console.md")
- [Connecting Amazon Q Business to Aurora (MySQL) using APIs](aurora-mysql-api.md "aurora-mysql-api.md")
- [How Amazon Q Business connector crawls Aurora (MySQL) ACLs](aurora-mysql-user-management.md "aurora-mysql-user-management.md")
- [Aurora (MySQL) data source connector field mappings](aurora-mysql-field-mappings.md "aurora-mysql-field-mappings.md")
- [IAM role for Aurora (MySQL) connector](aurora-mysql-iam-role.md "aurora-mysql-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
