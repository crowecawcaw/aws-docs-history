# Using S3 Object Lock with Amazon S3 File Gateway

Amazon S3 File Gateway supports accessing S3 buckets that have Amazon S3 Object Lock turned on. Amazon S3
Object Lock allows you to store objects using a "Write Once Read Many" (WORM) model.
When you use Amazon S3 Object Lock, you can prevent an object in your S3 bucket from being
deleted or overwritten. Amazon S3 Object Lock works together with object versioning to
protect your data.

If you turn on Amazon S3 Object Lock, you can still modify the object. For example, it can
be written to, deleted, or renamed through a file share on a S3 File Gateway. When you modify
an object in this way, S3 File Gateway places a new version of the object without affecting the
previous version (that is, the locked object).

For example, If you use the S3 File Gateway NFS or SMB interface to delete a file and the
corresponding S3 object is locked, the gateway places an S3 delete marker as the next
version of the object, and leaves the original object version in place. Similarly, If a
S3 File Gateway modifies the contents or metadata of a locked object, a new version of the
object is uploaded with the changes, but the original locked version of the object
remains unchanged.

For more information about Amazon S3 Object Lock, see [Locking objects using S3 Object
Lock](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md") in the _Amazon Simple Storage Service User Guide_.
