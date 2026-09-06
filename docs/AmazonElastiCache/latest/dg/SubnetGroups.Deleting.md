

# Deleting a subnet group
<a name="SubnetGroups.Deleting"></a>

If you decide that you no longer need your subnet group, you can delete it. You cannot delete a subnet group if it is currently in use by a cache.

The following procedures show you how to delete a subnet group.

## Deleting a subnet group (Console)
<a name="SubnetGroups.Deleting.CON"></a>

**To delete a subnet group**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In the navigation pane, choose **Subnet groups**.

1. In the list of subnet groups, choose the one you want to delete and then choose **Delete**.

1. When you are asked to confirm this operation, type the name of the subnet group in the text input field and choose **Delete**.

## Deleting a subnet group (AWS CLI)
<a name="SubnetGroups.Deleting.CLI"></a>

Using the AWS CLI, call the command **delete-cache-subnet-group** with the following parameter:
+ `--cache-subnet-group-name` {{mysubnetgroup}}

For Linux, macOS, or Unix:

```
aws elasticache delete-cache-subnet-group \
    --cache-subnet-group-name {{mysubnetgroup}}
```

For Windows:

```
aws elasticache delete-cache-subnet-group ^
    --cache-subnet-group-name {{mysubnetgroup}}
```

This command produces no output.

For more information, see the AWS CLI topic [delete-cache-subnet-group](https://docs.aws.amazon.com/cli/latest/reference/elasticache/delete-cache-subnet-group.html).