

# Troubleshooting access to HealthLake tables

This topic covers access problems that apply to every engine. For engine-specific issues, see the troubleshooting topic for your engine.

## Common issues
<a name="integrating-analytics-troubleshooting-common"></a>

The following table lists common issues, their causes, and resolutions.


**Common access issues**  

| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| Insufficient Lake Formation permission(s) | The principal doesn't have Lake Formation permissions, or the catalog ID is incorrect | Check the grants by following Step 2 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md), and confirm the HealthLake catalog ID with [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find). | 
| EntityNotFoundException for a database or table | The resource link name or catalog ID is incorrect | Confirm the resource link name and target database with [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find). | 
| AccessDenied on lakeformation:GetDataAccess (Databricks and Snowflake) | The engine's IAM role policy is missing the permission | Add lakeformation:GetDataAccess to the engine's IAM role policy. | 
| Credentials are returned, but reading data fails (Spark on Amazon EMR, Databricks, and Snowflake) | Full table access for external engines isn't on | Turn on full table access, as described in [Step 3: Turn on full table access (Spark on Amazon EMR, Databricks, and Snowflake)](integrating-analytics-getting-started.md#integrating-analytics-full-table-access). | 
| A new data store doesn't appear | There are no grants on the new resource link | Grant access to the new resource link by following Step 2 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md). | 
| Row counts are higher than expected | The tables contain multiple versions and delete markers | Query only the latest live version, as described in [Resource versions](integrating-analytics.md#integrating-analytics-tables-versions). | 

## Where to look
<a name="integrating-analytics-troubleshooting-diagnose"></a>

To diagnose a problem, check AWS CloudTrail for the following events:
+ `GetTable` (AWS Glue).
+ `GetDataAccess` and `GetTemporaryGlueTableCredentials` (Lake Formation).
+ `AssumeRole` and `AssumeRoleWithWebIdentity` (AWS STS).

For engine-specific issues, see [Troubleshooting the Databricks integration](integrating-databricks-troubleshooting.md) and [Troubleshooting the Snowflake integration](integrating-snowflake-troubleshooting.md).