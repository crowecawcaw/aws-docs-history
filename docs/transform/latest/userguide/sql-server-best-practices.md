

# Best practices and troubleshooting
<a name="sql-server-best-practices"></a>

Best practices, and common issues and their resolutions during the modernization process.

## Schema conversion issues
<a name="schema-conversion-issues"></a>

**Problem:** Schema conversion shows many action items

Solutions:
+ Review action items in conversion report
+ Prioritize based on impact
+ Use Amazon Q Developer for complex SQL conversions
+ Consult AWS Support for guidance
+ Consider phased approach for complex databases

## Application transformation issues
<a name="application-transformation-issues"></a>

**Problem:** Application transformation fails to build

Solutions:
+ Review build errors in transformation report
+ Configure private NuGet feeds if needed
+ Update package references if required
+ Check for Windows-specific dependencies
+ Review transformation logs for detailed errors

## Resource cleanup issues
<a name="resource-cleanup-issues"></a>

**Problem:** Transformation job fails with resource errors

Solutions:
+ Clean up failed or incomplete resources from previous attempts
+ Verify secrets are not scheduled for deletion
+ Check service quotas for Aurora PostgreSQL
+ Contact AWS Support if cleanup doesn't resolve the issue

## Database connection issues
<a name="deployment-issues"></a>

**Problem:** Cannot connect to the target Aurora PostgreSQL cluster

Solutions:
+ Verify connection string format for PostgreSQL
+ Check security group rules
+ Verify database credentials in Secrets Manager
+ Ensure SSL/TLS is properly configured
+ Test connection using psql or pgAdmin

## Getting additional help
<a name="getting-additional-help"></a>

When contacting AWS Support, please provide:
+ Transformation job ID
+ AWS account ID
+ Region
+ Error messages and screenshots
+ Transformation logs (available in AWS Transform console)