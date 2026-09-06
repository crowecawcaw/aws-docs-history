

# Actions, resources, and condition keys for Amazon Kendra
<a name="list_kendra"></a>

Amazon Kendra (service prefix: `kendra`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/kendra/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/kendra/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/kendra/latest/dg/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kendra/kendra.json) for this service.

**Topics**
+ [API operations defined by Amazon Kendra](#list_kendra-operations)
+ [Actions defined by Amazon Kendra](#list_kendra-actions-as-permissions)
+ [Resource types defined by Amazon Kendra](#list_kendra-resources-for-iam-policies)
+ [Condition keys for Amazon Kendra](#list_kendra-policy-keys)

## API operations defined by Amazon Kendra
<a name="list_kendra-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kendra-actions-as-permissions).




- **   AssociateEntitiesToExperience  **
  - **IAM action:**  [kendra:AssociateEntitiesToExperience](#list_kendra-action-AssociateEntitiesToExperience) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociatePersonasToEntities  **
  - **IAM action:**  [kendra:AssociatePersonasToEntities](#list_kendra-action-AssociatePersonasToEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteDocument  **
  - **IAM action:**  [kendra:BatchDeleteDocument](#list_kendra-action-BatchDeleteDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteFeaturedResultsSet  **
  - **IAM action:**  [kendra:BatchDeleteFeaturedResultsSet](#list_kendra-action-BatchDeleteFeaturedResultsSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetDocumentStatus  **
  - **IAM action:**  [kendra:BatchGetDocumentStatus](#list_kendra-action-BatchGetDocumentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutDocument  **
  - **IAM action:**  [kendra:BatchPutDocument](#list_kendra-action-BatchPutDocument)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   ClearQuerySuggestions  **
  - **IAM action:**  [kendra:ClearQuerySuggestions](#list_kendra-action-ClearQuerySuggestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAccessControlConfiguration  **
  - **IAM action:**  [kendra:CreateAccessControlConfiguration](#list_kendra-action-CreateAccessControlConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataSource  **
  - **IAM action:**  [kendra:CreateDataSource](#list_kendra-action-CreateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   CreateExperience  **
  - **IAM action:**  [kendra:CreateExperience](#list_kendra-action-CreateExperience)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   CreateFaq  **
  - **IAM action:**  [kendra:CreateFaq](#list_kendra-action-CreateFaq)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   CreateFeaturedResultsSet  **
  - **IAM action:**  [kendra:CreateFeaturedResultsSet](#list_kendra-action-CreateFeaturedResultsSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIndex  **
  - **IAM action:**  [kendra:CreateIndex](#list_kendra-action-CreateIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   CreateQuerySuggestionsBlockList  **
  - **IAM action:**  [kendra:CreateQuerySuggestionsBlockList](#list_kendra-action-CreateQuerySuggestionsBlockList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   CreateThesaurus  **
  - **IAM action:**  [kendra:CreateThesaurus](#list_kendra-action-CreateThesaurus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   DeleteAccessControlConfiguration  **
  - **IAM action:**  [kendra:DeleteAccessControlConfiguration](#list_kendra-action-DeleteAccessControlConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [kendra:DeleteDataSource](#list_kendra-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExperience  **
  - **IAM action:**  [kendra:DeleteExperience](#list_kendra-action-DeleteExperience) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFaq  **
  - **IAM action:**  [kendra:DeleteFaq](#list_kendra-action-DeleteFaq) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIndex  **
  - **IAM action:**  [kendra:DeleteIndex](#list_kendra-action-DeleteIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePrincipalMapping  **
  - **IAM action:**  [kendra:DeletePrincipalMapping](#list_kendra-action-DeletePrincipalMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQuerySuggestionsBlockList  **
  - **IAM action:**  [kendra:DeleteQuerySuggestionsBlockList](#list_kendra-action-DeleteQuerySuggestionsBlockList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThesaurus  **
  - **IAM action:**  [kendra:DeleteThesaurus](#list_kendra-action-DeleteThesaurus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccessControlConfiguration  **
  - **IAM action:**  [kendra:DescribeAccessControlConfiguration](#list_kendra-action-DescribeAccessControlConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataSource  **
  - **IAM action:**  [kendra:DescribeDataSource](#list_kendra-action-DescribeDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExperience  **
  - **IAM action:**  [kendra:DescribeExperience](#list_kendra-action-DescribeExperience) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFaq  **
  - **IAM action:**  [kendra:DescribeFaq](#list_kendra-action-DescribeFaq) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFeaturedResultsSet  **
  - **IAM action:**  [kendra:DescribeFeaturedResultsSet](#list_kendra-action-DescribeFeaturedResultsSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIndex  **
  - **IAM action:**  [kendra:DescribeIndex](#list_kendra-action-DescribeIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePrincipalMapping  **
  - **IAM action:**  [kendra:DescribePrincipalMapping](#list_kendra-action-DescribePrincipalMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQuerySuggestionsBlockList  **
  - **IAM action:**  [kendra:DescribeQuerySuggestionsBlockList](#list_kendra-action-DescribeQuerySuggestionsBlockList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQuerySuggestionsConfig  **
  - **IAM action:**  [kendra:DescribeQuerySuggestionsConfig](#list_kendra-action-DescribeQuerySuggestionsConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeThesaurus  **
  - **IAM action:**  [kendra:DescribeThesaurus](#list_kendra-action-DescribeThesaurus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateEntitiesFromExperience  **
  - **IAM action:**  [kendra:DisassociateEntitiesFromExperience](#list_kendra-action-DisassociateEntitiesFromExperience) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociatePersonasFromEntities  **
  - **IAM action:**  [kendra:DisassociatePersonasFromEntities](#list_kendra-action-DisassociatePersonasFromEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetQuerySuggestions  **
  - **IAM action:**  [kendra:GetQuerySuggestions](#list_kendra-action-GetQuerySuggestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSnapshots  **
  - **IAM action:**  [kendra:GetSnapshots](#list_kendra-action-GetSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessControlConfigurations  **
  - **IAM action:**  [kendra:ListAccessControlConfigurations](#list_kendra-action-ListAccessControlConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSourceSyncJobs  **
  - **IAM action:**  [kendra:ListDataSourceSyncJobs](#list_kendra-action-ListDataSourceSyncJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **IAM action:**  [kendra:ListDataSources](#list_kendra-action-ListDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntityPersonas  **
  - **IAM action:**  [kendra:ListEntityPersonas](#list_kendra-action-ListEntityPersonas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperienceEntities  **
  - **IAM action:**  [kendra:ListExperienceEntities](#list_kendra-action-ListExperienceEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperiences  **
  - **IAM action:**  [kendra:ListExperiences](#list_kendra-action-ListExperiences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFaqs  **
  - **IAM action:**  [kendra:ListFaqs](#list_kendra-action-ListFaqs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFeaturedResultsSets  **
  - **IAM action:**  [kendra:ListFeaturedResultsSets](#list_kendra-action-ListFeaturedResultsSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGroupsOlderThanOrderingId  **
  - **IAM action:**  [kendra:ListGroupsOlderThanOrderingId](#list_kendra-action-ListGroupsOlderThanOrderingId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIndices  **
  - **IAM action:**  [kendra:ListIndices](#list_kendra-action-ListIndices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQuerySuggestionsBlockLists  **
  - **IAM action:**  [kendra:ListQuerySuggestionsBlockLists](#list_kendra-action-ListQuerySuggestionsBlockLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [kendra:ListTagsForResource](#list_kendra-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListThesauri  **
  - **IAM action:**  [kendra:ListThesauri](#list_kendra-action-ListThesauri) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutPrincipalMapping  **
  - **IAM action:**  [kendra:PutPrincipalMapping](#list_kendra-action-PutPrincipalMapping)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   Query  **
  - **IAM action:**  [kendra:Query](#list_kendra-action-Query) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Retrieve  **
  - **IAM action:**  [kendra:Retrieve](#list_kendra-action-Retrieve) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartDataSourceSyncJob  **
  - **IAM action:**  [kendra:StartDataSourceSyncJob](#list_kendra-action-StartDataSourceSyncJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDataSourceSyncJob  **
  - **IAM action:**  [kendra:StopDataSourceSyncJob](#list_kendra-action-StopDataSourceSyncJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitFeedback  **
  - **IAM action:**  [kendra:SubmitFeedback](#list_kendra-action-SubmitFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [kendra:TagResource](#list_kendra-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kendra:UntagResource](#list_kendra-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccessControlConfiguration  **
  - **IAM action:**  [kendra:UpdateAccessControlConfiguration](#list_kendra-action-UpdateAccessControlConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSource  **
  - **IAM action:**  [kendra:UpdateDataSource](#list_kendra-action-UpdateDataSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   UpdateExperience  **
  - **IAM action:**  [kendra:UpdateExperience](#list_kendra-action-UpdateExperience)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   UpdateFeaturedResultsSet  **
  - **IAM action:**  [kendra:UpdateFeaturedResultsSet](#list_kendra-action-UpdateFeaturedResultsSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIndex  **
  - **IAM action:**  [kendra:UpdateIndex](#list_kendra-action-UpdateIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   UpdateQuerySuggestionsBlockList  **
  - **IAM action:**  [kendra:UpdateQuerySuggestionsBlockList](#list_kendra-action-UpdateQuerySuggestionsBlockList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write

- **   UpdateQuerySuggestionsConfig  **
  - **IAM action:**  [kendra:UpdateQuerySuggestionsConfig](#list_kendra-action-UpdateQuerySuggestionsConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThesaurus  **
  - **IAM action:**  [kendra:UpdateThesaurus](#list_kendra-action-UpdateThesaurus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kendra.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Kendra
<a name="list_kendra-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateEntitiesToExperience](https://docs.aws.amazon.com/kendra/latest/dg/API_PutPrincipalMapping.html)  **
  - **Description:** Grants permission to put principal mapping in index
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociatePersonasToEntities](https://docs.aws.amazon.com/kendra/latest/dg/API_AssociatePersonasToEntities.html)  **
  - **Description:** Defines the specific permissions of users or groups in your AWS SSO identity source with access to your Amazon Kendra experience
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchDeleteDocument.html)  **
  - **Description:** Grants permission to batch delete document
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteFeaturedResults.html)  **
  - **Description:** Grants permission to delete a featured results set
  - **Resource types (\*required):** [featured-results-set\*](#list_kendra-resource-featured-results-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetDocumentStatus](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchGetDocumentStatus.html)  **
  - **Description:** Grants permission to do batch get document status
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html)  **
  - **Description:** Grants permission to batch put document
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ClearQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_ClearQuerySuggestions.html)  **
  - **Description:** Grants permission to clear out the suggestions for a given index, generated so far
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateAccessControlConfiguration.html)  **
  - **Description:** Grants permission to create an access control configuration
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateDataSource.html)  **
  - **Description:** Grants permission to create a data source
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExperience](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateExperience.html)  **
  - **Description:** Creates an Amazon Kendra experience such as a search application
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFaq](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateFaq.html)  **
  - **Description:** Grants permission to create an Faq
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateFeaturedResults.html)  **
  - **Description:** Grants permission to create a featured results set
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIndex](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateIndex.html)  **
  - **Description:** Grants permission to create an Index
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateQuerySuggestionsBlockList.html)  **
  - **Description:** Grants permission to create a QuerySuggestions BlockList
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Write

- **   [CreateThesaurus](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateThesaurus.html)  **
  - **Description:** Grants permission to create a Thesaurus
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteAccessControlConfiguration.html)  **
  - **Description:** Grants permission to delete an access control configuration
  - **Resource types (\*required):** [access-control-configuration\*](#list_kendra-resource-access-control-configuration) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteDataSource.html)  **
  - **Description:** Grants permission to delete a data source
  - **Resource types (\*required):** [data-source\*](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExperience](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteExperience.html)  **
  - **Description:** Deletes your Amazon Kendra experience such as a search application
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFaq](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteFaq.html)  **
  - **Description:** Grants permission to delete an Faq
  - **Resource types (\*required):** [faq\*](#list_kendra-resource-faq) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIndex](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteIndex.html)  **
  - **Description:** Grants permission to delete an Index
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePrincipalMapping](https://docs.aws.amazon.com/kendra/latest/dg/API_DeletePrincipalMapping.html)  **
  - **Description:** Grants permission to delete principal mapping from index
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteQuerySuggestionsBlockList.html)  **
  - **Description:** Grants permission to delete a QuerySuggestions BlockList
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [query-suggestions-block-list\*](#list_kendra-resource-query-suggestions-block-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThesaurus](https://docs.aws.amazon.com/kendra/latest/dg/API_DeleteThesaurus.html)  **
  - **Description:** Grants permission to delete a Thesaurus
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thesaurus\*](#list_kendra-resource-thesaurus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeAccessControlConfiguration.html)  **
  - **Description:** Grants permission to describe an access control configuration
  - **Resource types (\*required):** [access-control-configuration\*](#list_kendra-resource-access-control-configuration) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataSource](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeDataSource.html)  **
  - **Description:** Grants permission to describe a data source
  - **Resource types (\*required):** [data-source\*](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExperience](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeExperience.html)  **
  - **Description:** Gets information about your Amazon Kendra experience such as a search application
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFaq](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeFaq.html)  **
  - **Description:** Grants permission to describe an Faq
  - **Resource types (\*required):** [faq\*](#list_kendra-resource-faq) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeThesaurus.html)  **
  - **Description:** Grants permission to describe a featured results set
  - **Resource types (\*required):** [featured-results-set\*](#list_kendra-resource-featured-results-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeIndex](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeIndex.html)  **
  - **Description:** Grants permission to describe an Index
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePrincipalMapping](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribePrincipalMapping.html)  **
  - **Description:** Grants permission to describe principal mapping from index
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeQuerySuggestionsBlockList.html)  **
  - **Description:** Grants permission to describe a QuerySuggestions BlockList
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [query-suggestions-block-list\*](#list_kendra-resource-query-suggestions-block-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeQuerySuggestionsConfig.html)  **
  - **Description:** Grants permission to describe the query suggestions configuration for an index
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeThesaurus](https://docs.aws.amazon.com/kendra/latest/dg/API_DescribeThesaurus.html)  **
  - **Description:** Grants permission to describe a Thesaurus
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thesaurus\*](#list_kendra-resource-thesaurus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateEntitiesFromExperience](https://docs.aws.amazon.com/kendra/latest/dg/API_DisassociateEntitiesFromExperience.html)  **
  - **Description:** Prevents users or groups in your AWS SSO identity source from accessing your Amazon Kendra experience
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociatePersonasFromEntities](https://docs.aws.amazon.com/kendra/latest/dg/API_DisassociatePersonasFromEntities.html)  **
  - **Description:** Removes the specific permissions of users or groups in your AWS SSO identity source with access to your Amazon Kendra experience
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html)  **
  - **Description:** Grants permission to get suggestions for a query prefix
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSnapshots](https://docs.aws.amazon.com/kendra/latest/dg/API_GetSnapshots.html)  **
  - **Description:** Retrieves search metrics data
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccessControlConfigurations](https://docs.aws.amazon.com/kendra/latest/dg/API_ListAccessControlConfigurations.html)  **
  - **Description:** Grants permission to list the access control configurations
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSourceSyncJobs](https://docs.aws.amazon.com/kendra/latest/dg/API_ListDataSourceSyncJobs.html)  **
  - **Description:** Grants permission to get Data Source sync job history
  - **Resource types (\*required):** [data-source\*](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSources](https://docs.aws.amazon.com/kendra/latest/dg/API_ListDataSources.html)  **
  - **Description:** Grants permission to list the data sources
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEntityPersonas](https://docs.aws.amazon.com/kendra/latest/dg/API_ListEntityPersonas.html)  **
  - **Description:** Lists specific permissions of users and groups with access to your Amazon Kendra experience
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExperienceEntities](https://docs.aws.amazon.com/kendra/latest/dg/API_ListExperienceEntities.html)  **
  - **Description:** Lists users or groups in your AWS SSO identity source that are granted access to your Amazon Kendra experience
  - **Resource types (\*required):** [experience\*](#list_kendra-resource-experience) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExperiences](https://docs.aws.amazon.com/kendra/latest/dg/API_ListExperiences.html)  **
  - **Description:** Lists one or more Amazon Kendra experiences. You can create an Amazon Kendra experience such as a search application
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFaqs](https://docs.aws.amazon.com/kendra/latest/dg/API_ListFaqs.html)  **
  - **Description:** Grants permission to list the Faqs
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFeaturedResultsSets](https://docs.aws.amazon.com/kendra/latest/dg/API_ListFeaturedResults.html)  **
  - **Description:** Grants permission to list the featured results sets
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGroupsOlderThanOrderingId](https://docs.aws.amazon.com/kendra/latest/dg/API_ListGroupsOlderThanOrderingId.html)  **
  - **Description:** Grants permission to list groups that are older than an ordering id
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIndices](https://docs.aws.amazon.com/kendra/latest/dg/API_ListIndices.html)  **
  - **Description:** Grants permission to list the indexes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQuerySuggestionsBlockLists](https://docs.aws.amazon.com/kendra/latest/dg/API_ListQuerySuggestionsBlockLists.html)  **
  - **Description:** Grants permission to list the QuerySuggestions BlockLists
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/kendra/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [faq](#list_kendra-resource-faq) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [featured-results-set](#list_kendra-resource-featured-results-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [query-suggestions-block-list](#list_kendra-resource-query-suggestions-block-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thesaurus](#list_kendra-resource-thesaurus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListThesauri](https://docs.aws.amazon.com/kendra/latest/dg/API_ListThesauri.html)  **
  - **Description:** Grants permission to list the Thesauri
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutPrincipalMapping](https://docs.aws.amazon.com/kendra/latest/dg/API_PutPrincipalMapping.html)  **
  - **Description:** Grants permission to put principal mapping in index
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Query](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html)  **
  - **Description:** Grants permission to query documents and faqs
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Retrieve](https://docs.aws.amazon.com/kendra/latest/dg/API_Retrieve.html)  **
  - **Description:** Grants permission to retrieve relevant content from an index
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartDataSourceSyncJob](https://docs.aws.amazon.com/kendra/latest/dg/API_StartDataSourceSyncJob.html)  **
  - **Description:** Grants permission to start Data Source sync job
  - **Resource types (\*required):** [data-source\*](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDataSourceSyncJob](https://docs.aws.amazon.com/kendra/latest/dg/API_StopDataSourceSyncJob.html)  **
  - **Description:** Grants permission to stop Data Source sync job
  - **Resource types (\*required):** [data-source\*](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitFeedback](https://docs.aws.amazon.com/kendra/latest/dg/API_SubmitFeedback.html)  **
  - **Description:** Grants permission to send feedback about a query results
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/kendra/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [faq](#list_kendra-resource-faq) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [featured-results-set](#list_kendra-resource-featured-results-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [index](#list_kendra-resource-index) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [query-suggestions-block-list](#list_kendra-resource-query-suggestions-block-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [thesaurus](#list_kendra-resource-thesaurus) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kendra-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/kendra/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the tag with the given key from a resource
  - **Resource types (\*required):** [data-source](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [faq](#list_kendra-resource-faq) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [featured-results-set](#list_kendra-resource-featured-results-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [index](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [query-suggestions-block-list](#list_kendra-resource-query-suggestions-block-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Resource types (\*required):** [thesaurus](#list_kendra-resource-thesaurus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kendra-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccessControlConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateAccessControlConfiguration.html)  **
  - **Description:** Grants permission to update an access control configuration
  - **Resource types (\*required):** [access-control-configuration\*](#list_kendra-resource-access-control-configuration) / **Condition keys:**  
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateDataSource.html)  **
  - **Description:** Grants permission to update a data source
  - **Resource types (\*required):** [data-source\*](#list_kendra-resource-data-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExperience](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateExperience.html)  **
  - **Description:** Updates your Amazon Kendra experience such as a search application
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResults.html)  **
  - **Description:** Grants permission to update a featured results set
  - **Resource types (\*required):** [featured-results-set\*](#list_kendra-resource-featured-results-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIndex](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html)  **
  - **Description:** Grants permission to update an Index
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQuerySuggestionsBlockList](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsBlockList.html)  **
  - **Description:** Grants permission to update a QuerySuggestions BlockList
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [query-suggestions-block-list\*](#list_kendra-resource-query-suggestions-block-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html)  **
  - **Description:** Grants permission to update the query suggestions configuration for an index
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThesaurus](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateThesaurus.html)  **
  - **Description:** Grants permission to update a thesaurus
  - **Resource types (\*required):** [index\*](#list_kendra-resource-index) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [thesaurus\*](#list_kendra-resource-thesaurus) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Kendra
<a name="list_kendra-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [access-control-configuration](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateAccessControlConfiguration.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/access-control-configuration/${AccessControlConfigurationId} |   | 
|  [data-source](https://docs.aws.amazon.com/kendra/latest/dg/data-source.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/data-source/${DataSourceId} | [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_) | 
|  [experience](https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/experience/${ExperienceId} |   | 
|  [faq](https://docs.aws.amazon.com/kendra/latest/dg/faq.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/faq/${FaqId} | [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_) | 
|  [featured-results-set](https://docs.aws.amazon.com/kendra/latest/dg/featured-results.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/featured-results-set/${FeaturedResultsSetId} | [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_) | 
|  [index](https://docs.aws.amazon.com/kendra/latest/dg/index.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId} | [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_) | 
|  [query-suggestions-block-list](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions-block-list.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/query-suggestions-block-list/${QuerySuggestionsBlockListId} | [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_) | 
|  [thesaurus](https://docs.aws.amazon.com/kendra/latest/dg/thesaurus.html)  | arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}/thesaurus/${ThesaurusId} | [aws:ResourceTag/${TagKey}](#list_kendra-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Kendra
<a name="list_kendra-policy-keys"></a>

Amazon Kendra defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 