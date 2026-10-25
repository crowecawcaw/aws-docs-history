

# SQL Server modernization
<a name="sql-server-modernization"></a>

AWS Transform for SQL Server Modernization is an AI-powered service that automates the full-stack modernization of Microsoft SQL Server databases and their associated .NET applications to Amazon Aurora PostgreSQL. AWS Transform converts SQL Server storage objects and code objects (stored procedures) using an agentic, interactive experience. The service orchestrates the migration journey from schema conversion, synthetic data generation, and modifying application code to match the new target PostgreSQL, making your teams more productive by automating complex and labor-intensive tasks.

## Supported regions
<a name="supported-regions"></a>

AWS Transform for SQL Server is available in US East (N. Virginia), Europe (Frankfurt), Europe (London), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Tokyo), Asia Pacific (Sydney), and Canada (Montreal).

**Cross-Region Usage:** For databases in unsupported regions, AWS Transform for full-stack Windows modernization supports cross-region deployment of converted Amazon Aurora PostgreSQL databases. You can upload SQL Server Database Design Language (DDL) files and set a target AWS Region in the transformation plan to convert the database and deploy the resulting Aurora PostgreSQL cluster to a different AWS Region. If you have data residency, latency, or disaster recovery requirements, you can start a job in any of the available AWS Regions and deploy the target cluster in the destination Region of your choice.

## Capabilities and key features
<a name="capabilities-key-features"></a>

### Database transformation
<a name="database-transformation"></a>
+ **Schema conversion:** Automatically converts SQL Server schemas to Aurora PostgreSQL, including tables, views, indexes, constraints, and relationships
+ **Stored procedure transformation:** Converts T-SQL stored procedures to PL/pgSQL with AI-enhanced accuracy
+ **Database objects:** Supports triggers, functions, views, computed columns, and identity columns
+ **Synthetic data generation:** Generate synthetic data for the converted PostgreSQL database to validate functionality
+ **Validation:** Automated functional equivalence checks for transformed database objects, stored procedures, and functions

### Application transformation
<a name="application-transformation"></a>
+ **Entity Framework transformation:** Updates Entity Framework 6.3-6.5 and EF Core 1.0-10.0 configurations for PostgreSQL
+ **ADO.NET transformation:** Converts ADO.NET data access code from SQL Server to PostgreSQL providers. 
+ **Connection string updates:** Automatically updates all database connection strings to the new target PostgreSQL database
+ **Database provider changes:** Replaces SQL Server providers with Npgsql (PostgreSQL provider)
+ **ORM configuration updates:** Modifies data type mappings, identity columns, and database-specific configurations

### Orchestration & validation
<a name="orchestration-validation"></a>
+ **Dependency mapping:** Identifies cross-database references and relationships between applications and databases to create a modernization plan
+ **Human-in-the-loop (HITL) checkpoints:** Provides review and approval gates at critical stages
+ **Automated validation:** Tests schema compatibility, data integrity, and application functionality
+ **Functional equivalence validation:** Loads the target database into a container to validate functional equivalence between the source and converted database

### Deployment
<a name="deployment"></a>
+ **Aurora PostgreSQL cluster:** Deploy the converted PostgreSQL database to an Amazon Aurora cluster
+ **Deployment capabilities:** Deploy to an existing cluster, or let AWS Transform automatically create a new cluster

## Supported versions and project types
<a name="supported-versions-project-types"></a>

### SQL Server versions
<a name="sql-server-versions"></a>

AWS Transform supports the following SQL Server versions:


| SQL Server Version | Support Status | 
| --- | --- | 
| SQL Server 2022 | Supported | 
| SQL Server 2019 | Supported | 
| SQL Server 2017 | Supported | 
| SQL Server 2016 | Supported | 
| SQL Server 2014 | Supported | 
| SQL Server 2012 | Supported | 
| SQL Server 2008 R2 | Supported | 

### .NET versions
<a name="dotnet-versions"></a>


| .NET Version | Support Status | 
| --- | --- | 
| .NET 10 | Supported | 
| .NET 8 | Supported | 
| .NET 7 | Supported | 
| .NET 6 (Core) | Supported | 
| .NET Framework 4.x and earlier | Not Supported | 

**Important**  
Legacy .NET Framework 4.x and earlier versions are not supported. If your application uses .NET Framework, you must first upgrade to .NET Core 6\+ using AWS Transform for .NET modernization before using SQL Server transformation capabilities.

### Entity Framework versions
<a name="entity-framework-versions"></a>


| Framework | Supported Versions | 
| --- | --- | 
| Entity Framework 6 | 6.3, 6.4, 6.5 | 
| Entity Framework Core | 1.0 through 10.0 | 
| ADO.NET | All versions (GA) | 

### Source code repositories
<a name="source-code-repositories"></a>

AWS Transform supports the following source code platforms:
+ GitHub and GitHub Enterprise Server
+ Bitbucket Cloud and Bitbucket Data Center
+ Azure DevOps and Azure DevOps Server
+ Amazon S3
+ Direct upload of source code zip files

### Target database
<a name="target-database"></a>

AWS Transform targets Amazon Aurora PostgreSQL (PostgreSQL 15\+ compatible) with support for the latest Aurora features and optimizations.

### Technical requirements
<a name="technical-requirements"></a>

#### Database requirements
<a name="database-requirements"></a>
+ Microsoft SQL Server version 2008 R2 through 2022
+ Database user with VIEW DEFINITION and VIEW DATABASE STATE permissions
+ Database passwords using printable ASCII characters only (excluding '/', '@', '"', and spaces)

#### Application requirements
<a name="application-requirements"></a>
+ .NET 6, 7, 8, or 10 applications
+ Entity Framework 6.3-6.5 or Entity Framework Core 1.0-10.0, or ADO.NET
+ Database connections discoverable in source code
+ Applications successfully build and run
+ Source code in supported repository platforms

#### AWS account requirements
<a name="aws-account-requirements"></a>
+ AWS account with administrator access
+ IAM Identity Center enabled

### Data processing and storage
<a name="data-processing-storage"></a>

#### Processing location
<a name="processing-location"></a>
+ Transformation artifacts are stored in the AWS Transform service region

#### Stored artifacts
<a name="stored-artifacts"></a>

The following items are stored in the service region:
+ Agent logs
+ Assessment results
+ SQL schema files

**Important**  
**Important for Data Residency:** Metadata and processing artifacts are stored in the service region. This is important for organizations with strict data residency requirements.

#### Artifact management
<a name="artifact-management"></a>
+ Customer option for encryption using your own KMS keys
+ Defined TTL (time-to-live) period for all artifacts
+ Artifacts can be downloaded for offline storage

## Application requirements
<a name="source-application-requirements"></a>

### Legacy .NET Framework
<a name="legacy-dotnet-framework"></a>
+ **Limitation:** .NET Framework 4.x and earlier versions are not supported.
+ **Workaround:** Use AWS Transform for .NET to upgrade to .NET Core 6\+ first, then use SQL Server transformation.

### Entity Framework versions
<a name="entity-framework-version-requirements"></a>
+ **Limitation:** Only Entity Framework 6.3-6.5 and EF Core 1.0-10.0 are supported.
+ **Workaround:** Upgrade to a supported Entity Framework version before transformation.

### VB.NET applications
<a name="vbnet-applications"></a>
+ **Limitation:** VB.NET is not supported.
+ **Workaround:** Convert to C\# or use AWS Transform custom to convert from VB.NET to C\#.

### Cross-database dependencies
<a name="cross-database-dependencies"></a>
+ **Limitation:** Challenges when database schemas interact across multiple databases.
+ **Workaround:** Review and refactor cross-database queries before migration. Consider consolidating databases or using PostgreSQL schemas.
+ **Impact:** May require human intervention for complex cross-database scenarios.

### Repository-database coupling
<a name="repository-database-coupling"></a>
+ **Limitation:** Challenges when a single repository serves multiple databases.
+ **Workaround:** Consider repository restructuring or phased migration approach.
+ **Impact:** May require additional planning when a repository spans multiple databases.

## Infrastructure requirements
<a name="infrastructure-requirements"></a>

### Single account/region per job
<a name="single-account-region-per-job"></a>
+ **Limitation:** Each transformation job targets one AWS account and region.
+ **Workaround:** Create multiple transformation jobs for multi-account or multi-region deployments.

### Deployment targets
<a name="deployment-targets"></a>
+ **Limitation:** AWS Transform supports deploying to Amazon Aurora as the target only. Amazon RDS cluster creation is not supported.

## Repository requirements
<a name="repository-requirements"></a>

### Private NuGet packages
<a name="private-nuget-packages"></a>
+ **Limitation:** Private NuGet packages require additional configuration.
+ **Workaround:** Configure private NuGet feeds in transformation settings before starting the job.