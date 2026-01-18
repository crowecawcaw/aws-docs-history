# Amazon ECR repository hosting GuardDuty

agent

The following sections list the Amazon Elastic Container Registry (Amazon ECR) repositories where GuardDuty hosts the security
agent that gets deployed on your Amazon EKS and Amazon ECS clusters.

The prerequisite to [Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs "prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs") requires you to provide a task execution
role that has certain Amazon Elastic Container Registry (Amazon ECR) permissions. To further restrict these permissions, you
can add the Amazon ECR repository URI that hosts the GuardDuty agent for Fargate-Amazon ECS resources.

###### Contents

- [ECR repository for EKS agent versions 1.12.1 - 1.8.1 (eks.build.2)](eks-runtime-agent-ecr-image-uri-v1-8-1-build-2.md "eks-runtime-agent-ecr-image-uri-v1-8-1-build-2.md")
- [ECR repository for EKS agent version 1.8.1 (eks.build.1)](eks-runtime-agent-ecr-image-uri-v1-8-1-build-1.md "eks-runtime-agent-ecr-image-uri-v1-8-1-build-1.md")
- [ECR Repository for GuardDuty agent on AWS Fargate
  (Amazon ECS only)](ecs-runtime-agent-ecr-image-uri.md "ecs-runtime-agent-ecr-image-uri.md")
