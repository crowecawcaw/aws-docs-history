# CreateTemplate

Use the `CreateTemplate` operation to create a template from an existing Quick Sight analysis or template. You can use the resulting template to create a dashboard.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-template
    --aws-account-id `555555555555`
    --template-id `TEMPLATEID`
    --source-entity `SOURCEENTITY`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-template
    --cli-input-json file://`createtemplate`.json
```

You can to get the ID the dataset ID by using a `DescribeAnalysis`operation. The `ANALYSISID`is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` operation to get the ID.

For more information about the `CreateTemplate` operation, see [CreateTemplate](../APIReference/API_CreateTemplate.md "../APIReference/API_CreateTemplate.md") in the _Quick Sight API Reference_.
