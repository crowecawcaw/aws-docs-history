# CreateAnalysis

Use the `CreateAnalysis` API operation to create an analysis in Amazon Quick Sight for a specified user. Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-analysis
    --aws-account-id `AWSACCOUNTID`
    --analysis-id `ANALYSISID`
    --name `NAME`
    --source-entity `SOURCEENTITY`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-analysis
    --cli-input-json file://`createanalysis`.json
```

For more information about the `CreateAnalysis` API operation, see [CreateAnalysis](../APIReference/API_CreateAnalysis.md "../APIReference/API_CreateAnalysis.md") in the _Amazon Quick Sight API Reference_.
