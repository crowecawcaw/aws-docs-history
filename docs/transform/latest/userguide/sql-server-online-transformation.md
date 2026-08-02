# Connect to database (online workflow)

In this workflow, AWS Transform connects directly to your source SQL Server and uses AWS Database Migration Service (DMS) to convert the schema and migrate data to Amazon Aurora PostgreSQL. This is the standard end-to-end workflow when a live database connection is available.

The workflow proceeds through the following phases:

1. **Prerequisites** — AWS Transform confirms the DMS prerequisites are in place (IAM roles, secrets, and network access to the source database).
2. **Connect** — You provide connection details, and AWS Transform establishes a connection to the source database.
3. **Validate** — AWS Transform validates connectivity and permissions.
4. **Discovery and assessment** — AWS Transform discovers the databases on the server, you choose which to modernize, and AWS Transform assesses them.
5. **Per-database transformation** — For each selected database, AWS Transform provisions an Aurora PostgreSQL target, converts the schema, and migrates data. Choose to migrate real data, generate synthetic data, or skip data migration.
6. **Code assessment and transformation** (optional) — If a source code repository is connected, AWS Transform assesses and transforms the associated .NET application.
7. **Deploy** (optional) — AWS Transform deploys the transformed application.

###### Note

This workflow migrates your real data using AWS DMS. Ensure the network and IAM prerequisites are satisfied before you begin. See the technical requirements in the preceding section.

## Application requirements

### Legacy .NET Framework

- **Limitation:** .NET Framework 4.x and earlier versions are not supported.
- **Workaround:** Use AWS Transform for .NET to upgrade to .NET Core 6+ first, then use SQL Server transformation.

### Entity Framework versions

- **Limitation:** Only Entity Framework 6.3-6.5 and EF Core 1.0-10.0 are supported.
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
