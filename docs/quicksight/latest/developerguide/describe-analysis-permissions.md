

# DescribeAnalysisPermissions
<a name="describe-analysis-permissions"></a>

Use the `DescribeAnalysisPermissions` API operation to view the read and write permissions for an analysis. To use this operation, you need the ID of the analysis whose permissions you want to view. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-analysis-permissions 
    --aws-account-id {{555555555555}} 
    --analysis-id {{ANALYSISID}}
```

------

For more information about the `DescribeAnalysisPermissions` API operation, see [DescribeAnalysisPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysisPermissions.html) in the *Amazon Quick Sight API Reference*.