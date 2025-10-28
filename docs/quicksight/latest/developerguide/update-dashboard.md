# UpdateDashboard

Use the `UpdateDashboard` API operation to update a dashboard in an AWS account. To use this operation, you need the ID of the dashboard that you want to update. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-dashboard
    --aws-account-id `555555555555`
    --dashboard-id `DASHBOARDID`
    --name `Dashboard`
    --source-entity '{"SourceTemplate":{"DataSetReferences":[{"DataSetPlaceholder": "`PLACEHOLDER`","DataSetArn": "arn:aws:quicksight:<region>:<awsaccountid>:dataset/<datasetid>"}],"Arn": "arn:aws:quicksight:<`region`>:<`awsaccountid`>:template/<`templateid`>"}}'
    --version-description `VERSION`
    --dashboard-publish-options AdHocFilteringOption={AvailabilityStatus=ENABLED},ExportToCSVOption={AvailabilityStatus=ENABLED},SheetControlsOption={VisibilityState=EXPANDED} /
    --theme-arn `THEMEARN`
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-dashboard
    --cli-input-json file://`updatedashboard`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateDashboard` API operation, see [UpdateDashboard](../APIReference/API_UpdateDashboard.md "../APIReference/API_UpdateDashboard.md") in the _Amazon Quick Sight API Reference_.
