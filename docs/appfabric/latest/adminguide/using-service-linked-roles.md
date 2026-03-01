# Using service-linked roles for AppFabric

AWS AppFabric uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AppFabric. Service-linked roles are predefined by AppFabric and
include all the permissions that the service requires to call other
AWS services
on your behalf.

A service-linked role makes setting up AppFabric easier because you don’t have to
manually add the necessary permissions. AppFabric defines the permissions of its
service-linked roles, and unless defined otherwise, only AppFabric can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy
can't
be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AppFabric resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions for AppFabric

AppFabric uses the service-linked role named
`AWSServiceRoleForAppFabric`

–
Allows AppFabric to put data in the an ingestion destination resource,
such as an Amazon S3 bucket or an Amazon Data Firehose delivery stream. It also allows AppFabric to put CloudWatch metric data
in the `AWS/AppFabric` namespace..

The
`AWSServiceRoleForAppFabric`
service-linked role trusts the following services to assume the role:

- `appfabric.amazonaws.com`

The role permissions policy named
`AWSAppFabricServiceRolePolicy`
allows AppFabric to complete the following actions on the specified resources:

- Action: `cloudwatch:PutMetricData` in the `AWS/AppFabric`
  namespace. This
  action
  grants permission for AppFabric to put metric data into the Amazon CloudWatch
  `AWS/AppFabric` namespace. For more information about the AppFabric metrics
  available in CloudWatch, see [Monitoring AWS AppFabric with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- Action: `s3:PutObject` in an Amazon S3 bucket. This
  action
  grants permission for AppFabric to put ingested data into an Amazon S3 bucket
  that you specify.
- Action: `firehose:PutRecordBatch` in an Amazon Data Firehose delivery stream. This
  action
  grants permission for AppFabric to put ingested data into
  an
  Amazon Data Firehose delivery stream that you specify.

For
more information, see [AWS managed
policies for AppFabric](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AppFabric

You don't need to manually create a service-linked role. When you
create an AppFabric app bundle in the AWS Management Console, the AWS CLI, or the AWS API, AppFabric creates
the service-linked role for you.

## Editing a service-linked role for AppFabric

AppFabric doesn't
allow you to
edit the
`AWSServiceRoleForAppFabric`
service-linked role. After you create a service-linked role, you
can't
change the name of the role because various entities might reference the role. However, you
can edit the description of the role using IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AppFabric

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must delete all of your AppFabric app bundles
before you can delete the service-linked role.

### Cleaning up a service-linked role

Before you can use IAM to delete a service-linked role, you must first delete any
resources used by the role. App bundles that you create in AppFabric are used by the role. For
more information, see [Delete AWS AppFabric for security resources](delete-resources.md "delete-resources.md").

###### Note

If the AppFabric service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

### Manually delete the service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForAppFabric`
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for AppFabric service-linked roles

AppFabric supports using service-linked roles in all of the
AWS Regions
where the service is available. For more information, see [AppFabric endpoints and
quotas](../../../general/latest/gr/appfabric.md "../../../general/latest/gr/appfabric.md") in the
_AWS General Reference_.
