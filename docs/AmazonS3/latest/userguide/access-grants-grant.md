# Working with grants in S3 Access Grants

An individual access *grant* in an S3 Access Grants instance allows a specific identity—an AWS Identity and Access Management (IAM) principal, or a user or group in a corporate directory—to get access within a location that is registered in your S3 Access Grants instance. A location maps buckets or prefixes to an IAM role. S3 Access Grants assumes this IAM role to vend temporary credentials to grantees. 

After you [register at least one
 location](access-grants-location.md "access-grants-location.md") in your S3 Access Grants instance, you can create an access grant.

The grantee can be an IAM user or role or a directory user or group. A
 directory user is a user from your corporate directory or external identity source that you [associated with your
 S3 Access Grants instance](access-grants-instance-idc.md "access-grants-instance-idc.md"). For more information, see [S3 Access Grants and corporate directory
 identities](access-grants-directory-ids.md "access-grants-directory-ids.md"). To create a grant for a specific directory user or group from IAM Identity Center, find
 the GUID that IAM Identity Center uses to identify that user in IAM Identity Center, for example,
 `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. For more information about how to use IAM Identity Center to view user information, see [View user and group assignments](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-view-assignments.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-view-assignments.html") in the *AWS IAM Identity Center user guide*. 

You can grant access to a bucket, a prefix, or an object. A prefix in Amazon S3 is a string
 of characters in the beginning of an object key name that is used to organize objects within
 a bucket. This can be any string of allowed characters, for example, object key names in your
 bucket that start with the `engineering/` prefix. 

###### Topics

* [Create grants](access-grants-grant-create.md "access-grants-grant-create.md")
* [View a grant](access-grants-grant-view.md "access-grants-grant-view.md")
* [Delete a grant](access-grants-grant-delete.md "access-grants-grant-delete.md")
