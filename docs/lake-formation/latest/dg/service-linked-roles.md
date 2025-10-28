# Using service-linked roles for Lake Formation

AWS Lake Formation uses an AWS Identity and Access Management (IAM) _service-linked role_. A
service-linked role is a unique type of IAM role that is linked directly to Lake Formation. The
service-linked role is predefined by Lake Formation and includes all the permissions that the service
requires to call other AWS services on your behalf.

A service-linked role makes setting up Lake Formation easier because you don’t have to create a role
and manually add the necessary permissions. Lake Formation defines the permissions of its service-linked
role, and unless defined otherwise, only Lake Formation can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions policy can't be
attached to any other IAM entity.

This service-linked role trusts the following services to assume the role:

- `lakeformation.amazonaws.com`
  When you use a service-linked role in account A to register an Amazon S3 location that is owned by account B, the Amazon S3
  bucket policy (a resource-based policy) in account B must grant access permissions to the service-linked role in account A.

For information about using service-linked role to register a data location, see [Service-linked role limitations](service-linked-role-limitations.md "service-linked-role-limitations.md").

###### Note

Service control policies (SCPs) don't affect service-linked roles.

For more information, see [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations user guide_.

## Service-linked role permissions for

Lake Formation

Lake Formation uses the service-linked role named
`AWSServiceRoleForLakeFormationDataAccess`. This role provides a set of Amazon Simple Storage Service
(Amazon S3) permissions that enable the Lake Formation integrated service (such as Amazon Athena) to
access registered locations. When you register a data lake location, you must provide a role
that has the required Amazon S3 read/write permissions on that location. Instead of creating a role
with the required Amazon S3 permissions, you can use this service-linked role.

The first time that you name the service-linked role as the role with which to register a
path, the service-linked role and a new IAM policy are created on your behalf. Lake Formation adds the
path to the inline policy and attaches it to the service-linked role. When you register
subsequent paths with the service-linked role, Lake Formation adds the path to the existing
policy.

While signed in as a data lake administrator, register a data lake location. Then, in the
IAM console, search for the role `AWSServiceRoleForLakeFormationDataAccess` and
view its attached policies.

For example, after you register the location
`s3://my-kinesis-test/logs`, Lake Formation creates the following inline policy and
attaches it to `AWSServiceRoleForLakeFormationDataAccess`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationDataAccessPermissionsForS3",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": [
 "arn:aws:s3:::`my-kinesis-test/logs/*`"
 ]
 },
 {
 "Sid": "LakeFormationDataAccessPermissionsForS3ListBucket",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads"
 ],
 "Resource": [
 "arn:aws:s3:::`my-kinesis-test`"
 ]
 }
 ]
}`

```

## Creating a service-linked role for

Lake Formation

You don't need to manually create a service-linked role. When you
register an Amazon S3 location with Lake Formation in the AWS Management Console, the AWS CLI, or the AWS API, Lake Formation
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. To learn more, see [A new
role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you register an Amazon S3 location with Lake Formation,
Lake Formation creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**Lake Formation** use case. In the AWS CLI or the AWS API, create
a service-linked role with the `lakeformation.amazonaws.com` service name. For more
information, see [Creating a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for

Lake Formation

Lake Formation does not allow you to edit the `AWSServiceRoleForLakeFormationDataAccess` service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for

Lake Formation

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Lake Formation service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete Lake Formation resources used by the Lake Formation

- If you've used the service-linked role to register Amazon S3 locations with Lake Formation, before deleting the service-linked role, you need to deregister the location and reregister it using a custom role.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForLakeFormationDataAccess`
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
