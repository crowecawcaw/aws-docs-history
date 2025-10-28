# AWS PCS compute node groups

An AWS PCS compute node group is a logical collection of nodes (Amazon EC2 instances). These nodes can be used to run computing jobs, as well as to provide interactive, shell-based access to an HPC system. A compute node group consists of rules for creating nodes, including which Amazon EC2 instances types to use, how many instances to run, whether to use Spot Instances or On-demand Instances, which subnets and security groups to use, and how to configure each instance when it launches. When those rules are updated, AWS PCS updates resources associated with the compute node group to match.

###### Topics

- [Creating a compute node group in
  AWS PCS](working-with_cng_create.md "working-with_cng_create.md")
- [Updating an AWS PCS compute node group](working-with_cng_update.md "working-with_cng_update.md")
- [Deleting a compute node group in AWS PCS](working-with_cng_delete.md "working-with_cng_delete.md")
- [Get compute node group details in
  AWS PCS](working-with_cng_get-details.md "working-with_cng_get-details.md")
- [Finding compute node group instances in
  AWS PCS](working-with_compute-instances.md "working-with_compute-instances.md")
