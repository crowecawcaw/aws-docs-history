

# Amazon CloudWatch Omni endpoints and quotas
<a name="cwomni"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service quotas
<a name="limits_cwomni"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Access profiles per space | Each supported Region: 100 | No | The maximum number of access profiles per space | 
| Alerts per space | Each supported Region: 500 | No | The maximum number of alerts per space | 
| Concurrent SQL queries per account per region | Each supported Region: 400 | No | The maximum number of concurrent SQL queries per account per region | 
| Concurrent query sessions per account per region | Each supported Region: 250 | No | The maximum number of concurrent query sessions per account per region | 
| Grants per space | Each supported Region: 500 | No | The maximum number of grants per space | 
| Monthly Omni agent credits | Each supported Region: 100 | No | The maximum number of Omni agent credits per account per region per month. | 
| Omni dashboards per space | Each supported Region: 200 | No | The maximum number of Omni dashboards per space | 
| Omni threads per principal per space | Each supported Region: 200 | No | The maximum number of Omni threads per principal per space | 
| Org-wide domain grants per domain | Each supported Region: 100 | No | The maximum number of org-wide (domain) grants per domain | 
| Rate of CreateAccessGrant requests | Each supported Region: 5 | No | Creates a new rich AccessGrant with optional field filters. | 
| Rate of CreateAccessProfile requests | Each supported Region: 5 | No | Creates a new Access Profile within a space. | 
| Rate of CreateAlert requests | Each supported Region: 5 | No | Creates a new alert within a space. | 
| Rate of CreateDomain requests | Each supported Region: 5 | No | Creates a new domain with identity provider configuration. | 
| Rate of CreateDomainAccessGrantForOrganization requests | Each supported Region: 5 | No | Creates an org-scoped ADMIN grant for a principal on the organization domain. | 
| Rate of CreateIntegration requests | Each supported Region: 10 | No | Creates an integration with a third-party provider. Returns the integration | 
| Rate of CreateOmniDashboard requests | Each supported Region: 5 | No | Creates a new dashboard within a space. | 
| Rate of CreateOneTimeDeepLinkCode requests | Each supported Region: 50 | No | Generates a one-time code for deep link authentication. | 
| Rate of CreateSpace requests | Each supported Region: 5 | No | Creates a new Space within a domain. | 
| Rate of CreateView requests | Each supported Region: 10 | No | Creates a new SQL view. | 
| Rate of DeleteAccessGrant requests | Each supported Region: 5 | No | Removes an existing AccessGrant and its associated Cedar policy. | 
| Rate of DeleteAccessProfile requests | Each supported Region: 5 | No | Removes an Access Profile. | 
| Rate of DeleteAlert requests | Each supported Region: 5 | No | Deletes an alert by its identifier. | 
| Rate of DeleteDomain requests | Each supported Region: 5 | No | Removes a domain and all associated resources. | 
| Rate of DeleteDomainAccessGrantForOrganization requests | Each supported Region: 5 | No | Deletes an org-scoped grant. Soft-deletes the grant record. | 
| Rate of DeleteDomainForOrganization requests | Each supported Region: 5 | No | Deletes an organization-scoped domain. All Spaces must be deleted first. | 
| Rate of DeleteIntegration requests | Each supported Region: 10 | No | Deletes an integration. Returns the resulting status. | 
| Rate of DeleteOmniDashboard requests | Each supported Region: 5 | No | Removes a dashboard from a space. | 
| Rate of DeleteSpace requests | Each supported Region: 5 | No | Removes a Space and all associated resources. | 
| Rate of DeleteView requests | Each supported Region: 10 | No | Deletes the specified view. | 
| Rate of GetAccessGrant requests | Each supported Region: 5 | No | Retrieves the full detail of a single AccessGrant by ID. | 
| Rate of GetAccessProfile requests | Each supported Region: 5 | No | Retrieves an Access Profile with its permissions and access grants. | 
| Rate of GetAlert requests | Each supported Region: 25 | No | Retrieves a single alert by its identifier. | 
| Rate of GetContextGraph requests | Each supported Region: 10 | No | Queries the context graph with filtering, traversal, and pagination support. | 
| Rate of GetDomain requests | Each supported Region: 5 | No | Retrieves a domain by its identifier. | 
| Rate of GetDomainAccessGrantForOrganization requests | Each supported Region: 5 | No | Retrieves an org-scoped grant on the organization domain. | 
| Rate of GetDomainForOrganization requests | Each supported Region: 5 | No | Retrieves details of an organization-scoped domain. | 
| Rate of GetIntegration requests | Each supported Region: 10 | No | Returns the details of a single integration, identified by its identifier. | 
| Rate of GetIntelligenceConfiguration requests | Each supported Region: 10 | No | Retrieves the intelligence configuration for the calling account. | 
| Rate of GetOmniDashboard requests | Each supported Region: 5 | No | Retrieves a dashboard by ID within a space. | 
| Rate of GetSpace requests | Each supported Region: 5 | No | Retrieves details of a specific Space. | 
| Rate of GetSpaceCredentialsForOrganization requests | Each supported Region: 5 | No | Vends space-scoped credentials for MA/DA in a member account. IAM\_DIRECT only. | 
| Rate of GetTelemetryQueryResults requests | Each supported Region: 20 | No | Returns the results for the specified query. | 
| Rate of GetView requests | Each supported Region: 10 | No | Returns the definition and metadata of the specified view. | 
| Rate of ListAccessGrants requests | Each supported Region: 5 | No | Returns AccessGrants within a space with optional filtering. | 
| Rate of ListAccessProfiles requests | Each supported Region: 5 | No | Returns all access profiles in a space. | 
| Rate of ListAlerts requests | Each supported Region: 10 | No | Lists alerts within a space, optionally filtered by exact name(s). | 
| Rate of ListDomainAccessGrantsForOrganization requests | Each supported Region: 5 | No | Lists org-scoped grants for the organization domain. | 
| Rate of ListDomains requests | Each supported Region: 5 | No | Returns all Domains visible to the caller. | 
| Rate of ListIntegrations requests | Each supported Region: 10 | No | Lists the integrations in the account, optionally filtered by type, status. | 
| Rate of ListOmniDashboards requests | Each supported Region: 5 | No | Returns dashboards within a space. | 
| Rate of ListSpaces requests | Each supported Region: 5 | No | Returns all Spaces in the account. | 
| Rate of ListSpacesForOrganization requests | Each supported Region: 5 | No | Lists all Spaces across all member accounts in the organization domain. | 
| Rate of ListTelemetryFields requests | Each supported Region: 10 | No | Lists fields available for telemetry queries. | 
| Rate of ListTelemetryQuerySessions requests | Each supported Region: 10 | No | Lists telemetry query sessions. | 
| Rate of ListViews requests | Each supported Region: 10 | No | Lists the views in the callers account and region. | 
| Rate of PutIntelligenceConfiguration requests | Each supported Region: 10 | No | Creates or updates the intelligence configuration for the calling account. | 
| Rate of SearchPrincipals requests | Each supported Region: 50 | No | Searches Identity Center for users and groups matching a query within a domain. | 
| Rate of StartTelemetryQuery requests | Each supported Region: 10 | No | Starts a telemetry query within a session. | 
| Rate of StartTelemetryQuerySession requests | Each supported Region: 10 | No | Starts a new telemetry query session. | 
| Rate of StopTelemetryQuery requests | Each supported Region: 10 | No | Stops a running telemetry query. | 
| Rate of StopTelemetryQuerySession requests | Each supported Region: 10 | No | Stops a telemetry query session. | 
| Rate of UpdateAccessProfile requests | Each supported Region: 5 | No | Updates the name and/or description of an Access Profile. | 
| Rate of UpdateAlert requests | Each supported Region: 5 | No | Updates an existing alert. | 
| Rate of UpdateDomain requests | Each supported Region: 5 | No | Updates a domains authentication provider configuration. | 
| Rate of UpdateDomainForOrganization requests | Each supported Region: 5 | No | Updates an organization-scoped domain. Must target the domains home region. | 
| Rate of UpdateIntegration requests | Each supported Region: 10 | No | Updates an existing integration, identified by its id, ARN, or name. | 
| Rate of UpdateOmniDashboard requests | Each supported Region: 5 | No | Updates an existing dashboard within a space. | 
| Rate of UpdateSpace requests | Each supported Region: 5 | No | Updates an existing Space within a domain. | 
| Rate of UpdateView requests | Each supported Region: 10 | No | Updates an existing views definition and/or description. | 

For more information, see [CloudWatch Quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html) in the *Amazon CloudWatch User Guide*.