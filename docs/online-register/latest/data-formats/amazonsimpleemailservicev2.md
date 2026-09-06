

# Data retrieval APIs for Amazon Simple Email Service v2
<a name="amazonsimpleemailservicev2"></a>

Amazon Simple Email Service v2 provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="ses-BatchGetMetricData"></a>[BatchGetMetricData](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_BatchGetMetricData.html) | Get metric data on your activity | Read | 
| <a name="ses-GetAccount"></a>[GetAccount](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetAccount.html) | Get information about the email-sending status and capabilities for your account | Read | 
| <a name="ses-GetBlacklistReports"></a>[GetBlacklistReports](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetBlacklistReports.html) | Retrieve a list of the deny lists on which your dedicated IP addresses or tracked domains appear | Read | 
| <a name="ses-GetConfigurationSet"></a>[GetConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetConfigurationSet.html) | Get information about an existing configuration set | Read | 
| <a name="ses-GetConfigurationSetEventDestinations"></a>[GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetConfigurationSetEventDestinations.html) | Retrieve a list of event destinations that are associated with a configuration set | Read | 
| <a name="ses-GetContact"></a>[GetContact](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetContact.html) | Return a contact from a contact list | Read | 
| <a name="ses-GetContactList"></a>[GetContactList](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetContactList.html) | Return contact list metadata | Read | 
| <a name="ses-GetCustomVerificationEmailTemplate"></a>[GetCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetCustomVerificationEmailTemplate.html) | Return the custom email verification template for the template name you specify | Read | 
| <a name="ses-GetDedicatedIp"></a>[GetDedicatedIp](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDedicatedIp.html) | Get information about a dedicated IP address | Read | 
| <a name="ses-GetDedicatedIpPool"></a>[GetDedicatedIpPool](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDedicatedIpPool.html) | Get information about a dedicated IP pool | Read | 
| <a name="ses-GetDedicatedIps"></a>[GetDedicatedIps](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDedicatedIps.html) | List the dedicated IP addresses a dedicated IP pool | Read | 
| <a name="ses-GetDeliverabilityDashboardOptions"></a>[GetDeliverabilityDashboardOptions](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDeliverabilityDashboardOptions.html) | Get the status of the Deliverability dashboard | Read | 
| <a name="ses-GetDeliverabilityTestReport"></a>[GetDeliverabilityTestReport](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDeliverabilityTestReport.html) | Retrieve the results of a predictive inbox placement test | Read | 
| <a name="ses-GetDomainDeliverabilityCampaign"></a>[GetDomainDeliverabilityCampaign](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDomainDeliverabilityCampaign.html) | Retrieve all the deliverability data for a specific campaign | Read | 
| <a name="ses-GetDomainStatisticsReport"></a>[GetDomainStatisticsReport](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetDomainStatisticsReport.html) | Retrieve inbox placement and engagement rates for the domains that you use to send email | Read | 
| <a name="ses-GetEmailAddressInsights"></a>[GetEmailAddressInsights](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailAddressInsights.html) | Get insights about email address | Read | 
| <a name="ses-GetEmailIdentity"></a>[GetEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailIdentity.html) | Get information about a specific identity | Read | 
| <a name="ses-GetEmailIdentityPolicies"></a>[GetEmailIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailIdentityPolicies.html) | Return the requested sending authorization policies for the given identity (an email address or a domain) | Read | 
| <a name="ses-GetEmailTemplate"></a>[GetEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetEmailTemplate.html) | Return the template object, which includes the subject line, HTML part, and text part for the template you specify | Read | 
| <a name="ses-GetExportJob"></a>[GetExportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetExportJob.html) | Get information about an export job | Read | 
| <a name="ses-GetImportJob"></a>[GetImportJob](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetImportJob.html) | Provide information about an import job | Read | 
| <a name="ses-GetMessageInsights"></a>[GetMessageInsights](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetMessageInsights.html) | Provide insights about a message | Read | 
| <a name="ses-GetMultiRegionEndpoint"></a>[GetMultiRegionEndpoint](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetMultiRegionEndpoint.html) | Get information about a multi-region endpoint | Read | 
| <a name="ses-GetReputationEntity"></a>[GetReputationEntity](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetReputationEntity.html) | Retrieve information about a reputation entity's status | Read | 
| <a name="ses-GetSuppressedDestination"></a>[GetSuppressedDestination](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetSuppressedDestination.html) | Retrieve information about a specific email address that's on the suppression list for your account or tenant | Read | 
| <a name="ses-GetTenant"></a>[GetTenant](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetTenant.html) | Get information about a tenant | Read | 
| <a name="ses-ListConfigurationSets"></a>[ListConfigurationSets](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListConfigurationSets.html) | List all of the configuration sets for your account | List | 
| <a name="ses-ListContactLists"></a>[ListContactLists](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListContactLists.html) | List all of the contact lists available for your account | List | 
| <a name="ses-ListContacts"></a>[ListContacts](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListContacts.html) | List the contacts present in a specific contact list | List | 
| <a name="ses-ListCustomVerificationEmailTemplates"></a>[ListCustomVerificationEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListCustomVerificationEmailTemplates.html) | List all of the existing custom verification email templates for your account | List | 
| <a name="ses-ListDedicatedIpPools"></a>[ListDedicatedIpPools](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListDedicatedIpPools.html) | List all of the dedicated IP pools for your account | List | 
| <a name="ses-ListDeliverabilityTestReports"></a>[ListDeliverabilityTestReports](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListDeliverabilityTestReports.html) | Retrieve the list of the predictive inbox placement tests that you've performed, regardless of their statuses, for your account | List | 
| <a name="ses-ListDomainDeliverabilityCampaigns"></a>[ListDomainDeliverabilityCampaigns](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListDomainDeliverabilityCampaigns.html) | List deliverability data for campaigns that used a specific domain to send email during a specified time range | Read | 
| <a name="ses-ListEmailIdentities"></a>[ListEmailIdentities](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListEmailIdentities.html) | List the email identities for your account | List | 
| <a name="ses-ListEmailTemplates"></a>[ListEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListEmailTemplates.html) | List all of the email templates for your account | List | 
| <a name="ses-ListExportJobs"></a>[ListExportJobs](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListExportJobs.html) | List all the exports jobs for your account | List | 
| <a name="ses-ListImportJobs"></a>[ListImportJobs](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListImportJobs.html) | List all of the import jobs for your account | List | 
| <a name="ses-ListMultiRegionEndpoints"></a>[ListMultiRegionEndpoints](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListMultiRegionEndpoints.html) | List all of the multi-region endpoints for your account | List | 
| <a name="ses-ListRecommendations"></a>[ListRecommendations](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListRecommendations.html) | List recommendations for your account | Read | 
| <a name="ses-ListReputationEntities"></a>[ListReputationEntities](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListReputationEntities.html) | Retrieve a list of reputation entities | List | 
| <a name="ses-ListResourceTenants"></a>[ListResourceTenants](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListResourceTenants) | List all the tenants associated to a SES resource | List | 
| <a name="ses-ListSuppressedDestinations"></a>[ListSuppressedDestinations](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListSuppressedDestinations.html) | List email addresses that are on the suppression list for your account or tenant | Read | 
| <a name="ses-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListTagsForResource.html) | Retrieve a list of the tags (keys and values) that are associated with a specific resource for your account | Read | 
| <a name="ses-ListTenantResources"></a>[ListTenantResources](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListTenantResources) | List all the resources associated to a tenant | List | 
| <a name="ses-ListTenants"></a>[ListTenants](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListTenants) | List all the tenants for your account | List | 