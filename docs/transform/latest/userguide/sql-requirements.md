# SQL Server requirements

## Database requirements

### Source databases

- **Limitation:** Direct connection to on-premises SQL Server is not supported.
- **Limitation:** Databases should be running on a VPC in AWS.
- **Workaround:** Create a clone of your database on EC2 in a supported AWS region for testing and transformation. Apply learnings to your production migration using AWS DMS.

### SSIS workloads

- **Limitation:** SQL Server Integration Services (SSIS) transformation is not supported.
- **Workaround:** Use AWS Glue or other ETL services for SSIS migration.

### Linked servers

- **Limitation:** External database connections via linked servers require human configuration.
- **Workaround:** Reconfigure linked servers after migration or use alternative approaches such as database links or application-level integration.

### Complex T-SQL patterns

- **Limitation:** Some advanced T-SQL patterns may need human intervention.
- **Workaround:** Use Amazon Kiro CLI for complex SQL conversions. AWS Transform flags these for review during the transformation process.
