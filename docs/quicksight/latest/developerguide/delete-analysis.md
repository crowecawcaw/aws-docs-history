# DeleteAnalysis

Use the `DeleteAnalysis` API operation to delete an analysis from Amazon Quick Sight for a specified user. To use this operation, you need the ID of the analysis that you want to delete. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight delete-analysis
    --aws-account-id `555555555555`
    --analysis-id ``ANALYSISID``
```

For more information about the `DeleteAnalysis` API operation, see [DeleteAnalysis](../APIReference/API_DeleteAnalysis.md "../APIReference/API_DeleteAnalysis.md") in the _Amazon Quick Sight API Reference_.
