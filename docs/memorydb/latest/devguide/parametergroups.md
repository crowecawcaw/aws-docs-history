# Deleting a parameter group

You can delete a custom parameter group using the MemoryDB console, the AWS CLI, or the MemoryDB API.

You cannot delete a parameter group if it is associated with any clusters.
Nor can you delete any of the default parameter groups.

## Deleting a parameter group (Console)

The following procedure shows how to delete a parameter group using the MemoryDB console.

###### To delete a parameter group using the MemoryDB console

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. To see a list of all available parameter groups,
   in the left hand navigation pane choose **Parameter Groups**.
3. Choose the parameter groups you want to delete by choosing the radio button to the left of
   the parameter group's name.

Choose **Actions** and then choose **Delete**. 4. The **Delete Parameter Groups** confirmation screen will appear. 5. To delete the parameter groups enter **Delete** in the confirmation text box.

To keep the parameter groups, choose **Cancel**.

## Deleting a parameter group (AWS CLI)

To delete a parameter group using the AWS CLI,
use the command `delete-parameter-group`.
For the parameter group to delete, the parameter group specified by
`--parameter-group-name` cannot have any clusters associated with it,
nor can it be a default parameter group.

The following sample code deletes the _myRedis6x_ parameter group.

For Linux, macOS, or Unix:

```
aws memorydb delete-parameter-group \
    --parameter-group-name `myRedis6x`
```

For Windows:

```
aws memorydb delete-parameter-group ^
    --parameter-group-name `myRedis6x`
```

For more information, see [delete-parameter-group](../../../cli/latest/reference/memorydb/delete-parameter-group.md "../../../cli/latest/reference/memorydb/delete-parameter-group.md").

## Deleting a parameter group (MemoryDB API)

To delete a parameter group using the MemoryDB API,
use the `DeleteParameterGroup` action.
For the parameter group to delete, the parameter group specified by
`ParameterGroupName`
cannot have any clusters associated with it,
nor can it be a default parameter group.

The following sample code deletes the _myRedis6x_ parameter group.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=DeleteParameterGroup
   &ParameterGroupName=`myRedis6x`
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20210802T192317Z
   &Version=2021-01-01
   &X-Amz-Credential=<credential>
```

For more information, see [`DeleteParameterGroup`](../APIReference/API_DeleteParameterGroup.md "../APIReference/API_DeleteParameterGroup.md").
