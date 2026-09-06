

# Data retrieval APIs for Amazon Detective
<a name="amazondetective"></a>

Amazon Detective provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="detective-BatchGetGraphMemberDatasources"></a>[BatchGetGraphMemberDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetGraphMemberDatasources.html) | Retrieve the datasource package history for the specified member accounts in a behavior graph managed by this account | Read | 
| <a name="detective-BatchGetMembershipDatasources"></a>[BatchGetMembershipDatasources](https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetMembershipDatasources.html) | Retrieve the datasource package history of the caller account for the specified graphs | Read | 
| <a name="detective-DescribeOrganizationConfiguration"></a>[DescribeOrganizationConfiguration](https://docs.aws.amazon.com/detective/latest/APIReference/API_DescribeOrganizationConfiguration.html) | View the current configuration related to the Amazon Detective integration with AWS Organizations | Read | 
| <a name="detective-GetFreeTrialEligibility"></a>[GetFreeTrialEligibility](https://docs.aws.amazon.com/detective/latest/adminguide/free-trial-overview.html) | Retrieve a behavior graph's eligibility for a free trial period | Read | 
| <a name="detective-GetGraphIngestState"></a>[GetGraphIngestState](https://docs.aws.amazon.com/detective/latest/adminguide/detective-source-data-about.html) | Retrieve the data ingestion state of a behavior graph | Read | 
| <a name="detective-GetInvestigation"></a>[GetInvestigation](https://docs.aws.amazon.com/detective/latest/APIReference/API_GetInvestigation.html) | Get an investigation's status and metadata | Read | 
| <a name="detective-GetMembers"></a>[GetMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_GetMembers.html) | Retrieve details on specified members of a behavior graph | Read | 
| <a name="detective-GetPricingInformation"></a>[GetPricingInformation](https://docs.aws.amazon.com/detective/latest/adminguide/usage-projected-cost-calculation.html) | Retrieve information about Amazon Detective's pricing | Read | 
| <a name="detective-GetUsageInformation"></a>[GetUsageInformation](https://docs.aws.amazon.com/detective/latest/adminguide/tracking-usage-logging.html) | List usage information of a behavior graph | Read | 
| <a name="detective-InvokeAssistant"></a>[InvokeAssistant](https://docs.aws.amazon.com/detective/latest/userguide/finding-groups-summary.html) | Invoke Detective's Assistant | Read | 
| <a name="detective-ListDatasourcePackages"></a>[ListDatasourcePackages](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListDatasourcePackages.html) | List a graph's datasource package ingest states and timestamps for the most recent state changes in a behavior graph managed by this account | List | 
| <a name="detective-ListGraphs"></a>[ListGraphs](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListGraphs.html) | List behavior graphs managed by this account | List | 
| <a name="detective-ListHighDegreeEntities"></a>[ListHighDegreeEntities](https://docs.aws.amazon.com/detective/latest/userguide/high-volume-entities.html) | Retrieve high volume entities whose relationships cannot be stored by Detective | List | 
| <a name="detective-ListIndicators"></a>[ListIndicators](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListIndicators.html) | List the indicators of an investigation | List | 
| <a name="detective-ListInvestigations"></a>[ListInvestigations](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvestigations.html) | List the investigations of a behavior graph | List | 
| <a name="detective-ListInvitations"></a>[ListInvitations](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvitations.html) | Retrieve details on the behavior graphs to which this account has been invited to join | List | 
| <a name="detective-ListMembers"></a>[ListMembers](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListMembers.html) | Retrieve details on all members of a behavior graph | List | 
| <a name="detective-ListOrganizationAdminAccount"></a>[ListOrganizationAdminAccount](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListOrganizationAdminAccounts.html) | View the current Amazon Detective delegated administrator account for an organization | List | 
| <a name="detective-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/detective/latest/APIReference/API_ListTagsForResource.html) | List the tag values that are assigned to a behavior graph | List | 
| <a name="detective-SearchGraph"></a>[SearchGraph](https://docs.aws.amazon.com/detective/latest/userguide/detective-search.html) | Search the data stored in a behavior graph | Read | 