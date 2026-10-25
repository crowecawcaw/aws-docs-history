

# Setting up source code connector and HITL review
<a name="sql-server-source-connector-hitl"></a>



## Connect source code repository
<a name="sql-server-connect-database-repo"></a>

### Connect source code repository
<a name="sql-server-connect-source-code"></a>

Enable AWS Transform to access your .NET application source code. AWS Transform supports three methods for providing source code: a Personal Access Token (PAT) connector (recommended), AWS CodeConnections, or Amazon S3. This integration allows the service to analyze your application code, identify database dependencies, and perform automated code transformations for PostgreSQL compatibility.

**Actions to Complete:**
+ Navigate to **Connect Source Code Repository** section
+ Choose your authentication method: **PAT Connector** (recommended), **AWS CodeConnections**, or **Amazon S3**
+ Select repositories containing .NET applications
+ Specify branch for analysis (typically main/master or development)
+ Validate repository access and code structure

**Note**  
**Repository Discovery:** AWS Transform automatically scans your repositories to identify .NET projects, Entity Framework configurations, database connection strings, and SQL dependencies.

**Note**  
**Security Note:** AWS Transform only requires read access to your repositories and creates new feature branches for transformed code. Your main branch remains untouched.

## Human in the loop
<a name="human-in-the-loop"></a>

AWS Transform uses human-in-the-loop (HITL) mechanisms to ensure quality and allow you to review and approve critical transformation decisions. The following checkpoints require your attention:

### Customized transformation plan
<a name="customized-transformation-plan"></a>

**What you review:** The proposed transformation plan, including the job steps AWS Transform will run (such as synthetic data generation and application code conversion), data type mappings, transformation rules, and deployment options.

You can:
+ View and edit the job steps, such as synthetic data generation and application code conversion
+ Edit custom data type mappings, for example mapping `BIT` to `BOOLEAN` instead of `NUMERIC`
+ Set custom rules for the transformation
+ Set deployment options, such as creating a new Aurora PostgreSQL cluster or deploying to an existing cluster

After you approve the plan, AWS Transform proceeds with schema conversion. For details about each part of the plan you can edit, see [Custom transformation plan](sql-server-custom-transformation-plan.md).

### Schema conversion review
<a name="schema-conversion-review"></a>

**What you review:** Converted database objects including tables, stored procedures, functions, and triggers. Action items highlight objects that require attention.

You can:
+ Accept converted code
+ Modify converted code
+ Flag for human review after transformation
+ View side-by-side comparison of original and converted code

**What happens after approval:** AWS Transform applies the schema to Aurora PostgreSQL. You can then optionally generate synthetic test data to validate the converted database.

### Application code review
<a name="application-code-review"></a>

**What you review:** All application code changes including Entity Framework configurations, connection strings, data access code, and stored procedure calls.

You can:
+ Accept changes for each file
+ Modify transformed code
+ Reject changes (not recommended)
+ Add comments for your team
+ Download transformed code for local review

**What happens after approval:** AWS Transform commits the changes to a new branch in your repository and proceeds with validation.

### Validation results review
<a name="validation-results-review"></a>

**What you review:** Automated validation results including schema compatibility, data integrity checks, and application build status.

You can:
+ Review passed tests
+ Investigate failed tests
+ Address warnings
+ Proceed to deployment or return to fix issues

**What happens after approval:** AWS Transform prepares to deploy the converted database to the target Aurora PostgreSQL cluster.

### Deployment approval
<a name="deployment-approval"></a>

**What you review:** The target Aurora PostgreSQL cluster and the database deployment settings.

You can:
+ Review and customize the database deployment settings
+ Approve deployment to proceed
+ Delay deployment for additional testing

After approval, AWS Transform deploys the converted database to the target Aurora PostgreSQL cluster you provided. AWS Transform deploys the database only; it does not deploy your application.