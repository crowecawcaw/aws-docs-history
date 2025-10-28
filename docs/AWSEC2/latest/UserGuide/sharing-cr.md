# Share a Capacity Reservation

When you share a Capacity Reservation that you own with other AWS accounts, you enable them to
launch instances into your reserved capacity. If you share an open Capacity Reservation, keep the
following in mind as it could lead to unintended Capacity Reservation usage:

- If consumers have running instances that match the attributes of the Capacity Reservation,
  have the `CapacityReservationPreference` parameter set to
  `open`, and are not yet running in reserved capacity, they
  automatically use the shared Capacity Reservation.
- If consumers launch instances that have matching attributes (instance
  type, platform, Availability Zone, and tenancy) and have the
  `CapacityReservationPreference` parameter set to
  `open`, they automatically launch into the shared
  Capacity Reservation.
  To share a Capacity Reservation, you must add it to a resource share. A resource share is an AWS RAM
  resource that lets you share your resources across AWS accounts. A resource share
  specifies the resources to share, and the consumers with whom they are shared. When
  you share a Capacity Reservation using the Amazon EC2 console, you add it to an existing resource share.
  To add the Capacity Reservation to a new resource share, you must create the resource share using
  the [AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, consumers in your organization are granted access to the shared Capacity Reservation if the
[prerequisites for sharing](capacity-reservation-sharing.md#sharing-cr-prereq "capacity-reservation-sharing.md#sharing-cr-prereq") are met. If
the Capacity Reservation is shared with external accounts, they receive an invitation to join the
resource share and are granted access to the shared Capacity Reservation after accepting the
invitation.

###### Important

Before launching instances into a Capacity Reservation that is shared with you, verify that
you have access to the shared Capacity Reservation by viewing it in the console or by describing
it using the [describe-capacity-reservations](../../../cli/latest/reference/ec2/describe-capacity-reservations.md "../../../cli/latest/reference/ec2/describe-capacity-reservations.md") AWS CLI command. If you can view the
shared Capacity Reservation in the console or describe it using the AWS CLI, it is available for
your use and you can launch instances into it. If you attempt to launch
instances into the Capacity Reservation and it is not accessible due to a sharing failure, the
instances will launch into On-Demand capacity.

Console

###### To share a Capacity Reservation that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Capacity Reservations**.
3. Choose the Capacity Reservation to share and choose
   **Actions**, **Share
   reservation**.
4. Select the resource share to which to add the Capacity Reservation and choose
   **Share Capacity Reservation**.

It could take a few minutes for consumers to get access to the
shared Capacity Reservation.

###### To share a Capacity Reservation that you own using the AWS RAM console

See [Creating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the _AWS RAM User Guide_.

AWS CLI

###### To share a Capacity Reservation that you own

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

```
aws ram create-resource-share \
    --name `my-resource-share` \
    --resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`
```

PowerShell

###### To share a Capacity Reservation that you own

Use the [New-RAMResourceShare](../../../powershell/latest/reference/items/New-RAMResourceShare.md "../../../powershell/latest/reference/items/New-RAMResourceShare.md") cmdlet.

```
New-RAMResourceShare `
    -Name `my-resource-share` `
    -ResourceArn "arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`"
```
