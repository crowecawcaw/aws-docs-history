

# SQL Server modernization workflow
<a name="sql-server-modernization-workflow"></a>

This section provides a step-by-step walkthrough of the complete SQL Server modernization process using AWS Transform.

## Step 1: Create SQL Server modernization job
<a name="step-1-create-job"></a>

Begin your modernization journey by creating a new transformation job in the AWS Transform console.

1. Sign in to the AWS Transform console

1. Choose **Create modernization job**

1. Select **Windows modernization **job and then select **SQL Server modernization**

1. Enter job details:
   + **Job name**: Descriptive name for your project
   + **Description**: Optional description
   + **Target region**: AWS region for deployment

1. Choose **Create job**
**Important**  
Do not include personally identifiable information (PII) in your job name.

## Step 2: Connect to SQL Server database
<a name="step-2-connect-sql-server"></a>

Connect AWS Transform to your SQL Server database to enable schema analysis and conversion.

### Create a database connector
<a name="create-database-connector"></a>

1. In your SQL Server modernization job, navigate to Connect to resources

1. Choose **Connect to SQL Server database**

1. Choose **Create new connector**

1. Enter the connector information:
   + C**onnector name**: Descriptive name
   + **AWS account ID**: Account where SQL Server is hosted

1. Once confirmed, you will receive a link for approval. Copy the approval link to get approval from your AWS admin for the account. Once they have approved, you can proceed to the next step.

1. After your administrator has approved the connector request, click Submit to proceed to the source code connection setup.

## Step 3: Connect source code repository
<a name="step-3-connect-source-code"></a>

AWS Transform needs access to your .NET application source code to analyze and transform the code that interacts with your SQL Server database. AWS Transform supports three methods for providing source code.

### Choose your authentication method
<a name="authentication-methods-overview"></a>

Personal Access Token (PAT) connector (recommended)  
Best for teams that need custom permission scopes, self-hosted provider support, or access to provider-specific APIs such as GitHub Secrets. You create a PAT in your source code provider with custom permissions, store it in AWS Secrets Manager, and AWS Transform retrieves it when needed. You are responsible for managing token rotation and expiration.

AWS CodeConnections  
Best for teams that want automated credential management. AWS CodeConnections uses a managed provider integration that handles authentication through an OAuth 2.0 authorization flow. AWS manages the entire credential lifecycle, including automatic token refresh and rotation. No manual credential management is required.

Amazon S3  
Upload your source code directly to an Amazon S3 bucket. AWS Transform accesses the code from the bucket during the transformation job.


| Feature | PAT connector (recommended) | AWS CodeConnections | 
| --- | --- | --- | 
| Credential management | Manual (customer-managed) | Automatic (AWS-managed) | 
| Token lifecycle | Manual rotation required | Automatic refresh | 
| Permission flexibility | Fully customizable scopes | Fixed permissions | 
| Self-hosted provider support | Supported | Not available | 
| Setup complexity | Moderate (manual token creation and storage) | Low (one-time authorization) | 
| Token storage | Customer's AWS Secrets Manager | AWS-managed | 

### Set up a PAT connector (recommended)
<a name="setup-pat-connector"></a>

With a PAT connector, you create a Personal Access Token in your source code provider with custom permissions, store it securely in AWS Secrets Manager, and AWS Transform retrieves it when needed. You are responsible for managing the token lifecycle including rotation and expiration. AWS Transform automatically creates the necessary IAM role with permissions to access your secret.

PAT connector supports the following providers, including self-hosted and custom DNS/URL versions:
+ GitHub and GitHub Enterprise Server
+ GitLab.com and GitLab Self-Managed
+ Bitbucket Cloud and Bitbucket Data Center
+ Azure DevOps and Azure DevOps Server

#### Create a Personal Access Token
<a name="pat-step-1-create-token"></a>

Create a PAT in your source code provider. The required permissions vary by provider. Choose the tab for your provider.

**Important**  
Copy the token immediately after creation. You cannot view it again. Set the expiration for the duration of the transformation job. Do not set the expiration to never expire.

**Warning**  
Never commit PAT tokens to code repositories or share them through insecure channels. Always store them in AWS Secrets Manager.

##### GitHub
<a name="pat-github-permissions"></a>

Navigate to **Settings**, **Developer settings**, **Personal access tokens**, **Fine-grained tokens**. Select the repositories to transform and grant the following permissions.

**Repository permissions**


| Permission | Access | Purpose | 
| --- | --- | --- | 
| Contents | Read and write | Reads source code and writes transformed code back to repository | 
| Metadata | Read-only | Accesses basic repository information | 

**Organization permissions (required for organization repositories)**


| Permission | Access | Purpose | 
| --- | --- | --- | 
| Members | Read-only | Lists organizations accessible to the token for repository discovery | 

##### GitLab
<a name="pat-gitlab-permissions"></a>

Navigate to **Edit Profile**, **Access Tokens**. Select the following scopes.


| Scope | Purpose | 
| --- | --- | 
| read\_api | Reads repository metadata, project information, user details, and lists groups and branches | 
| read\_repository | Reads source code files and repository structure for analysis | 
| write\_repository | Writes transformed code back to repository | 

##### Bitbucket
<a name="pat-bitbucket-permissions"></a>

Navigate to **Account settings**, **Security**, **Create and manage API Tokens**. The required scopes depend on your token type.

**Workspace/Repository Token (ATCT — Bearer auth, no username required)**


| Permission | Access | Purpose | 
| --- | --- | --- | 
| Repositories | Read and write | Lists repos, reads branches, and writes transformed code via git push | 

**Account API Token (ATAT — Basic auth with email) or App Password (ATBB — Basic auth with username)**


| Scope | Purpose | 
| --- | --- | 
| read:account | Identifies the authenticated user to resolve repository membership | 
| read:workspace:bitbucket | Lists the workspaces the token can access so AWS Transform can enumerate their repositories. Not required if you specify a workspaces list in the secret. | 
| read:repository:bitbucket | Lists repositories and reads metadata and branch information | 
| write:repository:bitbucket | Writes transformed code back to repository via git push | 

##### Azure DevOps
<a name="pat-ado-permissions"></a>

Navigate to **User settings**, **Personal access tokens**. Select **Custom defined** scopes. For organization scope, choose **All accessible organizations** (recommended) or specify a single organization.


| Scope | Access | Purpose | 
| --- | --- | --- | 
| Code | Read & write | Reads source code, lists repositories and branches, and writes transformed code back | 
| User Profile | Read | Validates token access and discovers user identity for organization lookup | 
| Member Entitlement Management | Read | Lists organizations accessible to the token for repository discovery | 

#### Store the PAT in AWS Secrets Manager
<a name="pat-step-2-store-secret"></a>

1. Open the AWS Secrets Manager console.

1. Choose **Store a new secret**.

1. For **Secret type**, choose **Other type of secret**.

1. Add key-value pairs based on your provider and hosting type:
   + **Cloud-hosted providers** — Add a key named `token` with your PAT as the value.
     + For Azure DevOps with a specific organization, also add a key named `organization` with your organization name.
     + For Bitbucket app passwords (ATBB), also add a key named `username` with your Bitbucket username. For Bitbucket account API tokens (ATAT), add a key named `email` with your Bitbucket email address.
   + **Self-hosted and custom DNS/URL providers** — Add the following keys: `host` (your server URL, for example `https://github.mycompany.com`), `provider_type` (`github`, `gitlab`, `bitbucket`, or `ado`), and `token` (your PAT).
     + For Azure DevOps with a specific organization, also add a key named `organization` with your organization name.
     + For Bitbucket app passwords (ATBB), also add a key named `username` with your Bitbucket username. For Bitbucket account API tokens (ATAT), add a key named `email` with your Bitbucket email address.

   The following example shows how a secret looks in AWS Secrets Manager for a GitHub cloud-hosted provider:

   ```
   {
     "token": "{{your-github-personal-access-token}}"
   }
   ```

   The following example shows a Bitbucket app password (ATBB):

   ```
   {
     "token": "{{your-bitbucket-app-password}}",
     "username": "my-bitbucket-username"
   }
   ```

   The following example shows a self-hosted GitLab instance:

   ```
   {
     "host": "https://gitlab.mycompany.com",
     "provider_type": "gitlab",
     "token": "{{your-gitlab-personal-access-token}}"
   }
   ```

1. Choose **Next**.

1. Enter a secret name, for example `github-pat-myproject`.

1. (Optional) Select a customer-managed KMS key for encryption.

1. Complete the wizard and choose **Store**.

1. Copy the Secret ARN. You need this value when you configure the AWS Transform job.

If you use a customer-managed KMS key to encrypt your secret (instead of the default AWS-managed key), you must update the KMS key policy to allow AWS Transform to decrypt the secret. Add the following statement to your customer-managed KMS key policy:

```
{
  "Sid": "Allow AWS Transform to decrypt secrets",
  "Effect": "Allow",
  "Principal": {
    "Service": "transform.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "secretsmanager.{{REGION}}.amazonaws.com",
      "kms:EncryptionContext:SecretARN": "{{YOUR-SECRET-ARN}}"
    }
  }
}
```

Replace {{REGION}} with your AWS Region (for example, `us-east-1`) and {{YOUR-SECRET-ARN}} with the ARN of your secret. The `kms:ViaService` condition ensures the KMS key can only be used through the AWS Secrets Manager service. The `kms:EncryptionContext:SecretARN` condition restricts decryption to your specific secret.

To update your KMS key policy:

1. Open the AWS KMS console at `https://console.aws.amazon.com/kms`.

1. In the navigation pane, choose **Customer managed keys**.

1. Select your KMS key.

1. On the **Key policy** tab, choose **Edit**.

1. Add the policy statement to the existing policy.

1. Choose **Save changes**.

**Note**  
If you use the default AWS-managed key (`aws/secretsmanager`), you do not need to modify any KMS key policy.

#### Configure the AWS Transform job
<a name="pat-step-3-configure-job"></a>

1. In your AWS Transform job, navigate to **Connect to resources**.

1. Choose **Connect source code repository**.

1. Select **PAT Connector** as the authentication method.

1. Enter the Secret ARN from Step 2.

1. (Optional) Enter the KMS Key ARN if you used a customer-managed KMS key.

1. Select your repository and branch.

1. Choose **Continue**.

AWS Transform automatically creates an IAM role with the permissions required to access your secret.

#### Token rotation and maintenance
<a name="pat-token-rotation"></a>

You are responsible for rotating PAT tokens before they expire. To rotate a token:

1. Generate a new PAT in your source code provider with the same permissions.

1. Update the secret value in AWS Secrets Manager.

1. Verify that your AWS Transform job can access the repository with the new token.

1. Revoke the old PAT in your source code provider.

#### Troubleshoot PAT connector issues
<a name="pat-troubleshooting"></a>

Access Denied — Invalid PAT  
Verify that the PAT has not expired. Confirm that the PAT has the required scopes for your provider. Check that the PAT is correctly stored in AWS Secrets Manager.

Cannot retrieve secret  
Verify that the Secret ARN is correct. Check the job logs to confirm that AWS Transform created the IAM role. If you are using a customer-managed KMS key, verify the key policy.

Insufficient permissions  
The PAT might lack the required scopes for the operation. Regenerate the PAT with the required scopes and update the secret value in AWS Secrets Manager.

### Set up AWS CodeConnections
<a name="setup-codeconnections"></a>

AWS CodeConnections uses a managed provider integration that automatically retrieves temporary OAuth credentials through an OAuth 2.0 authorization flow. Permissions are configured in the provider app and managed entirely by AWS. You authorize the app once, and AWS handles all credential management.

1. In your SQL Server modernization job, navigate to **Connect to resources**.

1. Choose **Connect source code repository**.

1. If you don't have an existing connection, choose **Create connection**.

1. Select your repository provider:
   + GitHub / GitHub Enterprise
   + GitLab.com
   + Bitbucket Cloud
   + Azure Repositories

1. Follow the authorization flow for your provider.

1. After authorization, choose **Connect**.

### Select your repository and branch
<a name="select-repository-branch"></a>

1. Select your repository from the list.

1. Choose the branch you want to transform (typically main, master, or develop).

1. (Optional) Specify a subdirectory if your .NET application is not in the repository root.

1. Choose **Continue**.

**Note**  
AWS Transform creates a new branch for the transformed code. You can review and merge the changes through your normal code review process.

### Repository access approval
<a name="repository-access-approval"></a>

For GitHub and some other platforms, the repository administrator must approve the connection request:

1. AWS Transform displays a verification link.

1. Share this link with your repository administrator.

1. The administrator reviews and approves the request in their repository settings.

1. After the administrator approves the request, the connection status changes to *Approved*.

**Important**  
The approval process can take time depending on your organization's policies. Plan accordingly.

## Step 4: Create deployment connector (optional)
<a name="step-4-create-deployment-connector"></a>

If you want to deploy the transformed applications into your AWS account, you have the option to select a deployment connector.

### Set up deployment connector
<a name="setup-deployment-connector"></a>

1. Select **Yes** if you want to deploy your applications. Selecting **No** will skip this step.

1. Add your AWS account where you want to deploy the transformed applications.

1. Add a name that helps you remember the connector easily

1. Submit the connector request for approval.

### Deployment connector approval
<a name="deployment-connector-approval"></a>

Your AWS account administrator must approve the connection request for deployment connector.

1. AWS Transform displays a verification link

1. Share this link with your AWS account administrator

1. The administrator reviews and approves the request in their repository settings

1. Once approved, the connection status changes to *Approved*

**Important**  
The approval process can take time depending on your organization's policies. Plan accordingly.

## Step 5: Confirm your resources
<a name="step-5-confirm-resources"></a>

After connecting to your database and repository, AWS Transform verifies that all required resources are accessible and ready for transformation.

### What AWS Transform verifies
<a name="what-trn-verifies"></a>
+ **Database connectivity:** Connection is active, user has required permissions, databases are accessible, version is supported
+ **Repository access:** Repository is accessible, branch exists, .NET project files detected, database connections discoverable
+ **Environment readiness:** VPC configuration supports DMS, required AWS service roles exist, network connectivity established, region compatibility confirmed

### Review the pre-flight checklist
<a name="review-preflight-checklist"></a>

1. Navigate to **Confirm your resources** in the job plan

1. Review the checklist items:
   + ✅ Database connection verified
   + ✅ Repository access confirmed
   + ✅ .NET version supported
   + ✅ Entity Framework or ADO.NET detected
   + ✅ Network configuration valid
   + ✅ Required permissions granted

1. If all items show as complete, choose Continue

1. If any items show warnings or errors, address them before proceeding

## Step 6: Discovery and assessment
<a name="step-6-discovery-assessment"></a>

AWS Transform analyzes your SQL Server database and .NET application to understand the scope and complexity of the modernization.

### What gets discovered
<a name="what-gets-discovered"></a>
+ **Database objects:** Tables, views, indexes, stored procedures, functions, triggers, constraints, data types, computed columns, identity columns, foreign key relationships
+ **Application code:** .NET project structure, Entity Framework models and configurations, ADO.NET data access code, database connection strings, stored procedure calls, SQL queries in code
+ **Dependencies:** Which applications use which databases, cross-database dependencies, shared stored procedures, common data access patterns

### Discovery process
<a name="discovery-process"></a>
+ AWS Transform begins discovery automatically after resource confirmation
+ Discovery typically takes 5-15 minutes depending on database size and application complexity
+ Monitor progress in the worklog
+ AWS Transform displays real-time updates as objects are discovered

### Review discovery results
<a name="review-discovery-results"></a>

After discovery completes, navigate to **Discovery and assessment **to review:

**Database Analysis:**
+ **Object count**: Number of tables, views, stored procedures, functions, triggers
+ **Complexity score**: Assessment of transformation complexity (Low, Medium, High)
+ **Action items**: Objects that may require human attention
+ **Supported features**: Database features that will convert automatically
+ **Unsupported features**: Features that require workarounds

**Application Analysis:**
+ **Project type**: ASP.NET Core, Console App, Class Library, etc.
+ **.NET version**: Detected .NET Core version
+ **Data access framework**: Entity Framework version or ADO.NET
+ **Database connections**: Number of connection strings found
+ **Code complexity**: Assessment of transformation complexity

**Dependency Map:**
+ Visual representation of application-to-database relationships
+ Cross-database dependencies
+ Shared components

### Understanding complexity assessment
<a name="understanding-complexity-assessment"></a>

AWS Transform classifies your modernization into three categories:


| Complexity | Characteristics | Expected Outcome | 
| --- | --- | --- | 
| Low (Class A) | Standard SQL patterns (ANSI SQL), simple stored procedures, basic data types, Entity Framework with standard configurations | Minimal human intervention expected, high automation success rate | 
| Medium (Class B) | Advanced T-SQL patterns, complex stored procedures with business logic, user-defined functions, computed columns | Some human intervention required, expert review recommended | 
| High (Class C) | CLR assemblies, linked servers, Service Broker, complex full-text search | Significant human refactoring required, consider phased approach | 

### Assessment report
<a name="assessment-report"></a>

AWS Transform generates a detailed assessment report that includes:
+ Executive summary with high-level overview
+ Complete database inventory
+ Application inventory
+ Transformation readiness percentage
+ Effort estimation
+ Risk assessment and mitigation strategies
+ Recommended approach

You can download the assessment report for offline review and sharing with stakeholders.

## Step 7: Generate and review wave plan
<a name="step-7-wave-plan"></a>

For large estates with multiple databases and applications, AWS Transform generates a wave plan that sequences the modernization in logical groups.

### What is a wave plan?
<a name="what-is-wave-plan"></a>

A wave plan organizes your modernization into phases (waves) based on:
+ Dependencies between databases and applications
+ Business priorities
+ Risk tolerance
+ Resource availability
+ Technical complexity

Each wave contains a group of databases and applications that can be modernized together without breaking dependencies.

### Review the wave plan
<a name="review-wave-plan"></a>

1. Navigate to **Wave planning** in the job plan

1. Review the proposed waves

1. For each wave, review:
   + Databases included
   + Applications included
   + Dependencies on other waves
   + Estimated transformation time
   + Complexity level
   + Deployable applications

### Customize the wave plan
<a name="customize-wave-plan"></a>

You can customize the wave plan to match your business needs in 2 ways:

**Using JSON:**

1. Choose **Download all waves** to get a JSON file with all the waves

1. Modify waves in the JSON by:
   + Moving databases between waves
   + Splitting waves into smaller groups
   + Merging waves together
   + Changing wave sequence
   + Adding or removing databases from scope

1. Upload the JSON file back to the console by choosing **Upload wave plan**

1. AWS Transform validates your changes and warns if dependencies are violated

1. Choose **Confirm waves** to update the wave plan

**Using Chat:**

You can modify the wave plans by chatting with the agent and asking it to move the repositories and databases to specific waves. This approach works well if you need to make minor edits to the waves.

**Important**  
Ensure that dependencies are respected when customizing waves. Transforming a dependent application before its database can cause issues.

### Single database modernization
<a name="single-database-modernization"></a>

If you're modernizing a single database and application, AWS Transform creates a simple plan with one wave. You can proceed directly to transformation without wave planning.

### Approve the wave plan
<a name="approve-wave-plan"></a>

1. After reviewing and customizing (if needed), choose **Approve wave plan**

1. AWS Transform locks the wave plan and proceeds to transformation

1. You can still modify the plan later by choosing **Edit wave plan**

## Step 8: Schema conversion
<a name="step-8-schema-conversion"></a>

AWS Transform converts your SQL Server database schema to Aurora PostgreSQL, including tables, views, stored procedures, functions, and triggers.

### How schema conversion works
<a name="how-schema-conversion-works"></a>

AWS Transform uses AWS DMS Schema Conversion enhanced with generative AI to:
+ Analyze SQL Server schemas and relationships
+ Map data types from SQL Server to PostgreSQL equivalents
+ Transform T-SQL to PL/pgSQL
+ Handle identity columns, computed columns, and constraints
+ Validate conversion and referential integrity
+ Generate action items for objects requiring human review

### Supported conversions
<a name="supported-conversions"></a>

**Automatically converted:**
+ Tables, views, and indexes
+ Primary keys and foreign keys
+ Check constraints and default values
+ Most common data types
+ Simple stored procedures
+ Basic functions and triggers
+ Identity columns (converted to SERIAL or GENERATED)
+ Most computed columns

**May require human review:**
+ Complex stored procedures with advanced T-SQL
+ SQL Server-specific functions (GETUTCDATE, SUSER\_SNAME, etc.)
+ Computed columns with complex expressions
+ Full-text search indexes
+ XML data type operations
+ HIERARCHYID data type (requires ltree extension)

**Not automatically converted:**
+ CLR assemblies
+ Linked servers
+ Service Broker
+ SQL Server Agent jobs

### Start schema conversion
<a name="start-schema-conversion"></a>

1. Navigate to Schema conversion in the job plan

1. Review the conversion settings:
   + Target PostgreSQL version
   + Extension options (ltree, PostGIS, etc.)
   + Naming conventions

1. Choose **Start conversion**

1. Monitor progress in the worklog

1. Conversion typically takes 10-30 minutes depending on the number of database objects

### Review conversion results
<a name="review-conversion-results"></a>

After conversion completes, navigate to Review schema conversion:

**Conversion Summary:**
+ **Objects converted**: Count of successfully converted objects
+ **Action items**: Objects requiring human attention
+ **Warnings**: Potential issues to review
+ **Errors**: Objects that could not be converted

**Review by Object Type:**
+ **Tables**: Data type mappings, constraints, indexes
+ **Stored procedures**: T-SQL to PL/pgSQL conversion
+ **Functions**: Function signature and logic changes
+ **Triggers**: Trigger syntax and timing changes

### Review action items
<a name="review-action-items"></a>

1. Choose **View action items**

1. For each action item, review:
   + **Object name**: The database object
   + **Issue type**: What requires attention
   + **Severity**: Critical, Warning, or Info
   + **Recommendation**: Suggested resolution
   + **Original code**: SQL Server version
   + **Converted code**: PostgreSQL version

1. For each action item, you can:
   + **Accept**: Use the converted code
   + **Modify**: Edit the converted code
   + **Flag for later**: Mark for human review after transformation

### Example: Stored procedure conversion
<a name="example-stored-procedure-conversion"></a>

SQL Server T-SQL:

```
CREATE PROCEDURE GetProductsByCategory
    @CategoryId INT,
    @PageSize INT = 10
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT TOP (@PageSize)
        ProductId,
        Name,
        Price,
        DATEDIFF(DAY, CreatedDate, GETUTCDATE()) AS DaysOld
    FROM Products
    WHERE CategoryId = @CategoryId
    ORDER BY Name
END
```

Converted PostgreSQL PL/pgSQL:

```
CREATE OR REPLACE FUNCTION get_products_by_category(
    p_category_id INTEGER,
    p_page_size INTEGER DEFAULT 10
)
RETURNS TABLE (
    product_id INTEGER,
    name VARCHAR(255),
    price NUMERIC(18,2),
    days_old INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        p.product_id,
        p.name,
        p.price,
        EXTRACT(DAY FROM (NOW() - p.created_date))::INTEGER AS days_old
    FROM products p
    WHERE p.category_id = p_category_id
    ORDER BY p.name
    LIMIT p_page_size;
END;
$$ LANGUAGE plpgsql;
```

Changes made:
+ Procedure converted to function returning TABLE
+ Parameter names prefixed with p\_
+ TOP converted to LIMIT
+ DATEDIFF converted to EXTRACT
+ GETUTCDATE() converted to NOW()
+ Column names converted to lowercase (PostgreSQL convention)

### Approve schema conversion
<a name="approve-schema-conversion"></a>

1. After reviewing all action items and making necessary modifications

1. Choose **Approve schema conversion**

1. AWS Transform prepares the converted schema for deployment to Aurora PostgreSQL

**Note**  
You can download the converted schema as SQL scripts for offline review or version control.

## Step 9: Data migration (optional)
<a name="step-9-data-migration"></a>

AWS Transform provides options for migrating data from SQL Server to Aurora PostgreSQL. Data migration is optional and can be skipped if you only need schema and code transformation.

### Data migration options
<a name="data-migration-options"></a>

**Option 1: Production Data Migration**

Migrate your actual production data using AWS DMS:
+ Full initial load of all data
+ Continuous replication during testing (CDC)
+ Minimal downtime cutover
+ Data validation and integrity checks

**Option 2: Skip Data Migration**

Transform schema and code only:
+ Useful for development/testing environments
+ When data will be migrated separately
+ For proof-of-concept projects

### Configure data migration
<a name="configure-data-migration"></a>

1. Navigate to **Data migration** in the job plan

1. Choose your migration option:
   + **Migrate production data**
   + **Skip data migration**

1. If migrating production data, configure:
   + **Migration type**: Full load, or Full load \+ CDC
   + **Validation**: Enable data validation
   + **Performance**: DMS instance size
   + Choose **>Start migration**

### Production data migration process
<a name="production-data-migration-process"></a>

If you choose to migrate production data:

1. **Initial sync**: AWS DMS performs full load of all tables

1. **Continuous replication**: (If CDC enabled) Keeps data synchronized

1. **Validation**: Verifies row counts and data integrity

1. **Cutover preparation**: Prepares for final synchronization

Migration Timeline:
+ Small databases (< 10 GB): 30 minutes - 2 hours
+ Medium databases (10-100 GB): 2-8 hours
+ Large databases (> 100 GB): 8\+ hours

### Data validation
<a name="data-validation"></a>

AWS Transform validates migrated data with the following checks:
+ Row count comparison (source vs target)
+ Primary key integrity
+ Foreign key relationships
+ Data type compatibility
+ Computed column results
+ Null value handling

## Step 10: Application code transformation
<a name="step-10-application-code-transformation"></a>

AWS Transform transforms your .NET application code to work with Aurora PostgreSQL instead of SQL Server. It asks for a target branch name in your repositories to commit the transformed source code. Once you enter the branch name, AWS Transform will create a new branch and initiate the transformation to match the PostgreSQL database.

### What gets transformed
<a name="what-gets-transformed"></a>

**Entity Framework Changes:**
+ **Database provider**: UseSqlServer() → UseNpgsql()
+ **Connection strings**: SQL Server format → PostgreSQL format
+ **Data type mappings**: SQL Server types → PostgreSQL types
+ **DbContext configurations**: SQL Server-specific → PostgreSQL-specific
+ **Migration files**: Updated for PostgreSQL compatibility

**ADO.NET Changes:**
+ **Connection classes**: SqlConnection → NpgsqlConnection
+ **Command classes**: SqlCommand → NpgsqlCommand
+ **Data reader**: SqlDataReader → NpgsqlDataReader
+ **Parameters**: SqlParameter → NpgsqlParameter
+ S**QL syntax**: T-SQL → PostgreSQL SQL

**Configuration Changes:**
+ Connection strings in appsettings.json
+ Database provider NuGet packages
+ Dependency injection configurations
+ Startup/Program.cs configurations

### Start code transformation
<a name="start-code-transformation"></a>

1. Navigate to Application transformation in the job plan

1. Review the transformation settings:
   + **Target .NET version** (if upgrading)
   + **PostgreSQL provider version**
   + **Code style preferences**

1. Choose **Start transformation**

1. Monitor progress in the worklog

1. Transformation typically takes 15-45 minutes depending on codebase size

## Step 11: Review transformation results
<a name="step-11-review-transformation-results"></a>

Before proceeding to deployment, review the complete transformation results to ensure everything is ready for testing.

You can download the transformed code from the repository branch for:
+ Local testing and validation
+ Code review in your IDE
+ Integration with your CI/CD pipeline
+ Version control commit

You can also download the transformation summary to review the natural language changes that are made by AWS Transform as part of the transformation.

### Transformation summary
<a name="transformation-summary"></a>

1. Navigate to **Transformation summary** in the job plan

1. Review the overall results:
   + **Schema conversion**: Objects converted, action items, warnings
   + **Data migration**: Tables migrated, rows transferred, validation status
   + **Code transformation**: Files changed, lines modified, issues resolved
   + **Readiness score**: Overall readiness for deployment

### Generate transformation report
<a name="generate-transformation-report"></a>

AWS Transform generates a comprehensive transformation report:

1. Choose **Generate report**

1. Select report type:
   + **Executive summary**: High-level overview for stakeholders
   + **Technical details**: Complete transformation documentation
   + **Action items**: List of human tasks required

1. Choose **Download report**

The report includes:
+ Transformation scope and objectives
+ Objects and code transformed
+ Issues encountered and resolutions
+ Validation results
+ Deployment readiness assessment
+ Recommendations for testing

## Step 12: Validation and testing
<a name="step-12-validation-testing"></a>

Before deploying to production, validate that the transformed application works correctly with Aurora PostgreSQL.

### Validation types
<a name="validation-types"></a>

**Automated Validation:** AWS Transform performs automated checks:
+ Schema validation against source database
+ Data integrity verification
+ Query equivalence testing
+ Connection string validation
+ Configuration validation

**Human Validation:** You should perform additional testing:
+ Functional testing of application features
+ Integration testing with other systems
+ Performance testing and benchmarking
+ User acceptance testing
+ Security testing

### Run automated validation
<a name="run-automated-validation"></a>

1. Navigate to **Validation** in the job plan

1. Choose **Run validation**

1. AWS Transform executes validation tests:
   + Database connectivity
   + Schema compatibility
   + Data integrity
   + Application build
   + Basic functionality

1. Review validation results:
   + Passed: Tests that succeeded
   + Failed: Tests that need attention
   + Warnings: Potential issues to review

### Testing checklist
<a name="testing-checklist"></a>

**Database Functionality:**
+ All tables accessible
+ Stored procedures execute correctly
+ Functions return expected results
+ Triggers fire appropriately
+ Constraints enforced properly
+ Indexes improve query performance

**Application Functionality:**
+ Application starts successfully
+ Database connections established
+ CRUD operations work correctly
+ Stored procedure calls succeed
+ Transactions commit/rollback properly
+ Error handling works as expected

**Data Integrity:**
+ Row counts match source
+ Primary keys unique
+ Foreign keys valid
+ Computed columns correct
+ Null handling appropriate
+ Data types compatible

**Performance:**
+ Query response times acceptable
+ Connection pooling configured
+ Indexes optimized
+ No N\+1 query issues
+ Batch operations efficient
+ Resource utilization reasonable

## Step 13: Deployment
<a name="step-13-deployment"></a>

After successful validation deploy your modernized application and database to production.

### Deployment options
<a name="deployment-options"></a>
+ Amazon ECS and Amazon EC2 Linux

### Pre-deployment checklist
<a name="pre-deployment-checklist"></a>

Before deploying to production:
+ All validation tests passed
+ Performance testing completed
+ Security review completed
+ Backup and rollback plan documented
+ Monitoring and alerting configured
+ Team trained on new environment
+ Stakeholders informed of deployment
+ Maintenance window scheduled

### Deploy to Amazon ECS
<a name="deploy-to-amazon-ecs"></a>

1. Navigate to **Deployment** in the job plan

1. Choose **Deploy to ECS**

1. Configure deployment settings:
   + **Cluster**: Select or create ECS cluster
   + **Service**: Configure ECS service
   + **Task definition**: Review generated task definition
   + **Load balancer**: Configure ALB/NLB
   + **Auto-scaling**: Set scaling policies

1. Review infrastructure-as-code (CloudFormation template or AWS CDK code)

1. Choose **Deploy**

### Monitor deployment
<a name="monitor-deployment"></a>

AWS Transform deploys your application:

1. Creates Aurora PostgreSQL cluster

1. Applies database schema

1. Loads data (if applicable)

1. Deploys application containers

1. Configures load balancer

1. Sets up auto-scaling

Monitor deployment progress and verify:
+ Infrastructure provisioning
+ Database initialization
+ Application deployment
+ Health checks passing
+ Application accessible
+ Database connections working
+ Logs showing normal operation

### Post-deployment validation
<a name="post-deployment-validation"></a>

After deployment:

**Smoke Testing:**
+ Verify critical functionality
+ Test key user workflows
+ Check integration points
+ Monitor error rates

**Performance Monitoring:**
+ Track response times
+ Monitor database queries
+ Check resource utilization
+ Review application logs

**User Validation:**
+ Conduct user acceptance testing
+ Gather feedback
+ Address any issues
+ Document lessons learned

### Rollback procedures
<a name="rollback-procedures"></a>

If issues arise after deployment:

**Immediate Rollback:**
+ Revert to previous application version
+ Switch back to SQL Server (if still available)
+ Restore from backup if needed

**Partial Rollback:**
+ Roll back specific components
+ Keep database changes
+ Revert application code only

**Forward Fix:**
+ Apply hotfix to Aurora PostgreSQL version
+ Deploy updated application code
+ Monitor for resolution

**Important**  
Keep your SQL Server database available for a period after cutover to enable rollback if needed.

### Post-deployment optimization
<a name="post-deployment-optimization"></a>

After successful deployment:

**Performance Tuning:**
+ Optimize slow queries
+ Adjust connection pool settings
+ Fine-tune Aurora PostgreSQL parameters
+ Review and optimize indexes

**Cost Optimization:**
+ Right-size Aurora instance
+ Configure auto-scaling appropriately
+ Review storage settings
+ Optimize backup retention

**Monitoring Setup:**
+ Configure CloudWatch dashboards
+ Set up alerting
+ Enable Enhanced Monitoring
+ Configure Performance Insights

**Documentation:**
+ Update runbooks
+ Document architecture changes
+ Train operations team
+ Create troubleshooting guides