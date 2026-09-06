

# Actions, resources, and condition keys for Amazon Connect Customer Profiles
<a name="list_customer-profiles"></a>

Amazon Connect Customer Profiles (service prefix: `profile`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connect/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/profile/profile.json) for this service.

**Topics**
+ [API operations defined by Amazon Connect Customer Profiles](#list_customer-profiles-operations)
+ [Actions defined by Amazon Connect Customer Profiles](#list_customer-profiles-actions-as-permissions)
+ [Permission-only actions for Amazon Connect Customer Profiles](#list_customer-profiles-permission-only-actions)
+ [Resource types defined by Amazon Connect Customer Profiles](#list_customer-profiles-resources-for-iam-policies)
+ [Condition keys for Amazon Connect Customer Profiles](#list_customer-profiles-policy-keys)

## API operations defined by Amazon Connect Customer Profiles
<a name="list_customer-profiles-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_customer-profiles-actions-as-permissions).




- **   AddProfileKey  **
  - **IAM action:**  [profile:AddProfileKey](#list_customer-profiles-action-AddProfileKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateStreamForSegments  **
  - **IAM action:**  [profile:AssociateStreamForSegments](#list_customer-profiles-action-AssociateStreamForSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetCalculatedAttributeForProfile  **
  - **IAM action:**  [profile:BatchGetCalculatedAttributeForProfile](#list_customer-profiles-action-BatchGetCalculatedAttributeForProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetProfile  **
  - **IAM action:**  [profile:BatchGetProfile](#list_customer-profiles-action-BatchGetProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateCalculatedAttributeDefinition  **
  - **IAM action:**  [profile:CreateCalculatedAttributeDefinition](#list_customer-profiles-action-CreateCalculatedAttributeDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDomain  **
  - **IAM action:**  [profile:CreateDomain](#list_customer-profiles-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDomainLayout  **
  - **IAM action:**  [profile:CreateDomainLayout](#list_customer-profiles-action-CreateDomainLayout)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventStream  **
  - **IAM action:**  [profile:CreateEventStream](#list_customer-profiles-action-CreateEventStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventTrigger  **
  - **IAM action:**  [profile:CreateEventTrigger](#list_customer-profiles-action-CreateEventTrigger)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIntegrationWorkflow  **
  - **IAM action:**  [profile:CreateIntegrationWorkflow](#list_customer-profiles-action-CreateIntegrationWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** profile.amazonaws.com / **Access level:** Write

- **   CreateProfile  **
  - **IAM action:**  [profile:CreateProfile](#list_customer-profiles-action-CreateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRecommender  **
  - **IAM action:**  [profile:CreateRecommender](#list_customer-profiles-action-CreateRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRecommenderFilter  **
  - **IAM action:**  [profile:CreateRecommenderFilter](#list_customer-profiles-action-CreateRecommenderFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecommenderSchema  **
  - **IAM action:**  [profile:CreateRecommenderSchema](#list_customer-profiles-action-CreateRecommenderSchema)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSegmentDefinition  **
  - **IAM action:**  [profile:CreateSegmentDefinition](#list_customer-profiles-action-CreateSegmentDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSegmentEstimate  **
  - **IAM action:**  [profile:CreateSegmentEstimate](#list_customer-profiles-action-CreateSegmentEstimate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSegmentSnapshot  **
  - **IAM action:**  [profile:CreateSegmentSnapshot](#list_customer-profiles-action-CreateSegmentSnapshot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** profile.amazonaws.com / **Access level:** Write

- **   CreateUploadJob  **
  - **IAM action:**  [profile:CreateUploadJob](#list_customer-profiles-action-CreateUploadJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCalculatedAttributeDefinition  **
  - **IAM action:**  [profile:DeleteCalculatedAttributeDefinition](#list_customer-profiles-action-DeleteCalculatedAttributeDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **IAM action:**  [profile:DeleteDomain](#list_customer-profiles-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainLayout  **
  - **IAM action:**  [profile:DeleteDomainLayout](#list_customer-profiles-action-DeleteDomainLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomainObjectType  **
  - **IAM action:**  [profile:DeleteDomainObjectType](#list_customer-profiles-action-DeleteDomainObjectType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventStream  **
  - **IAM action:**  [profile:DeleteEventStream](#list_customer-profiles-action-DeleteEventStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventTrigger  **
  - **IAM action:**  [profile:DeleteEventTrigger](#list_customer-profiles-action-DeleteEventTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **IAM action:**  [profile:DeleteIntegration](#list_customer-profiles-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfile  **
  - **IAM action:**  [profile:DeleteProfile](#list_customer-profiles-action-DeleteProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfileKey  **
  - **IAM action:**  [profile:DeleteProfileKey](#list_customer-profiles-action-DeleteProfileKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfileObject  **
  - **IAM action:**  [profile:DeleteProfileObject](#list_customer-profiles-action-DeleteProfileObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfileObjectType  **
  - **IAM action:**  [profile:DeleteProfileObjectType](#list_customer-profiles-action-DeleteProfileObjectType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommender  **
  - **IAM action:**  [profile:DeleteRecommender](#list_customer-profiles-action-DeleteRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommenderFilter  **
  - **IAM action:**  [profile:DeleteRecommenderFilter](#list_customer-profiles-action-DeleteRecommenderFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommenderSchema  **
  - **IAM action:**  [profile:DeleteRecommenderSchema](#list_customer-profiles-action-DeleteRecommenderSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSegmentDefinition  **
  - **IAM action:**  [profile:DeleteSegmentDefinition](#list_customer-profiles-action-DeleteSegmentDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSegmentSubscription  **
  - **IAM action:**  [profile:DeleteSegmentSubscription](#list_customer-profiles-action-DeleteSegmentSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [profile:DeleteWorkflow](#list_customer-profiles-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetectProfileObjectType  **
  - **IAM action:**  [profile:DetectProfileObjectType](#list_customer-profiles-action-DetectProfileObjectType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateStreamForSegments  **
  - **IAM action:**  [profile:DisassociateStreamForSegments](#list_customer-profiles-action-DisassociateStreamForSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAutoMergingPreview  **
  - **IAM action:**  [profile:GetAutoMergingPreview](#list_customer-profiles-action-GetAutoMergingPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCalculatedAttributeDefinition  **
  - **IAM action:**  [profile:GetCalculatedAttributeDefinition](#list_customer-profiles-action-GetCalculatedAttributeDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCalculatedAttributeForProfile  **
  - **IAM action:**  [profile:GetCalculatedAttributeForProfile](#list_customer-profiles-action-GetCalculatedAttributeForProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomain  **
  - **IAM action:**  [profile:GetDomain](#list_customer-profiles-action-GetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainLayout  **
  - **IAM action:**  [profile:GetDomainLayout](#list_customer-profiles-action-GetDomainLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainObjectType  **
  - **IAM action:**  [profile:GetDomainObjectType](#list_customer-profiles-action-GetDomainObjectType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventStream  **
  - **IAM action:**  [profile:GetEventStream](#list_customer-profiles-action-GetEventStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventTrigger  **
  - **IAM action:**  [profile:GetEventTrigger](#list_customer-profiles-action-GetEventTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIdentityResolutionJob  **
  - **IAM action:**  [profile:GetIdentityResolutionJob](#list_customer-profiles-action-GetIdentityResolutionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegration  **
  - **IAM action:**  [profile:GetIntegration](#list_customer-profiles-action-GetIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMatches  **
  - **IAM action:**  [profile:GetMatches](#list_customer-profiles-action-GetMatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetObjectTypeAttributeStatistics  **
  - **IAM action:**  [profile:GetObjectTypeAttributeStatistics](#list_customer-profiles-action-GetObjectTypeAttributeStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileHistoryRecord  **
  - **IAM action:**  [profile:GetProfileHistoryRecord](#list_customer-profiles-action-GetProfileHistoryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileObjectType  **
  - **IAM action:**  [profile:GetProfileObjectType](#list_customer-profiles-action-GetProfileObjectType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileObjectTypeTemplate  **
  - **IAM action:**  [profile:GetProfileObjectTypeTemplate](#list_customer-profiles-action-GetProfileObjectTypeTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfileRecommendations  **
  - **IAM action:**  [profile:GetProfileRecommendations](#list_customer-profiles-action-GetProfileRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommender  **
  - **IAM action:**  [profile:GetRecommender](#list_customer-profiles-action-GetRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommenderFilter  **
  - **IAM action:**  [profile:GetRecommenderFilter](#list_customer-profiles-action-GetRecommenderFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommenderSchema  **
  - **IAM action:**  [profile:GetRecommenderSchema](#list_customer-profiles-action-GetRecommenderSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentDefinition  **
  - **IAM action:**  [profile:GetSegmentDefinition](#list_customer-profiles-action-GetSegmentDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentEstimate  **
  - **IAM action:**  [profile:GetSegmentEstimate](#list_customer-profiles-action-GetSegmentEstimate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentMembership  **
  - **IAM action:**  [profile:GetSegmentMembership](#list_customer-profiles-action-GetSegmentMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentSnapshot  **
  - **IAM action:**  [profile:GetSegmentSnapshot](#list_customer-profiles-action-GetSegmentSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentSubscription  **
  - **IAM action:**  [profile:GetSegmentSubscription](#list_customer-profiles-action-GetSegmentSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSimilarProfiles  **
  - **IAM action:**  [profile:GetSimilarProfiles](#list_customer-profiles-action-GetSimilarProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetStreamForSegments  **
  - **IAM action:**  [profile:GetStreamForSegments](#list_customer-profiles-action-GetStreamForSegments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUploadJob  **
  - **IAM action:**  [profile:GetUploadJob](#list_customer-profiles-action-GetUploadJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUploadJobPath  **
  - **IAM action:**  [profile:GetUploadJobPath](#list_customer-profiles-action-GetUploadJobPath) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflow  **
  - **IAM action:**  [profile:GetWorkflow](#list_customer-profiles-action-GetWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowSteps  **
  - **IAM action:**  [profile:GetWorkflowSteps](#list_customer-profiles-action-GetWorkflowSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountIntegrations  **
  - **IAM action:**  [profile:ListAccountIntegrations](#list_customer-profiles-action-ListAccountIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCalculatedAttributeDefinitions  **
  - **IAM action:**  [profile:ListCalculatedAttributeDefinitions](#list_customer-profiles-action-ListCalculatedAttributeDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCalculatedAttributesForProfile  **
  - **IAM action:**  [profile:ListCalculatedAttributesForProfile](#list_customer-profiles-action-ListCalculatedAttributesForProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainLayouts  **
  - **IAM action:**  [profile:ListDomainLayouts](#list_customer-profiles-action-ListDomainLayouts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainObjectTypes  **
  - **IAM action:**  [profile:ListDomainObjectTypes](#list_customer-profiles-action-ListDomainObjectTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomains  **
  - **IAM action:**  [profile:ListDomains](#list_customer-profiles-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventStreams  **
  - **IAM action:**  [profile:ListEventStreams](#list_customer-profiles-action-ListEventStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventTriggers  **
  - **IAM action:**  [profile:ListEventTriggers](#list_customer-profiles-action-ListEventTriggers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIdentityResolutionJobs  **
  - **IAM action:**  [profile:ListIdentityResolutionJobs](#list_customer-profiles-action-ListIdentityResolutionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntegrations  **
  - **IAM action:**  [profile:ListIntegrations](#list_customer-profiles-action-ListIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListObjectTypeAttributeValues  **
  - **IAM action:**  [profile:ListObjectTypeAttributeValues](#list_customer-profiles-action-ListObjectTypeAttributeValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListObjectTypeAttributes  **
  - **IAM action:**  [profile:ListObjectTypeAttributes](#list_customer-profiles-action-ListObjectTypeAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileAttributeValues  **
  - **IAM action:**  [profile:ListProfileAttributeValues](#list_customer-profiles-action-ListProfileAttributeValues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileHistoryRecords  **
  - **IAM action:**  [profile:ListProfileHistoryRecords](#list_customer-profiles-action-ListProfileHistoryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileObjectTypeTemplates  **
  - **IAM action:**  [profile:ListProfileObjectTypeTemplates](#list_customer-profiles-action-ListProfileObjectTypeTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileObjectTypes  **
  - **IAM action:**  [profile:ListProfileObjectTypes](#list_customer-profiles-action-ListProfileObjectTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileObjects  **
  - **IAM action:**  [profile:ListProfileObjects](#list_customer-profiles-action-ListProfileObjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommenderFilters  **
  - **IAM action:**  [profile:ListRecommenderFilters](#list_customer-profiles-action-ListRecommenderFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommenderRecipes  **
  - **IAM action:**  [profile:ListRecommenderRecipes](#list_customer-profiles-action-ListRecommenderRecipes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommenderSchemas  **
  - **IAM action:**  [profile:ListRecommenderSchemas](#list_customer-profiles-action-ListRecommenderSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommenders  **
  - **IAM action:**  [profile:ListRecommenders](#list_customer-profiles-action-ListRecommenders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleBasedMatches  **
  - **IAM action:**  [profile:ListRuleBasedMatches](#list_customer-profiles-action-ListRuleBasedMatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSegmentDefinitions  **
  - **IAM action:**  [profile:ListSegmentDefinitions](#list_customer-profiles-action-ListSegmentDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSegmentSubscriptionEvents  **
  - **IAM action:**  [profile:ListSegmentSubscriptionEvents](#list_customer-profiles-action-ListSegmentSubscriptionEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [profile:ListTagsForResource](#list_customer-profiles-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUploadJobs  **
  - **IAM action:**  [profile:ListUploadJobs](#list_customer-profiles-action-ListUploadJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [profile:ListWorkflows](#list_customer-profiles-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   MergeProfiles  **
  - **IAM action:**  [profile:MergeProfiles](#list_customer-profiles-action-MergeProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDomainObjectType  **
  - **IAM action:**  [profile:PutDomainObjectType](#list_customer-profiles-action-PutDomainObjectType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutIntegration  **
  - **IAM action:**  [profile:PutIntegration](#list_customer-profiles-action-PutIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutProfileObject  **
  - **IAM action:**  [profile:PutProfileObject](#list_customer-profiles-action-PutProfileObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutProfileObjectType  **
  - **IAM action:**  [profile:PutProfileObjectType](#list_customer-profiles-action-PutProfileObjectType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutSegmentSubscription  **
  - **IAM action:**  [profile:PutSegmentSubscription](#list_customer-profiles-action-PutSegmentSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchProfiles  **
  - **IAM action:**  [profile:SearchProfiles](#list_customer-profiles-action-SearchProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartRecommender  **
  - **IAM action:**  [profile:StartRecommender](#list_customer-profiles-action-StartRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartUploadJob  **
  - **IAM action:**  [profile:StartUploadJob](#list_customer-profiles-action-StartUploadJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRecommender  **
  - **IAM action:**  [profile:StopRecommender](#list_customer-profiles-action-StopRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopUploadJob  **
  - **IAM action:**  [profile:StopUploadJob](#list_customer-profiles-action-StopUploadJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [profile:TagResource](#list_customer-profiles-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [profile:UntagResource](#list_customer-profiles-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCalculatedAttributeDefinition  **
  - **IAM action:**  [profile:UpdateCalculatedAttributeDefinition](#list_customer-profiles-action-UpdateCalculatedAttributeDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomain  **
  - **IAM action:**  [profile:UpdateDomain](#list_customer-profiles-action-UpdateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainLayout  **
  - **IAM action:**  [profile:UpdateDomainLayout](#list_customer-profiles-action-UpdateDomainLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventTrigger  **
  - **IAM action:**  [profile:UpdateEventTrigger](#list_customer-profiles-action-UpdateEventTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfile  **
  - **IAM action:**  [profile:UpdateProfile](#list_customer-profiles-action-UpdateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecommender  **
  - **IAM action:**  [profile:UpdateRecommender](#list_customer-profiles-action-UpdateRecommender) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Connect Customer Profiles
<a name="list_customer-profiles-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddProfileKey](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AddProfileKey.html)  **
  - **Description:** Grants permission to add a profile key
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateStreamForSegments](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AssociateStreamForSegments.html)  **
  - **Description:** Grants permission to associate an Amazon Kinesis data stream to receive segment membership events for a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetCalculatedAttributeForProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchGetCalculatedAttributeForProfile.html)  **
  - **Description:** Grants permission to retrieve a calculated attribute for the specific profiles in the domain
  - **Resource types (\*required):** [calculated-attributes\*](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_BatchGetProfile.html)  **
  - **Description:** Grants permission to get profiles in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateCalculatedAttributeDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateCalculatedAttributeDefinition.html)  **
  - **Description:** Grants permission to create a calculated attribute definition in the domain
  - **Resource types (\*required):** [calculated-attributes\*](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a Domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDomainLayout](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomainLayout.html)  **
  - **Description:** Grants permission to create a layout in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [layouts\*](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventStream](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateEventStream.html)  **
  - **Description:** Grants permission to put an event stream in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-streams\*](#list_customer-profiles-resource-event-streams) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventTrigger](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateEventTrigger.html)  **
  - **Description:** Grants permission to create an event trigger in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-triggers\*](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegrationWorkflow](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateIntegrationWorkflow.html)  **
  - **Description:** Grants permission to create an integration workflow in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrations\*](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateProfile.html)  **
  - **Description:** Grants permission to create a profile in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateRecommender.html)  **
  - **Description:** Grants permission to create a Recommender in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecommenderFilter](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateRecommenderFilter.html)  **
  - **Description:** Grants permission to create a recommender filter in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommender-filters\*](#list_customer-profiles-resource-recommender-filters) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecommenderSchema](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateRecommenderSchema.html)  **
  - **Description:** Grants permission to create a recommender schema in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommender-schemas\*](#list_customer-profiles-resource-recommender-schemas) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSegmentDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateSegmentDefinition.html)  **
  - **Description:** Grants permission to create a segment definition in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSegmentEstimate](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateSegmentEstimate.html)  **
  - **Description:** Grants permission to create a segment estimate in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSegmentSnapshot](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateSegmentSnapshot.html)  **
  - **Description:** Grants permission to create a segment snapshot in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUploadJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateUploadJob.html)  **
  - **Description:** Grants permission to create an upload job in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCalculatedAttributeDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteCalculatedAttributeDefinition.html)  **
  - **Description:** Grants permission to delete a calculated attribute definition in the domain
  - **Resource types (\*required):** [calculated-attributes\*](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a Domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainLayout](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteDomainLayout.html)  **
  - **Description:** Grants permission to delete a layout in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [layouts\*](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteDomainObjectType.html)  **
  - **Description:** Grants permission to delete a specific domain object type in the domain
  - **Resource types (\*required):** [domain-object-types\*](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventStream](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteEventStream.html)  **
  - **Description:** Grants permission to delete an event stream in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-streams\*](#list_customer-profiles-resource-event-streams) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventTrigger](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteEventTrigger.html)  **
  - **Description:** Grants permission to delete an event trigger in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-triggers\*](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteIntegration.html)  **
  - **Description:** Grants permission to delete a integration in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrations\*](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteProfile.html)  **
  - **Description:** Grants permission to delete a profile
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfileKey](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteProfileKey.html)  **
  - **Description:** Grants permission to delete a profile key
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfileObject](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteProfileObject.html)  **
  - **Description:** Grants permission to delete a profile object
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteProfileObjectType.html)  **
  - **Description:** Grants permission to delete a specific profile object type in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteRecommender.html)  **
  - **Description:** Grants permission to delete a recommender in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecommenderFilter](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteRecommenderFilter.html)  **
  - **Description:** Grants permission to delete a recommender filter in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender-filters\*](#list_customer-profiles-resource-recommender-filters) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecommenderSchema](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteRecommenderSchema.html)  **
  - **Description:** Grants permission to delete a recommender schema in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender-schemas\*](#list_customer-profiles-resource-recommender-schemas) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSegmentDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteSegmentDefinition.html)  **
  - **Description:** Grants permission to delete a segment definition in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSegmentSubscription](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteSegmentSubscription.html)  **
  - **Description:** Grants permission to delete a segment subscription for membership events
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteWorkflow.html)  **
  - **Description:** Grants permission to delete a workflow in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DetectProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DetectProfileObjectType.html)  **
  - **Description:** Grants permission to auto detect object type
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateStreamForSegments](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DisassociateStreamForSegments.html)  **
  - **Description:** Grants permission to disassociate the Amazon Kinesis data stream configured for segment membership events in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAutoMergingPreview](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetAutoMergingPreview.html)  **
  - **Description:** Grants permission to get a preview of auto merging in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCalculatedAttributeDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeDefinition.html)  **
  - **Description:** Grants permission to get a calculated attribute definition in the domain
  - **Resource types (\*required):** [calculated-attributes\*](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCalculatedAttributeForProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeForProfile.html)  **
  - **Description:** Grants permission to retrieve a calculated attribute for a specific profile in the domain
  - **Resource types (\*required):** [calculated-attributes\*](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetDomain.html)  **
  - **Description:** Grants permission to get a specific domain in an account
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainLayout](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetDomainLayout.html)  **
  - **Description:** Grants permission to get a layout in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [layouts\*](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetDomainObjectType.html)  **
  - **Description:** Grants permission to get a specific domain object type in the domain
  - **Resource types (\*required):** [domain-object-types\*](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventStream](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetEventStream.html)  **
  - **Description:** Grants permission to get a specific event stream in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-streams\*](#list_customer-profiles-resource-event-streams) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventTrigger](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetEventTrigger.html)  **
  - **Description:** Grants permission to get an event trigger in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-triggers\*](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIdentityResolutionJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetIdentityResolutionJob.html)  **
  - **Description:** Grants permission to get an identity resolution job in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegration](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetIntegration.html)  **
  - **Description:** Grants permission to get a specific integrations in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrations\*](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html)  **
  - **Description:** Grants permission to get profile matches in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetObjectTypeAttributeStatistics](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetObjectTypeAttributeStatistics.html)  **
  - **Description:** Grants permission to get statistics of a specific attribute for object type in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfileHistoryRecord](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileHistoryRecord.html)  **
  - **Description:** Grants permission to get a profile history record for a profile in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfileInsights](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileInsights.html)  **
  - **Description:** Grants permission to list insights for a profile
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectType.html)  **
  - **Description:** Grants permission to get a specific profile object type in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfileObjectTypeTemplate](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectTypeTemplate.html)  **
  - **Description:** Grants permission to get a specific object type template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProfileRecommendations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileRecommendations.html)  **
  - **Description:** Grants permission to list recommendations for a profile
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommender.html)  **
  - **Description:** Grants permission to get Recommender details in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommenderFilter](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommenderFilter.html)  **
  - **Description:** Grants permission to get recommender filter details in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender-filters\*](#list_customer-profiles-resource-recommender-filters) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommenderSchema](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetRecommenderSchema.html)  **
  - **Description:** Grants permission to get recommender schema details in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender-schemas\*](#list_customer-profiles-resource-recommender-schemas) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentDefinition.html)  **
  - **Description:** Grants permission to get a segment definition in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentEstimate](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentEstimate.html)  **
  - **Description:** Grants permission to get a segment estimate in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentMembership](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentMembership.html)  **
  - **Description:** Grants permission to determine if the given profiles are part of a segment in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentSnapshot](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentSnapshot.html)  **
  - **Description:** Grants permission to get a segment snapshot in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegmentSubscription](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSegmentSubscription.html)  **
  - **Description:** Grants permission to get the configuration, schedule, and status of a segment subscription for membership events
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSimilarProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetSimilarProfiles.html)  **
  - **Description:** Grants permission to get all the similar profiles in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetStreamForSegments](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetStreamForSegments.html)  **
  - **Description:** Grants permission to get information about the segment membership event stream configured for a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUploadJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetUploadJob.html)  **
  - **Description:** Grants permission to get details of an upload job in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUploadJobPath](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetUploadJobPath.html)  **
  - **Description:** Grants permission to get a pre-signed URL to upload file for an upload job
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflow](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetWorkflow.html)  **
  - **Description:** Grants permission to get workflow details in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowSteps](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetWorkflowSteps.html)  **
  - **Description:** Grants permission to get workflow step details in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccountIntegrations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListAccountIntegrations.html)  **
  - **Description:** Grants permission to list all the integrations in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCalculatedAttributeDefinitions](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListCalculatedAttributeDefinitions.html)  **
  - **Description:** Grants permission to list all the calculated attribute definitions in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCalculatedAttributesForProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListCalculatedAttributesForProfile.html)  **
  - **Description:** Grants permission to list all calculated attributes for a specific profile in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainLayouts](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainLayouts.html)  **
  - **Description:** Grants permission to list all the layouts in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainObjectTypes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainObjectTypes.html)  **
  - **Description:** Grants permission to list all the domain object types in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainObjects](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainObjects.html)  **
  - **Description:** Grants permission to list domain objects in a domain
  - **Resource types (\*required):** [domain-object-types\*](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list all the domains in an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEventStreams](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListEventStreams.html)  **
  - **Description:** Grants permission to list all the event streams in a specific domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEventTriggers](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListEventTriggers.html)  **
  - **Description:** Grants permission to list all the event triggers in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIdentityResolutionJobs](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListIdentityResolutionJobs.html)  **
  - **Description:** Grants permission to list identity resolution jobs in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntegrations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListIntegrations.html)  **
  - **Description:** Grants permission to list all the integrations in a specific domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListObjectTypeAttributeValues](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListObjectTypeAttributeValues.html)  **
  - **Description:** Grants permission to list values of a specific attribute for object type in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListObjectTypeAttributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListObjectTypeAttributes.html)  **
  - **Description:** Grants permission to list all the attributes of a specific object type in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfileAttributeValues](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileAttributeValues.html)  **
  - **Description:** Grants permission to list all the values of a profile attribute in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfileHistoryRecords](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileHistoryRecords.html)  **
  - **Description:** Grants permission to list all the profile history records for a profile in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html)  **
  - **Description:** Grants permission to list all the profile object type templates in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfileObjectTypes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypes.html)  **
  - **Description:** Grants permission to list all the profile object types in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfileObjects](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjects.html)  **
  - **Description:** Grants permission to list all the profile objects for a profile
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecommenderFilters](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderFilters.html)  **
  - **Description:** Grants permission to list all recommender filters in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecommenderRecipes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderRecipes.html)  **
  - **Description:** Grants permission to list all the Recommenders Recipes in the domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommenderSchemas](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenderSchemas.html)  **
  - **Description:** Grants permission to list all recommender schemas in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecommenders](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRecommenders.html)  **
  - **Description:** Grants permission to list all the Recommenders in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRuleBasedMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListRuleBasedMatches.html)  **
  - **Description:** Grants permission to list all the rule-based matching result in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSegmentDefinitions](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListSegmentDefinitions.html)  **
  - **Description:** Grants permission to list all the segment definitions in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSegmentSubscriptionEvents](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListSegmentSubscriptionEvents.html)  **
  - **Description:** Grants permission to list the most recent segment membership events for a segment
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [calculated-attributes](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domain-object-types](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-streams](#list_customer-profiles-resource-event-streams) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-triggers](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrations](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [layouts](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender-filters](#list_customer-profiles-resource-recommender-filters) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommender-schemas](#list_customer-profiles-resource-recommender-schemas) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUploadJobs](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListUploadJobs.html)  **
  - **Description:** Grants permission to list all upload jobs in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListWorkflows.html)  **
  - **Description:** Grants permission to list all the workflows in a specific domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [MergeProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MergeProfiles.html)  **
  - **Description:** Grants permission to merge profiles in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDomainObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutDomainObjectType.html)  **
  - **Description:** Grants permission to put a specific domain object type in the domain
  - **Resource types (\*required):** [domain-object-types\*](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutIntegration](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutIntegration.html)  **
  - **Description:** Grants permission to put a integration in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrations\*](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [PutProfileObject](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObject.html)  **
  - **Description:** Grants permission to put an object for a profile
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObjectType.html)  **
  - **Description:** Grants permission to put a specific profile object type in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [object-types\*](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Write

- **   [PutSegmentSubscription](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutSegmentSubscription.html)  **
  - **Description:** Grants permission to create or update a segment subscription for membership events
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [segment-definitions\*](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html)  **
  - **Description:** Grants permission to search for profiles in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_StartRecommender.html)  **
  - **Description:** Grants permission to start a recommender in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartUploadJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_StartUploadJob.html)  **
  - **Description:** Grants permission to start an upload job in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_StopRecommender.html)  **
  - **Description:** Grants permission to stop a recommender in a domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopUploadJob](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_StopUploadJob.html)  **
  - **Description:** Grants permission to stop an upload job in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to adds tags to a resource
  - **Resource types (\*required):** [calculated-attributes](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [domain-object-types](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [domains](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [event-streams](#list_customer-profiles-resource-event-streams) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [event-triggers](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [integrations](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [layouts](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [object-types](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommender-filters](#list_customer-profiles-resource-recommender-filters) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommender-schemas](#list_customer-profiles-resource-recommender-schemas) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommenders](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [segment-definitions](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_customer-profiles-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [calculated-attributes](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [domain-object-types](#list_customer-profiles-resource-domain-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [domains](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [event-streams](#list_customer-profiles-resource-event-streams) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [event-triggers](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [integrations](#list_customer-profiles-resource-integrations) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [layouts](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [object-types](#list_customer-profiles-resource-object-types) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommender-filters](#list_customer-profiles-resource-recommender-filters) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommender-schemas](#list_customer-profiles-resource-recommender-schemas) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [recommenders](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Resource types (\*required):** [segment-definitions](#list_customer-profiles-resource-segment-definitions) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_customer-profiles-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCalculatedAttributeDefinition](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateCalculatedAttributeDefinition.html)  **
  - **Description:** Grants permission to update a calculated attribute definition in the domain
  - **Resource types (\*required):** [calculated-attributes\*](#list_customer-profiles-resource-calculated-attributes) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html)  **
  - **Description:** Grants permission to update a Domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainLayout](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomainLayout.html)  **
  - **Description:** Grants permission to update a layout in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [layouts\*](#list_customer-profiles-resource-layouts) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventTrigger](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateEventTrigger.html)  **
  - **Description:** Grants permission to update an event trigger in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-triggers\*](#list_customer-profiles-resource-event-triggers) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html)  **
  - **Description:** Grants permission to update a profile in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecommender](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateRecommender.html)  **
  - **Description:** Grants permission to update a Recommender in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [recommenders\*](#list_customer-profiles-resource-recommenders) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Connect Customer Profiles
<a name="list_customer-profiles-permission-only-actions"></a>

The following actions are defined by Amazon Connect Customer Profiles but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateSnapshot](${UserGuideDocPage}set-up-bulk-export.html)  **
  - **Description:** Grants permission to create a snapshot in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetSnapshot](${UserGuideDocPage}set-up-bulk-export.html)  **
  - **Description:** Grants permission to get a snapshot in the domain
  - **Resource types (\*required):** [domains\*](#list_customer-profiles-resource-domains)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Connect Customer Profiles
<a name="list_customer-profiles-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [calculated-attributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/calculated-attributes/${CalculatedAttributeName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [domain-object-types](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/domain-object-types/${ObjectTypeName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [domains](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [event-streams](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/event-streams/${EventStreamName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [event-triggers](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/event-triggers/${EventTriggerName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [integrations](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/integrations/${Uri} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [layouts](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/layouts/${LayoutDefinitionName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [object-types](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/object-types/${ObjectTypeName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [recommender-filters](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/recommender-filters/${RecommenderFilterName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [recommender-schemas](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/recommender-schemas/${RecommenderSchemaName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [recommenders](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/recommenders/${RecommenderTypeName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 
|  [segment-definitions](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/)  | arn:${Partition}:profile:${Region}:${Account}:domains/${DomainName}/segment-definitions/${SegmentDefinitionName} | [aws:ResourceTag/${TagKey}](#list_customer-profiles-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Connect Customer Profiles
<a name="list_customer-profiles-policy-keys"></a>

Amazon Connect Customer Profiles defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by a key that is present in the request the user makes to the customer profile service | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by a tag key and value pair | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-permissions.html#iam-contextkeys)  | Filters access by the list of all the tag key names present in the request the user makes to the customer profile service | ArrayOfString | 