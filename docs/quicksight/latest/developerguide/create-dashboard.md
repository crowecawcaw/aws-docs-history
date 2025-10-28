# CreateDashboard

Use the `CreateDashboard` API operation to create a dashboard. Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-dashboard
    --aws-account-id `555555555555`
    --dashboard-id `newDash`
    --name `Dashboard1`
    --source-entity '{"SourceTemplate":{"DataSetReferences":[{"DataSetPlaceholder":"`PLACEHOLDER`","DataSetArn":"arn:aws:quicksight:`REGION`:`555555555555`:dataset/`DATASETID`"}],"Arn":"arn:aws:quicksight:`REGION`:`555555555555`:template/`TEMPLATEID`"}}'
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-dashbord
    --cli-input-json file://`createdashboard`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `CreateDashboard` API operation, see [CreateDashboard](../APIReference/API_CreateDashboard.md "../APIReference/API_CreateDashboard.md") in the _Amazon Quick Sight API Reference_.
