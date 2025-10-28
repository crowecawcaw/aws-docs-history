# RestoreAnalysis

Use the `RestoreAnalysis` API operation to restore an analysis for a specified user. To use this operation, you need the ID of the analysis that you want to restore. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight restore-analysis
    --analysis-id ``ANALYSISID``
    --aws-account-id `555555555555`
```

For more information about the `RestoreAnalysis` API operation, see [RestoreAnalysis](../APIReference/API_RestoreAnalysis.md "../APIReference/API_RestoreAnalysis.md") in the _Amazon Quick Sight API Reference_.
