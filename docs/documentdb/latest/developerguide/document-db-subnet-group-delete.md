# Deleting an Amazon DocumentDB subnet group

You can use the AWS Management Console or AWS CLI to delete an Amazon DocumentDB subnet group. However, you cannot delete the `default` subnet group.

Using the AWS Management Console
You can use the AWS Management Console to delete a subnet group. But you can't delete the `default` subnet group.

###### To delete a subnet group

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Subnet groups**. Then choose the button to the left of the subnet group's name. Remember
   that you can't delete the `default` subnet group.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. Choose **Actions**, and then choose **Delete**. 4. In the confirmation dialog box:

    * To delete the subnet group, choose **Delete**.
    * To keep the subnet group, choose **Cancel**.

Using the AWS CLI
To delete an Amazon DocumentDB subnet group using the AWS CLI, use the `delete-db-subnet-group` operation with the following parameter.

###### Parameter

- `--db-subnet-group-name`—Required. The name of the Amazon DocumentDB subnet group to delete. Remember that you can't delete the
  `default` subnet group.

###### Example

The following code deletes `sample-subnet-group`.

For Linux, macOS, or Unix:

```
aws docdb delete-db-subnet-group \
    --db-subnet-group-name `sample-subnet-group`
```

For Windows:

```
aws docdb delete-db-subnet-group ^
    --db-subnet-group-name `sample-subnet-group`
```

This operation produces no output.
