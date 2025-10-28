# Amazon EventBridge rule service-linked role for AMS Advanced

AMS Advanced uses the service-linked role (SLR) named **AWSServiceRoleForManagedServices_Events** – This role trusts one
of the AWS Managed Services service principals
(events.managedservices.amazonaws.com) to assume the role for you. The service
uses the role to create EventBridge managed rule. This rule is the infrastructure
required in your AWS account to deliver alarm state change information from
your account to AWS Managed Services.

## Permissions for EventBridge SLR for AMS Advanced

The **AWSServiceRoleForManagedServices_Events** service-linked role
trusts the following services to assume the role:

- events.managedservices.amazonaws.com

Attached to this role is the **AWSManagedServices_EventsServiceRolePolicy** AWS managed
policy (see [AWS managed policy:
AWSManagedServices_EventsServiceRolePolicy](../accelerate-guide/security-iam-awsmanpol.md#EventsServiceRolePolicy "../accelerate-guide/security-iam-awsmanpol.md#EventsServiceRolePolicy")). The service uses the
role to deliver alarm state change information from your account to AWS
Managed Services. You must configure permissions to allow an IAM entity
(such as a user, group, or role) to create, edit, or delete a service-linked
role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _AWS Identity and Access Management_ User Guide.

You can download the JSON **AWSManagedServices_EventsServiceRolePolicy** in this ZIP:
[EventsServiceRolePolicy.zip](../accelerate-guide/samples/EventsServiceRolePolicy.md "../accelerate-guide/samples/EventsServiceRolePolicy.md").

## Creating an EventBridge SLR for AMS Advanced

You don't need to manually create a service-linked role. When you Onboard
to AMS in the AWS Management Console, the AWS CLI, or the AWS API, then
AMS Advanced creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you were using
the AMS Advanced service before February 7, 2023, when it began supporting
service-linked roles then AMS Accelerate created the
AWSServiceRoleForManagedServices_Events role in your account. To learn
more, see [A new role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again,
you can use the same process to recreate the role in your account. When you
Onboard to AMS, AMS Advanced creates the service-linked role for you again.

## Editing an EventBridge SLR for AMS Advanced

AMS Advanced does not allow you to edit the
AWSServiceRoleForManagedServices_Events service-linked role. After you
create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting an EventBridge SLR for AMS Advanced

You don't need to manually delete the
AWSServiceRoleForManagedServices_Events role. When you Offboard from AMS
in the AWS Management Console, the AWS CLI or the AWS API, AMS Advanced cleans
up the resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the service-linked role. To do this, you must first manually clean
up the resources for your service-linked role and then you can manually delete it.

###### Note

If the AMS Advanced service is using the role when you try to delete the resources, then the
deletion might fail. If that happens, wait for a few minutes and try the
operation again.

**To delete AMS Advanced resources **used
by the AWSServiceRoleForManagedServices_Events service-linked
role\*\*\*\*

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
AWSServiceRoleForManagedServices_Events service-linked role.

For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
