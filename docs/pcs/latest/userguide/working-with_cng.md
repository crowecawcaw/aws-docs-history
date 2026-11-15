

# AWS PCS compute node groups
<a name="working-with_cng"></a>

An AWS Parallel Computing Service (AWS PCS) compute node group is a logical collection of compute nodes (Amazon EC2 instances). Compute nodes run jobs, and they can also provide interactive, shell-based access to an HPC system. A compute node group consists of rules for creating compute nodes. The rules include which Amazon EC2 instance types to use, how many instances to run, whether to use Spot Instances or On-Demand Instances, and which subnets to use. When you update these rules, AWS PCS updates the resources associated with the compute node group to match.

You also specify the AMI, security groups, and SSH key pair for compute nodes on the compute node group. These are called instance settings. To configure Amazon EC2 settings that aren't available as instance settings, such as network interfaces or capacity reservations, use a custom launch template. For more information, see [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md) and [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md).

**SMT is disabled on compute nodes**  
AWS PCS disables simultaneous multithreading (SMT), also known as Hyper-Threading on Intel processors, on all compute nodes at bootstrap. You can't change this setting. On SMT-capable instance types, each vCPU maps to a dedicated physical core rather than a hardware thread. This means the total vCPU count is half the default for the instance type, but each vCPU has exclusive access to the full core. For example, an instance type that advertises 96 vCPUs has 48 usable cores on AWS PCS compute nodes. Instance types that don't support SMT, such as those with AWS Graviton (Arm) processors, are unaffected.  
Most compute-bound HPC workloads see equivalent or better performance with SMT disabled. Disabling SMT eliminates resource contention between sibling threads and gives each physical core exclusive access to its cache and execution units. This is common practice across HPC environments.

**Topics**
+ [Creating a compute node group in AWS PCS](working-with_cng_create.md)
+ [Updating a compute node group in AWS PCS](working-with_cng_update.md)
+ [Deleting a compute node group in AWS PCS](working-with_cng_delete.md)
+ [Getting compute node group details in AWS PCS](working-with_cng_get-details.md)
+ [Finding compute node group instances in AWS PCS](working-with_compute-instances.md)
+ [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md)
+ [Run custom scripts with node lifecycle actions in AWS PCS](cng-node-lifecycle-actions.md)