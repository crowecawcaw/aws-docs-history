# Working with AWS Lake Formation-protected data

## Full Table Access

AWS Glue supports Full Table Access (FTA) for AWS Lake Formation-protected tables. This allows your ETL jobs to read and write data with full
table permissions.

### Prerequisites

- Appropriate IAM roles and permissions
- AWS Lake Formation configured for your data catalog
- Compatible table types (Hive or Iceberg)

### Key considerations

#### Required permissions

- `lakeformation:GetDataAccess` IAM permission
- AWS Lake Formation table permissions
- Amazon S3 bucket access permissions

#### Supported table types

- Hive tables
- Iceberg tables

#### Limitations

- Not compatible with Spark Streaming
- Cannot be used simultaneously with fine-grained access control
- Does not support Delta or Hudi tables

### Best Practices

1. Ensure IAM roles are properly configured before job execution
2. Test access permissions in a development environment
3. Monitor job execution logs for permission-related issues
4. Maintain clear documentation of access patterns

### Troubleshooting

Common issues include:

- Missing IAM permissions
- Incorrect AWS Lake Formation configuration
- Table type compatibility problems

For complete setup instructions and configuration details, see
[Using AWS Lake Formation with full table access](../../../emr/latest/EMR-Serverless-UserGuide/lake-formation-unfiltered-access.md "../../../emr/latest/EMR-Serverless-UserGuide/lake-formation-unfiltered-access.md").
