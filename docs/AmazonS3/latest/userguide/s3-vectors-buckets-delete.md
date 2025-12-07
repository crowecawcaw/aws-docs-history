# Deleting an empty vector bucket

You can delete a vector bucket when you no longer need it. To delete a vector bucket, you
must first delete all the vector indexes within the bucket. When you delete a vector index,
all vector data within it is deleted. Use the Amazon S3 REST API, AWS SDKs, S3 Console, or the AWS Command Line Interface (AWS CLI) to delete a vector bucket.

Before you can delete a vector bucket, you must:

- Delete all vector indexes in the bucket.
- Ensure no operations are in progress on the bucket or its indexes.

###### Important

- Bucket deletion is permanent and can't be undone.
- All data and configuration associated with the bucket is permanently
  lost.
- The bucket name becomes available for reuse after deletion.
- Any applications or scripts referencing the bucket will receive errors
  after deletion.

1. Sign in to the console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. The console displays a list of all your vector buckets. Find a bucket based on the start of the bucket name, enter a vector bucket name or prefix in the search box above the bucket list. Once you locate and choose your vector bucket, select the **Delete** option.
4. To confirm this deletion, type `delete` and then select **Delete vector bucket**.
   First, check that no vector indexes exist in the bucket. For more information
   about how to verify the bucket is empty, see [Listing vector indexes](s3-vectors-index-list.md "s3-vectors-index-list.md").

If indexes exist, you must delete all vectors from each index and then delete the
indexes. For more information about how to verify the bucket is empty, see [Listing vectors](s3-vectors-list.md "s3-vectors-list.md"), [Deleting vectors from a vector index](s3-vectors-delete.md "s3-vectors-delete.md"), and [Deleting a vector index](s3-vectors-index-delete.md "s3-vectors-index-delete.md").

To delete the empty vector bucket, use the following example command and replace
the `user input placeholders` with your own information.

```
aws s3vectors delete-vector-bucket \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`"
```

SDK for Python

```
import boto3

# Create a S3 Vectors client in the AWS Region of your choice.
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

#Delete a vector bucket
response = s3vectors.delete_vector_bucket(vectorBucketName="media-embeddings")

```
