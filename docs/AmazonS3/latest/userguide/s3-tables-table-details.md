# Viewing details about an Amazon S3 table

You can view the general details of a table in a table bucket, such creation details, format and type, in the console or programmatically. You can view table encryption settings, and maintenance settings programmatically by using the S3 Tables REST API, AWS CLI or AWS SDKs.


## Viewing table details


This example shows how to get details about a table by using the
 AWS CLI. To use this example, replace the `user input
 placeholders` with your own information.


```
aws s3tables get-table --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket --namespace `my-namespace` --name `my-table`
```

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table
 buckets**.
3. Select your table bucket, then select your table.
4. Select the **Properties** tab.
5. (Optional) For information about the permission policy attached to the table, select **Permissions**.

## Previewing table data


You can preview the data in your table directly from the Amazon S3 console using the following procedure.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the bucket that contains the table that you want to query.
4. Select the table you want to preview then, choose **Preview**.
###### Note

The preview shows the first 10 rows and up to 25 columns of your table. Tables over 50mb cannot be previewed.


## Encryption details


For more information about table bucket encryption, see [Using server-side encryption with AWS KMS keys
 (SSE-KMS) in table buckets](s3-tables-kms-encryption.md "s3-tables-kms-encryption.md").


This example shows how to get details about encryption settings for a
 table by using the AWS CLI. To use this example, replace the
 `user input placeholders` with your own
 information.


```
aws s3tables get-table-encryption --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket --namespace `my-namespace` --name `my-table`
```

## Maintenance details


For information about maintenance settings, see [Maintenance for table buckets](s3-table-buckets-maintenance.md "s3-table-buckets-maintenance.md")



This example shows how to get details about maintenance configuration settings
 for a table by using the AWS CLI. To use this example, replace the
 `user input placeholders` with your own
 information.


```
aws s3tables get-table-maintenance-configuration --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket --namespace `my-namespace` --name `my-table`
```
