# Managing access controls

You can control a user's access to AWS Transfer Family resources by using an AWS Identity and Access Management (IAM)
policy. An IAM policy is a statement, typically in JSON format, that allows a certain
level of access to a resource. You use an IAM policy to define what file operations that
you want to allow your users to perform and not perform. You can also use an IAM policy to
define what Amazon S3 bucket or buckets that you want to give your users access to. To specify
these policies for users, you create an IAM role for AWS Transfer Family that has the IAM policy
and trust relationship associated with it.

Each user is assigned an IAM role. The type of IAM role that AWS Transfer Family uses is called a
_service role_. When a user logs in to your server, AWS Transfer Family assumes
the IAM role mapped to the user. To learn about creating an IAM role that provides a
user access to an Amazon S3 bucket, see [Creating a role to delegate
permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

You can grant write-only access to Amazon S3 objects by using certain permissions within an
IAM policy. For details, see [Grant ability to only write and
list files](configure-storage.md#headobject-access-denied "configure-storage.md#headobject-access-denied").

The AWS Storage Blog contains a post detailing how to set up least privilege access. For
details, see [Implementing least privilege access in an AWS Transfer Family workflow](https://aws.amazon.com/blogs/storage/implementing-least-privilege-access-in-an-aws-transfer-family-workflow/ "https://aws.amazon.com/blogs/storage/implementing-least-privilege-access-in-an-aws-transfer-family-workflow/").

###### Note

If your Amazon S3 bucket is encrypted using AWS Key Management Service (AWS KMS), you must specify additional permissions in your policy.
For details, see [Data protection and encryption](encryption-at-rest.md "encryption-at-rest.md"). Additionally, you can see more information about
[session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session.html "../../../IAM/latest/UserGuide/access_policies.md#policies_session.html") in the _IAM User Guide_.

###### Topics

- [Allowing read and write access to an Amazon S3
  bucket](users-policies-all-access.md "users-policies-all-access.md")
- [Creating a session policy for an Amazon S3
  bucket](users-policies-session.md "users-policies-session.md")
- [Dynamic permission management
  approaches](dynamic-permission-management.md "dynamic-permission-management.md")
