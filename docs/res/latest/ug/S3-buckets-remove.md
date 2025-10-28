# Remove an Amazon S3 bucket

1. Select an S3 bucket in the S3 buckets list.
2. From the **Actions** menu, select **Remove**.

###### Important

    * You must first remove all project associations from the bucket.
    * The remove operation does not impact the data in the S3 bucket. It
     only removes the S3 bucket’s association with RES.
    * Removing a bucket will cause existing VDI sessions to lose access to
     the contents of that bucket at the expiration of that session’s credentials
     (~1 hour).
