

# Amazon ECS security considerations for when to use Fargate
<a name="security-fargate-ec2"></a>

 We recommend that customers looking for strong isolation for their tasks use Fargate. Fargate runs each task in a hardware virtualization environment. This ensures that these containerized workloads do not share network interfaces, Fargate ephemeral storage, CPU, or memory with other tasks.