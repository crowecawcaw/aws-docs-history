# Considerations for AWS Batch

Before you set up an interface endpoint for AWS Batch, review [Interface endpoint properties and
limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") in the _AWS PrivateLink Guide_.

AWS Batch supports making calls to all of its API actions through the interface endpoint.

Before you set up interface VPC endpoints for AWS Batch, be aware of the following considerations:

- Jobs using Fargate resources launch type don't require the interface VPC endpoints for Amazon ECS, but you might
  need interface VPC endpoints for AWS Batch, Amazon ECR, Secrets Manager, or Amazon CloudWatch Logs described in the following points.
  - To run jobs, you must create the interface VPC endpoints for Amazon ECS. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](../../../AmazonECS/latest/developerguide/vpc-endpoints.md "../../../AmazonECS/latest/developerguide/vpc-endpoints.md") in the
    _Amazon Elastic Container Service Developer Guide_.
  - To allow your jobs to pull private images from Amazon ECR, you must create the interface VPC endpoints for Amazon ECR.
    For more information, see [Interface VPC Endpoints
    (AWS PrivateLink)](../../../AmazonECR/latest/userguide/vpc-endpoints.md "../../../AmazonECR/latest/userguide/vpc-endpoints.md") in the _Amazon Elastic Container Registry User Guide_.
  - To allow your jobs to pull sensitive data from Secrets Manager, you must create the interface VPC endpoints for Secrets Manager.
    For more information, see [Using Secrets Manager with VPC Endpoints](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md")
    in the _AWS Secrets Manager User Guide_.
  - If your VPC doesn't have an internet gateway and your jobs use the `awslogs` log driver to send
    log information to CloudWatch Logs, you must create an interface VPC endpoint for CloudWatch Logs. For more information, see [Using CloudWatch Logs with Interface VPC Endpoints](../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md "../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md") in
    the _Amazon CloudWatch Logs User Guide_.

- Jobs using the EC2 resources require that the container instances that they're launched on to run version
  `1.25.1` or later of the Amazon ECS container agent. For more information, see [Amazon ECS Linux container agent versions](../../../AmazonECS/latest/developerguide/ecs-agent-versions.md "../../../AmazonECS/latest/developerguide/ecs-agent-versions.md") in the
  _Amazon Elastic Container Service Developer Guide_.
- VPC endpoints currently don't support cross-Region requests. Ensure that you create your endpoint in the same
  Region where you plan to issue your API calls to AWS Batch.
- VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want to use your own DNS, you can use
  conditional DNS forwarding. For more information, see [DHCP Options
  Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the _Amazon VPC User Guide_.
- The security group attached to the VPC endpoint must allow incoming connections on port 443 from the private
  subnet of the VPC.
- AWS Batch does not support VPC interface endpoints in the following AWS Regions:
  - Asia Pacific (Osaka) (`ap-northeast-3`)
  - Asia Pacific (Jakarta) (`ap-southeast-3`)
