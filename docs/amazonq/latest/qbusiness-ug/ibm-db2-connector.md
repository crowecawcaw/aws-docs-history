# Connecting IBM DB2 to Amazon Q Business

###### Note

IBM DB2 connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the [Amazon Q Business Custom Connector Framework](custom-connector.md "custom-connector.md"), designed to support a broader range of enterprise use cases with enhanced flexibility.

IBM DB2 is a relational database management system developed by IBM. If you are a
AWS user, you can use Amazon Q Business to index your IBM DB2
data source.

You can connect your IBM DB2 instance to Amazon Q—using either
the AWS Management Console, CLI, or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API—and create an Amazon Q web
experience.

The Amazon Q IBM DB2 data source connector supports DB2 11.5.7.

###### Important

As a best practice, provide Amazon Q with read-only database credentials. Also,
avoid adding tables with sensitive data or personal identifiable information (PII).

###### Topics

- [Known limitations for the IBM DB2
  connector](ibm-db2-limitations.md "ibm-db2-limitations.md")
- [IBM DB2 connector overview](ibm-db2-overview.md "ibm-db2-overview.md")
- [Prerequisites for connecting Amazon Q Business to IBM DB2](ibm-db2-prereqs.md "ibm-db2-prereqs.md")
- [Connecting Amazon Q Business to
  IBM DB2 using the console](ibm-db2-console.md "ibm-db2-console.md")
- [Connecting Amazon Q Business to
  IBM DB2 using APIs](ibm-db2-api.md "ibm-db2-api.md")
- [How Amazon Q Business connector
  crawls IBM DB2 ACLs](ibm-db2-user-management.md "ibm-db2-user-management.md")
- [IBM DB2 data source connector
  field mappings](ibm-db2-field-mappings.md "ibm-db2-field-mappings.md")
- [IAM role for IBM DB2
  connector](ibm-db2-iam-role.md "ibm-db2-iam-role.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
