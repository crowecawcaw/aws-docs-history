

# AWS PCS compute node groups
<a name="working-with_cng"></a>

An AWS PCS compute node group is a logical collection of nodes (Amazon EC2 instances). These nodes can be used to run computing jobs, as well as to provide interactive, shell-based access to an HPC system. A compute node group consists of rules for creating nodes, including which Amazon EC2 instances types to use, how many instances to run, whether to use Spot Instances or On-demand Instances, which subnets and security groups to use, and how to configure each instance when it launches. When those rules are updated, AWS PCS updates resources associated with the compute node group to match. 

**SMT is disabled on compute nodes**  
AWS PCS disables simultaneous multithreading (SMT), also known as Hyper-Threading on Intel processors, on all compute node instances at bootstrap. This is not configurable. On SMT-capable instance types, each vCPU maps to a dedicated physical core rather than a hardware thread. This means the total vCPU count is half the default for the instance type, but each vCPU has exclusive access to the full core. For example, an instance type that advertises 96 vCPUs has 48 usable cores on AWS PCS compute nodes. Instance types that don't support SMT, such as Graviton (Arm), are unaffected.  
Most compute-bound HPC workloads see equivalent or better performance with SMT disabled. Disabling hyperthreading eliminates resource contention between sibling threads and gives each physical core exclusive access to its cache and execution units. This is common practice across HPC environments.

**Topics**
+ [Creating a compute node group in AWS PCS](working-with_cng_create.md)
+ [Updating an AWS PCS compute node group](working-with_cng_update.md)
+ [Deleting a compute node group in AWS PCS](working-with_cng_delete.md)
+ [Get compute node group details in AWS PCS](working-with_cng_get-details.md)
+ [Finding compute node group instances in AWS PCS](working-with_compute-instances.md)
+ [Run custom scripts with node lifecycle actions in AWS PCS](cng-node-lifecycle-actions.md)