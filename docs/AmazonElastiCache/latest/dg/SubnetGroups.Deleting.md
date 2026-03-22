# Deleting a subnet group

If you decide that you no longer need your subnet group, you can delete it.
You cannot delete a subnet group if it is currently in use by a cache.

The following procedures show you how to delete a subnet group.

## Deleting a subnet group (Console)

###### To delete a subnet group

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Subnet groups**.
3. In the list of subnet groups,
   choose the one you want to delete and then choose **Delete**.
4. When you are asked to confirm this operation, type the name of the subnet group in the text input field and choose **Delete**.

## Deleting a subnet group (AWS CLI)

Using the AWS CLI, call the command **delete-cache-subnet-group** with the following
parameter:

- `--cache-subnet-group-name` `mysubnetgroup`

For Linux, macOS, or Unix:

```
aws elasticache delete-cache-subnet-group \
    --cache-subnet-group-name `mysubnetgroup`
```

For Windows:

```
aws elasticache delete-cache-subnet-group ^
    --cache-subnet-group-name `mysubnetgroup`
```

This command produces no output.

For more information, see the AWS CLI topic delete-cache-subnet-group.
