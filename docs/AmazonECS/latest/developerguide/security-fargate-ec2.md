# Amazon ECS security considerations for when to use Fargate

We recommend that customers looking for strong isolation for their tasks
use Fargate. Fargate runs each task in a hardware virtualization
environment. This ensures that these containerized workloads do not share
network interfaces, Fargate ephemeral storage, CPU, or memory with other
tasks. For more information, see [Security Overview of AWS Fargate](https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf "https://d1.awsstatic.com/whitepapers/AWS_Fargate_Security_Overview_Whitepaper.pdf").
