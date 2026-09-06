

# CreateGroup
<a name="create-group"></a>

Use the `CreateGroup` API operation to create a user group in Amazon Quick Sight. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-group 
    --namespace {{NAMESPACE}} 
    --aws-account-id {{AWSACCOUNTID}} 
    --group-name {{GROUPNAME}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-group 
    --cli-input-json file://{{creategroup}}.json
```

------

For more information about the `CreateGroup` API operation, see [CreateGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateGroup.html) in the *Amazon Quick Sight API Reference*.