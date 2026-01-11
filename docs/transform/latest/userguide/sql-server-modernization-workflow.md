# SQL Server modernization workflow

This section provides a step-by-step walkthrough of the complete SQL Server modernization process using AWS Transform.

## Step 1: Create SQL Server modernization job

Begin your modernization journey by creating a new transformation job in the AWS Transform console.

1. Sign in to the AWS Transform console
2. Choose **Create modernization job**
3. Select **Windows modernization** job and then select **SQL Server modernization**
4. Enter job details:
   - **Job name**: Descriptive name for your project
   - **Description**: Optional description
   - **Target region**: AWS region for deployment

5. Choose **Create job**

###### Important

Do not include personally identifiable information (PII) in your job name.

## Step 2: Connect to SQL Server database

Connect AWS Transform to your SQL Server database to enable schema analysis and conversion.

### Create a database connector

1. In your SQL Server modernization job, navigate to Connect to resources
2. Choose **Connect to SQL Server database**
3. Choose **Create new connector**
4. Enter the connector information:
   - C**onnector name**: Descriptive name
   - **AWS account ID**: Account where SQL Server is hosted

5. Once confirmed, you will receive a link for approval. Copy the approval link to get approval from your AWS admin for the account. Once they have approved, you can proceed to the next step.
6. After your administrator has approved the connector request, click Submit to proceed to the source code connection setup.

## Step 3: Connect source code repository

AWS Transform needs access to your .NET application source code to analyze and transform the code that interacts with your SQL Server database.

### Set up AWS CodeConnections

1. In your SQL Server modernization job, navigate to **Connect to
   resources**
2. Choose **Connect source code repository**
3. If you don't have an existing connection, choose **Create
   connection**
4. Select your repository provider:
   - GitHub / GitHub Enterprise
   - GitLab.com / GitLab self-managed
   - Bitbucket Cloud
   - Azure Repositories

5. Follow the authorization flow for your provider
6. After authorization, choose **Connect**

### Select your repository and branch

1. Select your repository from the list
2. Choose the branch you want to transform (typically main, master, or develop)
3. (Optional) Specify a subdirectory if your .NET application is not in the repository root
4. Choose **Continue**

###### Note

AWS Transform will create a new branch for the transformed code. You can review and merge the changes through your normal code review process.

### Repository access approval

For GitHub and some other platforms, the repository administrator must approve the connection request:

1. AWS Transform displays a verification link
2. Share this link with your repository administrator
3. The administrator reviews and approves the request in their repository settings
4. Once approved, the connection status changes to _Approved_

###### Important

The approval process can take time depending on your organization's policies. Plan accordingly.

## Step 4: Create deployment connector (optional)

If you want to deploy the transformed applications into your AWS account, you have the option to select a deployment connector.

### Set up deployment connector

1. Select **Yes** if you want to deploy your applications. Selecting
   **No** will skip this step.
2. Add your AWS account where you want to deploy the transformed applications.
3. Add a name that helps you remember the connector easily
4. Submit the connector request for approval.

### Deployment connector approval

Your AWS account administrator must approve the connection request for deployment connector.

1. AWS Transform displays a verification link
2. Share this link with your AWS account administrator
3. The administrator reviews and approves the request in their repository settings
4. Once approved, the connection status changes to _Approved_

###### Important

The approval process can take time depending on your organization's policies. Plan accordingly.

## Step 5: Confirm your resources

After connecting to your database and repository, AWS Transform verifies that all required resources are accessible and ready for transformation.

### What AWS Transform verifies

- **Database connectivity:** Connection is active, user has required permissions, databases are accessible, version is supported
- **Repository access:** Repository is accessible, branch exists, .NET project files detected, database connections discoverable
- **Environment readiness:** VPC configuration supports DMS, required AWS service roles exist, network connectivity established, region compatibility confirmed

### Review the pre-flight checklist

1. Navigate to **Confirm your resources** in the job plan
2. Review the checklist items:
   - ✅ Database connection verified
   - ✅ Repository access confirmed
   - ✅ .NET version supported
   - ✅ Entity Framework or ADO.NET detected
   - ✅ Network configuration valid
   - ✅ Required permissions granted

3. If all items show as complete, choose Continue
4. If any items show warnings or errors, address them before proceeding

## Step 6: Discovery and assessment

AWS Transform analyzes your SQL Server database and .NET application to understand the scope and complexity of the modernization.

### What gets discovered

- **Database objects:** Tables, views, indexes, stored procedures, functions, triggers, constraints, data types, computed columns, identity columns, foreign key relationships
- **Application code:** .NET project structure, Entity Framework models and configurations, ADO.NET data access code, database connection strings, stored procedure calls, SQL queries in code
- **Dependencies:** Which applications use which databases, cross-database dependencies, shared stored procedures, common data access patterns

### Discovery process

- AWS Transform begins discovery automatically after resource confirmation
- Discovery typically takes 5-15 minutes depending on database size and application complexity
- Monitor progress in the worklog
- AWS Transform displays real-time updates as objects are discovered

### Review discovery results

After discovery completes, navigate to **Discovery and assessment** to review:

**Database Analysis:**

- **Object count**: Number of tables, views, stored procedures,
  functions, triggers
- **Complexity score**: Assessment of transformation complexity
  (Low, Medium, High)
- **Action items**: Objects that may require human attention
- **Supported features**: Database features that will convert
  automatically
- **Unsupported features**: Features that require
  workarounds

**Application Analysis:**

- **Project type**: ASP.NET Core, Console App, Class Library,
  etc.
- **.NET version**: Detected .NET Core version
- **Data access framework**: Entity Framework version or
  ADO.NET
- **Database connections**: Number of connection strings
  found
- **Code complexity**: Assessment of transformation
  complexity

**Dependency Map:**

- Visual representation of application-to-database relationships
- Cross-database dependencies
- Shared components

### Understanding complexity assessment

AWS Transform classifies your modernization into three categories:

| Complexity       | Characteristics                                                                                                             | Expected Outcome                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Low (Class A)    | Standard SQL patterns (ANSI SQL), simple stored procedures, basic data types, Entity Framework with standard configurations | Minimal human intervention expected, high automation success rate |
| Medium (Class B) | Advanced T-SQL patterns, complex stored procedures with business logic, user-defined functions, computed columns            | Some human intervention required, expert review recommended       |
| High (Class C)   | CLR assemblies, linked servers, Service Broker, complex full-text search                                                    | Significant human refactoring required, consider phased approach  |

### Assessment report

AWS Transform generates a detailed assessment report that includes:

- Executive summary with high-level overview
- Complete database inventory
- Application inventory
- Transformation readiness percentage
- Effort estimation
- Risk assessment and mitigation strategies
- Recommended approach

You can download the assessment report for offline review and sharing with stakeholders.

## Step 7: Generate and review wave plan

For large estates with multiple databases and applications, AWS Transform generates a wave plan that sequences the modernization in logical groups.

### What is a wave plan?

A wave plan organizes your modernization into phases (waves) based on:

- Dependencies between databases and applications
- Business priorities
- Risk tolerance
- Resource availability
- Technical complexity

Each wave contains a group of databases and applications that can be modernized together without breaking dependencies.

### Review the wave plan

1. Navigate to **Wave planning** in the job plan
2. Review the proposed waves
3. For each wave, review:
   - Databases included
   - Applications included
   - Dependencies on other waves
   - Estimated transformation time
   - Complexity level
   - Deployable applications

### Customize the wave plan

You can customize the wave plan to match your business needs in 2 ways:

**Using JSON:**

1. Choose **Download all waves** to get a JSON file with all the
   waves
2. Modify waves in the JSON by:
   - Moving databases between waves
   - Splitting waves into smaller groups
   - Merging waves together
   - Changing wave sequence
   - Adding or removing databases from scope

3. Upload the JSON file back to the console by choosing **Upload wave
   plan**
4. AWS Transform validates your changes and warns if dependencies are violated
5. Choose **Confirm waves** to update the wave plan

**Using Chat:**

You can modify the wave plans by chatting with the agent and asking it to move the repositories and databases to specific waves. This approach works well if you need to make minor edits to the waves.

###### Important

Ensure that dependencies are respected when customizing waves. Transforming a dependent application before its database can cause issues.

### Single database modernization

If you're modernizing a single database and application, AWS Transform creates a simple plan with one wave. You can proceed directly to transformation without wave planning.

### Approve the wave plan

1. After reviewing and customizing (if needed), choose **Approve wave
   plan**
2. AWS Transform locks the wave plan and proceeds to transformation
3. You can still modify the plan later by choosing **Edit wave
   plan**

## Step 8: Schema conversion

AWS Transform converts your SQL Server database schema to Aurora PostgreSQL, including tables, views, stored procedures, functions, and triggers.

### How schema conversion works

AWS Transform uses AWS DMS Schema Conversion enhanced with generative AI to:

- Analyze SQL Server schemas and relationships
- Map data types from SQL Server to PostgreSQL equivalents
- Transform T-SQL to PL/pgSQL
- Handle identity columns, computed columns, and constraints
- Validate conversion and referential integrity
- Generate action items for objects requiring human review

### Supported conversions

**Automatically converted:**

- Tables, views, and indexes
- Primary keys and foreign keys
- Check constraints and default values
- Most common data types
- Simple stored procedures
- Basic functions and triggers
- Identity columns (converted to SERIAL or GENERATED)
- Most computed columns

**May require human review:**

- Complex stored procedures with advanced T-SQL
- SQL Server-specific functions (GETUTCDATE, SUSER_SNAME, etc.)
- Computed columns with complex expressions
- Full-text search indexes
- XML data type operations
- HIERARCHYID data type (requires ltree extension)

**Not automatically converted:**

- CLR assemblies
- Linked servers
- Service Broker
- SQL Server Agent jobs

### Start schema conversion

1. Navigate to Schema conversion in the job plan
2. Review the conversion settings:
   - Target PostgreSQL version
   - Extension options (ltree, PostGIS, etc.)
   - Naming conventions

3. Choose **Start conversion**
4. Monitor progress in the worklog
5. Conversion typically takes 10-30 minutes depending on the number of database objects

### Review conversion results

After conversion completes, navigate to Review schema conversion:

**Conversion Summary:**

- **Objects converted**: Count of successfully converted
  objects
- **Action items**: Objects requiring human attention
- **Warnings**: Potential issues to review
- **Errors**: Objects that could not be converted

**Review by Object Type:**

- **Tables**: Data type mappings, constraints, indexes
- **Stored procedures**: T-SQL to PL/pgSQL conversion
- **Functions**: Function signature and logic changes
- **Triggers**: Trigger syntax and timing changes

### Review action items

1. Choose **View action items**
2. For each action item, review:
   - **Object name**: The database object
   - **Issue type**: What requires attention
   - **Severity**: Critical, Warning, or Info
   - **Recommendation**: Suggested resolution
   - **Original code**: SQL Server version
   - **Converted code**: PostgreSQL version

3. For each action item, you can:
   - **Accept**: Use the converted code
   - **Modify**: Edit the converted code
   - **Flag for later**: Mark for human review after
     transformation

### Example: Stored procedure conversion

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

- Procedure converted to function returning TABLE
- Parameter names prefixed with p\_
- TOP converted to LIMIT
- DATEDIFF converted to EXTRACT
- GETUTCDATE() converted to NOW()
- Column names converted to lowercase (PostgreSQL convention)

### Approve schema conversion

1. After reviewing all action items and making necessary modifications
2. Choose **Approve schema conversion**
3. AWS Transform prepares the converted schema for deployment to Aurora PostgreSQL

###### Note

You can download the converted schema as SQL scripts for offline review or version control.

## Step 9: Data migration (optional)

AWS Transform provides options for migrating data from SQL Server to Aurora PostgreSQL. Data migration is optional and can be skipped if you only need schema and code transformation.

### Data migration options

**Option 1: Production Data Migration**

Migrate your actual production data using AWS DMS:

- Full initial load of all data
- Continuous replication during testing (CDC)
- Minimal downtime cutover
- Data validation and integrity checks

**Option 2: Skip Data Migration**

Transform schema and code only:

- Useful for development/testing environments
- When data will be migrated separately
- For proof-of-concept projects

### Configure data migration

1. Navigate to **Data migration** in the job plan
2. Choose your migration option:
   - **Migrate production data**
   - **Skip data migration**

3. If migrating production data, configure:
   - **Migration type**: Full load, or Full load + CDC
   - **Validation**: Enable data validation
   - **Performance**: DMS instance size
   - Choose **>Start migration**

### Production data migration process

If you choose to migrate production data:

1. **Initial sync**: AWS DMS performs full load of all
   tables
2. **Continuous replication**: (If CDC enabled) Keeps data
   synchronized
3. **Validation**: Verifies row counts and data integrity
4. **Cutover preparation**: Prepares for final
   synchronization

Migration Timeline:

- Small databases (< 10 GB): 30 minutes - 2 hours
- Medium databases (10-100 GB): 2-8 hours
- Large databases (> 100 GB): 8+ hours

### Data validation

AWS Transform validates migrated data with the following checks:

- Row count comparison (source vs target)
- Primary key integrity
- Foreign key relationships
- Data type compatibility
- Computed column results
- Null value handling

## Step 10: Application code transformation

AWS Transform transforms your .NET application code to work with Aurora PostgreSQL instead of SQL Server. It asks for a target branch name in your repositories to commit the transformed source code. Once you enter the branch name, AWS Transform will create a new branch and initiate the transformation to match the PostgreSQL database.

### What gets transformed

**Entity Framework Changes:**

- **Database provider**: UseSqlServer() → UseNpgsql()
- **Connection strings**: SQL Server format → PostgreSQL
  format
- **Data type mappings**: SQL Server types → PostgreSQL
  types
- **DbContext configurations**: SQL Server-specific →
  PostgreSQL-specific
- **Migration files**: Updated for PostgreSQL compatibility

**ADO.NET Changes:**

- **Connection classes**: SqlConnection → NpgsqlConnection
- **Command classes**: SqlCommand → NpgsqlCommand
- **Data reader**: SqlDataReader → NpgsqlDataReader
- **Parameters**: SqlParameter → NpgsqlParameter
- S**QL syntax**: T-SQL → PostgreSQL SQL

**Configuration Changes:**

- Connection strings in appsettings.json
- Database provider NuGet packages
- Dependency injection configurations
- Startup/Program.cs configurations

### Start code transformation

1. Navigate to Application transformation in the job plan
2. Review the transformation settings:
   - **Target .NET version** (if upgrading)
   - **PostgreSQL provider version**
   - **Code style preferences**

3. Choose **Start transformation**
4. Monitor progress in the worklog
5. Transformation typically takes 15-45 minutes depending on codebase size

## Step 11: Review transformation results

Before proceeding to deployment, review the complete transformation results to ensure everything is ready for testing.

You can download the transformed code from the repository branch for:

- Local testing and validation
- Code review in your IDE
- Integration with your CI/CD pipeline
- Version control commit

You can also download the transformation summary to review the natural language changes that are made by AWS Transform as part of the transformation.

### Transformation summary

1. Navigate to **Transformation summary** in the job plan
2. Review the overall results:
   - **Schema conversion**: Objects converted, action items,
     warnings
   - **Data migration**: Tables migrated, rows transferred, validation
     status
   - **Code transformation**: Files changed, lines modified, issues
     resolved
   - **Readiness score**: Overall readiness for deployment

### Generate transformation report

AWS Transform generates a comprehensive transformation report:

1. Choose **Generate report**
2. Select report type:
   - **Executive summary**: High-level overview for
     stakeholders
   - **Technical details**: Complete transformation
     documentation
   - **Action items**: List of human tasks required

3. Choose **Download report**

The report includes:

- Transformation scope and objectives
- Objects and code transformed
- Issues encountered and resolutions
- Validation results
- Deployment readiness assessment
- Recommendations for testing

## Step 12: Validation and testing

Before deploying to production, validate that the transformed application works correctly with Aurora PostgreSQL.

### Validation types

**Automated Validation:** AWS Transform performs automated checks:

- Schema validation against source database
- Data integrity verification
- Query equivalence testing
- Connection string validation
- Configuration validation

**Human Validation:** You should perform additional testing:

- Functional testing of application features
- Integration testing with other systems
- Performance testing and benchmarking
- User acceptance testing
- Security testing

### Run automated validation

1. Navigate to **Validation** in the job plan
2. Choose **Run validation**
3. AWS Transform executes validation tests:
   - Database connectivity
   - Schema compatibility
   - Data integrity
   - Application build
   - Basic functionality

4. Review validation results:
   - Passed: Tests that succeeded
   - Failed: Tests that need attention
   - Warnings: Potential issues to review

### Testing checklist

**Database Functionality:**

- All tables accessible
- Stored procedures execute correctly
- Functions return expected results
- Triggers fire appropriately
- Constraints enforced properly
- Indexes improve query performance

**Application Functionality:**

- Application starts successfully
- Database connections established
- CRUD operations work correctly
- Stored procedure calls succeed
- Transactions commit/rollback properly
- Error handling works as expected

**Data Integrity:**

- Row counts match source
- Primary keys unique
- Foreign keys valid
- Computed columns correct
- Null handling appropriate
- Data types compatible

**Performance:**

- Query response times acceptable
- Connection pooling configured
- Indexes optimized
- No N+1 query issues
- Batch operations efficient
- Resource utilization reasonable

## Step 13: Deployment

After successful validation deploy your modernized application and database to
production.

### Deployment options

- Amazon ECS and Amazon EC2 Linux

### Pre-deployment checklist

Before deploying to production:

- All validation tests passed
- Performance testing completed
- Security review completed
- Backup and rollback plan documented
- Monitoring and alerting configured
- Team trained on new environment
- Stakeholders informed of deployment
- Maintenance window scheduled

### Deploy to Amazon ECS

1. Navigate to **Deployment** in the job plan
2. Choose **Deploy to ECS**
3. Configure deployment settings:
   - **Cluster**: Select or create ECS cluster
   - **Service**: Configure ECS service
   - **Task definition**: Review generated task definition
   - **Load balancer**: Configure ALB/NLB
   - **Auto-scaling**: Set scaling policies

4. Review infrastructure-as-code (CloudFormation template or AWS CDK code)
5. Choose **Deploy**

### Monitor deployment

AWS Transform deploys your application:

1. Creates Aurora PostgreSQL cluster
2. Applies database schema
3. Loads data (if applicable)
4. Deploys application containers
5. Configures load balancer
6. Sets up auto-scaling

Monitor deployment progress and verify:

- Infrastructure provisioning
- Database initialization
- Application deployment
- Health checks passing
- Application accessible
- Database connections working
- Logs showing normal operation

### Post-deployment validation

After deployment:

**Smoke Testing:**

- Verify critical functionality
- Test key user workflows
- Check integration points
- Monitor error rates

**Performance Monitoring:**

- Track response times
- Monitor database queries
- Check resource utilization
- Review application logs

**User Validation:**

- Conduct user acceptance testing
- Gather feedback
- Address any issues
- Document lessons learned

### Rollback procedures

If issues arise after deployment:

**Immediate Rollback:**

- Revert to previous application version
- Switch back to SQL Server (if still available)
- Restore from backup if needed

**Partial Rollback:**

- Roll back specific components
- Keep database changes
- Revert application code only

**Forward Fix:**

- Apply hotfix to Aurora PostgreSQL version
- Deploy updated application code
- Monitor for resolution

###### Important

Keep your SQL Server database available for a period after cutover to enable rollback if needed.

### Post-deployment optimization

After successful deployment:

**Performance Tuning:**

- Optimize slow queries
- Adjust connection pool settings
- Fine-tune Aurora PostgreSQL parameters
- Review and optimize indexes

**Cost Optimization:**

- Right-size Aurora instance
- Configure auto-scaling appropriately
- Review storage settings
- Optimize backup retention

**Monitoring Setup:**

- Configure CloudWatch dashboards
- Set up alerting
- Enable Enhanced Monitoring
- Configure Performance Insights

**Documentation:**

- Update runbooks
- Document architecture changes
- Train operations team
- Create troubleshooting guides
