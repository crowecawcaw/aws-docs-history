# SQL Server modernization

AWS Transform for SQL Server Modernization is an AI-powered service that automates the full-stack modernization of
Microsoft SQL Server databases and their associated .NET applications to Amazon Aurora PostgreSQL. The service orchestrates the entire migration journey from schema conversion,
data migration and modifying application code to match the new target PostgreSQL,
making your teams more productive by automating complex and labor-intensive tasks.

## Supported regions

AWS Transform for SQL Server is available in US East (N. Virginia) - us-east-1

**Cross-Region Usage:** For databases in unsupported regions, you can clone the database to a supported region for transformation, then deploy the results back to your target region.

## Capabilities and key features

### Database transformation

- **Schema conversion:** Automatically converts SQL Server schemas to Aurora PostgreSQL, including tables, views, indexes, constraints, and relationships
- **Stored procedure transformation:** Converts T-SQL stored procedures to PL/pgSQL with AI-enhanced accuracy
- **Data migration:** Migrates data with integrity validation using AWS Database Migration Service (DMS)
- **Database objects:** Supports triggers, functions, views, computed columns, and identity columns
- **Validation:** Automated data integrity verification and referential integrity checks

### Application transformation

- **Entity Framework transformation:** Updates Entity Framework 6.3-6.5 and EF Core 1.0-8.0 configurations for PostgreSQL
- **ADO.NET transformation:** Converts ADO.NET data access code
  from SQL Server to PostgreSQL providers.
- **Connection string updates:** Automatically updates all database connection strings to the new target PostgreSQL database
- **Database provider changes:** Replaces SQL Server providers with Npgsql (PostgreSQL provider)
- **ORM configuration updates:** Modifies data type mappings, identity columns, and database-specific configurations

### Orchestration & validation

- **Wave-based modernization:** Organizes large estates into logical migration phases
- **Dependency mapping:** Identifies relationships between applications and databases
- **Human-in-the-loop (HITL) checkpoints:** Provides review and approval gates at critical stages
- **Automated validation:** Tests schema compatibility, data integrity, and application functionality
- **CI/CD integration:** Integrates with existing development pipelines

### Deployment

- **Amazon ECS and Amazon EC2 deployment:** Automated containerized deployment with auto-scaling support
- **Infrastructure-as-code generation:** Creates CloudFormation or AWS CDK templates
- **Automated deployment validation:** Verifies successful deployment with health checks
- **Rollback capabilities:** Supports rollback procedures if issues arise

## Supported versions and project types

### SQL Server versions

AWS Transform supports the following SQL Server versions:

| SQL Server Version | Support Status |
| ------------------ | -------------- |
| SQL Server 2022    | Supported      |
| SQL Server 2019    | Supported      |
| SQL Server 2017    | Supported      |
| SQL Server 2016    | Supported      |
| SQL Server 2014    | Supported      |
| SQL Server 2012    | Supported      |
| SQL Server 2008 R2 | Supported      |

###### Note

All SQL Server editions are supported (Express, Standard, Enterprise). SQL Server must be hosted on AWS (RDS SQL Server or SQL Server on EC2) in the same region as AWS Transform.

### .NET versions

| .NET Version                   | Support Status |
| ------------------------------ | -------------- |
| .NET 10                        | Supported      |
| .NET 8                         | Supported      |
| .NET 7                         | Supported      |
| .NET 6 (Core)                  | Supported      |
| .NET Framework 4.x and earlier | Not Supported  |

###### Important

Legacy .NET Framework 4.x and earlier versions are not supported. If your application uses .NET Framework, you must first upgrade to .NET Core 6+ using AWS Transform for .NET modernization before using SQL Server transformation capabilities.

### Entity Framework versions

| Framework             | Supported Versions |
| --------------------- | ------------------ |
| Entity Framework 6    | 6.3, 6.4, 6.5      |
| Entity Framework Core | 1.0 through 8.0    |
| ADO.NET               | All versions (GA)  |

### Source code repositories

AWS Transform supports the following repository platforms via AWS CodeConnections:

- GitHub and GitHub Enterprise
- GitLab.com and GitLab self-managed
- Bitbucket Cloud
- Azure Repositories
- AWS CodeCommit

### Target database

AWS Transform targets Amazon Aurora PostgreSQL (PostgreSQL 15+ compatible) with support for the latest Aurora features and optimizations.

### Technical requirements

#### Database requirements

- Microsoft SQL Server version 2008 R2 through 2022
- SQL Server hosted on AWS (RDS SQL Server or SQL Server on EC2)
- Database and AWS Transform in the same AWS region
- Network connectivity between AWS Transform and SQL Server
- Database user with VIEW DEFINITION and VIEW DATABASE STATE permissions
- Database passwords using printable ASCII characters only (excluding '/', '@', '"', and spaces)
- VPC containing the source SQL Server must have subnets in at least 2 different Availability Zones (required for DMS replication subnet groups)

#### Application requirements

- .NET Core 6, 7, or 8 applications
- Entity Framework 6.3-6.5 or Entity Framework Core 1.0-8.0, or ADO.NET
- Database connections discoverable in source code
- Applications successfully build and run
- Source code in supported repository platforms

#### AWS account requirements

- AWS account with administrator access
- IAM Identity Center enabled
- Required service roles created (see setup instructions below)
- VPC with appropriate network configuration

### Data processing and storage

#### Processing location

- Schema processing occurs in a DMS instance within your VPC
- Data migration is optional and can be excluded if required
- Transformation artifacts are stored in the AWS Transform service region

#### Stored artifacts

The following items are stored in the service region:

- Agent logs
- Assessment results
- SQL schema files
- DMS output artifacts

###### Important

**Important for Data Residency:** Even when data migration is opted out, metadata and processing artifacts are stored in the service region. This is important for organizations with strict data residency requirements.

#### Artifact management

- Customer option for encryption using your own KMS keys
- Defined TTL (time-to-live) period for all artifacts
- Artifacts can be downloaded for offline storage

## Application requirements

### Legacy .NET Framework

- **Limitation:** .NET Framework 4.x and earlier versions are not supported.
- **Workaround:** Use AWS Transform for .NET to upgrade to .NET Core 6+ first, then use SQL Server transformation.

### Entity Framework versions

- **Limitation:** Only Entity Framework 6.3-6.5 and EF Core 1.0-8.0 are supported.
- **Workaround:** Upgrade to a supported Entity Framework version before transformation.

### VB.NET applications

- **Limitation:** VB.NET is not supported.
- **Workaround:** Convert to C# or use AWS Transform custom to convert from VB.NET to C#.

### Cross-database dependencies

- **Limitation:** Challenges when database schemas interact across multiple databases.
- **Workaround:** Review and refactor cross-database queries before migration. Consider consolidating databases or using PostgreSQL schemas.
- **Impact:** May require human intervention for complex cross-database scenarios.

### Repository-database coupling

- **Limitation:** Challenges when a single repository serves multiple databases.
- **Workaround:** Consider repository restructuring or phased migration approach.
- **Impact:** May require additional planning for wave-based migrations.

## Infrastructure requirements

### Single account/region per job

- **Limitation:** Each transformation job targets one AWS account and region.
- **Workaround:** Create multiple transformation jobs for multi-account or multi-region deployments.

### Deployment targets

- **Limitation:** Amazon ECS and Amazon EC2 deployments are supported.

## Repository requirements

### Private NuGet packages

- **Limitation:** Private NuGet packages require additional configuration.
- **Workaround:** Configure private NuGet feeds in transformation settings before starting the job.
