# Amazon EC2 instance topology

Describing your instance topology provides a hierarchical view of the relative proximity
between your Amazon EC2 instances. You can use this information to manage high performance
computing (HPC) and machine learning (ML) compute infrastructure at scale, while optimizing
job placement. HPC and ML jobs are sensitive to latency and throughput. You can use the
instance topology to detect the location of your instances, and then use this information to
optimize HPC and ML jobs by running them on instances that are physically closer to each
other.

You can use instance topology to detect the location of your existing instances, but you
can't use it to choose to launch a new instance physically close to an existing
instance. To influence instance placement, you can [create Capacity Reservations in cluster placement groups](cr-cpg.md "cr-cpg.md").

###### Considerations

- Instance topology views are only available for instances in the
  `running` state.
- Each instance topology view is unique per account.
- The AWS Management Console does not support viewing the instance topology.

###### Pricing

There is no additional cost to describe your instance topology.

###### Contents

- [How it works](how-ec2-instance-topology-works.md "how-ec2-instance-topology-works.md")
- [Prerequisites](ec2-instance-topology-prerequisites.md "ec2-instance-topology-prerequisites.md")
- [Examples](ec2-instance-topology-examples.md "ec2-instance-topology-examples.md")
