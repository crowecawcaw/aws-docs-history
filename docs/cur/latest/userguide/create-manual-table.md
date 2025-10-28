# Creating an Athena table

AWS includes the SQL that you need to run to create this table in your AWS CUR
bucket.

###### To create your Athena table

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. From the list of buckets, choose the bucket where you chose to receive your
   Cost and Usage Reports.
3. Navigate the path
   ``your-report-prefix`-`your-report-name`-`path-to-report``.

The exact path depends on whether your AWS CUR is set to overwrite previous versions.
For more information, see [Cost and Usage Reports delivery timeline](understanding-report-versions.md#access-cur-s3-timeline "understanding-report-versions.md#access-cur-s3-timeline"). 4. Open the file
``my-report-name`-create-table.sql`.
5. Copy the SQL from the file, starting with `CREATE` and ending with
 `LOCATION
 's3://`your-report-prefix`/`your-report-name`/`the-rest-of-the=path`'`.
 Take note of the first line, as you need the database name and table to create the Athena
 database.
6. Open the Athena console at
 [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
7. In the **New query 1** query pane, paste the following SQL. For
 ``<database name>.<table name>``, use the
database and table name from the first line of the SQL that you copied.

```
CREATE DATABASE <database name>
```

8. Choose **Run query**.
9. In the dropdown menu, choose the database that you just created.
10. In the **New query 1** query pane, paste the rest of the SQL from
    the SQL file.
11. Choose **Run query**.
    After you create your table, you need to load your partitions before you can run a
    query. For more information, see [Uploading your report partitions](upload-report-partitions.md "upload-report-partitions.md").
