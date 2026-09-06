

# CreateGroupMembership
<a name="create-group-membership"></a>

Use the `CreateGroupMembership` API operation to add an Amazon Quick Sight user to a Quick Sight group. You can find users in a certain group by calling the `ListGroups` API operation, and then the `ListGroupMemberships` API operation on the group of your choice.

Following is an example AWS CLI command for this operation. In the following examples, the member {{`USERNAME`}} is added to the group {{`GROUPNAME`}}.

------
#### [ AWS CLI ]

```
aws quicksight create-group-membership 
    --namespace default 
    --aws-account-id {{AWSACCOUNTID}} 
    --group-name {{GROUPNAME}} 
    --member-name {{USERNAME}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-group-membership 
    --cli-input-json file://{{creategroupmembership}}.json
```

------

For more information about the `CreateGroupMembership` API operation, see [CreateGroupMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateGroupMembership.html) in the *Amazon Quick Sight API Reference*.