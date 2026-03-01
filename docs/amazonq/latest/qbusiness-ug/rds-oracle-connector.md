# Connecting Amazon RDS (Oracle) to Amazon Q Business

###### Note

Amazon RDS (Oracle) connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

Amazon RDS (Oracle) (Amazon Relational Database Service) is a web service that makes it
easier to set up, operate, and scale a relational database in the AWS Cloud. You can
connect your Amazon RDS (Oracle) instance to Amazon Q Business – using either
the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API – and create an Amazon Q web experience.

The Amazon RDS (Oracle) (Amazon Relational Database Service) data source connector supports
Amazon RDS Oracle Database 21c, Oracle Database 19c, Oracle Database 12c.

###### Important

As a best practice, provide Amazon Q with read-only database credentials.
Also, avoid adding tables with sensitive data or personal identifiable information
(PII).

###### Topics

- [Known limitations for the Amazon RDS (Oracle) connector](rds-oracle-limitations.md "rds-oracle-limitations.md")
- [Amazon RDS (Oracle) connector overview](rds-oracle-overview.md "rds-oracle-overview.md")
- [Prerequisites for connecting Amazon Q Business to Amazon RDS (Oracle)](rds-oracle-prereqs.md "rds-oracle-prereqs.md")
- [Connecting Amazon Q Business to Amazon RDS (Oracle) using the console](rds-oracle-console.md "rds-oracle-console.md")
- [Connecting Amazon Q Business to Amazon RDS (Oracle) using APIs](rds-oracle-api.md "rds-oracle-api.md")
- [How Amazon Q Business connector crawls Amazon RDS (Oracle) ACLs](rds-oracle-user-management.md "rds-oracle-user-management.md")
- [Amazon RDS (Oracle) data source connector field mappings](rds-oracle-field-mappings.md "rds-oracle-field-mappings.md")
- [IAM role for Amazon RDS (Oracle) connector](rds-oracle-iam-role.md "rds-oracle-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
