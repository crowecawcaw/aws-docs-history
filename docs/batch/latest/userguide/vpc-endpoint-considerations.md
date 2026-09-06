

# Considerations for AWS Batch
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for AWS Batch, review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) in the *AWS PrivateLink Guide*.

AWS Batch supports making calls to all of its API actions through the interface endpoint. 

Before you set up interface VPC endpoints for AWS Batch, be aware of the following considerations:
+ Jobs using Fargate resources launch type don't require the interface VPC endpoints for Amazon ECS, but you might need interface VPC endpoints for AWS Batch, Amazon ECR, Secrets Manager, or Amazon CloudWatch Logs described in the following points.
  + To run jobs, you must create the interface VPC endpoints for Amazon ECS. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html) in the *Amazon Elastic Container Service Developer Guide*.
  + To allow your jobs to pull private images from Amazon ECR, you must create the interface VPC endpoints for Amazon ECR. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html) in the *Amazon Elastic Container Registry User Guide*.
  + To allow your jobs to pull sensitive data from Secrets Manager, you must create the interface VPC endpoints for Secrets Manager. For more information, see [Using Secrets Manager with VPC Endpoints](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html) in the *AWS Secrets Manager User Guide*.
  + If your VPC doesn't have an internet gateway and your jobs use the `awslogs` log driver to send log information to CloudWatch Logs, you must create an interface VPC endpoint for CloudWatch Logs. For more information, see [Using CloudWatch Logs with Interface VPC Endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html) in the *Amazon CloudWatch Logs User Guide*.
+ Jobs using the EC2 resources require that the container instances that they're launched on to run version `1.25.1` or later of the Amazon ECS container agent. For more information, see [Amazon ECS Linux container agent versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-versions.html) in the *Amazon Elastic Container Service Developer Guide*.
+ VPC endpoints currently don't support cross-Region requests. Ensure that you create your endpoint in the same Region where you plan to issue your API calls to AWS Batch.
+ VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want to use your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP Options Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
+ The security group attached to the VPC endpoint must allow incoming connections on port 443 from the private subnet of the VPC.
+ AWS Batch does not support VPC interface endpoints in the following AWS Regions:
  + Asia Pacific (Osaka) (`ap-northeast-3`)
  + Asia Pacific (Jakarta) (`ap-southeast-3`)