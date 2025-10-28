# Using service-linked roles for

Capacity Reservation Fleet

On-Demand Capacity Reservation Fleet uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts"). A service-linked role is a unique type of IAM
role that is linked directly to Capacity Reservation Fleet. Service-linked roles are predefined
by Capacity Reservation Fleet and include all the permissions that the service requires to call
other AWS services on your behalf.

A service-linked role makes setting up Capacity Reservation Fleet easier because you don’t have
to manually add the necessary permissions. Capacity Reservation Fleet defines the permissions of
its service-linked roles, and unless defined otherwise, only Capacity Reservation Fleet can
assume its roles. The defined permissions include the trust policy and the
permissions policy, and that permissions policy cannot be attached to any other
IAM entity.

You can delete a service-linked role only after first deleting their related
resources. This protects your Capacity Reservation Fleet resources because you can't
inadvertently remove permission to access the resources.

## Service-linked role permissions for

Capacity Reservation Fleet

Capacity Reservation Fleet uses the service-linked role named
**AWSServiceRoleForEC2CapacityReservationFleet** to create, describe, modify, and cancel Capacity Reservations in a Capacity Reservation Fleet on your behalf.

The AWSServiceRoleForEC2CapacityReservationFleet service-linked role trusts the following entity to assume the
role:

- `capacity-reservation-fleet.amazonaws.com`

The role uses the `AWSEC2CapacityReservationFleetRolePolicy` AWS
managed policy. For more information, see [AWS managed policy: AWSEC2CapacityReservationFleetRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSEC2CapacityReservationFleetRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSEC2CapacityReservationFleetRolePolicy").

You must configure permissions to allow an IAM entity (such as a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Create a service-linked role for

Capacity Reservation Fleet

You don't need to manually create a service-linked role. When you
create a Capacity Reservation Fleet using the
`create-capacity-reservation-fleet` AWS CLI command or the
`CreateCapacityReservationFleet` API, the service-linked role is
automatically created for you.

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account. When you
create a Capacity Reservation Fleet, Capacity Reservation Fleet creates the service-linked role for you
again.

## Edit a service-linked role for Capacity Reservation Fleet

Capacity Reservation Fleet does not allow you to edit the AWSServiceRoleForEC2CapacityReservationFleet service-linked role.
After you create a service-linked role, you cannot change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the
_IAM User Guide_.

## Delete a service-linked role for

Capacity Reservation Fleet

If you no longer need to use a feature or service that requires a
service-linked role, we recommend that you delete that role. That way you don’t
have an unused entity that is not actively monitored or maintained. However, you
must delete the resources for your service-linked role before you can manually
delete it.

###### Note

If the Capacity Reservation Fleet service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few
minutes and try the operation again.

###### To delete the AWSServiceRoleForEC2CapacityReservationFleet service-linked role

1. Use the `delete-capacity-reservation-fleet` AWS CLI command
   or the `DeleteCapacityReservationFleet` API to delete the
   Capacity Reservation Fleets in your account.
2. Use the IAM console, the AWS CLI, or the AWS API to delete the
   AWSServiceRoleForEC2CapacityReservationFleet service-linked role. For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
   _IAM User Guide_.

## Supported Regions for Capacity Reservation Fleet service-linked

roles

Capacity Reservation Fleet supports using service-linked roles in all of the Regions where
the service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/ec2-service.md#ec2_region "../../../general/latest/gr/ec2-service.md#ec2_region").
