# Shared Capacity Reservations

Capacity Reservation sharing enables Capacity Reservation owners to share their reserved capacity with other AWS
accounts or within an AWS organization. This enables you to create and manage Capacity Reservations
centrally, and share the reserved capacity across multiple AWS accounts or within your
AWS organization.

In this model, the AWS account that owns the Capacity Reservation (owner) shares it with other AWS
accounts (consumers). Consumers can launch instances into Capacity Reservations that are shared with
them in the same way that they launch instances into Capacity Reservations that they own in their own
account. The Capacity Reservation owner is responsible for managing the Capacity Reservation and the instances that they
launch into it. Owners cannot modify instances that consumers launch into Capacity Reservations that
they have shared. Consumers are responsible for managing the instances that they launch
into Capacity Reservations shared with them. Consumers cannot view or modify instances owned by other
consumers or by the Capacity Reservation owner.

A Capacity Reservation owner can share a Capacity Reservation with:

- Specific AWS accounts inside or outside of its AWS organization
- An organizational unit inside its AWS organization
- Its entire AWS organization

## Prerequisites for sharing Capacity Reservations

- To share a Capacity Reservation, you must own it in your AWS account. You cannot share a
  Capacity Reservation that has been shared with you.
- You can only share Capacity Reservations for shared tenancy instances. You cannot share
  Capacity Reservations for dedicated tenancy instances.
- Capacity Reservation sharing is not available to new AWS accounts or AWS accounts that
  have a limited billing history.
- To share a Capacity Reservation with your AWS organization or an organizational unit in
  your AWS organization, you must enable sharing with AWS Organizations. For more
  information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS RAM User Guide_.

## Related services

Capacity Reservation sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables
you to share your AWS resources with any AWS account or through AWS Organizations. With
AWS RAM, you share resources that you own by creating a _resource
share_. A resource share specifies the resources to share, and the
consumers with whom to share them. Consumers can be individual AWS accounts, or
organizational units or an entire organization from AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Share across Availability Zones

To ensure that resources are distributed across the Availability Zones for a
Region, we independently map Availability Zones to names for each account. This
could lead to Availability Zone naming differences across accounts. For example, the
Availability Zone `us-east-1a` for your AWS account might not have the
same location as `us-east-1a` for another AWS account.

To identify the location of your Capacity Reservations relative to your accounts, you must use the
_Availability Zone ID_ (AZ ID). The AZ ID is a unique and
consistent identifier for an Availability Zone across all AWS accounts. For
example, `use1-az1` is an AZ ID for the `us-east-1` Region and
it is the same location in every AWS account.

###### To view the AZ IDs for the Availability Zones in your account

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. The AZ IDs for the current Region are displayed in the **Your AZ
   ID** panel on the right-hand side of the screen.

## Shared Capacity Reservation permissions

### Permissions for owners

Owners are responsible for managing and canceling their shared Capacity Reservations. Owners
cannot modify instances running in the shared Capacity Reservation that are owned by other
accounts. Owners remain responsible for managing instances that they launch into
the shared Capacity Reservation.

### Permissions for consumers

Consumers are responsible for managing their instances that are running the
shared Capacity Reservation. Consumers cannot modify the shared Capacity Reservation in any way, and they cannot
view or modify instances that are owned by other consumers or the Capacity Reservation
owner. Consumers can only view the total capacity and available capacity in the
shared reservation.

## Billing and metering

There are no additional charges for sharing Capacity Reservations.

By default, the Capacity Reservation owner is billed for instances that they run inside the Capacity Reservation
and for unused reserved capacity, while consumers are billed for the instances that
they run inside the shared Capacity Reservation. However, you can assign billing of the available
capacity of a shared Capacity Reservation to a specific consumer account. For more information, see
[Billing assignment for shared Amazon EC2 Capacity Reservations](assign-billing.md "assign-billing.md").

If the Capacity Reservation owner belongs to a different payer account and the Capacity Reservation is covered by
a Regional Reserved Instance or a Savings Plan, the Capacity Reservation owner continues to be billed for the
Regional Reserved Instance or Savings Plan. In these cases, the Capacity Reservation owner pays for the Regional
Reserved Instance or Savings Plan, and consumers are billed for the instances that the run in the
shared Capacity Reservation.

## Instance limits

All Capacity Reservation usage counts toward the Capacity Reservation owner's On-Demand Instance limits. This includes:

- Unused reserved capacity
- Usage by instances owned by the Capacity Reservation owner
- Usage by instances owned by consumers

Instances launched into the shared capacity by consumers count towards the Capacity Reservation
owner's On-Demand Instance limit. Consumers' instance limits are a sum of their own On-Demand Instance limits
and the capacity available in the shared Capacity Reservations to which they have access.
