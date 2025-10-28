# UpdateAnalysisPermissions

Use the `UpdateAnalysisPermissions` API operation to update the read and write permissions for an analysis. You can grant or revoke permissions in the same command. To use this operation, you need the ID of the analysis whose permissions you want to update. The analysis ID is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight update-analysis-permissions
    --aws-account-id `555555555555`
    --analysis-id `ANALYSISID`
    --grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:RestoreAnalysis,quicksight:UpdateAnalysisPermissions,quicksight:DeleteAnalysis,quicksight:QueryAnalysis,quicksight:DescribeAnalysisPermissions,quicksight:DescribeAnalysis,quicksight:UpdateAnalysis
    --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`555555555555`:user/default/`USERNAME`,Actions=quicksight:RestoreAnalysis,quicksight:UpdateAnalysisPermissions,quicksight:DeleteAnalysis,quicksight:QueryAnalysis,quicksight:DescribeAnalysisPermissions,quicksight:DescribeAnalysis,quicksight:UpdateAnalysis
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-analysis-permissions
    --cli-input-json file://`updateanalysispermissions`.json
```

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateAnalysisPermissions` API operation, see [UpdateAnalysisPermissions](../APIReference/API_UpdateAnalysisPermissions.md "../APIReference/API_UpdateAnalysisPermissions.md") in the _Amazon Quick Sight API Reference_.
