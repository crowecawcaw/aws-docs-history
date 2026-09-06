

# Data retrieval APIs for Amazon Connect Customer Profiles
<a name="amazonconnectcustomerprofiles"></a>

Amazon Connect Customer Profiles provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="profile-BatchGetCalculatedAttributeForProfile"></a>[BatchGetCalculatedAttributeForProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchGetCalculatedAttributeForProfile.html) | Retrieve a calculated attribute for the specific profiles in the domain | Read | 
| <a name="profile-BatchGetProfile"></a>[BatchGetProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchGetProfile.html) | Get profiles in the domain | Read | 
| <a name="profile-DetectProfileObjectType"></a>[DetectProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DetectProfileObjectType.html) | Auto detect object type | Read | 
| <a name="profile-GetAutoMergingPreview"></a>[GetAutoMergingPreview](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetAutoMergingPreview.html) | Get a preview of auto merging in a domain | Read | 
| <a name="profile-GetCalculatedAttributeDefinition"></a>[GetCalculatedAttributeDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeDefinition.html) | Get a calculated attribute definition in the domain | Read | 
| <a name="profile-GetCalculatedAttributeForProfile"></a>[GetCalculatedAttributeForProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeForProfile.html) | Retrieve a calculated attribute for a specific profile in the domain | Read | 
| <a name="profile-GetDomain"></a>[GetDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetDomain.html) | Get a specific domain in an account | Read | 
| <a name="profile-GetDomainLayout"></a>[GetDomainLayout](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetDomainLayout.html) | Get a layout in the domain | Read | 
| <a name="profile-GetDomainObjectType"></a>[GetDomainObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetDomainObjectType.html) | Get a specific domain object type in the domain | Read | 
| <a name="profile-GetEventStream"></a>[GetEventStream](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetEventStream.html) | Get a specific event stream in a domain | Read | 
| <a name="profile-GetEventTrigger"></a>[GetEventTrigger](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetEventTrigger.html) | Get an event trigger in the domain | Read | 
| <a name="profile-GetIdentityResolutionJob"></a>[GetIdentityResolutionJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetIdentityResolutionJob.html) | Get an identity resolution job in a domain | Read | 
| <a name="profile-GetIntegration"></a>[GetIntegration](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetIntegration.html) | Get a specific integrations in a domain | Read | 
| <a name="profile-GetMatches"></a>[GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) | Get profile matches in a domain | List | 
| <a name="profile-GetObjectTypeAttributeStatistics"></a>[GetObjectTypeAttributeStatistics](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetObjectTypeAttributeStatistics.html) | Get statistics of a specific attribute for object type in the domain | Read | 
| <a name="profile-GetProfileHistoryRecord"></a>[GetProfileHistoryRecord](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileHistoryRecord.html) | Get a profile history record for a profile in a domain | Read | 
| <a name="profile-GetProfileInsights"></a>[GetProfileInsights](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileInsights.html) | List insights for a profile | Read | 
| <a name="profile-GetProfileObjectType"></a>[GetProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectType.html) | Get a specific profile object type in the domain | Read | 
| <a name="profile-GetProfileObjectTypeTemplate"></a>[GetProfileObjectTypeTemplate](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectTypeTemplate.html) | Get a specific object type template | Read | 
| <a name="profile-GetProfileRecommendations"></a>[GetProfileRecommendations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileRecommendations.html) | List recommendations for a profile | Read | 
| <a name="profile-GetRecommender"></a>[GetRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommender.html) | Get Recommender details in a domain | Read | 
| <a name="profile-GetRecommenderFilter"></a>[GetRecommenderFilter](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommenderFilter.html) | Get recommender filter details in the domain | Read | 
| <a name="profile-GetRecommenderSchema"></a>[GetRecommenderSchema](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommenderSchema.html) | Get recommender schema details in the domain | Read | 
| <a name="profile-GetSegmentDefinition"></a>[GetSegmentDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentDefinition.html) | Get a segment definition in the domain | Read | 
| <a name="profile-GetSegmentEstimate"></a>[GetSegmentEstimate](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentEstimate.html) | Get a segment estimate in the domain | Read | 
| <a name="profile-GetSegmentMembership"></a>[GetSegmentMembership](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentMembership.html) | Determine if the given profiles are part of a segment in the domain | Read | 
| <a name="profile-GetSegmentSnapshot"></a>[GetSegmentSnapshot](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentSnapshot.html) | Get a segment snapshot in the domain | Read | 
| <a name="profile-GetSegmentSubscription"></a>[GetSegmentSubscription](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentSubscription.html) | Get the configuration, schedule, and status of a segment subscription for membership events | Read | 
| <a name="profile-GetSimilarProfiles"></a>[GetSimilarProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSimilarProfiles.html) | Get all the similar profiles in the domain | List | 
| <a name="profile-GetSnapshot"></a>[GetSnapshot](${UserGuideDocPage}set-up-bulk-export.html) | Get a snapshot in the domain | Read | 
| <a name="profile-GetStreamForSegments"></a>[GetStreamForSegments](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetStreamForSegments.html) | Get information about the segment membership event stream configured for a domain | Read | 
| <a name="profile-GetUploadJob"></a>[GetUploadJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetUploadJob.html) | Get details of an upload job in the domain | Read | 
| <a name="profile-GetUploadJobPath"></a>[GetUploadJobPath](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetUploadJobPath.html) | Get a pre-signed URL to upload file for an upload job | Read | 
| <a name="profile-GetWorkflow"></a>[GetWorkflow](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetWorkflow.html) | Get workflow details in a domain | Read | 
| <a name="profile-GetWorkflowSteps"></a>[GetWorkflowSteps](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetWorkflowSteps.html) | Get workflow step details in a domain | Read | 
| <a name="profile-ListAccountIntegrations"></a>[ListAccountIntegrations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListAccountIntegrations.html) | List all the integrations in the account | List | 
| <a name="profile-ListCalculatedAttributeDefinitions"></a>[ListCalculatedAttributeDefinitions](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListCalculatedAttributeDefinitions.html) | List all the calculated attribute definitions in the domain | List | 
| <a name="profile-ListCalculatedAttributesForProfile"></a>[ListCalculatedAttributesForProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListCalculatedAttributesForProfile.html) | List all calculated attributes for a specific profile in the domain | List | 
| <a name="profile-ListDomainLayouts"></a>[ListDomainLayouts](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainLayouts.html) | List all the layouts in the domain | List | 
| <a name="profile-ListDomainObjectTypes"></a>[ListDomainObjectTypes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainObjectTypes.html) | List all the domain object types in the domain | List | 
| <a name="profile-ListDomainObjects"></a>[ListDomainObjects](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainObjects.html) | List domain objects in a domain | List | 
| <a name="profile-ListDomains"></a>[ListDomains](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomains.html) | List all the domains in an account | List | 
| <a name="profile-ListEventStreams"></a>[ListEventStreams](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListEventStreams.html) | List all the event streams in a specific domain | List | 
| <a name="profile-ListEventTriggers"></a>[ListEventTriggers](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListEventTriggers.html) | List all the event triggers in the domain | List | 
| <a name="profile-ListIdentityResolutionJobs"></a>[ListIdentityResolutionJobs](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListIdentityResolutionJobs.html) | List identity resolution jobs in a domain | List | 
| <a name="profile-ListIntegrations"></a>[ListIntegrations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListIntegrations.html) | List all the integrations in a specific domain | List | 
| <a name="profile-ListObjectTypeAttributeValues"></a>[ListObjectTypeAttributeValues](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListObjectTypeAttributeValues.html) | List values of a specific attribute for object type in the domain | List | 
| <a name="profile-ListObjectTypeAttributes"></a>[ListObjectTypeAttributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListObjectTypeAttributes.html) | List all the attributes of a specific object type in the domain | List | 
| <a name="profile-ListProfileAttributeValues"></a>[ListProfileAttributeValues](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileAttributeValues.html) | List all the values of a profile attribute in the domain | List | 
| <a name="profile-ListProfileHistoryRecords"></a>[ListProfileHistoryRecords](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileHistoryRecords.html) | List all the profile history records for a profile in a domain | List | 
| <a name="profile-ListProfileObjectTypeTemplates"></a>[ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html) | List all the profile object type templates in the account | List | 
| <a name="profile-ListProfileObjectTypes"></a>[ListProfileObjectTypes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypes.html) | List all the profile object types in the domain | List | 
| <a name="profile-ListProfileObjects"></a>[ListProfileObjects](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjects.html) | List all the profile objects for a profile | List | 
| <a name="profile-ListRecommenderFilters"></a>[ListRecommenderFilters](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderFilters.html) | List all recommender filters in the domain | List | 
| <a name="profile-ListRecommenderRecipes"></a>[ListRecommenderRecipes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderRecipes.html) | List all the Recommenders Recipes in the domain | List | 
| <a name="profile-ListRecommenderSchemas"></a>[ListRecommenderSchemas](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderSchemas.html) | List all recommender schemas in the domain | List | 
| <a name="profile-ListRecommenders"></a>[ListRecommenders](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenders.html) | List all the Recommenders in the domain | List | 
| <a name="profile-ListRuleBasedMatches"></a>[ListRuleBasedMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRuleBasedMatches.html) | List all the rule-based matching result in the domain | List | 
| <a name="profile-ListSegmentDefinitions"></a>[ListSegmentDefinitions](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListSegmentDefinitions.html) | List all the segment definitions in the domain | List | 
| <a name="profile-ListSegmentSubscriptionEvents"></a>[ListSegmentSubscriptionEvents](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListSegmentSubscriptionEvents.html) | List the most recent segment membership events for a segment | Read | 
| <a name="profile-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListTagsForResource.html) | List tags for a resource | Read | 
| <a name="profile-ListUploadJobs"></a>[ListUploadJobs](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListUploadJobs.html) | List all upload jobs in the domain | List | 
| <a name="profile-ListWorkflows"></a>[ListWorkflows](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListWorkflows.html) | List all the workflows in a specific domain | List | 
| <a name="profile-SearchProfiles"></a>[SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) | Search for profiles in a domain | Read | 