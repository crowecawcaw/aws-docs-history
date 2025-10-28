# Manage Amazon EC2 instances scheduled to

stop or retire

When AWS detects irreparable failure of the underlying host for your instance,
it schedules the instance to either stop or terminate, depending on the instance's
root volume type.

- If the instance has an Amazon EBS root volume, the instance is scheduled to
  stop.
- If the instance has an instance store root volume, the instance is
  scheduled to terminate.
  For more information, see [Instance retirement](instance-retirement.md "instance-retirement.md").

###### Important

Any data stored on instance store volumes is lost when an instance is stopped,
hibernated, or terminated. This includes instance store volumes that are
attached to an instance that has an EBS root volume. Be sure to save data from
your instance store volumes that you might need later before the instance is
stopped, hibernated, or terminated.

## Actions you can take

###### Actions you can take for instances with an EBS root volume

When you receive a scheduled `instance-stop` event
notification, you can take one of the following actions:

- **Wait for scheduled stop:** You can wait
  for the instance to stop within its scheduled maintenance window.
- **Perform manual stop and start:** You
  can stop and start the instance yourself at a time that suits you, which
  migrates it to a new host. This is not the same as rebooting the
  instance. For more information, see [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md").
- **Automate stop and start:** You can
  automate an immediate stop and start in response to a scheduled
  `instance-stop` event. For more information, see [Running
  operations on EC2 instances automatically in response to events in
  AWS Health](../../../health/latest/ug/automating-instance-actions.md "../../../health/latest/ug/automating-instance-actions.md") in the
  _AWS Health User Guide_.

###### Actions you can take for instances with an instance store root

volume

When you receive a scheduled `system-retirement` event
notification, and you want to retain your data, you can take the following
actions:

1. Launch a replacement instance from your most recent AMI.
2. Migrate all necessary data to the replacement instance before the
   instance is scheduled to terminate.
3. Terminate the original instance, or wait for it to terminate as
   scheduled.

For more information about the actions you can take, see [Instance retirement](instance-retirement.md "instance-retirement.md").
