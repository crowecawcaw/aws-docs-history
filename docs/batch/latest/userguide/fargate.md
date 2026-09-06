

# Fargate compute environments
<a name="fargate"></a>

Fargate is a technology that you can use with AWS Batch to run [containers](https://aws.amazon.com/what-are-containers) without having to manage servers or clusters of Amazon EC2 instances. With Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

When you run your jobs with Fargate resources, you package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application. Each Fargate job has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another job.

Fargate runs both x86 (`X86_64`) and `ARM64` (AWS Graviton) jobs. You select the architecture per job in the job definition with `runtimePlatform.cpuArchitecture`. A single Fargate compute environment and job queue can run both architectures. For more information, see [Running mixed-architecture jobs (X86\_64 and ARM64)](fargate-multi-architecture.md).

Fargate is only available for AWS Batch compute environments that use Amazon ECS as the orchestrator. Fargate is not supported for AWS Batch on Amazon EKS compute environments. For more information, see [Amazon EKS compute environments](eks.md).

**Topics**
+ [When to use Fargate](when-to-use-fargate.md)
+ [Job definitions on Fargate](fargate-job-definitions.md)
+ [Running mixed-architecture jobs (X86\_64 and ARM64)](fargate-multi-architecture.md)
+ [Job queues on Fargate](fargate-job-queues.md)
+ [Compute environments on Fargate](fargate-compute-environments.md)