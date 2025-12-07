# Working with SQL Server Developer Edition on RDS for SQL Server

RDS for SQL Server now supports SQL Server Developer Edition. Developer Edition includes all SQL Server Enterprise Edition features but is licensed only for non-production use. You can create RDS for SQL Server Developer Edition instances using your own installation media through the custom engine version (CEV) feature.

## Benefits

You can use RDS for SQL Server Developer Edition to:

- Lower costs in development and test environments while maintaining feature parity with production databases.
- Access Enterprise Edition capabilities in non-production environments without Enterprise licensing fees.
- Use Amazon RDS-automated management features, including backups, patching, and monitoring.

###### Note

SQL Server Developer Edition is licensed for development and testing purposes only and cannot be used in production environments.

## Region availability

RDS for SQL Server Developer Edition is available in the following AWS Regions:

- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Tokyo)

## Licensing and usage

SQL Server Developer Edition is licensed by Microsoft for development and test environments only. You cannot use Developer Edition as a production server. When you use SQL Server Developer Edition on Amazon RDS, you are responsible for complying with Microsoft's SQL Server Developer Edition licensing terms. You pay only for the AWS infrastructure costs - there is no additional SQL Server licensing fee. For pricing details, see [RDS for SQL Server pricing](https://aws.amazon.com/rds/sqlserver/pricing/ "https://aws.amazon.com/rds/sqlserver/pricing/").

## Prerequisites

Before using SQL Server Developer Edition on RDS for SQL Server, ensure you have the following requirements:

- You must obtain the installation binaries directly from Microsoft and ensure compliance with Microsoft's licensing terms.
- You must have access to use the following resources to create a Developer Edition DB instance:
  - AWS account with `AmazonRDSFullAccess` and `s3:GetObject` permissions.

- An Amazon S3 bucket is required for storing installation media. You will need an ISO and cumulative update file to upload to the Amazon S3 bucket as part of CEV creation. For more information, see [Uploading installation media to an Amazon S3 bucket](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md").
- All installation media files must reside within the same Amazon S3 bucket and the same folder path within that Amazon S3 bucket in the same Region where the CEV is created.

### Supported versions

Developer Edition on RDS for SQL Server supports the following versions:

- SQL Server 2022 CU 21 (16.00.4215.2) or higher

To list all supported engine versions for Developer Edition CEV creation, run the following AWS CLI command:

```
aws rds describe-db-engine-versions --engine sqlserver-dev-ee --output json --query "{DBEngineVersions: DBEngineVersions[?Status=='requires-custom-engine-version'].{Engine: Engine, EngineVersion: EngineVersion, Status: Status, DBEngineVersionDescription: DBEngineVersionDescription}}"
```

The command returns output similar to the following:

```
{
    "DBEngineVersions": [
        {
            "Engine": "sqlserver-dev-ee",
            "EngineVersion": "16.00.4215.2.v1",
            "Status": "requires-custom-engine-version",
            "DBEngineDescription": "Microsoft SQL Server Enterprise Developer Edition",
            "DBEngineVersionDescription": "SQL Server 2022 16.00.4215.2.v1"
        }
    ]
}
```

The engine version status as `requires_custom_engine_version` identifies template engine versions that are supported. These templates show which SQL Server versions you can import.

## Limitations

The following limitations apply to SQL Server Developer Edition on Amazon RDS:

- Currently only supported on M6i and R6i instance classes.
- Multi-AZ deployments and read replicas are not supported.
- You must provide and manage your own SQL Server installation media.
- Cross-Region and cross-account custom engine versions (CEVs) are not supported.
