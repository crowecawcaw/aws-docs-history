# Deleting a subnet group

If you decide that you no longer need your subnet group, you can delete it.
You cannot delete a subnet group if it is currently in use by a cluster. You also cannot delete a subnet group on a cluster with Multi-AZ enabled if doing so leaves
that cluster with fewer than two subnets. You must first uncheck **Multi-AZ** and then delete the subnet.

The following procedures show you how to delete a subnet group.

## Deleting a subnet group (Console)

###### To delete a subnet group

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. In the left navigation pane, choose **Subnet Groups**.
3. In the list of subnet groups,
   choose the one you want to delete, choose **Actions** and then choose **Delete**.

###### Note

You cannot delete a default subnet group or one that is associated with any clusters. 4. The **Delete Subnet Groups** confirmation screen will appear. 5. To delete the subnet group, enter `delete` in the confirmation text box.

To keep the subnet group, choose **Cancel**.

## Deleting a subnet group (AWS CLI)

Using the AWS CLI, call the command **delete-subnet-group** with the following
parameter:

- `--subnet-group-name` `mysubnetgroup`

For Linux, macOS, or Unix:

```
aws memorydb delete-subnet-group \
    --subnet-group-name `mysubnetgroup`
```

For Windows:

```
aws memorydb delete-subnet-group ^
    --subnet-group-name `mysubnetgroup`
```

For more information, see the AWS CLI topic [delete-subnet-group](../../../cli/latest/reference/memorydb/delete-subnet-group.md "../../../cli/latest/reference/memorydb/delete-subnet-group.md").

## Deleting a subnet group (MemoryDB API)

Using the MemoryDB API, call `DeleteSubnetGroup` with the following
parameter:

- `SubnetGroupName=`mysubnetgroup``

###### Example

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=DeleteSubnetGroup
    &SubnetGroupName=mysubnetgroup
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Timestamp=20210801T220302Z
    &Version=2021-01-01
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Credential=<credential>
    &X-Amz-Date=20210801T220302Z
    &X-Amz-Expires=20210801T220302Z
    &X-Amz-Signature=<signature>
    &X-Amz-SignedHeaders=Host
```

This command produces no output.

For more information, see the MemoryDB API topic [DeleteSubnetGroup](../APIReference/API_DeleteSubnetGroup.md "../APIReference/API_DeleteSubnetGroup.md").
