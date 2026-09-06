

# Working with SQL Server Developer Edition on RDS for SQL Server
<a name="sqlserver-dev-edition"></a>

RDS for SQL Server supports SQL Server Developer Edition. Developer Edition includes all SQL Server Enterprise Edition features but is licensed only for non-production use. You can create RDS for SQL Server Developer Edition instances using your own installation media through the custom engine version (CEV) feature. Amazon RDS SQL Server also supports Bring Your Own Media (BYOM) for Standard Edition and Enterprise Edition, however, there are some feature differences between them. For more details, see [Differences between Developer Edition and BYOM](sqlserver-byom-comparison.md).

## Benefits
<a name="sqlserver-dev-edition.benefits"></a>

You can use RDS for SQL Server Developer Edition to:
+ Lower costs in development and test environments while maintaining feature parity with production databases.
+ Access Enterprise Edition capabilities in non-production environments without Enterprise licensing fees.
+ Use Amazon RDS-automated management features, including backups, patching, and monitoring.

**Note**  
SQL Server Developer Edition is licensed for development and testing purposes only and cannot be used in production environments.

## Region availability
<a name="sqlserver-dev-edition.regions"></a>

RDS for SQL Server Developer Edition is available in the following AWS Regions:
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (N. California)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Taipei)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Mumbai)
+ Asia Pacific (New Zealand)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Thailand)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Canada West (Calgary)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Milan)
+ Europe (Paris)
+ Europe (Spain)
+ Europe (Stockholm)
+ Israel (Tel Aviv)
+ Mexico (Central)
+ South America (São Paulo)
+ AWS GovCloud (US-East)
+ AWS GovCloud (US-West)

## Licensing and usage
<a name="sqlserver-dev-edition.licensing"></a>

SQL Server Developer Edition is licensed by Microsoft for development and test environments only. You cannot use Developer Edition as a production server. When you use SQL Server Developer Edition on Amazon RDS, you are responsible for complying with Microsoft's SQL Server Developer Edition licensing terms. You pay only for the AWS infrastructure costs - there is no additional SQL Server licensing fee. For pricing details, see [RDS for SQL Server pricing](https://aws.amazon.com/rds/sqlserver/pricing/).

## Prerequisites
<a name="sqlserver-dev-edition.prerequisites"></a>

Before using SQL Server Developer Edition on RDS for SQL Server, ensure you have the following requirements:
+ You must obtain the installation binaries directly from Microsoft and ensure compliance with Microsoft's licensing terms.
+ You must have access to use the following resources to create a Developer Edition DB instance:
  + AWS account with `AmazonRDSFullAccess` and `s3:GetObject` permissions.
+ An Amazon S3 bucket is required for storing installation media. You will need an ISO and cumulative update file to upload to the Amazon S3 bucket as part of CEV creation. For more information, see [Uploading installation media to an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).
+ All installation media files must reside within the same Amazon S3 bucket and the same folder path within that Amazon S3 bucket in the same Region where the custom engine version is created.

### Supported versions
<a name="sqlserver-dev-edition.supported-versions"></a>

Developer Edition on RDS for SQL Server supports the following versions:
+ SQL Server 2025 CU5 (17.00.4045.5) – Developer Edition (Enterprise Edition capabilities)
+ SQL Server 2025 CU5 (17.00.4045.5) – Developer Edition (Standard Edition capabilities)
+ SQL Server 2022 CU 21 (16.00.4215.2)
+ SQL Server 2019 CU 32 GDR (15.00.4455.2)

**Note**  
Starting with SQL Server 2025, Amazon RDS supports two Developer Edition engine types:  
`sqlserver-dev-ee` – includes all Enterprise Edition features, licensed for non-production use only.
`sqlserver-dev-se` – new in SQL Server 2025, includes all Standard Edition features, licensed for non-production use only.
For more information about SQL Server Developer Edition variants, see [Editions and supported features of SQL Server 2025](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2025?view=sql-server-ver17) in the Microsoft documentation.

To list all supported engine versions for Developer Edition (Enterprise Edition capabilities) CEV creation, use the following AWS CLI command:

```
aws rds describe-db-engine-versions --engine sqlserver-dev-ee --output json --query "{DBEngineVersions: DBEngineVersions[?Status=='requires-custom-engine-version'].{Engine: Engine, EngineVersion: EngineVersion, Status: Status, DBEngineDescription: DBEngineDescription, DBEngineVersionDescription: DBEngineVersionDescription}}"
```

The command returns output similar to the following example:

```
{
    "DBEngineVersions": [
        {
            "Engine": "sqlserver-dev-ee",
            "EngineVersion": "{{16.00.4215.2.v1}}",
            "Status": "requires-custom-engine-version",
            "DBEngineDescription": "Microsoft SQL Server Enterprise Developer Edition",
            "DBEngineVersionDescription": "SQL Server 2022 16.00.4215.2.v1"
        }
    ]
}
```

To list all supported engine versions for Developer Edition (Standard Edition capabilities) CEV creation, use the following AWS CLI command:

```
aws rds describe-db-engine-versions --engine sqlserver-dev-se --output json --query "{DBEngineVersions: DBEngineVersions[?Status=='requires-custom-engine-version'].{Engine: Engine, EngineVersion: EngineVersion, Status: Status, DBEngineDescription: DBEngineDescription, DBEngineVersionDescription: DBEngineVersionDescription}}"
```

The command returns output similar to the following example:

```
{
    "DBEngineVersions": [
        {
            "Engine": "sqlserver-dev-se",
            "EngineVersion": "{{17.00.4045.5.v1}}",
            "Status": "requires-custom-engine-version",
            "DBEngineDescription": "Microsoft SQL Server Standard Developer Edition",
            "DBEngineVersionDescription": "SQL Server 2025 17.00.4045.5.v1"
        }
    ]
}
```

The engine version status as `requires_custom_engine_version` identifies template engine versions that are supported. These templates show which SQL Server versions you can import.

## Limitations
<a name="sqlserver-dev-edition.limitations"></a>

The following limitations apply to SQL Server Developer Edition on Amazon RDS:
+ Supported instance classes vary by SQL Server version. For the current list, see [DB instance class support for Microsoft SQL Server](SQLServer.Concepts.General.InstanceClasses.md), or use the [describe-orderable-db-instance-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-orderable-db-instance-options.html) AWS CLI command.
+ Amazon RDS doesn't support Multi-AZ deployments or read replicas for this edition.
+ You must provide and manage your own SQL Server installation media.
+ You can't share custom engine versions for SQL Server Developer Edition (`sqlserver-dev-ee` and `sqlserver-dev-se`) across Regions or accounts.