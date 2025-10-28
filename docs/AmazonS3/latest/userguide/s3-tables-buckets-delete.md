# Deleting a table bucket

You can use the Amazon S3 APIs, AWS Command Line Interface, or AWS SDKs to delete a table bucket. Before you
delete a table bucket, you must first delete all namespaces and tables within the bucket.

###### Important

When you delete a table bucket, you need to know the following:

- Bucket deletion is permanent and can't be undone.
- All data and configurations associated with the bucket are permanently lost.
  This example shows how to delete a table bucket by using the AWS CLI. To use this
  example, replace the `user input placeholders` with your
  own information.

```
aws s3tables delete-table-bucket \
    --region `us-east-2` \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1`
```
