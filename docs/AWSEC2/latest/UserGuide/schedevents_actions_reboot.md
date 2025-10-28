# Manage Amazon EC2 instances scheduled for

reboot

When AWS must perform tasks such as installing updates or maintaining the
underlying host, it can schedule an instance reboot. During the scheduled reboot,
the instance either stays on the same host, or migrates to a different host,
depending on the event, as follows:

- `instance-reboot` event
  - During the reboot, the instance remains on the host. This is known
    as an _in-place reboot_.
  - The current host undergoes maintenance.
  - Typically completes in seconds.

- `system-reboot` event

      + During the reboot, the instance is migrated to a new host. This is
       known as a *reboot
       migration*.
      + Typically completes in minutes.

  To check what type of event is scheduled for your instance, see [Determine the event type](monitoring-instances-status-check_sched.md#scheduled-event-type "monitoring-instances-status-check_sched.md#scheduled-event-type").

## Actions you

can take

When you receive a scheduled `instance-reboot` or
`system-reboot` event notification, you can take one of the
following actions:

- **Wait for scheduled reboot:** You can
  wait for the instance reboot to occur within its scheduled maintenance
  window.
- **Reschedule the reboot:** You can [reschedule](reschedule-event.md "reschedule-event.md") the instance reboot to
  a date and time that suits you.
- **Perform a user-initiated reboot:** You
  can manually [reboot](ec2-instance-reboot.md "ec2-instance-reboot.md") the
  instance yourself at a time that suits you. However, the outcome depends
  on the event:
  - `instance-reboot` event – Your instance
    remains on the current hardware (in-place reboot), no host
    maintenance takes place, and the event stays open.
  - `system-reboot` event
    - If reboot migration is enabled on your instance, a
      user-initiated reboot attempts to migrate your instance
      to new hardware. If successful, the event is cleared. If
      unsuccessful, an in-place reboot occurs and the event
      remains scheduled.
    - If reboot migration is disabled on your instance, a
      user-initiated reboot keeps the instance on the same
      hardware (in-place reboot), no host maintenance takes
      place, and the event remains scheduled. When the
      scheduled event eventually takes place, AWS will move
      your instance to new hardware (reboot migration).

**After AWS reboots your instance**

The following applies after AWS reboots your instance:

- The scheduled event is cleared.
- The event description is updated.
- For an `instance-reboot` event:
  - Maintenance of the underlying host is complete.

- For a `system-reboot` event:
  - The instance moves to a new host.
  - The instance retains its IP address and DNS name.
  - Any data on local instance store volumes is preserved.

- You can use your instance after it has fully booted.

**Alternative options**

If you can't reschedule the reboot event or enable reboot migration for a
user-initiated reboot, but want to maintain normal operation during the
scheduled maintenance window, you can do the following:

- **For an instance with an EBS root
  volume**
  - Manually stop and start the instance to migrate it to a new host.
    This is not the same as manually rebooting the instance, where the
    instance stays on the same host.
  - Optionally, automate an immediate instance stop and start in
    response to the scheduled reboot event. For more information, see
    [Running operations on EC2 instances automatically in response
    to events in AWS Health](../../../health/latest/ug/automating-instance-actions.md "../../../health/latest/ug/automating-instance-actions.md") in the _AWS Health User Guide_.

###### Important

The data on instance store volumes is lost when an instance is
stopped. For more information, see [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md").

- **For an instance with an instance store root
  volume**
  1.  Launch a replacement instance from your most recent AMI.
  2.  Migrate all necessary data to the replacement instance before the
      scheduled maintenance window.
  3.  Terminate the original instance.

## Enable or disable reboot migration

When an instance is scheduled for a `system-reboot` event, you can
reboot it before the event. The outcome of a user-initiated reboot depends on
the instance's reboot migration setting:

- Enabled – A user-initiated reboot attempts to migrate your
  instance to new hardware (reboot migration). If successful, the event is
  cleared. If unsuccessful, an in-place reboot occurs and the event
  remains scheduled. Note that even when enabled, reboot migration can
  only occur if your instance meets the [reboot migration
  requirements](#requirements-for-reboot-migration "#requirements-for-reboot-migration").
- Disabled – A user-initiated reboot keeps the instance on the
  same hardware (in-place reboot), no host maintenance takes place, and
  the event remains scheduled. When the scheduled event eventually takes
  place, AWS will move your instance to new hardware (reboot
  migration).

A reboot with migration takes longer than an in-place reboot:

- In-place reboot: Approximately 30 seconds
- Reboot with migration: Several minutes

###### Note

Instances that receive a `system-reboot` event notification are
enabled for user-initiated reboot migration by default.

### Requirements for enabling

reboot migration

Reboot migration can be enabled on instances that meet the following
criteria:

**Instance types**

Not all instance types support enabling reboot migration. You
can view the instance types that support enabling reboot
migration.

Console

###### To view the instance types that support enabling

reboot migration

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Instance
   Types**.
3. In the filter bar, enter **Reboot
   Migration support: supported**. As you
   enter the characters and the filter name appears,
   you can select it.

The **Instance types** table
displays all the instance types that support
enabling reboot migration.

AWS CLI

###### To view the instance types that support enabling

reboot migration

Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command with the
`reboot-migration-support`
filter.

```
aws ec2 describe-instance-types \
    --filters Name=reboot-migration-support,Values=supported \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

PowerShell

###### To view the instance types that support enabling

reboot migration

Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md")
cmdlet with the `reboot-migration-support` filter.

```
Get-EC2InstanceType `
    -Filter @{Name="reboot-migration-support";Values="true"} | `
    Select InstanceType | Sort-Object InstanceType
```

**Tenancy**

- Shared
- Dedicated Instance

For more information, see [Amazon EC2 Dedicated Instances](dedicated-instance.md "dedicated-instance.md").

**Limitations**

Reboot migration is **not** supported for instances
with the following characteristics:

- Platform: Instances running natively on the Xen hypervisor
- Instance size: `metal` instances
- Tenancy: Dedicated Host. For Dedicated Hosts, use [Dedicated Host Auto Recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md")
  instead.
- Storage: Instances with instance store volumes
- Networking: Instances using an Elastic Fabric Adapter
- Auto Scaling: Instances that are part of an Auto Scaling group

### Steps for enabling or

disabling reboot migration

When an instance receives a `system-reboot` event, it is enabled
for reboot migration by default. You can disable reboot migration so that
during a user-initiated reboot, the instance stays on the same hardware
(in-place reboot).

The `default` configuration doesn't enable reboot migration for an
unsupported instance. For more information, see [Requirements for enabling
reboot migration](#requirements-for-reboot-migration "#requirements-for-reboot-migration").

You can disable or enable reboot migration on a running or stopped
instance.

AWS CLI

###### To disable reboot migration

Use the [modify-instance-maintenance-options](../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md "../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md") command and
set the `--reboot-migration` parameter to
`disabled`.

```
aws ec2 modify-instance-maintenance-options \

    --instance-id `i-0abcdef1234567890` \

    --reboot-migration disabled
```

###### To enable reboot migration

Use the [modify-instance-maintenance-options](../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md "../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md") command and
set the `--reboot-migration` parameter to
`default`.

```
aws ec2 modify-instance-maintenance-options \

    --instance-id `i-0abcdef1234567890` \

    --reboot-migration default
```

PowerShell

###### To disable reboot migration

Use the [Edit-EC2InstanceMaintenanceOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md")
cmdlet.

```
Edit-EC2InstanceMaintenanceOption `
    -InstanceId  `
    -RebootMigration Disabled
```

###### To enable reboot migration

Use the [Edit-EC2InstanceMaintenanceOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md") cmdlet.

```
Edit-EC2InstanceMaintenanceOption `
    -InstanceId `i-1234567890abcdef0` `
    -RebootMigration Enabled
```
