

# Troubleshoot a ServiceNow data source
<a name="kb-managed-ds-servicenow-troubleshooting"></a>

Use this page to diagnose common issues with ServiceNow authentication and syncing.

## Authentication and API access errors
<a name="kb-managed-ds-servicenow-troubleshooting-auth"></a>

The following table describes common authentication and API access errors, their likely causes, and how to fix them.


**Authentication and API access errors**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| The Table API returns HTTP 401 even though the token request succeeds. | The Inbound Authentication Profile is not linked to the REST API Access Policy, or the Allow Access Policy was not added to the profile. | Verify both sides of the API access policy configuration. See [Step 6: Configure API access policies](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-step6). | 
| Sync completes but reports 0 documents crawled. | The service account has the basic knowledge or catalog role instead of knowledge\_admin or catalog\_admin. | Assign knowledge\_admin and catalog\_admin to the service account. See [Step 3: Assign service account roles](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-step3). | 
| Token request fails, or the connector cannot reach your instance. | The glide.oauth.inbound.client.credential.grant\_type.enabled system property is not set to true, or the instance is not reachable from AWS. | Verify the system property and network connectivity. See [Step 1: Enable client credentials grant type](kb-managed-servicenow-oauth2-setup.md#kb-managed-servicenow-oauth2-step1). | 

## Sync performance
<a name="kb-managed-ds-servicenow-troubleshooting-sync"></a>

The following table describes a common sync performance issue and how to resolve it.


**Sync performance issues**  

| Symptom | Likely cause | Fix | 
| --- | --- | --- | 
| Sync takes hours on large instances. | No catalog ID filtering is configured, so the connector crawls all active catalog items (100,000 or more on enterprise instances). | Use serviceCatalogFilter (with inclusionServiceCatalogSysIds) in filterConfiguration to scope the crawl to specific service catalogs. See [Connector parameters](kb-managed-ds-servicenow-connect.md#kb-managed-config-servicenow). | 