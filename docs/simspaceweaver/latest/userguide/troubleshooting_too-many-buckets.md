End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# TooManyBuckets

You might receive the following error while creating a project:

```
An error occurred (TooManyBuckets) when calling the CreateBucket operation: You have attempted to create more buckets than allowed.
```

Amazon Simple Storage Service (Amazon S3) has a limit on the number of buckets that you can have in your AWS account (for
more information, see [Bucket restrictions and
limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the _Amazon Simple Storage Service User Guide_).

You must do one of the following before you can continue:

- Delete 2 or more existing Amazon S3 buckets that you don't need.
- Request an Amazon S3 limit increase (for more information, see [Bucket restrictions and limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the _Amazon Simple Storage Service User
  Guide_ ).
- Use a different AWS account.

###### Note

The `DeleteSimulation` API in SimSpace Weaver doesn't delete Amazon S3 resources
associated with your simulation. We recommend that you remove all resources
associated with your simulations when you no longer need them.
