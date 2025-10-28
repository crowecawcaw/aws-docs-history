# Amazon EC2 instance type changes

As your needs change, you might find that your instance is over-utilized (the instance type
is too small) or under-utilized (the instance type is too large). If this is the case, you can
resize your instance by changing its instance type. For example, if your `t2.micro`
instance is too small for its workload, you can increase its size by changing it to a bigger T2
instance type, such as `t2.large`. Or you can change it to another instance type,
such as `m5.large`. You might also want to change from a previous generation to a
current generation instance type to take advantage of some features, such as support for
IPv6.

If you want a recommendation for an instance type that is best able to handle your existing
workload, you can use AWS Compute Optimizer. For more information, see [Get EC2 instance recommendations from Compute Optimizer](ec2-instance-recommendations.md "ec2-instance-recommendations.md").

When you change the instance type, you'll start paying the rate of the new instance type.
For the on-demand rates of all instance types, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

To add additional storage to your instance without changing the instance type, add an
EBS volume to the instance. For more information, see [Attach an Amazon EBS volume to an instance](../../../ebs/latest/userguide/ebs-attaching-volume.md "../../../ebs/latest/userguide/ebs-attaching-volume.md")
in the _Amazon EBS User Guide_.

## Which instructions to follow?

There are different instructions for changing the instance type. The instructions to use
depend on the instance's root volume, and whether the instance type is compatible with the
instance's current configuration. For information about how compatibility is determined, see
[Compatibility for changing the instance type](resize-limitations.md "resize-limitations.md").

Use the following table to determine which instructions to follow.

| Root volume    | Compatibility  | Use these instructions                                                                                                      |
| -------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| EBS            | Compatible     | [Change the instance type](change-instance-type-of-ebs-backed-instance.md "change-instance-type-of-ebs-backed-instance.md") |
| EBS            | Not compatible | [Migrate to a new instance type](migrate-instance-configuration.md "migrate-instance-configuration.md")                     |
| Instance store | Not applicable | [Migrate to a new instance type](migrate-instance-configuration.md "migrate-instance-configuration.md")                     |
