# Amazon EC2 topology

Amazon EC2 topology provides a hierarchical view of the relative proximity of your compute
capacity. You can then use this information to manage high performance computing (HPC),
machine learning (ML), and generative AI compute infrastructure at scale.

###### Available APIs

Amazon EC2 provides two APIs for understanding your EC2 topology:

- [DescribeInstanceTopology](../APIReference/API_DescribeInstanceTopology.md "../APIReference/API_DescribeInstanceTopology.md")
  - Shows where your _running_ instances are
    located relative to each other in the network hierarchy.
  - Helps optimize where to run your workloads on your existing
    instances.

- [DescribeCapacityReservationTopology](../APIReference/API_DescribeCapacityReservationTopology.md "../APIReference/API_DescribeCapacityReservationTopology.md")
  - Shows where your reserved capacity will be located relative to each other
    in the network hierarchy _before you launch
    instances_.
  - Helps with capacity planning by letting you know the placement of reserved
    capacity before launching instances.

###### Key benefits

EC2 topology provides the following key benefits:

- Capacity management – Optimize resource utilization.
- Job scheduling – Make informed decisions about workload placement.
- Node ranking – Understand relative proximity for performance optimization
  on tightly coupled instances.

###### Considerations

- Topology views are only available for:
  - Instances in the `running` state
  - Capacity Reservations in the `pending` or `active` state

- Each topology view is unique per AWS account.
- The AWS Management Console does not support viewing topology.
- While topology information helps you understand instance placement, you can't use
  it to launch a new instance physically close to an existing instance. To influence instance placement, you can [create Capacity Reservations in cluster placement
  groups](cr-cpg.md "cr-cpg.md").

###### Pricing

There is no additional cost for describing your EC2 topology.

###### Contents

- [How it works](how-ec2-instance-topology-works.md "how-ec2-instance-topology-works.md")
- [Prerequisites](ec2-instance-topology-prerequisites.md "ec2-instance-topology-prerequisites.md")
- [Examples](ec2-instance-topology-examples.md "ec2-instance-topology-examples.md")
