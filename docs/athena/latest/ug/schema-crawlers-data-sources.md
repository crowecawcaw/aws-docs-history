# Use multiple data sources with a crawler

When an AWS Glue crawler scans Amazon S3 and detects multiple directories, it uses a heuristic
to determine where the root for a table is in the directory structure, and which
directories are partitions for the table. In some cases, where the schema detected in
two or more directories is similar, the crawler may treat them as partitions instead of
separate tables. One way to help the crawler discover individual tables is to add each
table's root directory as a data store for the crawler.

The following partitions in Amazon S3 are an example:

```
s3://amzn-s3-demo-bucket/folder1/table1/partition1/file.txt
s3://amzn-s3-demo-bucket/folder1/table1/partition2/file.txt
s3://amzn-s3-demo-bucket/folder1/table1/partition3/file.txt
s3://amzn-s3-demo-bucket/folder1/table2/partition4/file.txt
s3://amzn-s3-demo-bucket/folder1/table2/partition5/file.txt
```

If the schema for `table1` and `table2` are similar, and a
single data source is set to `s3://amzn-s3-demo-bucket/folder1/` in AWS Glue,
the crawler may create a single table with two partition columns: one partition column
that contains `table1` and `table2`, and a second partition column
that contains `partition1` through `partition5`.

To have the AWS Glue crawler create two separate tables, set the crawler to have two data
sources, `s3://amzn-s3-demo-bucket/folder1/table1/` and
`s3://amzn-s3-demo-bucket/folder1/table2`, as shown in the following
procedure.

###### To add an S3 data store to an existing crawler in AWS Glue

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **Crawlers**.
3. Choose the link to your crawler, and then choose **Edit**.
4. For **Step 2: Choose data sources and classifiers**, choose
   **Edit**.
5. For **Data sources and catalogs**, choose **Add a data
   source**.
6. In the **Add data source** dialog box, for **S3
   path**, choose **Browse**.
7. Select the bucket that you want to use, and then choose
   **Choose**.

The data source that you added appears in the **Data
sources** list. 8. Choose **Next**. 9. On the **Configure security settings** page, create or choose
an IAM role for the crawler, and then choose **Next**. 10. Make sure that the S3 path ends in a trailing slash, and then choose
**Add an S3 data source**. 11. On the **Set output and scheduling** page, for
**Output configuration**, choose the target
database. 12. Choose **Next**. 13. On the **Review and update** page, review the choices that
you made. To edit a step, choose **Edit**. 14. Choose **Update**.
