# Capacity Reservations in AWS PCS

You can reserve Amazon EC2 capacity in a specific Availability Zone and for a specific
duration using On-Demand Capacity Reservations or Amazon EC2 Capacity Blocks for ML to make sure
that you have the necessary compute capacity available when you need it.

**On-Demand Capacity Reservations (ODCRs)** let you reserve compute capacity
for your Amazon EC2 instances in a specific Availability Zone for any duration. You can create and cancel
reservations at any time, with no long-term commitments or upfront payments. ODCRs are ideal when you
need flexible capacity reservations that you can modify as your requirements change. For more information,
see [On-Demand
Capacity Reservations](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") in the _Amazon Elastic Compute Cloud User Guide_.

**Amazon EC2 Capacity Blocks for ML** allow you to reserve GPU-based accelerated computing instances on a future date to support your machine learning (ML) workloads. For more information, see
[Capacity Blocks for ML](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md")
in the _Amazon Elastic Compute Cloud User Guide_.

###### Topics

- [Using ODCRs with AWS PCS](capacity-reservations-odcr.md "capacity-reservations-odcr.md")
- [Using I-ODCRs with AWS PCS](capacity-reservations-iodcr.md "capacity-reservations-iodcr.md")
- [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md "capacity-blocks.md")
