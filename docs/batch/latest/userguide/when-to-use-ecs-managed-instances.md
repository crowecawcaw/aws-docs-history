# When to use Amazon ECS Managed Instances

Use Amazon ECS Managed Instances when your jobs need capabilities beyond what Fargate provides
and you prefer not to manage the underlying Amazon EC2 infrastructure. Amazon ECS Managed Instances
combines the operational simplicity of Fargate with the compute flexibility of
Amazon EC2.

Use Amazon ECS Managed Instances if your jobs require any of the following:

- Your jobs require GPU instances (NVIDIA accelerators) for machine learning or rendering
  workloads.
- Your jobs need more than 32 vCPUs or 244 GiB of memory.
- Your containers require privileged access.
- Your containers need host-level devices or volumes.
- You need specific Amazon EC2 instance types or instance families.
- You want to use On-Demand Capacity Reservations, Reserved Instances, or Amazon EC2 Instance
  Savings Plans.
- You need ARM64 (AWS Graviton) instances through `runtimePlatform`
  configuration.
- You want to run both x86 (`X86_64`) and `ARM64` jobs from a single
  compute environment. For more information, see
  [Running mixed-architecture jobs (X86\_64 and ARM64)](ecs-managed-instances-multi-architecture.md "ecs-managed-instances-multi-architecture.md").
- You need arbitrary vCPU and memory combinations without the fixed size pairings that
  Fargate requires.
  Fargate is the simplest and recommended option if you don't have specific requirements for
  the underlying compute infrastructure. Continue to use Fargate if:

- Your jobs fit within Fargate resource limits (up to 32 vCPUs, 244 GiB memory).
- You need host-level isolation (each Fargate task runs in its own dedicated
  kernel runtime environment).
- You don't need GPU, privileged access, or host-level resources.
  Use Amazon EC2 managed compute environments if:

- You need multi-node parallel (MNP) jobs.
- You require custom AMIs or launch templates.
- You need fine-grained control over allocation strategies.
- You need a minimum capacity warm pool (`minvCpus`).
