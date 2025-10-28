# Deleting a CEV

You can delete a CEV using the AWS Management Console or the AWS CLI. Typically, deletion takes a few minutes.

To delete a CEV, it can't be in use by any of the following:

- An RDS Custom DB instance
- A snapshot of an RDS Custom DB instance
- An automated backup of your RDS Custom DB instance

###### To delete a CEV

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Custom engine versions**.
3. Choose a CEV whose description or status you want to delete.
4. For **Actions**, choose **Delete**.

The **Delete `cev_name`?** dialog box appears. 5. Enter `delete me`, and then choose **Delete**.

In the **Custom engine versions** page, the banner shows that your CEV is being deleted.
To delete a CEV by using the AWS CLI, run the [delete-custom-db-engine-version](../../../cli/latest/reference/rds/delete-custom-db-engine-version.md "../../../cli/latest/reference/rds/delete-custom-db-engine-version.md") command.

The following options are required:

- `--engine `engine-type``, where
`engine-type`is`custom-oracle-ee`,
`custom-oracle-se2`, `custom-oracle-ee-cdb`, or
`custom-oracle-se2-cdb`
- `--engine-version `cev``, where `cev`is the name of the custom
 engine version to be deleted
The following example deletes a CEV named`19.my_cev1`.

For Linux, macOS, or Unix:

```
aws rds delete-custom-db-engine-version \
    --engine custom-oracle-ee \
    --engine-version `19.my_cev1`
```

For Windows:

```
aws rds delete-custom-db-engine-version ^
    --engine custom-oracle-ee ^
    --engine-version `19.my_cev1`
```
