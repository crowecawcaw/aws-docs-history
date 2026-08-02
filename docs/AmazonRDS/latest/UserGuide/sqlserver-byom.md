# Bring Your Own Media (BYOM) for RDS for SQL Server

Bring Your Own Media (BYOM) for RDS for SQL Server lets you use your existing SQL Server licenses on Amazon RDS through Microsoft's License Mobility through Software Assurance benefit.

You can license Microsoft SQL Server on Amazon RDS in two ways:

- **License Included** AWS provides the SQL Server license. The license fee is included in your RDS hourly rate.
- **Bring Your Own Media (BYOM)** You bring your existing SQL Server licenses through Microsoft's License Mobility through Software Assurance benefit. AWS does not charge a SQL Server license fee.
  Your use case and existing license agreements determine which model is more cost-effective for your workload. To use BYOM, you must have SQL Server licenses with active Software Assurance.

You download your SQL Server Release To Manufacturing (RTM) installation media as an ISO file from Microsoft and upload it to an Amazon S3 bucket. Amazon RDS uses that media to install SQL Server and automatically applies the required cumulative updates.

After Amazon RDS creates the instance, it manages all ongoing database operations including patching, automated backups, high availability, and monitoring using the same infrastructure as License Included instances. BYOM supports SQL Server Enterprise Edition and Standard Edition.

Amazon RDS SQL Server also supports BYOM for Developer Edition, however, there are some feature differences between them. For more details, see [Differences between Developer Edition and BYOM](sqlserver-byom-comparison.md "sqlserver-byom-comparison.md").

## Benefits

- **Use your existing licenses** You pay for AWS infrastructure (compute, storage, I/O, and data transfer) and Windows OS fees. Your existing Microsoft licenses cover the SQL Server license cost. AWS does not charge a SQL Server license fee.
- **Fully managed operations** Amazon RDS manages all ongoing database operations, including infrastructure management, automated backups, point-in-time recovery, Multi-AZ failover, and engine version upgrades.
- **Full feature parity** BYOM instances support the same RDS for SQL Server feature set as License Included instances. For exceptions, see [Current limitations](#sqlserver-byom.limitations "#sqlserver-byom.limitations").
- **License usage visibility** Amazon RDS integrates with [AWS License Manager](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md"), so you can track SQL Server license consumption across your AWS environment and maintain compliance with your licensing agreements.

## How BYOM works

The end-to-end workflow for using BYOM on RDS for SQL Server consists of the following steps:

1. **Prepare your installation media** Download the SQL Server RTM from Microsoft and upload it to an Amazon S3 bucket. For more information, see [Before you begin](sqlserver-byom-creating-cev.md#sqlserver-byom-creating-cev.before-you-begin "sqlserver-byom-creating-cev.md#sqlserver-byom-creating-cev.before-you-begin").
2. **Create a BYOM engine version** Create a BYOM engine version that references your uploaded installation media. Amazon RDS validates the files and creates a reusable BYOM engine version for launching instances. For more information, see [Creating and managing BYOM engine versions for RDS for SQL Server](sqlserver-byom-creating-cev.md "sqlserver-byom-creating-cev.md").
3. **Launch a BYOM instance** Launch an RDS for SQL Server instance using the `license-model` as `bring-your-own-media` option. For more information, see [Creating a BYOM DB instance for RDS for SQL Server](sqlserver-byom-creating-instance.md "sqlserver-byom-creating-instance.md").

###### Note

If you use the AWS Management Console, you can skip step 2. When you launch a BYOM instance from the console, select your target major and minor engine version and Amazon RDS creates the BYOM engine version automatically. Step 2 is required only when you use the AWS CLI or API.

###### Note

When you use BYOM, you are responsible for:

1. Providing valid SQL Server installation media (RTM ISO file)
2. Maintaining Microsoft licensing compliance through License Mobility
   Amazon RDS manages all other database operations the same way it does for License Included instances.

## How BYOM differs from License Included

| Aspect                        | License Included (LI)                                             | Bring Your Own Media (BYOM)                                                                                                                                             |
| ----------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL Server license            | Included                                                          | You provide your own license through Microsoft's License Mobility program                                                                                               |
| SQL Server installation media | AWS provides and manages                                          | You upload your SQL Server RTM to Amazon S3                                                                                                                             |
| Engine version management     | AWS manages all engine versions. You select which version to use. | You create a BYOM engine version for each target minor version, then you create or modify your instance to use it. The RTM file is reused across minor engine versions. |
| License compliance            | AWS manages                                                       | You maintain compliance through License Mobility. AWS License Manager provides usage tracking.                                                                          |

## Supported editions and major versions

| Edition                 | Major Versions                                    |
| ----------------------- | ------------------------------------------------- |
| Enterprise Edition (EE) | SQL Server 2019, SQL Server 2022, SQL Server 2025 |
| Standard Edition (SE)   | SQL Server 2019, SQL Server 2022, SQL Server 2025 |

## Supported instance types

For current BYOM instance support, visit the [Amazon RDS for SQL Server pricing page](https://aws.amazon.com/rds/sqlserver/pricing/ "https://aws.amazon.com/rds/sqlserver/pricing/").

## Region availability

BYOM for RDS for SQL Server is available in the following AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hyderabad)
- Asia Pacific (Jakarta)
- Asia Pacific (Malaysia)
- Asia Pacific (Melbourne)
- Asia Pacific (Mumbai)
- Asia Pacific (New Zealand)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Taipei)
- Asia Pacific (Thailand)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- Mexico (Central)
- South America (São Paulo)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)

## Pricing

For current pricing in your Region, see the [Amazon RDS for SQL Server pricing page](https://aws.amazon.com/rds/sqlserver/pricing/ "https://aws.amazon.com/rds/sqlserver/pricing/").

## AWS License Manager integration

Amazon RDS integrates with [AWS License Manager](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md") to help you track and manage your SQL Server license usage. When you configure License Manager, Amazon RDS automatically detects BYOM instances and reports vCPU usage. License Manager provides:

- Visibility into SQL Server license consumption across all BYOM instances
- Tracking of which instances use your own licenses versus License Included
- Audit-ready reports for Microsoft license compliance

If you do not configure License Manager, BYOM instances still function normally. However, you are responsible for monitoring license usage and maintaining compliance independently.

There is no additional charge for AWS License Manager. For pricing information, see [AWS License Manager pricing](https://aws.amazon.com/license-manager/pricing/ "https://aws.amazon.com/license-manager/pricing/").

## Current limitations

- **Major version upgrades** In-place major version upgrades are not supported. For example, you cannot upgrade a BYOM instance from SQL Server 2019 to SQL Server 2022 or SQL Server 2025 directly. To move to a newer major version, create a new BYOM DB instance with the target version and migrate your data using native backup and restore.
- A BYOM engine version is specific to your AWS account and Region. Each account must create its own BYOM engine versions independently. Cross-account operations are currently not supported.
- **Cross-region operations** BYOM engine versions are Region-specific. To perform cross-region operations, you must first create a BYOM engine version for the same engine version in the target Region. This applies to:

  - Cross-region read replicas
  - Cross-region snapshot copies
  - Cross-region automated backup replication

- BYOM does not support the following features:

  - SQL Server Analysis Services (SSAS)
  - SQL Server Reporting Services (SSRS)

- BYOM does not currently support SQL Server 2019 engine version `15.00.4043.16.v1`. To use BYOM with SQL Server 2019, choose a different supported engine version.
- BYOM supports SQL Server 2025 Enterprise Edition and Standard Edition starting with version `17.00.4045.5.v1`.
