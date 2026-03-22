# Downloading a database log file

You can use the AWS Management Console, AWS CLI, or API to download a database log file.

###### To download a database log file

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the name of the DB instance that has the log file that you want to view.
4. Choose the **Logs & events** tab.
5. Scroll down to the **Logs** section.
6. In the **Logs** section, choose the button next to the log that you want to
   download, and then choose **Download**.
7. Open the context (right-click) menu for the link provided, and then choose **Save Link
   As**. Enter the location where you want the log file to be saved, and then choose
   **Save**.

![viewing log file](images/log_download2.png)
To download a database log file, use the AWS CLI command [`download-db-log-file-portion`](../../../cli/latest/reference/rds/download-db-log-file-portion.md "../../../cli/latest/reference/rds/download-db-log-file-portion.md"). By default, this command downloads only the
latest portion of a log file. However, you can download an entire file by specifying the parameter
`--starting-token 0`.

The following example shows how to download the entire contents of a log file called
_log/ERROR.4_ and store it in a local file called
_errorlog.txt_.

###### Example

For Linux, macOS, or Unix:

```
aws rds download-db-log-file-portion \
    --db-instance-identifier `myexampledb` \
    --starting-token 0 --output text \
    --log-file-name `log/ERROR.4` > `errorlog.txt`
```

For Windows:

```
aws rds download-db-log-file-portion ^
    --db-instance-identifier `myexampledb` ^
    --starting-token 0 --output text ^
    --log-file-name `log/ERROR.4` > `errorlog.txt`
```

To download a database log file, use the Amazon RDS API [`DownloadDBLogFilePortion`](../APIReference/API_DownloadDBLogFilePortion.md "../APIReference/API_DownloadDBLogFilePortion.md")
action.
