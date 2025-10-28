# Resolve insufficient instance capacity

errors in Lightsail

You might get an insufficient error when you try to launch an instance or restart a
stopped instance. This means that AWS doesn’t have the available instance capacity to
fulfill your request at the current time. Following is an example of the insufficient
instance capacity error:

_InsufficientInstanceCapacity: There is not enough capacity to fulfill your
instance request. Reduce the number of instances in your request, or wait for additional
capacity to become available. You can also try launching an instance by selecting a
smaller Lightsail plan (which you can resize at a later stage).”_

In this guide, you will learn about the actions you can take if you get an insufficient
instance capacity error.

**Contents**

- [Insufficient
  capacity when launching a new instance](#insufficient-capacity-new-instance "#insufficient-capacity-new-instance")
- [Insufficient
  capacity when starting a stopped instance](#insufficient-capacity-stopped-instance "#insufficient-capacity-stopped-instance")
- [Related
  information](#insufficient-capacity-related-info "#insufficient-capacity-related-info")

## Insufficient capacity when

launching a new instance

Use the following options if you get an insufficient instance capacity error when
launching a new instance. You can complete each option in order, or choose an option
that works for you.

1. Wait a few minutes and then submit your request again. Instance capacity can
   shift frequently. Continue to option 2 if you are unable to create your instance
   after waiting a few minutes.
2. Select a different Availability Zone (AZ) when creating your instance. Each
   AWS Region contains three or more AZs, and each AZ maintains different
   instance capacities. By selecting a different AZ, you can take advantage of its
   current instance capacity. Continue to option 3 if you are unable to create an
   instance in a different AWS Region or AZ.
3. Reduce the number of instances in your request. If you’re creating multiple
   instances at the same time, reduce the number of instances and submit your
   request again. Continue to option 4 if reducing the number of instances doesn’t
   resolve the issue.
4. Choose a different instance plan when creating your instance. Choose a
   different instance plan if you are unable to create an instance in a different
   AZ or Region. You can resize the instance at a later stage. For more information
   about resizing your instance, see [Create an instance
   from a snapshot](lightsail-how-to-create-instance-from-snapshot.md "lightsail-how-to-create-instance-from-snapshot.md").

## Insufficient capacity when

starting a stopped instance

Use the following options if you get an insufficient instance capacity error when
starting an existing instance that was previously stopped.

1. Wait a few minutes and then submit your request again. Instance capacity can
   shift frequently. Continue to option 2 if you are unable to create your instance
   after waiting a few minutes.
2. Create a new instance from a snapshot. Take a snapshot of the stopped
   instance. Then, use the snapshot to create a new instance in an AZ that’s
   different from the original instance. For example, if your instance is currently
   in us-east-2a (Zone A), select us-east-2c (Zone C) when you create the new
   instance. For more information, see [Create an instance
   from a snapshot](lightsail-how-to-create-instance-from-snapshot.md "lightsail-how-to-create-instance-from-snapshot.md").
3. You can also choose a different instance plan when creating a new instance
   from a snapshot. This action is optional.

###### Important

After the new instance is running, verify you have access to the new instance and
everything is working properly. For example, if your instance was running an
application, make sure that the application is working as expected. If so, you can
delete the earlier instance.

## Related information

[Frequently asked
questions](amazon-lightsail-faq-instances.md "amazon-lightsail-faq-instances.md")

[Resilience in Lightsail](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
