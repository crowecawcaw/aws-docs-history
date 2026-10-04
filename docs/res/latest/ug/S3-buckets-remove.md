

End of development notice: AWS is discontinuing development of Research and Engineering Studio on AWS (RES). 2026.09 is the final release, supported through September 30, 2027. RES remains open source and keeps running in your account. For more information, see [RES end of support](res-end-of-support.md).

# Remove an Amazon S3 bucket
<a name="S3-buckets-remove"></a>

1. Select an S3 bucket in the S3 buckets list.

1. From the **Actions** menu, select **Remove**.
**Important**  
You must first remove all project associations from the bucket.
The remove operation does not impact the data in the S3 bucket. It only removes the S3 bucket’s association with RES.
Removing a bucket will cause existing VDI sessions to lose access to the contents of that bucket at the expiration of that session’s credentials (\~1 hour).