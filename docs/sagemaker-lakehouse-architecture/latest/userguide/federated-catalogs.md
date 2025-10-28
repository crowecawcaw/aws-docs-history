# Federated catalogs for the lakehouse architecture of Amazon SageMaker

The lakehouse architecture with integrated access controls for Athena federated queries enables you to connect to and query data across multiple data sources without moving or duplicating data. Federated catalogs establish secure links to external data sources, breaking down data silos while maintaining consistent governance and security controls. For a step-by-step guide, see [Get started with lakehouse architecture integrated access controls for Athena federated queries](../../../next-generation-sagemaker/latest/userguide/lakehouse-athena-federated-queries.md "../../../next-generation-sagemaker/latest/userguide/lakehouse-athena-federated-queries.md").

## Overview

Federated connections address common data infrastructure challenges:

- **Complex connectivity setup** - Streamline connection creation through a unified interface
- **Fragmented governance** - Centralize access control management through Lake Formation
- **Data duplication** - Enable in-place querying without data movement

Key capabilities include:

- Unified interface for connecting to diverse data sources
- Fine-grained permissions at catalog, database, table, and column levels
- In-place querying through federated catalogs
- Support for ad hoc reporting and proof of concept analysis

## Supported data sources

The lakehouse architecture federated catalogs support the following data sources:

| Data Source         | Type     |
| ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Google BigQuery     | Database |
| Amazon DocumentDB   | Database |
| DynamoDB            | Database |
| Amazon Redshift     | Database |
| MySQL               | Database |
| PostgreSQL          | Database |
| SQL Server          | Database |
| Snowflake           | Database |
| Oracle              | Database |
| Aurora MySQL        | Database |
| Aurora Postgres     | Database |
| Microsoft Azure SQL | Database | ###### Note The lakehouse architecture currently supports lowercase table, column, and database names. For optimal experience, ensure that all database identifiers are in lowercase. For more information about data connections and their capabilities, see [Data connections in the lakehouse architecture of Amazon SageMaker](lakehouse-data-connection.md "lakehouse-data-connection.md"). ## Setting up federated connections The process for implementing federated connections involves these high-level steps: 1. **Create federated connections** <br>• Establish connections that serve as bridges between lakehouse architecture and external data sources <br>• Configure secure connectivity while maintaining security boundaries <br>• Eliminate the need for data movement or duplication 2. **Create federated catalogs** <br>• Establish catalogs containing metadata about tables from connected data sources <br>• Make external tables discoverable and queryable through the Lakehouse interface <br>• Use catalogs as directories of available data assets 3. **Implement access controls** <br>• Configure fine-grained permissions using Lake Formation <br>• Apply column-level security for sensitive data <br>• Ensure consistent security policies across all data sources 4. **Validate and query** <br>• Test access permissions with different user personas <br>• Run federated queries across multiple data sources <br>• Verify security controls and data access policies ## Prerequisites Before setting up federated connections, ensure you have: <br>• AWS account with permissions to create IAM roles and policies <br>• Data lake administrator role in Lake Formation <br>• SageMaker AI Unified Studio domain with SQL Analytics profile enabled <br>• SageMaker AI Unified Studio projects configured for administration and data analysis <br>• Administrator access to target data sources ## Best practices Follow these best practices when implementing federated connections: <br>• **Security** - Implement least-privilege access and use column-level security for sensitive data <br>• **Performance** - Optimize queries by using appropriate filters and limiting data scanned <br>• **Monitoring** - Track query performance and resource usage across federated sources <br>• **Governance** - Maintain consistent data classification and access policies For detailed implementation steps, see [Get started with lakehouse architecture integrated access controls for Athena federated queries](../../../next-generation-sagemaker/latest/userguide/lakehouse-athena-federated-queries.md "../../../next-generation-sagemaker/latest/userguide/lakehouse-athena-federated-queries.md"). |
