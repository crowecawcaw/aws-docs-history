# Create SQL Server modernization job

## Connect database and source code repo

### Configure database connector

Establish secure connectivity to your SQL Server databases by configuring database connectors. The connector performs environment analysis, dependency discovery, and enables AWS Transform to access your database schemas and metadata for assessment and conversion.

**Actions to Complete:**

- Select **Configure Database Connector** from the setup
  wizard
- Choose connection method: **New Connection** or **Existing Connection**
- Provide SQL Server connection details (endpoint, port, database names)
- Configure authentication and test connectivity
- Review discovered databases and confirm selection

###### Note

**Network Connectivity:** Ensure your SQL Server security groups and NACLs allow inbound connections from AWS Transform service endpoints.

### Connect source code repository

Enable AWS Transform to access your .NET application source code through AWS CodeConnections. This integration allows the service to analyze your application code, identify database dependencies, and perform automated code transformations for PostgreSQL compatibility.

**Actions to Complete:**

- Navigate to **Connect Source Code Repository** section
- Select your source code platform (GitHub, GitLab, Bitbucket, CodeCommit)
- Configure AWS CodeConnections and authorize access
- Select repositories containing .NET applications
- Specify branch for analysis (typically main/master or development)
- Validate repository access and code structure

###### Note

**Repository Discovery:** AWS Transform automatically scans your repositories to identify .NET projects, Entity Framework configurations, database connection strings, and SQL dependencies.

###### Note

**Security Note:** AWS Transform only requires read access to your repositories and creates new feature branches for transformed code. Your main branch remains untouched.

## Human in the loop

AWS Transform uses human-in-the-loop (HITL) mechanisms to ensure quality and allow you to review and approve critical transformation decisions. The following checkpoints require your attention:

### Wave plan review and approval

**What you review:** The proposed migration waves, including which databases and applications are grouped together and the sequence of waves.

You can:

- Approve the wave plan
- Customize waves by moving databases between waves
- Modify wave sequence
- Split or merge waves

After approval, AWS Transform proceeds with schema conversion.

### Schema conversion review

**What you review:** Converted database objects including tables, stored procedures, functions, and triggers. Action items highlight objects that require attention.

You can:

- Accept converted code
- Modify converted code
- Flag for human review after transformation
- View side-by-side comparison of original and converted code

**What happens after approval:** AWS Transform applies the schema to Aurora PostgreSQL and proceeds with data migration (if configured).

### Application code review

**What you review:** All application code changes including Entity Framework configurations, connection strings, data access code, and stored procedure calls.

You can:

- Accept changes for each file
- Modify transformed code
- Reject changes (not recommended)
- Add comments for your team
- Download transformed code for local review

**What happens after approval:** AWS Transform commits the changes to a new branch in your repository and proceeds with validation.

### Validation results review

**What you review:** Automated validation results including schema compatibility, data integrity checks, and application build status.

You can:

- Review passed tests
- Investigate failed tests
- Address warnings
- Proceed to deployment or return to fix issues

**What happens after approval:** AWS Transform prepares for deployment to your target environment.

### Deployment approval

**What you review:** Deployment configuration including infrastructure-as-code templates, ECS service configuration, and deployment settings.

You can:

- Review and customize deployment settings
- Approve deployment to proceed
- Delay deployment for additional testing
- Download infrastructure code for review

After approval, AWS Transform deploys your modernized application and database to the target environment.

## Assessment and wave planning

### Set up landing zone

Configure the target infrastructure environment where your modernized applications will be deployed. The landing zone setup includes Aurora PostgreSQL provisioning, networking configuration, and reference deployment configurations.

**Actions to Complete:**

- Select **Set up Landing Zone** from the configuration menu
- Configure Aurora PostgreSQL target (version, instance class, Multi-AZ)
- Configure network and security settings (VPC, subnets, security groups)

###### Note

**Cost Consideration:** Aurora PostgreSQL instances incur ongoing costs. Consider using Aurora Serverless v2 for development/testing environments.

### Assessment

Conduct comprehensive analysis of your database schemas, application code, and dependencies. The assessment phase provides transformation complexity ratings, identifies potential challenges, and generates detailed reports.

**Actions to Complete:**

- Select Repository Branch for code analysis
- Select Repositories and Databases for transformation
- Review Assessment Results and complexity ratings
- Generate Assessment Report with effort projections
- Export report for stakeholder review and approval

###### Note

**Assessment Insights:** The assessment provides detailed analysis of schema objects, stored procedures, application dependencies, and estimates the level of human intervention required.

### Wave planning

Organize your modernization into manageable waves based on transformation complexity, business priorities, and application dependencies. AWS Transform generates intelligent wave recommendations that you can customize.

**Actions to Complete:**

- Review AI-Generated Wave Plan and recommendations
- Customize Wave Configuration based on business priorities
- Validate Dependencies between applications and databases
- Finalize Wave Plan using conversational interface
- Set wave execution priorities and assign responsibilities

###### Note

**AI-Powered Recommendations:** You can interact with the AI through natural language to adjust recommendations: 'Move CustomerDB to Wave 1' or 'Combine these two applications into the same wave.'

###### Note

**Best Practice:** Start with a pilot wave containing 1-2 low-complexity databases to establish processes and build team confidence.

## Data migration for each wave

### Schema conversion for each wave

Transform SQL Server database schemas to PostgreSQL-compatible equivalents using AI-enhanced conversion capabilities. This process converts tables, stored procedures, functions, triggers, and other database objects.

**Actions to Complete:**

- Provide Schema Conversion Targets and configure preferences
- Execute Automated Conversion using DMS Schema Conversion service
- Review Conversion Results and identify human intervention items
- Handle Manual Interventions through HITL prompts
- Validate human corrections and re-run conversion if needed

###### Note

**Common Manual Interventions:** Linked servers, user-defined types, advanced T-SQL patterns, and vendor-specific SQL features typically require human review and correction.

### Data migration for each wave

Transfer data from SQL Server to Aurora PostgreSQL using AWS Database Migration Service (AWS DMS) integration. Choose between production data migration or synthetic data generation for testing purposes.

**Actions to Complete:**

- Choose **Production Data Migration** or **Synthetic Data Generation**
- Configure DMS replication instance for data transfer
- Monitor migration progress and handle data inconsistencies
- Validate data integrity and referential constraints
- Confirm successful completion before proceeding

###### Note

**Automated DMS Integration:** AWS Transform abstracts the complexity of DMS configuration, automatically handling endpoint creation, task configuration, and data type mappings.

###### Note

**Data Validation:** The service performs empirical testing by running identical queries against both source and target databases to ensure data consistency.

## Code migration for each wave

Transform .NET application code to work with Aurora PostgreSQL, including Entity Framework configuration updates, connection string modifications, SQL query adaptations, and framework-specific adjustments.

**Actions to Complete:**

- Execute Automated Code Analysis for SQL Server dependencies
- Perform Framework Transformation (Entity Framework provider updates)
- Adapt SQL Query syntax to PostgreSQL-compatible SQL
- Configure Target Branch Management for transformed code
- Handle Manual Interventions for complex patterns
