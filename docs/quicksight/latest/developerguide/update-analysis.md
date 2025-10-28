# UpdateAnalysis

Use the `UpdateAnalysis` API operation to update an analysis in Amazon Quick Sight. To use this operation, you need the ID of the analysis that you want to update. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-analysis
    --aws-account-id `555555555555`
    --analysis-id ``ANALYSISID``
    --name `NAME`
    --source-entity '{"SourceTemplate":{"DataSetReferences":[{"DataSetPlaceholder":"`PLACEHOLDER`","DataSetArn":"arn:aws:quicksight:`us-west-2`:`555555555555`:dataset/`DATASETID`"}],"Arn":"arn:aws:quicksight:`us-west-2`:`555555555555`:template/`TEMPLATEID`"}}'
    --theme-arn `THEMEARN`
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-analysis
    --cli-input-json file://`updateanalysis`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateAnalysis` API operation, see [UpdateAnalysis](../APIReference/API_UpdateAnalysis.md "../APIReference/API_UpdateAnalysis.md") in the _Amazon Quick Sight API Reference_.
