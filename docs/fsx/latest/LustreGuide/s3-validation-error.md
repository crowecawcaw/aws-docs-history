# Unable to validate access to an S3 bucket when creating a DRA

Creating a data repository association (DRA) from the Amazon FSx console or using the
`create-data-repository-association` CLI command
([CreateDataRepositoryAssociation](../APIReference/API_CreateDataRepositoryAssociation.md "../APIReference/API_CreateDataRepositoryAssociation.md")
is the equivalent API action) fails with the following error message.

```
Amazon FSx is unable to validate access to the S3 bucket. Ensure the IAM role or user
you are using has s3:Get*, s3:List* and s3:PutObject permissions to the S3 bucket prefix.
```

###### Note

You can also get the above error when creating a Scratch 1, Scratch 2, or Persistent 1
file system that is linked to a data repository (S3 bucket or prefix) using the Amazon FSx console
or the `create-file-system` CLI command
([CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md")
is the equivalent API action).

**Action to take**

If the FSx for Lustre file system is in the same account as the S3 bucket, this error means
the IAM role you used for the create request doesn't have the necessary permissions to access the S3 bucket.
Make sure the IAM role has the permissions listed in the error message. These permissions
support the Amazon FSx for Lustre service-linked role that is used to access the specified Amazon S3 bucket on
your behalf.

If the FSx for Lustre file system is in a different account as the S3 bucket (cross-account case),
in additional to making sure the IAM role you used has the required permissions,
the S3 bucket policy should be configured to allow the access from the account that the
FSx for Lustre is created in.

For more information about S3 cross-account bucket permissions, see [Example 2: Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md")
in the _Amazon Simple Storage Service User Guide_.
