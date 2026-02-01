# Deleting an RDS Custom for Oracle snapshot

You can delete DB snapshots managed by RDS Custom for Oracle when you no longer need them. The deletion procedure is the same for both Amazon RDS and
RDS Custom DB instances.

The Amazon EBS snapshots for the binary and root volumes remain in your account for a longer time because they might be linked
to some instances running in your account or to other RDS Custom for Oracle snapshots. These EBS snapshots are automatically deleted after
they're no longer related to any existing RDS Custom for Oracle resources (DB instances or backups).

###### To delete a snapshot of an RDS Custom DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the DB snapshot that you want to delete.
4. For **Actions**, choose **Delete snapshot**.
5. Choose **Delete** on the confirmation page.
   To delete an RDS Custom snapshot, use the AWS CLI command [delete-db-snapshot](../../../cli/latest/reference/rds/delete-db-snapshot.md "../../../cli/latest/reference/rds/delete-db-snapshot.md").

The following option is required:

- `--db-snapshot-identifier` – The snapshot to be deleted
  The following example deletes the `my-custom-snapshot` DB snapshot.

For Linux, macOS, or Unix:

```
aws rds delete-db-snapshot \
  --db-snapshot-identifier `my-custom-snapshot`
```

For Windows:

```
aws rds delete-db-snapshot ^
  --db-snapshot-identifier `my-custom-snapshot`
```
