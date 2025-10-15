# Deleting an Amazon S3 table

You can delete a table by using the Amazon S3 REST API, AWS SDK, AWS CLI or using integrated query engines.

###### Note

S3 Tables doesn't support the `DROP TABLE` operation with
 `purge=false`. Some versions of Spark always set this flag to
 false even when running `DROP TABLE PURGE` commands. You can retry with
 `DROP TABLE` with `purge=true` or use the S3 Tables [DeleteTable](../API/API_s3TableBuckets_DeleteTable.md "../API/API_s3TableBuckets_DeleteTable.md") REST API to delete a table.

###### Important


 When you delete a table, you need to know the following:


* When you delete a table, the objects associated with that table become non-current and can take up to one day to get removed.
* Deleting a table is permanent and cannot be undone. Before deleting a table, make sure that you have backed up or replicated any important data.
This example shows how to delete a table by using the AWS CLI. To use the
 command replace the `user input placeholders` with your own
 information.


```
aws s3tables delete-table \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
    --namespace `example_namespace` --name `example_table`
```
You can delete a table in an Apache Spark session connected to your
 Amazon S3 table buckets.

This example shows how to delete a table by using the `DROP TABLE PURGE` command. To use the command replace the
 `user input placeholders` with your own
 information.


```
spark.sql( 
" DROP TABLE [IF EXISTS] s3tablesbucket.`example_namespace`.`example_table` PURGE")
```
