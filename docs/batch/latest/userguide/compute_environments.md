# Compute environments for AWS Batch

Job queues are mapped to one or more compute environments. Compute environments contain the Amazon ECS container
instances that are used to run containerized batch jobs. A specific compute environment can also be mapped to one or
more than one job queue. Within a job queue, the associated compute environments each have an order that's used by the
scheduler to determine where jobs that are ready to be run will run. If the first compute environment has a status of
`VALID` and has available resources, the job is scheduled to a container instance within that compute
environment. If the first compute environment has a status of `INVALID` or can't provide a suitable compute
resource, the scheduler attempts to run the job on the next compute environment.

###### Topics

- [Managed compute environments](managed_compute_environments.md "managed_compute_environments.md")
- [Unmanaged compute environments](unmanaged_compute_environments.md "unmanaged_compute_environments.md")
- [Create a compute environment](create-compute-environment.md "create-compute-environment.md")
- [Update a compute environment in
  AWS Batch](updating-compute-environments.md "updating-compute-environments.md")
- [Compute resource AMIs](compute_resource_AMIs.md "compute_resource_AMIs.md")
- [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md "launch-templates.md")
- [Instance Metadata Service (IMDS) configuration](imds-compute-environments.md "imds-compute-environments.md")
- [EC2 configurations](ec2-configurations.md "ec2-configurations.md")
- [Instance type allocation strategies for AWS Batch](allocation-strategies.md "allocation-strategies.md")
- [Compute resource memory management](memory-management.md "memory-management.md")
- [Fargate compute environments](fargate.md "fargate.md")
- [Amazon EKS compute environments](eks.md "eks.md")
