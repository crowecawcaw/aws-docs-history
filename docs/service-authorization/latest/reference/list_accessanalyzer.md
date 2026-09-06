

# Actions, resources, and condition keys for AWS IAM Access Analyzer
<a name="list_accessanalyzer"></a>

AWS IAM Access Analyzer (service prefix: `access-analyzer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-permissions) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/access-analyzer/access-analyzer.json) for this service.

**Topics**
+ [API operations defined by AWS IAM Access Analyzer](#list_accessanalyzer-operations)
+ [Actions defined by AWS IAM Access Analyzer](#list_accessanalyzer-actions-as-permissions)
+ [Resource types defined by AWS IAM Access Analyzer](#list_accessanalyzer-resources-for-iam-policies)
+ [Condition keys for AWS IAM Access Analyzer](#list_accessanalyzer-policy-keys)

## API operations defined by AWS IAM Access Analyzer
<a name="list_accessanalyzer-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_accessanalyzer-actions-as-permissions).




- **   ApplyArchiveRule  **
  - **IAM action:**  [access-analyzer:ApplyArchiveRule](#list_accessanalyzer-action-ApplyArchiveRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelPolicyGeneration  **
  - **IAM action:**  [access-analyzer:CancelPolicyGeneration](#list_accessanalyzer-action-CancelPolicyGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CheckAccessNotGranted  **
  - **IAM action:**  [access-analyzer:CheckAccessNotGranted](#list_accessanalyzer-action-CheckAccessNotGranted) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CheckNoNewAccess  **
  - **IAM action:**  [access-analyzer:CheckNoNewAccess](#list_accessanalyzer-action-CheckNoNewAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CheckNoPublicAccess  **
  - **IAM action:**  [access-analyzer:CheckNoPublicAccess](#list_accessanalyzer-action-CheckNoPublicAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAccessPreview  **
  - **IAM action:**  [access-analyzer:CreateAccessPreview](#list_accessanalyzer-action-CreateAccessPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAnalyzer  **
  - **IAM action:**  [access-analyzer:CreateAnalyzer](#list_accessanalyzer-action-CreateAnalyzer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [access-analyzer:TagResource](#list_accessanalyzer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateArchiveRule  **
  - **IAM action:**  [access-analyzer:CreateArchiveRule](#list_accessanalyzer-action-CreateArchiveRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateServiceLinkedAnalyzer  **
  - **IAM action:**  [access-analyzer:CreateServiceLinkedAnalyzer](#list_accessanalyzer-action-CreateServiceLinkedAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnalyzer  **
  - **IAM action:**  [access-analyzer:DeleteAnalyzer](#list_accessanalyzer-action-DeleteAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArchiveRule  **
  - **IAM action:**  [access-analyzer:DeleteArchiveRule](#list_accessanalyzer-action-DeleteArchiveRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceLinkedAnalyzer  **
  - **IAM action:**  [access-analyzer:DeleteServiceLinkedAnalyzer](#list_accessanalyzer-action-DeleteServiceLinkedAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateFindingRecommendation  **
  - **IAM action:**  [access-analyzer:GenerateFindingRecommendation](#list_accessanalyzer-action-GenerateFindingRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessPreview  **
  - **IAM action:**  [access-analyzer:GetAccessPreview](#list_accessanalyzer-action-GetAccessPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnalyzedResource  **
  - **IAM action:**  [access-analyzer:GetAnalyzedResource](#list_accessanalyzer-action-GetAnalyzedResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnalyzer  **
  - **IAM action:**  [access-analyzer:GetAnalyzer](#list_accessanalyzer-action-GetAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetArchiveRule  **
  - **IAM action:**  [access-analyzer:GetArchiveRule](#list_accessanalyzer-action-GetArchiveRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFinding  **
  - **IAM action:**  [access-analyzer:GetFinding](#list_accessanalyzer-action-GetFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingRecommendation  **
  - **IAM action:**  [access-analyzer:GetFindingRecommendation](#list_accessanalyzer-action-GetFindingRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingV2  **
  - **IAM action:**  [access-analyzer:GetFinding](#list_accessanalyzer-action-GetFinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsStatistics  **
  - **IAM action:**  [access-analyzer:GetFindingsStatistics](#list_accessanalyzer-action-GetFindingsStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGeneratedPolicy  **
  - **IAM action:**  [access-analyzer:GetGeneratedPolicy](#list_accessanalyzer-action-GetGeneratedPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessPreviewFindings  **
  - **IAM action:**  [access-analyzer:ListAccessPreviewFindings](#list_accessanalyzer-action-ListAccessPreviewFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccessPreviews  **
  - **IAM action:**  [access-analyzer:ListAccessPreviews](#list_accessanalyzer-action-ListAccessPreviews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnalyzedResources  **
  - **IAM action:**  [access-analyzer:ListAnalyzedResources](#list_accessanalyzer-action-ListAnalyzedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnalyzers  **
  - **IAM action:**  [access-analyzer:ListAnalyzers](#list_accessanalyzer-action-ListAnalyzers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArchiveRules  **
  - **IAM action:**  [access-analyzer:ListArchiveRules](#list_accessanalyzer-action-ListArchiveRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindings  **
  - **IAM action:**  [access-analyzer:ListFindings](#list_accessanalyzer-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFindingsV2  **
  - **IAM action:**  [access-analyzer:ListFindings](#list_accessanalyzer-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPolicyGenerations  **
  - **IAM action:**  [access-analyzer:ListPolicyGenerations](#list_accessanalyzer-action-ListPolicyGenerations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [access-analyzer:ListTagsForResource](#list_accessanalyzer-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartPolicyGeneration  **
  - **IAM action:**  [access-analyzer:StartPolicyGeneration](#list_accessanalyzer-action-StartPolicyGeneration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** access-analyzer.amazonaws.com / **Access level:** Write

- **   StartResourceScan  **
  - **IAM action:**  [access-analyzer:StartResourceScan](#list_accessanalyzer-action-StartResourceScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [access-analyzer:TagResource](#list_accessanalyzer-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [access-analyzer:UntagResource](#list_accessanalyzer-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAnalyzer  **
  - **IAM action:**  [access-analyzer:UpdateAnalyzer](#list_accessanalyzer-action-UpdateAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateArchiveRule  **
  - **IAM action:**  [access-analyzer:UpdateArchiveRule](#list_accessanalyzer-action-UpdateArchiveRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFindings  **
  - **IAM action:**  [access-analyzer:UpdateFindings](#list_accessanalyzer-action-UpdateFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidatePolicy  **
  - **IAM action:**  [access-analyzer:ValidatePolicy](#list_accessanalyzer-action-ValidatePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS IAM Access Analyzer
<a name="list_accessanalyzer-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ApplyArchiveRule](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ApplyArchiveRule.html)  **
  - **Description:** Grants permission to apply an archive rule
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelPolicyGeneration](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CancelPolicyGeneration.html)  **
  - **Description:** Grants permission to cancel a policy generation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CheckAccessNotGranted](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckAccessNotGranted.html)  **
  - **Description:** Grants permission to check that specified access is not allowed by a policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CheckNoNewAccess](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoNewAccess.html)  **
  - **Description:** Grants permission to check that no new access is allowed when compared to an existing policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CheckNoPublicAccess](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoPublicAccess.html)  **
  - **Description:** Grants permission to check that public access is not allowed by a resource policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateAccessPreview](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAccessPreview.html)  **
  - **Description:** Grants permission to create an access preview for the specified analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAnalyzer.html)  **
  - **Description:** Grants permission to create an analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_accessanalyzer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateArchiveRule](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateArchiveRule.html)  **
  - **Description:** Grants permission to create an archive rule for the specified analyzer
  - **Resource types (\*required):** [ArchiveRule\*](#list_accessanalyzer-resource-ArchiveRule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateServiceLinkedAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateServiceLinkedAnalyzer.html)  **
  - **Description:** Grants permission to create a service-linked analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_accessanalyzer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DeleteAnalyzer.html)  **
  - **Description:** Grants permission to delete the specified analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_accessanalyzer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteArchiveRule](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DeleteArchiveRule.html)  **
  - **Description:** Grants permission to delete archive rules for the specified analyzer
  - **Resource types (\*required):** [ArchiveRule\*](#list_accessanalyzer-resource-ArchiveRule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteServiceLinkedAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DeleteServiceLinkedAnalyzer.html)  **
  - **Description:** Grants permission to delete the specified service-linked analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_accessanalyzer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Write

- **   [GenerateFindingRecommendation](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GenerateFindingRecommendation.html)  **
  - **Description:** Grants permission to generate recommendation steps to resolve a finding
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccessPreview](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAccessPreview.html)  **
  - **Description:** Grants permission to retrieve information about an access preview
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnalyzedResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzedResource.html)  **
  - **Description:** Grants permission to retrieve information about an analyzed resource
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html)  **
  - **Description:** Grants permission to retrieve information about analyzers
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_accessanalyzer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Read

- **   [GetArchiveRule](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetArchiveRule.html)  **
  - **Description:** Grants permission to retrieve information about archive rules for the specified analyzer
  - **Resource types (\*required):** [ArchiveRule\*](#list_accessanalyzer-resource-ArchiveRule)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFinding](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingV2.html)  **
  - **Description:** Grants permission to retrieve findings
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingRecommendation](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingRecommendation.html)  **
  - **Description:** Grants permission to retrieve recommendation steps to resolve a finding
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingsStatistics](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-permissions)  **
  - **Description:** Grants permission to retrieve statistics for findings
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGeneratedPolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetGeneratedPolicy.html)  **
  - **Description:** Grants permission to retrieve a policy that was generated using StartPolicyGeneration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccessPreviewFindings](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviewFindings.html)  **
  - **Description:** Grants permission to retrieve a list of findings from an access preview
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccessPreviews](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviews.html)  **
  - **Description:** Grants permission to retrieve a list of access previews
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAnalyzedResources](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzedResources.html)  **
  - **Description:** Grants permission to retrieve a list of resources that have been analyzed
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnalyzers](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html)  **
  - **Description:** Grants permission to retrieves a list of analyzers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArchiveRules](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListArchiveRules.html)  **
  - **Description:** Grants permission to retrieve a list of archive rules from an analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFindings](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListFindingsV2.html)  **
  - **Description:** Grants permission to retrieve a list of findings from an analyzer
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPolicyGenerations](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListPolicyGenerations.html)  **
  - **Description:** Grants permission to list all the recently started policy generations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags applied to a resource
  - **Resource types (\*required):** [Analyzer](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartPolicyGeneration](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StartPolicyGeneration.html)  **
  - **Description:** Grants permission to start a policy generation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartResourceScan](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_StartResourceScan.html)  **
  - **Description:** Grants permission to start a scan of the policies applied to a resource
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add a tag to a resource
  - **Resource types (\*required):** [Analyzer](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_accessanalyzer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [Analyzer](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_accessanalyzer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateAnalyzer.html)  **
  - **Description:** Grants permission to modify an analyzer's configuration
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateArchiveRule](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateArchiveRule.html)  **
  - **Description:** Grants permission to modify an archive rule
  - **Resource types (\*required):** [ArchiveRule\*](#list_accessanalyzer-resource-ArchiveRule)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFindings](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UpdateFindings.html)  **
  - **Description:** Grants permission to modify findings
  - **Resource types (\*required):** [Analyzer\*](#list_accessanalyzer-resource-Analyzer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidatePolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html)  **
  - **Description:** Grants permission to validate a policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS IAM Access Analyzer
<a name="list_accessanalyzer-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources)  | arn:${Partition}:access-analyzer:${Region}:${Account}:analyzer/${AnalyzerName} | [aws:ResourceTag/${TagKey}](#list_accessanalyzer-aws_ResourceTag___TagKey_) | 
|  [ArchiveRule](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources)  | arn:${Partition}:access-analyzer:${Region}:${Account}:analyzer/${AnalyzerName}/archive-rule/${RuleName} |   | 

## Condition keys for AWS IAM Access Analyzer
<a name="list_accessanalyzer-policy-keys"></a>

AWS IAM Access Analyzer defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 