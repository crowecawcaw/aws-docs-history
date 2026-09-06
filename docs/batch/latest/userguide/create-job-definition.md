

# Create a single-node job definition
<a name="create-job-definition"></a>

Before you can run jobs in AWS Batch, you must create a job definition. This process varies slightly between single-node and multi-node parallel jobs. This topic covers specifically how to create a job definition for an AWS Batch job that's not a multi-node parallel job (also known as *gang scheduling*).

You can create a multi-node parallel job definition on Amazon Elastic Container Service resources. For more information, see [Create a multi-node parallel job definition](create-multi-node-job-def.md). 

**Topics**
+ [Create a single-node job definition on Amazon EC2 resources](create-job-definition-EC2.md)
+ [Create a single-node job definition on Fargate resources](create-job-definition-Fargate.md)
+ [Create a job definition on Amazon ECS Managed Instances](create-job-definition-ecs-managed-instances.md)
+ [Create a single-node job definition on Amazon EKS resources](create-job-definition-eks.md)
+ [Create a single-node job definition with multiple containers on Amazon EC2 resources](create-job-definition-single-node-multi-container.md)