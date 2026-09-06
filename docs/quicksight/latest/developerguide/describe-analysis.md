

# DescribeAnalysis
<a name="describe-analysis"></a>

Use the `DescribeAnalysis` API operation to view a summary of the metadata for an analysis for a specified user. To use this operation, you need the ID of the analysis that you want to describe. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-analysis 
    --analysis-id {{{{ANALYSISID}}}} 
    --aws-account-id {{555555555555}}
```

------

For more information about the `DescribeAnalysis` API operation, see [DescribeAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysis.html) in the *Amazon Quick Sight API Reference*.