# Behavior of Spot Instance interruptions

When you create a Spot request, you can specify the interruption behavior. The following
are the possible interruption behaviors:

- [Stop](#stop-spot-instances "#stop-spot-instances")
- [Hibernate](#hibernate-spot-instances "#hibernate-spot-instances")
- [Terminate](#terminate-interrupted-spot-instances "#terminate-interrupted-spot-instances")
  The default behavior is that Amazon EC2 terminates Spot Instances when they are interrupted.

## Stop interrupted Spot Instances

You can specify that Amazon EC2 stops your Spot Instances when they are interrupted. The Spot Instance
request type must be `persistent`. You can't specify a launch group
in the Spot Instance request. For EC2 Fleet or Spot Fleet, the request type must be `maintain`.

###### Considerations

- Only Amazon EC2 can restart an interrupted stopped Spot Instance.
- For a Spot Instance launched by a `persistent` Spot Instance request: Amazon EC2 restarts the
  stopped instance when capacity is available in the same Availability
  Zone and for the same instance type as the stopped instance (the same
  launch specification must be used).
- While a Spot Instance is stopped, you can modify some of its instance attributes, but not the
  instance type. If you detach or delete an EBS volume, it is not attached
  when the Spot Instance is started. If you detach the root volume and Amazon EC2
  attempts to start the Spot Instance, the instance will fail to start and Amazon EC2
  will terminate the stopped instance.
- You can terminate a Spot Instance while it is stopped.
- If you cancel a Spot Instance request, an EC2 Fleet, or a Spot Fleet, Amazon EC2 terminates any
  associated Spot Instances that are stopped.
- While an interrupted Spot Instance is stopped, you are charged only for the EBS volumes, which
  are preserved. With EC2 Fleet and Spot Fleet, if you have many stopped instances,
  you can exceed the limit on the number of EBS volumes for your account.
  For more information about how you're charged when a Spot Instance is
  interrupted, see [Billing for interrupted Spot Instances](billing-for-interrupted-spot-instances.md "billing-for-interrupted-spot-instances.md").
- Make sure that you are familiar with the implications of stopping an
  instance. For information about what happens when an instance is
  stopped, see [Differences between instance states](ec2-instance-lifecycle.md#lifecycle-differences "ec2-instance-lifecycle.md#lifecycle-differences").

## Hibernate interrupted Spot Instances

You can specify that Amazon EC2 hibernates your Spot Instances when they are interrupted. For more
information, see [Hibernate your Amazon EC2 instance](Hibernate.md "Hibernate.md").

Amazon EC2 now offers the same hibernation experience for Spot Instances as is currently available for
On-Demand Instances. It offers more extensive support, where the following is now supported for
Spot Instance hibernation:

- [More supported AMIs](hibernating-prerequisites.md#hibernation-prereqs-supported-amis "hibernating-prerequisites.md#hibernation-prereqs-supported-amis")
- [More supported instance families](hibernating-prerequisites.md#hibernation-prereqs-supported-instance-families "hibernating-prerequisites.md#hibernation-prereqs-supported-instance-families")
- [User-initiated hibernation](hibernating-instances.md "hibernating-instances.md")

## Terminate interrupted Spot Instances

When Amazon EC2 interrupts a Spot Instance, it terminates the instance by default, unless you specify a
different interruption behavior, such as stop or hibernate. For more information,
see [Terminate Amazon EC2 instances](terminating-instances.md "terminating-instances.md").
