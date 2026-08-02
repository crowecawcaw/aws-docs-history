# SQL Server modernization

AWS Transform for SQL Server Modernization is an AI-powered service that automates the full-stack modernization of
Microsoft SQL Server databases and their associated .NET applications to Amazon Aurora PostgreSQL. AWS Transform now converts SQL Server storage objects, powered by AWS DMS, and code objects (stored procedures) using an agentic, interactive experience. The service orchestrates the entire migration journey from schema conversion,
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

- **Entity Framework transformation:** Updates Entity Framework 6.3-6.5 and EF Core 1.0-10.0 configurations for PostgreSQL
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

All SQL Server editions are supported (Express, Standard, Enterprise). SQL Server can be hosted on AWS (Amazon RDS for SQL Server or SQL Server on Amazon EC2) or hosted outside of AWS.

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
| Entity Framework Core | 1.0 through 10.0   |
| ADO.NET               | All versions (GA)  |

### Source code repositories

AWS Transform supports the following source code platforms:

- GitHub and GitHub Enterprise Server
- GitLab.com and GitLab Self-Managed
- Bitbucket Cloud and Bitbucket Data Center
- Azure DevOps and Azure DevOps Server
- Amazon S3

### Target database

AWS Transform targets Amazon Aurora PostgreSQL (PostgreSQL 15+ compatible) with support for the latest Aurora features and optimizations.

### Technical requirements

#### Database requirements

- Microsoft SQL Server version 2008 R2 through 2022
- SQL Server hosted on AWS (Amazon RDS for SQL Server or SQL Server on Amazon EC2) or hosted outside of AWS
- For AWS-hosted databases, the database and AWS Transform must be in the same AWS Region.
- For databases hosted outside of AWS, network connectivity to the AWS Transform service is required.
- Database user with VIEW DEFINITION and VIEW DATABASE STATE permissions
- Database passwords using printable ASCII characters only (excluding '/', '@', '"', and spaces)
- VPC containing the source SQL Server must have subnets in at least 2 different Availability Zones (required for DMS replication subnet groups)

#### Application requirements

- .NET 6, 7, 8, or 10 applications
- Entity Framework 6.3-6.5 or Entity Framework Core 1.0-10.0, or ADO.NET
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
