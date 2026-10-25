

# SQL Server requirements
<a name="sql-requirements"></a>

## Database requirements
<a name="sql-database-requirements"></a>

### Externally hosted databases
<a name="externally-hosted-databases"></a>

Databases hosted outside of AWS are supported. Because AWS Transform modernizes your schema from uploaded DDL files, no network connectivity between your database and the AWS Transform service is required. You run the extraction script in your own environment and upload the resulting schema files.

### SSIS workloads
<a name="ssis-workloads"></a>
+ **Limitation:** SQL Server Integration Services (SSIS) transformation is not supported.
+ **Workaround:** Use AWS Glue or other ETL services for SSIS migration.

### Linked servers
<a name="linked-servers"></a>
+ **Limitation:** External database connections via linked servers require human configuration.
+ **Workaround:** Reconfigure linked servers after migration or use alternative approaches such as database links or application-level integration.

### Complex T-SQL patterns
<a name="complex-tsql-patterns"></a>
+ **Limitation:** Some advanced T-SQL patterns may need human intervention.
+ **Workaround:** Use Amazon Kiro CLI for complex SQL conversions. AWS Transform flags these for review during the transformation process.