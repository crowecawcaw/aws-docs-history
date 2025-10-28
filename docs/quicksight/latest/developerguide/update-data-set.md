# UpdateDataSet

Use the `UpdateDataSet` API operation to update a dataset. To use this operation, you need the ID of the dataset that you want to update. The dataset ID is part of the dataset URL in Quick Sight. You can also use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

AWS CLI

```
 aws quicksight update-data-set
    --aws-account-id `AWSACCOUNTID`
    --data-set-id `DATASETID`
    --name `NAME`
    --physical-table-map `PHYSICALTABLEMAP`
    --import-mode `IMPORTMODE`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight update-data-set
    --cli-input-json file://`updatedataset`.json
```

For more information about the `UpdateDataSet` API operation, see [UpdateDataSet](../APIReference/API_UpdateDataSet.md "../APIReference/API_UpdateDataSet.md") in the _Amazon Quick Sight API Reference_.
