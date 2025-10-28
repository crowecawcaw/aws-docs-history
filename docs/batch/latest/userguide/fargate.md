# Fargate compute environments

Fargate is a technology that you can use with AWS Batch to run [containers](https://aws.amazon.com/what-are-containers "https://aws.amazon.com/what-are-containers") without having to manage servers or clusters of Amazon EC2 instances. With Fargate, you no longer
have to provision, configure, or scale clusters of virtual machines to run containers. This removes the need to choose
server types, decide when to scale your clusters, or optimize cluster packing.

When you run your jobs with Fargate resources, you package your application in containers, specify the CPU and
memory requirements, define networking and IAM policies, and launch the application. Each Fargate job has its own
isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network
interface with another job.

###### Topics

- [When to use Fargate](when-to-use-fargate.md "when-to-use-fargate.md")
- [Job definitions on Fargate](fargate-job-definitions.md "fargate-job-definitions.md")
- [Job queues on Fargate](fargate-job-queues.md "fargate-job-queues.md")
- [Compute environments on Fargate](fargate-compute-environments.md "fargate-compute-environments.md")
