# Manage Amazon EC2 instances scheduled

for maintenance

When AWS must maintain the underlying host for an instance, it schedules the
instance for maintenance. There are two types of maintenance events: network
maintenance and power maintenance.

- During network maintenance, scheduled instances lose network connectivity
  for a brief period of time. Normal network connectivity to your instance is
  restored after maintenance is complete.
- During power maintenance, scheduled instances are taken offline for a
  brief period, and then rebooted. When a reboot is performed, all of your
  instance's configuration settings are retained.
  After your instance has rebooted (this normally takes a few minutes), verify that
  your application is working as expected. At this point, your instance should no
  longer have a scheduled event associated with it, or if it does, the description of
  the scheduled event begins with **[Completed]**. It sometimes takes
  up to 1 hour for the instance status description to refresh. Completed maintenance
  events are displayed on the Amazon EC2 console dashboard for up to a week.

## Actions

you can take

###### Actions you can take for instances with an EBS root volume

When you receive a `system-maintenance` event notification, you
can take one of the following actions:

- **Wait for scheduled maintenance:** You
  can wait for the maintenance to occur as scheduled.
- **Perform manual stop and stop:** You can
  stop and start the instance, which migrates it to a new host. This is
  not the same as rebooting the instance. For more information, see [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md").
- **Automate stop and start:** You can
  automate an immediate stop and start in response to a scheduled
  maintenance event. For more information, see [Running
  operations on EC2 instances automatically in response to events in
  AWS Health](../../../health/latest/ug/automating-instance-actions.md "../../../health/latest/ug/automating-instance-actions.md") in the _AWS Health User Guide_.

###### Actions you can take for instances with an instance store root

volume

When you receive a `system-maintenance` event notification, you
can take one of the following actions:

- **Wait for scheduled maintenance:** You
  can wait for the maintenance to occur as scheduled.
- **Launch a replacement instance:** If you
  want to maintain normal operation during the scheduled maintenance
  window:
  1.  Launch a replacement instance from your most recent
      AMI.
  2.  Migrate all necessary data to the replacement instance before
      the scheduled maintenance window.
  3.  Terminate the original instance.
