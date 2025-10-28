# Viewing DNS aliases for file systems and backups

You can view the DNS aliases currently associated with your FSx for Windows File Server file systems and backups
using the AWS Management Console, the AWS CLI, and API, as described in the following procedures.

###### To view DNS aliases associated with file systems

- Using the console — Choose a file system to view the **File
  systems** detail page. Choose the **Network & security** tab to
  view the **DNS aliases**.
- Using the CLI or API — Use the `describe-file-system-aliases` CLI
  command or the [DescribeFileSystemAliases](../APIReference/API_DescribeFileSystemAliases.md "../APIReference/API_DescribeFileSystemAliases.md") API operation.

###### To view DNS aliases associated with backups

- Using the console — In the navigation pane, choose **Backups**,
  and then choose the backup that you want to view. In the **Summary** pane,
  view the **DNS aliases** field.
- Using the CLI or API — Use the `describe-backups` CLI command or the
  [DescribeBackups](../APIReference/API_DescribeBackups.md "../APIReference/API_DescribeBackups.md") API operation.
