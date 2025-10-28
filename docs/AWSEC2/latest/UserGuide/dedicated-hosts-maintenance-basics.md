# How host maintenance works for Amazon EC2 Dedicated Hosts

When a degradation is detected on a Dedicated Host that is enabled for host maintenance,
we automatically allocate a replacement Dedicated Host in your account. The replacement Dedicated Host
receives a new host ID, but retains the same attributes as the original Dedicated Host,
including:

- Auto placement settings
- Availability Zone
- Dedicated Host Reservation association
- Host affinity
- Host maintenance settings
- Host recovery settings
- Instance type
- Tags
  After the replacement host has been allocated, we migrate the instances using either
  **live migration host maintenance** or
  **reboot-based host maintenance**, depending on the instance.

After the degraded host has no more running instances, it is permanently released from
your account.

## Live migration host maintenance

Instances that require live migration host maintenance are automatically migrated to the
replacement host within 24 hours, without stopping and restarting them. The migrated
instances retain their existing attributes, including:

- Instance ID
- Instance metadata
- Amazon EBS volume attachments
- Elastic IP addresses and private IP address
- Memory, CPU, and networking states

Some larger instance sizes might experience a slight performance decrease during the
migration.

After the instances are automatically migrated to the replacement host, we
send you email and AWS Health Dashboard notifications. Notifications include the IDs of the
degraded and replacement hosts, information about the instances that were automatically
migrated using live migration host maintenance, and information about the remaining
instances.

## Reboot-based host maintenance

Instances that require reboot-based host maintenance are scheduled for instance
reboot scheduled events for 14 days from the date of the notification. You can continue
to access your instances on the degraded Dedicated Host before the scheduled event.

You can reschedule reboot events for a date that is within 7 days of the original
event date and time. For more information, see [Reschedule a scheduled event for an EC2 instance](reschedule-event.md "reschedule-event.md").

Amazon EC2 automatically reserves capacity on the replacement host for these instances.
You can't run instances in this reserved capacity.

The Amazon EC2 console shows the reserved capacity as used capacity. It could appear
that the instances are running on both the degraded host and the replacement host.
However, the instances will continue to run only on the degraded host until they
are stopped or they are migrated into the reserved capacity on the replacement
host.

At the date and time of the scheduled event, the instances are automatically stopped
and restarted into the reserved capacity on the replacement host. The migrated instances
retain their existing attributes, including:

- Instance ID
- Instance metadata
- Amazon EBS volume attachments
- Elastic IP addresses and private IP address

However, since the instances are stopped and restarted during the migration, they do
not retain their memory, CPU, and networking states.

You can also manually stop and restart these instances at any time before the scheduled
event to migrate them to the replacement host or to a different host. You might need to
modify your instance's host affinity to restart it on a different host. If you stop an
instance before the scheduled event, the reserved capacity on the replacement host is
released and becomes available for use.

## Host maintenance states

When a host becomes degraded, it enters the `permanent-failure` state.
You can't launch instances on a Dedicated Host that is in the `permanent-failure`
state.

After the replacement host is allocated, it remains in the `pending`
state until the instances that support live migration host maintenance are
automatically migrated from the degraded host, and until the scheduled events
are scheduled for the remaining instances. After these tasks are completed, the
replacement host enters the `available` state.

After the replacement host enters the `available` state, you can use it
in the same way that you use any host in your account. However, some instance capacity
on the replacement host is reserved for the instances that require reboot-based
host migration. You can't launch new instances into this reserved capacity.

When the degraded host has no more running instances, it enters the `released,
 permanent-failure` state, and it is permanently released from your account.
Note that the host and its resources remain visible in the console for a short time.

## Automatic migration

Some instances can't be automatically migrated to the replacement host.

###### Instances with EBS-backed root volumes

For these instances, we schedule instance stop events for 28 days from the date of the
notification. At the date and time of the scheduled event, the instances are stopped. We
recommend that you manually stop on restart the instance on the replacement host or on a
different host. You might need to modify your instance's host affinity to restart it on
a different host.

###### Instances with an instance store root volume

For these instances, we schedule instance retirement events for 28 days from the date
of the notification. At the date and time of the scheduled event, the instances are
permanently terminated. We recommend that you manually launch replacement instances on
the replacement host and then migrate the required data to the replacement instances
before the scheduled event.

The following instances have instance store root volumes:
C1, C3, D2, I2, M1, M2, M3, R3, and X1.

You can continue to access your instances on the degraded Dedicated Host before the scheduled
event.
