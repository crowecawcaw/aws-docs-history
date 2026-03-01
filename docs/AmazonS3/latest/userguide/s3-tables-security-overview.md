# Security for S3 Tables

Amazon S3 provides a variety of security features and tools. The following is a list of these
features and tools supported by S3 Tables. Proper application of these tools can help
ensure that your resources are protected and accessible only to the intended users.

###### Identity-based policies

[Identity-based
policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") are attached to an IAM user, group, or role. You can use
identity-based policies to grant an IAM identity access to your table buckets or
tables. By default, users and roles don't have permission to create and modify tables
and table buckets. They also can't perform tasks by using S3 console, AWS CLI, or Amazon S3
REST APIs. You can create IAM users, groups, and roles in your account and attach
access policies to them. You can then grant access to your resources. To create and
access table buckets and tables, an IAM administrator must grant the necessary
permissions to the AWS Identity and Access Management (IAM) role or users. For more information, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").

###### Resource-based policies

[Resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md")
are attached to a resource. You can create resource-based policies
for table buckets and tables. You can use a table bucket policy to control table bucket and
namespace-level API access permissions. You can also use a table bucket policy to
control table-level API permissions on multiple tables in a bucket.
Depending on the policy definition, the permissions attached to the bucket can apply to all or
specific tables in the bucket. You can also use a table policy to grant table-level API access permissions to individual tables in the bucket.

When S3 Tables receives a request to perform a table bucket operation or a table operation, it first
verifies that the requester has the necessary permissions. It evaluates all the relevant
access policies, user policies, and resource-based policies in deciding whether to authorize the
request (IAM user policy, IAM role policy, table bucket policy, and table policy). With table bucket policies and table policies, you can personalize access to
your resources to ensure that only the identities you have approved can
access your resources and perform actions on them. For more
information, see [Access management for
S3 Tables.](s3-tables-setting-up.md "s3-tables-setting-up.md")

###### AWS Organizations service control policies (SCPs) for S3 Tables.

You can use Amazon S3 Tables in Service Control Policies (SCPs) to manage permissions to
users in your organization. Similar to IAM and resource policies, all table and bucket
level actions are referenced as part of `s3tables` namespace in the policies. For more information, see [Service
control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide._

###### Topics

- [Protecting S3 table data with encryption](s3-tables-encryption.md "s3-tables-encryption.md")
- [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md")
- [VPC connectivity for S3 Tables](s3-tables-VPC.md "s3-tables-VPC.md")
- [Security considerations and limitations for S3 Tables](s3-tables-restrictions.md "s3-tables-restrictions.md")
