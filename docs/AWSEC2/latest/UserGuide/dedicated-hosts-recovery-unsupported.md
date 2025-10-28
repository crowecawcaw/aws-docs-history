# Manually recover instances that are not supported by Amazon EC2 Dedicated Host recovery

Host recovery does not support recovering instances that use instance store
volumes. Follow the instructions below to manually recover any of your instances
that could not be automatically recovered.

###### Warning

Data on instance store volumes is lost when an instance is stopped, hibernated, or
terminated. This includes instance store volumes that are attached to an
instance that has an EBS root volume. To protect data from instance store
volumes, back it up to persistent storage before the instance is stopped or
terminated.

## Manually recover EBS-backed

instances

For EBS-backed instances that could not be automatically recovered, we
recommend that you manually stop and start the instances to recover them onto a
new Dedicated Host. For more information about stopping your instance, and about the
changes that occur in your instance configuration when it's stopped, see [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md").

## Manually recover instances with

instance store root volumes

For instances with instance store root volumes that could not be automatically recovered,
we recommend that you do the following:

1. Launch a replacement instance on a new Dedicated Host from your most recent
   AMI.
2. Migrate all of the necessary data to the replacement instance.
3. Terminate the original instance on the impaired Dedicated Host.
