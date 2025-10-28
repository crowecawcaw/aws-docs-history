# AWS PCS queues

An AWS PCS queue is a lightweight abstraction over the scheduler’s native implementation
of a work queue. In the case of Slurm, an AWS PCS queue is equivalent to a Slurm partition.

Users submit jobs to a queue where they reside until they can be scheduled to run on nodes
provided by one or more compute node groups. An AWS PCS cluster can have multiple job queues.
For example, you can create a queue that uses Amazon EC2 On-demand Instances for high priority jobs and
another queue that uses Amazon EC2 Spot Instances for low-priority jobs.

###### Topics

- [Creating a queue in AWS PCS](working-with_queues_create.md "working-with_queues_create.md")
- [Updating an AWS PCS queue](working-with_queues_update.md "working-with_queues_update.md")
- [Deleting a queue in AWS PCS](working-with_queues_delete.md "working-with_queues_delete.md")
