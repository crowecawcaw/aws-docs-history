

# CreateDataSource
<a name="create-data-source"></a>

Use the `CreateDataSource` API operation to create a data source. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-data-source 
    --aws-account-id {{AWSACCOUNTID}} 
    --data-source-id {{DATASOURCEID}} 
    --name {{NAME}} 
    --type {{ATHENA}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-data-source
    --cli-input-json file://{{createdatasource}}.json
```

------

For more information about the `CreateDataSource` API operation, see [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html) in the *Amazon Quick Sight API Reference*.