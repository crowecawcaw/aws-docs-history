

# Migrating to Linux platform version 1.4.0 on Amazon ECS
<a name="platform-version-migration"></a>

Consider the following when migrating your Amazon ECS on Fargate tasks from platform version `1.0.0`, `1.1.0`, `1.2.0`, or `1.3.0` to platform version `1.4.0`. It is best practice to confirm your task works properly on platform version `1.4.0` before you migrate the tasks.
+ The network traffic behavior to and from tasks has been updated. Starting with platform version 1.4.0, all Amazon ECS on Fargate tasks receive a single elastic network interface (referred to as the task ENI) and all network traffic flows through that ENI within your VPC. The traffic is visible to you through your VPC flow logs. For more information see [Amazon ECS task networking options for Fargate](fargate-task-networking.md).
+ If you use interface VPC endpoints, consider the following.
  + For container images hosted with Amazon ECR, you need the following endpoints. For more information, see [Amazon ECR interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html) in the *Amazon Elastic Container Registry User Guide*.
    + **com.amazonaws.{{region}}.ecr.dkr** Amazon ECR VPC endpoint
    + **com.amazonaws.{{region}}.ecr.api** Amazon ECR VPC endpoint
    +  Amazon S3 gateway endpoint
  + When your task definition references Secrets Manager secrets to retrieve sensitive data for your containers, you must create the interface VPC endpoints for Secrets Manager. For more information, see [Using Secrets Manager with VPC Endpoints](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html) in the *AWS Secrets Manager User Guide*.
  + When your task definition references Systems Manager Parameter Store parameters to retrieve sensitive data for your containers, you must create the interface VPC endpoints for Systems Manager. For more information, see [Improve the security of EC2 instances by using VPC endpoints for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html) in the *AWS Systems Manager User Guide*.
  + The security group for the Elastic Network Interface (ENI) associated with your task needs the security group rules to allow traffic between the task and the VPC endpoints.