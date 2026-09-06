

# Best practices for using Neptune with Amazon ECS and Amazon EKS
<a name="best-practices-ecs-eks"></a>

Running your graph application in containers on [Amazon Elastic Container Service](https://docs.aws.amazon.com/ecs/) (Amazon ECS) or [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/) (Amazon EKS) introduces considerations that don't apply to traditional long-running server deployments. Containers are ephemeral — they start, stop, and replace each other during rolling updates and scaling events. This lifecycle affects how your application manages connections to Neptune, handles host replacements, and authenticates with IAM.

The following sections describe practical considerations for running Neptune workloads in containerized environments.

**Topics**
+ [Manage connection pools and lifecycle in containerized environments](best-practices-ecs-eks-connections.md)
+ [Handle host replacement and connection stalling](best-practices-ecs-eks-host-replacement.md)
+ [Configure networking, security groups, and IAM authentication](best-practices-ecs-eks-networking-iam.md)