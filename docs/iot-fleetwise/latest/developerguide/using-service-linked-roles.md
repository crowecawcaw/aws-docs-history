# Using service-linked roles for

AWS IoT FleetWise

AWS IoT FleetWise uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS IoT FleetWise. Service-linked roles are predefined by AWS IoT FleetWise and
include the permissions that AWS IoT FleetWise needs to send metrics to Amazon CloudWatch. For more information, see [Monitor AWS IoT FleetWise with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

A service-linked role makes setting up AWS IoT FleetWise quicker because you don’t have to
manually add the necessary permissions. AWS IoT FleetWise defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS IoT FleetWise can assume its roles. The
defined permissions include the trust policy and the permissions policy. This permissions policy
can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS IoT FleetWise resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"), and look for the services that have **Yes** in the **Service-linked roles**
column. To view the service-linked role documentation for that service, choose a **Yes** with a link.

## Service-linked role permissions for

AWS IoT FleetWise

AWS IoT FleetWise uses the service-linked role named **AWSServiceRoleForIoTFleetWise** –
An AWS managed policy that is used for all out-of-the-box permissions for AWS IoT FleetWise.

The AWSServiceRoleForIoTFleetWise service-linked role trusts the following services to assume the
role:

- `IoTFleetWise`

The role permissions policy named [AWSIoTFleetwiseServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSIoTFleetwiseServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSIoTFleetwiseServiceRolePolicy.md") allows AWS IoT FleetWise to
complete the following actions on the specified resources:

- Action: `cloudwatch:PutMetricData` on resource: `*`

For information about changes to this policy, see [AWSIoTFleetwiseServiceRolePolicy policy updates](managed-policy-updates.md "managed-policy-updates.md").

The service-linked role has permissions to publish metrics to the following CloudWatch namespaces:

- `AWS/IoTFleetWise` – For service-specific metrics
- `AWS/Usage` – For usage metrics

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS IoT FleetWise

You don't need to manually create a service-linked role. When you
register an account in the AWS IoT FleetWise console, the AWS CLI, or the AWS API, AWS IoT FleetWise creates
the service-linked role for you. For more information, see [Configure your AWS IoT FleetWise settings](configure-settings.md "configure-settings.md").

### Creating a service-linked role

in AWS IoT FleetWise (console)

You don't need to manually create a service-linked role. When you
register an account in the AWS IoT FleetWise console, the AWS CLI,
or the AWS API, AWS IoT FleetWise creates the service-linked role for you.

### Editing a service-linked role for

AWS IoT FleetWise

You can't edit the AWSServiceRoleForIoTFleetWise service-linked role in AWS IoT FleetWise. Because various
entities might reference any service-linked role you create, you can't change the name of
the role. However, you can edit the description of the role by using IAM. For more
information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

### Cleaning up a service-linked

role

Before you can use IAM to delete a service-linked role, you must first delete any
resources used by the role.

###### Note

If AWS IoT FleetWise is using the role when you try to delete the resources, then the
deletion might fail. If that happens, wait for a few minutes and try the operation again.
To learn how to delete the service-linked-role through the console, AWS CLI, or AWS
API, see [Using service-linked
roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the _IAM User Guide_.

If you delete this service-linked role, and then need to create it again, you can
register an account with AWS IoT FleetWise. AWS IoT FleetWise then creates the service-linked
role for you again.
