# Deleting an empty vector bucket

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

You can delete a vector bucket when you no longer need it. To delete a vector bucket, you
 must first delete all the vector indexes within the bucket. When you delete a vector index,
 all vector data within it is deleted. Use the AWS CLI, SDKs, or API to delete a vector
 bucket or index. You can't delete a vector bucket or vector index using the console.

Before you can delete a vector bucket, you must:


* Delete all vector indexes in the bucket.
* Ensure no operations are in progress on the bucket or its indexes.
###### Important


* Bucket deletion is permanent and can't be undone.
* All data and configuration associated with the bucket is permanently
 lost.
* The bucket name becomes available for reuse after deletion.
* Any applications or scripts referencing the bucket will receive errors
 after deletion.
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
