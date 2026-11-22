

# Troubleshooting the Snowflake integration

Use the failing boundary to locate the configuration error. IAM controls whether Snowflake can assume the role. Lake Formation controls whether that role can discover and query the named table. The resource link connects your namespace to the HealthLake target database. For issues that are common to all analytics engines, see [Troubleshooting access to HealthLake tables](integrating-analytics-troubleshooting.md).

## Common issues
<a name="integrating-snowflake-troubleshooting-common"></a>

The following table lists issues that are specific to the Snowflake integration, their causes, and resolutions.


**Snowflake integration troubleshooting**  

| Symptom | Possible cause | Resolution | 
| --- | --- | --- | 
| The blocked-state check doesn't report sts:AssumeRole | Another setup layer failed first, such as the warehouse, privileges, endpoint, integration properties, or namespace | Correct that layer, and repeat the check in [Step 3: Create the catalog integration](integrating-snowflake-setting-up.md#integrating-snowflake-step3). | 
| sts:AssumeRole is denied after you apply the final trust policy | The IAM identity or external ID doesn't match the current catalog integration | Run DESCRIBE CATALOG INTEGRATION again, and replace the trust policy with the current values in [Step 4: Authorize Snowflake](integrating-snowflake-setting-up.md#integrating-snowflake-step4). | 
| Catalog metadata access is denied | A customer or target catalog ancestor is missing from the role's scoped AWS Glue policy | Compare the validated account, database, and table values with every resource in the permissions policy in [Step 2: Create the IAM role](integrating-snowflake-setting-up.md#integrating-snowflake-step2). | 
| The catalog requires DESCRIBE | The role lacks DESCRIBE on the target table or the resource link database | Confirm both grants in [Step 4: Authorize Snowflake](integrating-snowflake-setting-up.md#integrating-snowflake-step4). | 
| The catalog requires SELECT | The role lacks SELECT on the target table | Grant SELECT on that named table in [Step 4: Authorize Snowflake](integrating-snowflake-setting-up.md#integrating-snowflake-step4). | 
| A query succeeds after you revoke access | Previously issued credentials or an AWS STS session remain valid, or result reuse is on | Disable result reuse, wait for both lifetimes to expire, and run a fresh query, as described in [Testing revocation (optional)](integrating-snowflake-setting-up.md#integrating-snowflake-revocation). | 
| Cleanup reports an absent grant or role | A prior cleanup pass already removed it | Accept the documented empty result or a NoSuchEntity response as proof of absence. | 
| Resource link discovery returns zero or more than one candidate | The account, Region, or data store is wrong, or the links are ambiguous | Select one exact resource link before you grant access, as described in [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find). | 