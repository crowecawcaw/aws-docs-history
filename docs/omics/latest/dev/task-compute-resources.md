# Task compute and resources

When you define tasks in a HealthOmics workflow, you specify the compute, memory, and container resources that
each task requires. HealthOmics allocates the appropriate instance type for each task based on the resources you
request.

In the workflow definition, define the following for each task:

- **CPU and memory** – The number of vCPUs and amount of memory for
  standard, compute-optimized, or memory-optimized instances. See [Task resources in a HealthOmics workflow definition](task-resources.md "task-resources.md").
- **Container image** – The Amazon ECR container image for the
  task. See [Container images for private workflows](workflows-ecr.md "workflows-ecr.md").
- **GPU accelerators** – Optionally, a GPU accelerator type to
  allocate an accelerated-computing instance (G4, G5, G6, or G6e) for tasks that benefit from GPU
  processing. See [Task accelerators in a HealthOmics workflow definition](task-accelerators.md "task-accelerators.md").
- **Advanced resource configuration** – Optionally, an ordered list of
  accelerator types (GPU) to search and execute at run time. HealthOmics tries each accelerator profile in order
  until one succeeds, enabling fallback from one accelerator type to another or from
  accelerators to CPU. See [Advanced resource configuration](advanced-resource-configuration.md "advanced-resource-configuration.md").

###### Note

HealthOmics matches instance types to fit the compute and memory requirements that you specify. If you don't
specify any compute or memory requirements, HealthOmics defaults to 1 vCPU and 1 GiB of memory for a CPU
instance.

###### Topics

- [Task resources in a HealthOmics workflow definition](task-resources.md "task-resources.md")
- [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md "memory-and-compute-tasks.md")
- [Task accelerators in a HealthOmics workflow definition](task-accelerators.md "task-accelerators.md")
- [Advanced resource configuration](advanced-resource-configuration.md "advanced-resource-configuration.md")
