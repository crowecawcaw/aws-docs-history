# Concepts in AWS PCS

A cluster in AWS PCS has 1 or more queues, associated with at least 1 compute node
group. Jobs are submitted to queues and run on EC2 instances defined by compute node groups. You
can use these foundations to implement sophisticated HPC architectures.

###### Cluster

A cluster is a resource for managing resources and running workloads. A cluster is an
AWS PCS resource that defines an assembly of compute, networking, storage, identity, and job
scheduler configuration. You create a cluster by specifying which job scheduler you want to use
(Slurm currently), what scheduler configuration you want, what service controller you want to
manage the cluster, and in which VPC you want the cluster resources to be launched. The
scheduler accepts and schedules jobs, and also launches the compute nodes (EC2 instances) that
process those jobs.

###### Compute node group

A compute node group is a collection of compute nodes that AWS PCS uses to run jobs or
provide interactive access to a cluster. When you define a compute node group, you specify
common traits such as Amazon EC2 instance types, minimum and maximum instance count, target VPC
subnets, Amazon Machine Image (AMI), purchase option, and custom launch configuration.
AWS PCS uses these settings to efficiently launch, manage, and terminate compute nodes in a
compute node group.

###### Queue

When you want to run a job on a specific cluster, you submit it to a particular queue
(also sometimes called a _partition_). The job remains in the queue until
AWS PCS schedules it to run on a compute node group. You associate one or more compute node
groups with each queue. A queue is required to schedule and execute jobs on the underlying
compute node group resources using various scheduling policies offered by the job scheduler.
Users don’t submit jobs directly to a compute node or compute node group.

###### System administrator

A system administrator deploys, maintains, and operates a cluster. They can access
AWS PCS through the AWS Management Console, AWS PCS API, and AWS SDK. They have access to specific
clusters through SSH or AWS Systems Manager, where they can run administrative tasks, run jobs, manage
data, and perform other shell-based activities. For more information, see _[AWS Systems Manager Documentation](../../../systems-manager.md "../../../systems-manager.md")_.

###### End user

An end user doesn't have day-to-day responsibility to deploy or operate a cluster. They
use a terminal interface (such as SSH) to access cluster resources, run jobs, manage data, and
perform other shell-based activities.
