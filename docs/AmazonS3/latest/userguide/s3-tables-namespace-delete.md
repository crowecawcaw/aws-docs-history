# Delete a namespace

Before you delete a table namespace from an Amazon S3 table bucket, you must delete all tables within
the namespace, or move them under another namespace. You can delete a namespace by using the Amazon S3 REST
API, AWS SDKs, AWS Command Line Interface (AWS CLI), or integrated query engines.

For information about the permissions required to delete a namespace, see [DeleteNamespace](../API/API_s3TableBuckets_DeleteNamespace.md "../API/API_s3TableBuckets_DeleteNamespace.md") in the _Amazon Simple Storage Service API Reference_.

This example shows you how to delete a table namespace by using the AWS CLI. To use this
example, replace the `user input placeholders` with your own
information.

```
aws s3tables delete-namespace \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1` \
    --namespace `example_namespace`
```
