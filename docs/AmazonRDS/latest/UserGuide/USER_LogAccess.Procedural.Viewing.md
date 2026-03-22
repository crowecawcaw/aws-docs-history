# Viewing and listing database log files

You can view database log files for your Amazon RDS DB engine by
using the AWS Management Console. You can list what log files are available for download or monitoring by using the AWS CLI or Amazon RDS API.

###### Note

If you can't view the list of log files for an existing RDS for Oracle DB instance, reboot the instance to view the list.

###### To view a database log file

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the name of the DB instance that has the log file that you want to view.
4. Choose the **Logs & events** tab.
5. Scroll down to the **Logs** section.
6. (Optional) Enter a search term to filter your results.
7. Choose the log that you want to view, and then choose **View**.
   To list the available database log files for a DB instance, use the AWS CLI [`describe-db-log-files`](../../../cli/latest/reference/rds/describe-db-log-files.md "../../../cli/latest/reference/rds/describe-db-log-files.md")
   command.

The following example returns a list of log files for a DB instance named
`my-db-instance`.

###### Example

```
aws rds describe-db-log-files --db-instance-identifier my-db-instance
```

To list the available database log files for a DB instance, use the Amazon RDS API [`DescribeDBLogFiles`](../APIReference/API_DescribeDBLogFiles.md "../APIReference/API_DescribeDBLogFiles.md") action.
