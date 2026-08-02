# Upload DDL files (offline workflow)

In this workflow, AWS Transform modernizes your schema entirely from uploaded DDL files — no direct connection to your database is required. You run a provided extraction script against your SQL Server, upload the resulting schema files, and AWS Transform discovers, assesses, converts, and deploys the schema to Amazon Aurora PostgreSQL. Choose this workflow when your database cannot be exposed to a direct connection, or when you want a feasibility assessment and schema conversion before granting network access.

###### Important

The offline workflow converts and deploys your schema only. It does not migrate real data. Where available, you can generate synthetic test data to validate the target. If you need to migrate real data, use the AWS DMS console to create a new data migration project.

## Prerequisites for the offline workflow

- A supported SQL Server version (2008 R2 through 2022, all editions).
- **PowerShell 7 or later** to run the extraction script. PowerShell is pre-installed on Windows. On macOS or Linux, install PowerShell 7+ and run the script with `pwsh`. See the [Microsoft installation guide](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell "https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell").
- The `sqlcmd` utility available on the PATH. See [sqlcmd utility](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility "https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility").
- A SQL Server authentication login (username and password) with at least `VIEW SERVER STATE` and `VIEW ANY DEFINITION` permissions. The script does not support Windows or domain authentication.
- An AWS account for the later phases (creating the Aurora PostgreSQL target and deploying the converted schema), with IAM Identity Center or IAM authentication enabled.
- No inbound or outbound database connectivity to AWS is required for the schema analysis and conversion phases.

## Workflow steps

1. **Upload DDL files** — AWS Transform provides a download button for an extraction script in the chat. Download and run the script against your SQL Server. Optionally limit extraction to specific databases with a comma-separated include list (case-insensitive). The script produces a timestamped `.zip` of SQL DDL files. Upload the `.zip` (or individual `.sql` files) using the chat upload button.
2. **Discovery** — AWS Transform parses the uploaded files and catalogs the database objects (tables, stored procedures, views, triggers, indexes, constraints, sequences, and more), grouped by database. You review a per-database summary and choose which databases to assess. If some statements cannot be parsed, AWS Transform reports the issues and lets you continue with the objects that parsed, choose specific databases, or upload corrected files.
3. **Assessment** — AWS Transform evaluates conversion feasibility for the selected databases and produces a downloadable report with an executive summary, a per-database object summary, and a level-of-effort (LOE) estimate. Customize the LOE scores, upload additional files, or proceed to conversion.
4. **Schema conversion** — AWS Transform converts the SQL Server schema (including T-SQL stored procedures) to Aurora PostgreSQL, one database at a time. A single database converts automatically; with multiple databases, you choose which to convert. Databases convert independently and in parallel.
5. **Target provisioning** — For each converted database, AWS Transform creates or reuses an Amazon Aurora PostgreSQL cluster in your AWS account. You choose networking and target configuration through guided prompts.
6. **Schema deployment** — AWS Transform applies the converted schema to the Aurora cluster. After deployment, fix remaining objects in the chat or in an IDE, generate synthetic test data (where available), or finish.
7. **Application code modernization** (optional) — AWS Transform can update associated .NET 6+ applications to work with Aurora PostgreSQL. The service updates database connections in the source code and modifies ORM code in Entity Framework and ADO.NET to be compatible with Aurora PostgreSQL in a unified workflow with human supervision. Connect your source code repository using AWS CodeConnections or a Personal Access Token (PAT) for GitHub and GitLab, or provide an S3 URI for a zip file containing the source code.

###### Note

Amazon Aurora PostgreSQL is the only supported target engine for this workflow.

## Service limits for the offline workflow

The following default limits apply to the offline workflow. Some limits are configurable per account; contact your AWS account team to request an increase.

| Limit                          | Default                                                   | Applies to        |
| ------------------------------ | --------------------------------------------------------- | ----------------- |
| Upload size per job            | 1,024 MB (1 GB), cumulative across all uploads in the job | Upload DDL files  |
| Databases converted per month  | 10 per account                                            | Schema conversion |
| Stored procedures per database | 250                                                       | Schema conversion |
| Concurrent schema conversions  | 5 databases at a time                                     | Schema conversion |
| Concurrent running jobs        | 5                                                         | Per account       |

- The upload size limit is a per-job cumulative budget. If you reset input setup, the budget is cleared (this discards the files already uploaded and re-runs discovery and assessment within the same job).
- When you choose more than 5 databases for conversion, the additional databases are queued and start automatically as running conversions finish.
- Assessment is never blocked by the stored-procedure-per-database limit; only schema conversion is affected.

## Troubleshooting the offline workflow

### Extraction script

- **`pwsh: command not found` (macOS/Linux)** — PowerShell 7+ is not installed. Install it and run `pwsh ./ExtractDatabaseMetadata.ps1`.
- **Errors referencing `sqlcmd`** — The `sqlcmd` utility is not on the PATH. Install it and ensure it is on the PATH.
- **Login or permission errors** — Use a SQL Server authentication login with `VIEW SERVER STATE` and `VIEW ANY DEFINITION`. Windows/domain authentication is not supported.
- **Only some databases exported** — The include list narrowed the scope. Re-run without it, or specify the correct comma-separated database names.

### Upload

- **Upload rejected with a size message** — The per-job upload budget is exceeded. Upload a smaller file, or ask the agent to reset input setup to clear the budget within the same job. Ask the agent for the current remaining budget rather than estimating.
- **File not accepted** — Upload the `.zip` produced by the script, or individual `.sql` files. Zip multiple files into a single archive.

### Discovery

- **SQL syntax issues detected** — Download the issues report. Objects in error-free sections are still cataloged. Choose to continue with the parsed objects, choose specific databases, or upload corrected files.
- **Objects grouped under a generic name** — The parser could not find a `USE [Database]` statement. When prompted, provide the correct database name.
- **No objects found** — The files contained no `CREATE` statements, or all failed to parse. Re-upload valid DDL.

### Assessment

- **LOE estimates look off** — Choose to customize LOE scores, edit the template, and re-upload to regenerate the assessment.
- **Missed objects** — Choose to upload additional SQL files; discovery and assessment re-run automatically.

### Schema conversion

- **A database conversion fails** — AWS Transform reports the reason. Reply asking to retry; conversion restarts for that database.
- **A response goes to the wrong database** — When multiple databases are awaiting input, specify which database your message is for. You can address a specific database with `@DatabaseName:`.

### Target provisioning and deployment

- **Cannot create the Aurora cluster** — Complete the guided credential and networking prompts, and ensure the account has permission to create Aurora PostgreSQL.
- **Some objects did not deploy** — Use the post-deployment options to fix remaining objects in the chat or in an IDE, then redeploy.
