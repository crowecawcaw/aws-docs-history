# On-Demand Capacity Reservations and Capacity Blocks for ML

Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone.
There are two types of Capacity Reservations serving different use cases.

###### Types of Capacity Reservations

- [On-Demand Capacity Reservations](ec2-capacity-reservations.md "ec2-capacity-reservations.md")
- [Capacity Blocks for ML](ec2-capacity-blocks.md "ec2-capacity-blocks.md")
  The following are some common use cases for On-Demand Capacity Reservations:

- **Scaling events** – Create On-Demand Capacity Reservations ahead of
  your business-critical events to ensure that you can scale when you need to.
- **Regulatory requirements and disaster recovery** –
  Use On-Demand Capacity Reservations to satisfy regulatory requirements for high availability, and reserve
  capacity in a different Availability Zone or Region for disaster recovery.
  The following are some common use cases for Capacity Blocks for ML:

- **Machine learning (ML) model training and fine-tuning**
  – Get uninterrupted access to the GPU instances that you reserved to complete ML
  model training and fine-tuning.
- **ML experiments and prototypes** – Run experiments
  and build prototypes that require GPU instances for short durations.

###### When to use On-Demand Capacity Reservation

Use On-Demand Capacity Reservations if you have strict capacity requirements, and your current or future
business-critical workloads require capacity assurance. With On-Demand Capacity Reservations, you can ensure that
you'll always have access to the Amazon EC2 capacity you've reserved for as long as you need it.

###### When to use Capacity Blocks for ML

Use Capacity Blocks for ML when you need to ensure that you have uninterrupted access to GPU instances for
a defined period of time starting on a future date. Capacity Blocks are ideal for training and
fine-tuning ML models, short experimentation runs, and handling temporary surges in inference
demand in the future. With Capacity Blocks, you can ensure that you'll have access to GPU resources
on a specific date to run your ML workloads.
