# CreateDataSet

Use the `CreateDataSet` API operation to create a dataset. Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight create-data-set
    --aws-account-id `AWSACCOUNTID`
    --data-set-id `DATASETID`
    --name `NAME`
    --physical-table-map '{"PhysicalTableMap":{"`string`":{"CustomSql":{"Columns":[{"Name":"`string`","Type":"`string`"}],"DataSourceArn":"`string`","Name":"`string`","SqlQuery":"`string`"},"RelationalTable":{"Catalog":"`string`","DataSourceArn":"`string`","InputColumns":[{"Name":"`string`","Type":"`string`"}],"Name":"`string`","Schema":"`string`"},"S3Source":{"DataSourceArn":"`string`","InputColumns":[{"Name":"`string`","Type":"`string`"}],"UploadSettings":{"ContainsHeader":boolean,"Delimiter":"`string`","Format":"`string`","StartFromRow":number,"TextQualifier":"`string`"}}}}'
    --import-mode DIRECT_QUERY
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight create-data-set
    --cli-input-json file://`createdataset`.json
```

For more information about the `CreateDataSet` API operation, see [CreateDataSet](../APIReference/API_CreateDataSet.md "../APIReference/API_CreateDataSet.md") in the _Amazon Quick Sight API Reference_.
