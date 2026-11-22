

# Troubleshooting the Databricks integration

This topic helps you diagnose and resolve common issues with the Databricks integration. For issues that are common to all analytics engines, see [Troubleshooting access to HealthLake tables](integrating-analytics-troubleshooting.md).

## Common issues
<a name="integrating-databricks-troubleshooting-common"></a>

The following table lists common issues, their causes, and resolutions.


**Databricks integration troubleshooting**  

| Symptom | Possible cause | Resolution | 
| --- | --- | --- | 
| The app can't assume the role | The trust policy issuer, sub, or aud doesn't match the app identity | Compare the trust policy in [Step 3: Create and authorize the IAM role](integrating-databricks-setting-up.md#integrating-databricks-step3) with the DATABRICKS\_IDENTITY log line from [Step 2: Deploy the OpenSharing server](integrating-databricks-setting-up.md#integrating-databricks-step2). | 
| AccessDenied on lakeformation:GetDataAccess | The role's permissions policy is missing the permission | Check the permissions policy in [Step 3: Create and authorize the IAM role](integrating-databricks-setting-up.md#integrating-databricks-step3). | 
| A Databricks user can't see the catalog | The user doesn't have Unity Catalog permissions | Grant permissions in Unity Catalog, as described in [Step 4: Add the catalogs and run a test query](integrating-databricks-setting-up.md#integrating-databricks-step4). | 
| Queries are slow or use a lot of compute | Each query reads all of a table's files | Build curated tables, as described in [Building curated tables for repeated queries](integrating-databricks.md#integrating-databricks-querying-pattern). | 

## Where to look
<a name="integrating-databricks-troubleshooting-diagnose"></a>

To diagnose a problem, check the following sources:
+ HealthLake OpenSharing server logs, with `databricks apps logs {{app-name}}`.
+ AWS CloudTrail events for the role, including the `errorCode`: `AssumeRoleWithWebIdentity` (AWS STS), `GetTemporaryGlueTableCredentials` (Lake Formation), and `GetTable` (Glue).
+ Unity Catalog audit logs, for user-level denials.
+ For server-side issues, see [Troubleshooting](https://github.com/databricks-industry-solutions/healthlake-opensharing#troubleshooting) on the GitHub website.