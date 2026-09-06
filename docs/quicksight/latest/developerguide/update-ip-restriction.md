

# UpdateIpRestriction
<a name="update-ip-restriction"></a>

Use the `UpdateIpRestriction` operation to update the content and status of IP rules. To use this operation, provide the entire map of rules. You can use the `DescribeIpRestriction` operation to get the current rule map.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-ip-restriction \
    --aws-account-id {{AWSACCOUNTID}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-ip-restriction \
    --cli-input-json file://{{updateiprestriction}}.json
```

------

For more information about the `UpdateIpRestriction` operation, see [UpdateIpRestriction](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIpRestriction) in the *Quick Sight API Reference*.