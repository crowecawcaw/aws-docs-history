# DescribeAnalysis

Use the `DescribeAnalysis` API operation to view a summary of the metadata for an analysis for a specified user. To use this operation, you need the ID of the analysis that you want to describe. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight describe-analysis
    --analysis-id ``ANALYSISID``
    --aws-account-id `555555555555`
```

For more information about the `DescribeAnalysis` API operation, see [DescribeAnalysis](../APIReference/API_DescribeAnalysis.md "../APIReference/API_DescribeAnalysis.md") in the _Amazon Quick Sight API Reference_.
