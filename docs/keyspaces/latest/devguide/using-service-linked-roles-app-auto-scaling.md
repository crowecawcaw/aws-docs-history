# Using roles for Amazon Keyspaces application auto scaling

Amazon Keyspaces (for Apache Cassandra) uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Keyspaces. Service-linked roles are predefined by Amazon Keyspaces and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon Keyspaces easier because you don’t have to
manually add the necessary permissions. Amazon Keyspaces defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon Keyspaces can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your Amazon Keyspaces resources because you can't inadvertently remove permission to
access the resources.

## Service-linked role

permissions for Amazon Keyspaces

Amazon Keyspaces uses the service-linked role named **AWSServiceRoleForApplicationAutoScaling_CassandraTable**
to allow Application Auto Scaling to call Amazon Keyspaces and Amazon CloudWatch on your behalf.

The AWSServiceRoleForApplicationAutoScaling_CassandraTable service-linked role trusts the following services to assume the
role:

- `cassandra.application-autoscaling.amazonaws.com`

The role permissions policy allows Application Auto Scaling to complete the following actions on the
specified Amazon Keyspaces resources:

- Action: `cassandra:Select` on
  `arn:*:cassandra:*:*:/keyspace/system/table/*`
- Action: `cassandra:Select` on the resource
  `arn:*:cassandra:*:*:/keyspace/system_schema/table/*`
- Action: `cassandra:Select` on the resource
  `arn:*:cassandra:*:*:/keyspace/system_schema_mcs/table/*`
- Action: `cassandra:Alter` on the resource
  `arn:*:cassandra:*:*:"*"`

## Creating a service-linked role for

Amazon Keyspaces

You don't need to manually create a service-linked role for Amazon Keyspaces automatic scaling. When you
enable Amazon Keyspaces auto scaling on a table with the AWS Management Console, CQL, the AWS CLI, or the AWS API, Application Auto Scaling
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you enable Amazon Keyspaces auto scaling for a
table, Application Auto Scaling creates the service-linked role for you again.

###### Important

This service-linked role can appear in your account if you completed an action in another
service that uses the features supported by this role.
To
learn more, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

## Editing a service-linked role for

Amazon Keyspaces

Amazon Keyspaces does not allow you to edit the AWSServiceRoleForApplicationAutoScaling_CassandraTable service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Amazon Keyspaces

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that isn't
actively monitored or maintained. However, you must first disable automatic scaling on all
tables in the account across all AWS Regions before you can delete the service-linked role
manually. To disable automatic scaling on Amazon Keyspaces tables, see [Turn off Amazon Keyspaces auto scaling for a table](autoscaling.md "autoscaling.md").

###### Note

If Amazon Keyspaces automatic scaling is using the role when you try to modify the resources,
then the deregistration might fail. If that happens, wait for a few minutes and try the
operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForApplicationAutoScaling_CassandraTable service-linked
role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

###### Note

To delete the service-linked role used by Amazon Keyspaces automatic scaling, you must first disable
automatic scaling on all tables in the account.

## Supported Regions for Amazon Keyspaces

service-linked roles

Amazon Keyspaces supports using service-linked roles in all of the Regions where the
service is available. For more information, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").
