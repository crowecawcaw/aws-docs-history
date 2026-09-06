

# UpdateDataSet
<a name="update-data-set"></a>

Use the `UpdateDataSet` API operation to update a dataset. To use this operation, you need the ID of the dataset that you want to update. The dataset ID is part of the dataset URL in Quick Sight. You can also use the `ListDataSets` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
 aws quicksight update-data-set
    --aws-account-id {{AWSACCOUNTID}}
    --data-set-id {{DATASETID}}
    --name {{NAME}}
    --physical-table-map {{PHYSICALTABLEMAP}}
    --import-mode {{IMPORTMODE}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-data-set
    --cli-input-json file://{{updatedataset}}.json
```

------

For more information about the `UpdateDataSet` API operation, see [UpdateDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSet.html) in the *Amazon Quick Sight API Reference*.