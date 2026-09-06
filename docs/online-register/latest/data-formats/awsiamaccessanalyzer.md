

# Data retrieval APIs for AWS IAM Access Analyzer
<a name="awsiamaccessanalyzer"></a>

AWS IAM Access Analyzer provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="access-analyzer-CheckAccessNotGranted"></a>[CheckAccessNotGranted](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckAccessNotGranted.html) | Check that specified access is not allowed by a policy | Read | 
| <a name="access-analyzer-CheckNoNewAccess"></a>[CheckNoNewAccess](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoNewAccess.html) | Check that no new access is allowed when compared to an existing policy | Read | 
| <a name="access-analyzer-CheckNoPublicAccess"></a>[CheckNoPublicAccess](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoPublicAccess.html) | Check that public access is not allowed by a resource policy | Read | 
| <a name="access-analyzer-GetAccessPreview"></a>[GetAccessPreview](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAccessPreview.html) | Retrieve information about an access preview | Read | 
| <a name="access-analyzer-GetAnalyzedResource"></a>[GetAnalyzedResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzedResource.html) | Retrieve information about an analyzed resource | Read | 
| <a name="access-analyzer-GetAnalyzer"></a>[GetAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html) | Retrieve information about analyzers | Read | 
| <a name="access-analyzer-GetArchiveRule"></a>[GetArchiveRule](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetArchiveRule.html) | Retrieve information about archive rules for the specified analyzer | Read | 
| <a name="access-analyzer-GetFinding"></a>[GetFinding](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingV2.html) | Retrieve findings | Read | 
| <a name="access-analyzer-GetFindingRecommendation"></a>[GetFindingRecommendation](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingRecommendation.html) | Retrieve recommendation steps to resolve a finding | Read | 
| <a name="access-analyzer-GetFindingsStatistics"></a>[GetFindingsStatistics](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-permissions) | Retrieve statistics for findings | Read | 
| <a name="access-analyzer-GetGeneratedPolicy"></a>[GetGeneratedPolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetGeneratedPolicy.html) | Retrieve a policy that was generated using StartPolicyGeneration | Read | 
| <a name="access-analyzer-ListAccessPreviewFindings"></a>[ListAccessPreviewFindings](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviewFindings.html) | Retrieve a list of findings from an access preview | Read | 
| <a name="access-analyzer-ListAccessPreviews"></a>[ListAccessPreviews](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAccessPreviews.html) | Retrieve a list of access previews | List | 
| <a name="access-analyzer-ListAnalyzedResources"></a>[ListAnalyzedResources](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzedResources.html) | Retrieve a list of resources that have been analyzed | Read | 
| <a name="access-analyzer-ListAnalyzers"></a>[ListAnalyzers](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html) | Retrieves a list of analyzers | List | 
| <a name="access-analyzer-ListArchiveRules"></a>[ListArchiveRules](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListArchiveRules.html) | Retrieve a list of archive rules from an analyzer | List | 
| <a name="access-analyzer-ListFindings"></a>[ListFindings](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListFindingsV2.html) | Retrieve a list of findings from an analyzer | Read | 
| <a name="access-analyzer-ListPolicyGenerations"></a>[ListPolicyGenerations](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListPolicyGenerations.html) | List all the recently started policy generations | Read | 
| <a name="access-analyzer-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListTagsForResource.html) | Retrieve a list of tags applied to a resource | Read | 
| <a name="access-analyzer-ValidatePolicy"></a>[ValidatePolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html) | Validate a policy | Read | 