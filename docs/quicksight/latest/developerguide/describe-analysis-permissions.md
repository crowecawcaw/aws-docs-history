# DescribeAnalysisPermissions

Use the `DescribeAnalysisPermissions` API operation to view the read and write permissions for an analysis. To use this operation, you need the ID of the analysis whose permissions you want to view. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-analysis-permissions
    --aws-account-id `555555555555`
    --analysis-id `ANALYSISID`
```

For more information about the `DescribeAnalysisPermissions` API operation, see [DescribeAnalysisPermissions](../APIReference/API_DescribeAnalysisPermissions.md "../APIReference/API_DescribeAnalysisPermissions.md") in the _Amazon Quick Sight API Reference_.
