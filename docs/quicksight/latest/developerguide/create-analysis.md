

# CreateAnalysis

Use the `CreateAnalysis` API operation to create an analysis in AWS Quick Sight for a specified user. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```bash
aws quicksight create-analysis
    --aws-account-id {{AWSACCOUNTID}}
    --analysis-id {{ANALYSISID}}
    --name {{NAME}}
    --source-entity {{SOURCEENTITY}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-analysis
    --cli-input-json file://{{createanalysis}}.json
```

------

For more information about the `CreateAnalysis` API operation, see [CreateAnalysis](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateAnalysis.html) in the *AWS Quick Sight API Reference*.